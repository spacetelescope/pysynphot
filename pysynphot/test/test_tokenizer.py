from __future__ import absolute_import, division, print_function

import pytest

from ..spparser import Scanner

scanner = Scanner()

# Test of a single instance of each token. Does not test them in
# context, but at least it tests that each one is recognized.
tokens = [
    # bug: the original pysynphot could not recognize integer
    # ('INTEGER', '1'),

    # basic float
    ('FLOAT', '.1'),
    ('FLOAT', '1.1'),
    ('FLOAT', '1.'),
    ('FLOAT', '1'),

    # basic float with e+
    ('FLOAT', '.1e+1'),
    ('FLOAT', '1.1e+1'),
    ('FLOAT', '1.e+1'),
    ('FLOAT', '1e+1'),

    # basic float with e-
    ('FLOAT', '.1e-1'),
    ('FLOAT', '1.1e-1'),
    ('FLOAT', '1.e-1'),
    ('FLOAT', '1e-1'),

    # basic float with e
    ('FLOAT', '.1e1'),
    ('FLOAT', '1.1e1'),
    ('FLOAT', '1.e1'),
    ('FLOAT', '1e1'),

    # identifier
    ('IDENTIFIER', 'xyzzy'),
    ('IDENTIFIER', 'xyzzy20'),
    ('IDENTIFIER', '20xyzzy'),
    ('IDENTIFIER', '20xyzzy20'),

    # special characters
    ('LPAREN', '('),
    ('RPAREN', ')'),
    (',', ','),
    ('/', ' / '),

    # filename
    ('IDENTIFIER', '/a/b/c'),
    ('IDENTIFIER', 'foo$bar'),
    ('IDENTIFIER', 'a/b'),

    # file list
    ('FILELIST', '@arf'),
    ('FILELIST', '@narf')]


def print_token_list(tklist):
    s = 'Token list: {} items\n'.format(len(tklist))
    for x in tklist:
        s += '{:<20s} \n'.format(x.type, x.attr)
    s += '---\n'
    return s


def ptl2(tkl):
    """
    Use this to generate the list of tokens in a form easy to copy/paste
    into a test.
    """
    s = ''
    for x in tkl:
        s += '    ( "{}", {} ),  \n'.format(x.type, repr(x.attr))
    s += '\n'
    return s


def stream_t(text, result):
    """
    Parse a bit of text and compare it to the expected token stream.
    Each actual test function calls this.
    """
    tkl = scanner.tokenize(text)
    msg = print_token_list(tkl)

    assert result is not None, \
        msg + 'NO EXPECT LIST\n    [\n' + ptl2(tkl) + '    ]\n'

    for n, (expect, actual) in enumerate(zip(result, tkl)):
        assert expect[0] == actual.type and expect[1] == actual.attr, \
            (msg + '{} expect={} actual=({}, {})'.format(
                n, expect, actual.type, actual.attr))


