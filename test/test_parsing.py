from nose.exc import SkipTest
import pysynphot.spparser as parser

def test_double_slash():
    sp = parser.parse_spec("spec($PYSYN_CDBS//calspec/gd71_mod_005.fits)")
    assert True

def test_pound():
    sp = parser.parse_spec("rn(unit(1.,flam),band(acs,wfc1,fr388n#3881.0),10.000000,abmag)")
    assert True

def test_x_decimal():
    raise SkipTest('does not work')
    sp = parser.parse_spec("rn(unit(1.,flam),band(stis,ccd,g430m,c4451,52X0.2),10.000000,abmag)")
    assert True

def test_50CCD():
    raise SkipTest('does not work')
    sp = parser.parse_spec("rn(unit(1.,flam),band(stis,ccd,mirror,50CCD),10.000000,abmag)")
    assert True

