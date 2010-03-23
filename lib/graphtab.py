from __future__ import division
from collections import defaultdict
import pyfits

class GraphNode(object):
    """ Structure to hold all the information associated with a single
    innode of the graph table. The constructor produces an empty node,
    which must be filled later.
    This structure will be the value associated with the GraphTab dict.
    """
    
    def __init__(self):
        """ ( (default_outnode, compname, thcompname),
              {'kwd':(outnode, compname, thcompname)} )"""
        self.default = (None,None,None)
        self.named   = {}
        self.entry = ( self.default, self.named )

    def __repr__(self):
        """Maybe change this"""
        return str((self.default, self.named))

    def set_default(self, outnode, compname, thcompname):
        self.default = (outnode, compname, thcompname)
        self.entry = (self.default, self.named)

    def set_named(self, kwd, outnode, compname, thcompname):
        if kwd in self.named:
            raise IndexError("%s entry already exists for this node"%kwd)
        else:
            self.named[kwd]=(outnode, compname, thcompname)
            self.entry = (self.default, self.named)

    def get_default(self):
        return self.default

    def get_named(self,kwd):
        return self.named[kwd]
    
class GraphTable(object):
    def __init__(self, fname):
        self.tab = defaultdict(GraphNode)
        self.tname = fname
        self.inittab()

        
    def inittab(self):
        #Both FITS files and text files are supported
        # In either case, process one row at a time
        if self.tname.endswith('.fits'):
            f = pyfits.open(self.tname)
            for row in f[1].data:
                if not row.field('compname').endswith('graph'):
                    #Make it a list because FITS_records don't fully
                    #implement all the usual sequence behaviors
                    self._setrow(list(row))
                else:
                    raise NotImplementedError('Segmented graph tables not yet supported')

        else: #Not a FITS file; assume text
            f=open(self.tname)
            for line in f:
                try:
                    row = line.split()
                except ValueError,e:
                    print "Error parsine line %s"%line
                    raise e
                self._setrow(row)
            f.close()

    def _setrow(self, row):
        """ row = a list or tuple containing ordered elements
        kwd, innode, outnode, compname, thcomp
        followed by comments & other ignored things
        """
        try:
            compname, kwd, innode, outnode, thcomp = row[0:5]
        except ValueError:
            raise ValueError('Error unpacking row: %s'%row)

        #Innode is an integer
        k=int(innode)

        #"Clear" should become None
        if compname == 'clear':
            compname = None
        if thcomp == 'clear':
            thcomp = None

        #Now create the GraphNode defined by this row,
        #and add it to the table. Default nodes are special.
        if kwd == 'default':
            self.tab[k].set_default(int(outnode),compname, thcomp)
        else:
            self.tab[k].set_named(kwd,int(outnode),compname, thcomp)


    def traverse(self,icss,verbose=False):
        opt=[]
        thm=[]
        used = set()

        #Returns a list of keywords and a dict of paramkeys
        kws, paramdict = extract_keywords(icss)
        if verbose:
            print kws
            print paramdict
        #Always start with innode=1
        nextnode = 1

        #Keep going as long as the next node is in this table
        while nextnode in self.tab:
            defnode, othernodes = self.tab[nextnode].default, self.tab[nextnode].named

            #Check if the keywords match a named option
            found = kws & set(othernodes)
            
            
            if found:
                if verbose: print found
                #...and that we don't have ambiguity
                if len(found) == 1:
                    used.update(found)
                    matchnode = othernodes[found.pop()]
                else:
                    raise ValueError("Invalid obsmode: cannot use %s together"%found)
            else:
                #fall back to default
                matchnode = defnode

            #Having picked out the matching node, also pick up
            #the optical & thermal components from it
            nextnode, ocomp, tcomp  = matchnode
            if ocomp is not None:
                #Special handling of paramterization
                
                opt.append(ocomp)
            if tcomp is not None:
                thm.append(tcomp)

            if verbose: print matchnode

            if nextnode is None:
                raise ValueError("Incomplete obsmode: legal possibilities %s"%str(othernodes.keys()))

        #We're done with the table. If there are any keywords left over,
        #raise an exception.
        if kws != used:
            raise ValueError("Unused keywords %s"%str([k for k in (kws-used)]))

        #Return None for thermal if it's empty
        if thm == []:
            thm = None

        #The optical & thermal components are returned as a tuple
        return opt, thm

def extract_keywords(icss):
    """icss: input comma-separated string
    """
    # Force to lower case & split into keywords
    kws=set(icss.lower().split(','))
    #parameterized keywords require special handling
    paramdict={}
    for k in kws:
        if "#" in k:
            key,val=k.split('#')
            kws.remove(k)
            kws.add(key+'#')
            paramdict[key]=val
    return kws, paramdict
