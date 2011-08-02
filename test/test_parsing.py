import pysynphot.spparser as parser

def test_double_slash():
  sp = parser.parse_spec("spec($PYSYN_CDBS//calspec/gd71_mod_005.fits)")
  assert True
