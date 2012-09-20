import pysynphot.spparser as parser

def test_double_slash():
  sp = parser.parse_spec("spec($PYSYN_CDBS//calspec/gd71_mod_005.fits)")
  assert True

def test_pound():
  sp = parser.parse_spec("rn(unit(1.,flam),band(acs,wfc1,fr388n#3881.0),10.000000,abmag)")
  assert True
  
