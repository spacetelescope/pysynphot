from spark import GenericScanner, GenericParser, GenericASTTraversal
from spark import GenericASTBuilder, GenericASTMatcher
import spectrum
import observationmode
import etc

syfunctions = [
    'spec',
    'unit',
    'box',
    'bb',
    'pl',
    'hi',
    'cat',
    'icat',
    'grid',
    'rn',
    'z',
    'ebmv',
    'embvx',
    'band'
    ]
syforms = [
    'fnu',
    'flam',
    'photnu',
    'photlam',
    'counts',
    'abmag',
    'stmag',
    'obmag',
    'vegamag',
    'jy',
    'mjy'
    ]
syredlaws = [
    'gal1',
    'gal2',
    'gal3',
    'smc',
    'lmc',
    'xgal'
    ]
class Token:
    def __init__(self, type=None, attr=None):
        self.type = type
        self.attr = attr
    def __cmp__(self, o):
        return cmp(self.type, o)
    def __repr__(self):
        if self.attr is not None:
            return str(self.attr) 
        else:
            return self.type

class AST:
    def __init__(self, type):
        self.type = type
        self._kids = []
    def __getitem__(self, i):
        return self._kids[i]
    def __len__(self):
        return len(self._kids)
    def __setslice__(self, low, high, seq):
        self._kids[low:high] = seq
    def __cmp__(self, o):
        return cmp(self.type, o)
        
class BaseScanner(GenericScanner):
    def __init__(self):
        GenericScanner.__init__(self)
    def tokenize(self, input):
        self.rv = []
        GenericScanner.tokenize(self, input)
        return self.rv
    def t_whitespace(self, s):
        r' \s+ '
    def t_op(self, s):
        r' \+ | \* | - '
        self.rv.append(Token(type=s))
    def t_lparens(self, s):
        r' \( '
        self.rv.append(Token(type='LPAREN'))
    def t_rparens(self, s):
        r' \) '
        self.rv.append(Token(type='RPAREN'))
    def t_comma(self, s):
        r' , '
        self.rv.append(Token(type=s))
    def t_integer(self, s):
        r' \d+ '
        self.rv.append(Token(type='INTEGER', attr=s))
    def t_identifier(self, s):
        r' [a-z_A-Z][\w/\.\$]*'
        self.rv.append(Token(type='IDENTIFIER', attr=s))
    def t_filelist(self, s):
        r' @\w+'
        self.rv.append(Token(type='FILELIST', attr=s[1:]))

class Scanner(BaseScanner):
    def __init__(self):
        BaseScanner.__init__(self)
    def t_float(self, s):
        r' ((\d*\.\d+)|(\d+\.d*)) ([eE][-+]?\d+)?'
        self.rv.append(Token(type='FLOAT', attr=s))
    def t_divop(self, s):
        r' \s/\s '
        self.rv.append(Token(type='/'))

class BaseParser(GenericASTBuilder):
    def __init__(self, ASTclass, start='top'):
        GenericASTBuilder.__init__(self, ASTclass, start)
    def p_top(self, args):
        '''
            top ::= expr
            top ::= FILELIST
            expr ::= expr + term
            expr ::= expr - term
            expr ::= term
            term ::= term * factor
            term ::= term / factor
            term ::= LPAREN expr RPAREN
            term ::= factor
            factor ::= unaryop value
            factor ::= value
            unaryop ::= +
            unaryop ::= -
            value ::= INTEGER
            value ::= FLOAT
            value ::= IDENTIFIER
            value ::= function_call
            function_call ::= IDENTIFIER LPAREN arglist RPAREN
            arglist ::= arglist , expr
            arglist ::= expr
        '''
    def terminal(self, token):
        rv = AST(token.type)
        rv.attr = token.attr
        return rv
    def nonterminal(self, type, args):
        if len(args) == 1:
            return args[0]
        return GenericASTBuilder.nonterminal(self, type, args)