@pytest.mark.parametrize(
    ('text', 'result'),
    [('spec($PYSYN_CDBS//calspec/gd71_mod_005.fits)',
      [('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', '$PYSYN_CDBS//calspec/gd71_mod_005.fits'),
       ('RPAREN', None)]),
     (('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),'
       'band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+'
       'spec(el1302a.fits)+spec(el1356a.fits)+'
       'spec(el2471a.fits))*0.5'),
      [('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'earthshine.fits'),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.5'),
       ('+', None),
       ('IDENTIFIER', 'rn'),
       ('LPAREN', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'Zodi.fits'),
       ('RPAREN', None),
       (',', None),
       ('IDENTIFIER', 'band'),
       ('LPAREN', None),
       ('IDENTIFIER', 'johnson'),
       (',', None),
       ('IDENTIFIER', 'v'),
       ('RPAREN', None),
       (',', None),
       ('FLOAT', '22.7'),
       (',', None),
       ('IDENTIFIER', 'vegamag'),
       ('RPAREN', None),
       ('+', None),
       ('LPAREN', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1215a.fits'),
       ('RPAREN', None),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1302a.fits'),
       ('RPAREN', None),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1356a.fits'),
       ('RPAREN', None),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el2471a.fits'),
       ('RPAREN', None),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.5')]),
     (('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),'
       'band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.1+'
       'spec(el1302a.fits)*0.066666667+spec(el1356a.fits)*0.0060+'
       'spec(el2471a.fits)*0.0050)'),
      [('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'earthshine.fits'),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.5'),
       ('+', None),
       ('IDENTIFIER', 'rn'),
       ('LPAREN', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'Zodi.fits'),
       ('RPAREN', None),
       (',', None),
       ('IDENTIFIER', 'band'),
       ('LPAREN', None),
       ('IDENTIFIER', 'johnson'),
       (',', None),
       ('IDENTIFIER', 'v'),
       ('RPAREN', None),
       (',', None),
       ('FLOAT', '22.7'),
       (',', None),
       ('IDENTIFIER', 'vegamag'),
       ('RPAREN', None),
       ('+', None),
       ('LPAREN', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1215a.fits'),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.1'),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1302a.fits'),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.066666667'),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1356a.fits'),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.0060'),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el2471a.fits'),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.0050'),
       ('RPAREN', None)]),
     (('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),'
       '22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+'
       'spec(el1356a.fits)+spec(el2471a.fits))'),
      [('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'earthshine.fits'),
       ('RPAREN', None),
       ('*', None),
       ('FLOAT', '0.5'),
       ('+', None),
       ('IDENTIFIER', 'rn'),
       ('LPAREN', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'Zodi.fits'),
       ('RPAREN', None),
       (',', None),
       ('IDENTIFIER', 'band'),
       ('LPAREN', None),
       ('IDENTIFIER', 'johnson'),
       (',', None),
       ('IDENTIFIER', 'v'),
       ('RPAREN', None),
       (',', None),
       ('FLOAT', '22.7'),
       (',', None),
       ('IDENTIFIER', 'vegamag'),
       ('RPAREN', None),
       ('+', None),
       ('LPAREN', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1215a.fits'),
       ('RPAREN', None),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1302a.fits'),
       ('RPAREN', None),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el1356a.fits'),
       ('RPAREN', None),
       ('+', None),
       ('IDENTIFIER', 'spec'),
       ('LPAREN', None),
       ('IDENTIFIER', 'el2471a.fits'),
       ('RPAREN', None),
       ('RPAREN', None)])])
def test_stream(text, result):
    stream_t(text, result)


@pytest.mark.xfail(reason='does not work')
@pytest.mark.parametrize(
    ('text', 'result'),
    [('rn(unit(1.,flam),band(stis,ccd,g430m,c4451,52X0.2),10.000000,abmag)',
      [('IDENTIFIER', 'rn'),
       ('LPAREN', None),
       ('IDENTIFIER', 'unit'),
       ('LPAREN', None),
       ('FLOAT', '1.'),
       (',', None),
       ('IDENTIFIER', 'flam'),
       ('RPAREN', None),
       (',', None),
       ('IDENTIFIER', 'band'),
       ('LPAREN', None),
       ('IDENTIFIER', 'stis'),
       (',', None),
       ('IDENTIFIER', 'ccd'),
       (',', None),
       ('IDENTIFIER', 'g430m'),
       (',', None),
       ('IDENTIFIER', 'c4451'),
       (',', None),
       ('IDENTIFIER', '52X0.2'),
       ('RPAREN', None),
       (',', None),
       ('FLOAT', '10.000000'),
       (',', None),
       ('IDENTIFIER', 'abmag'),
       ('RPAREN', None)]),
     ('rn(unit(1.,flam),band(stis,ccd,mirror,50CCD),10.000000,abmag)',
      [('IDENTIFIER', 'rn'),
       ('LPAREN', None),
       ('IDENTIFIER', 'unit'),
       ('LPAREN', None),
       ('FLOAT', '1.'),
       (',', None),
       ('IDENTIFIER', 'flam'),
       ('RPAREN', None),
       (',', None),
       ('IDENTIFIER', 'band'),
       ('LPAREN', None),
       ('IDENTIFIER', 'stis'),
       (',', None),
       ('IDENTIFIER', 'ccd'),
       (',', None),
       ('IDENTIFIER', 'mirror'),
       (',', None),
       ('IDENTIFIER', '50CCD'),
       ('RPAREN', None),
       (',', None),
       ('FLOAT', '10.000000'),
       (',', None),
       ('IDENTIFIER', 'abmag'),
       ('RPAREN', None)])])
def test_stream_xfail(text, result):
    stream_t(text, result)


@pytest.mark.xfail(reason='does not work')
def test_tokens():
    for x in tokens:
        typ, val = x
        tkl = scanner.tokenize(val)

        assert len(tkl) == 1, 'too many tokens\n' + print_token_list(tkl)

        assert tkl[0].type == typ, \
            ('wrong type: found {} want {}\n'.format(tkl[0].type, typ) +
             print_token_list(tkl))
        assert tkl[0].attr == val or tkl[0].attr is None or \
            (val.startswith('@') and tkl[0].attr == val[1:]), \
            ('token value incorrect: found {} want {}'.format(
                tkl[0].attr, val) + print_token_list(tkl))