class Interpreter(GenericASTMatcher):
    def __init__(self, ast):
        GenericASTMatcher.__init__(self, 'V', ast)
    def error(self, token):
        raise ValueError("problems in interpreting AST")
    def p_int(self, tree):
        ''' V ::= INTEGER '''
        tree.value = int(tree.attr)
    def p_float(self, tree):
        ''' V ::= FLOAT '''
        tree.value = float(tree.attr)
    def p_identifier(self, tree):
        ''' V ::= IDENTIFIER '''
        tree.value = tree.attr
    def p_factor_unary_plus(self, tree):
        ''' V ::= factor ( + V ) '''
        tree.value = convertstr(tree[1].value)
    def p_factor_unary_minus(self, tree):
        ''' V ::= factor ( - V ) '''
        tree.value = - convertstr(tree[1].value)
    def p_expr_plus(self, tree):
        ''' V ::= expr ( V + V )'''
        tree.value = convertstr(tree[0].value) + convertstr(tree[2].value)
    def p_expr_minus(self, tree):
        ''' V ::= expr ( V - V )'''
        tree.value = convertstr(tree[0].value) - convertstr(tree[2].value)
    def p_term_mult(self, tree):
        ''' V ::= term ( V * V )'''
        tree.value = convertstr(tree[0].value) * convertstr(tree[2].value)
    def p_term_div(self, tree):
        ''' V ::= term ( V / V )'''
        tree.value = convertstr(tree[0].value) / tree[2].value
    def p_term_paren(self, tree):
        ''' V ::= term ( LPAREN V RPAREN )'''
        tree.value = convertstr(tree[1].value)
    def p_arglist(self, tree):
        ''' V ::= arglist ( V , V )'''
        if type(tree[0].value) == type([]):
            tree.value = tree[0].value + [tree[2].value]
        else:
            tree.value = [tree[0].value, tree[2].value]
    def p_functioncall(self, tree):
        # Where all the real interpreter action is
        # Note that things that should only be done at the top level
        # are performed in the interpret function defined below.
        ''' V ::= function_call ( V LPAREN V RPAREN )'''
        if type(tree[2].value) != type([]):
            args = [tree[2].value]
        else:
            args = tree[2].value
        fname = tree[0].value
        if fname not in syfunctions:
            print "Error: unknown function:", fname
            self.error(fname)
        else:
            if fname == 'unit':
                # constant spectrum
                tree.value = spectrum.UnitSpectrum(args[0], fluxunits=args[1])
            elif fname == 'bb':
                # black body
                tree.value = spectrum.BlackBody(args[0])
            elif fname == 'pl':
                # power law
                if arg[2] not in synforms:
                    print "Error: unrecognized units:", arg[2]
                # code to create powerlaw spectrum object
            elif fname == 'box':
                # box throughput
                tree.value = spectrum.Box(args[0],args[1])
            elif fname == 'rn':
                # renormalize
                tree.value = spectrum.renormalize(args[0],args[1],args[2],args[3])
            elif fname == 'z':
                # Don't know what the real method is
                tree.value = arg[0].redshift(arg[1])
            else:
                tree.value = "would call %s with the following args: %s" % (fname, repr(args))
            
        
# stuff not yet handled, namely, Filelist, should be handled in interp function        
zzz =   '''
          
            top ::= FILELIST

        '''
def convertstr(value):
    # Any string appearing in numeric expressions must be
    # assumed to be a filename that should be read in as a table
    # This is a utility function used by the interpreter to do the
    # conversion from string to spectrum object
    if type(value) == type(''):
        return spectrum.TabularSourceSpectrum(value)
    else:
        return value

def scan(input):
    scanner = Scanner()
    input = input.replace('%2b','+')
    return scanner.tokenize(input)

def parse(tokens):
    parser = BaseParser(AST)
    return parser.parse(tokens)

def interpret(ast):
    interpreter = Interpreter(ast)
    interpreter.match()
    value = ast.value
    if type(value) == type(''):
        # means we need to read from a file
        # needs extra logic to search for different file types?
        return spectrum.TabularSourceSpectrum(value)
    else:
        return value
    
def ptokens(tlist):
    for token in tlist:
        print token.type, token.attr
