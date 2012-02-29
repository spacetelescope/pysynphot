import os

# test the ability of pysynphot.locations to auto-gather extinction laws
# from $PYSYN_CDBS/grid/extinction/
def test_get_RedLaws():
  cdbs = os.environ['PYSYN_CDBS']
  os.environ['PYSYN_CDBS'] = os.path.abspath('./data/cdbs/')
  
  import pysynphot.locations as locations
  
  os.environ['PYSYN_CDBS'] = cdbs
  
  shouldbe = {'lmc30dor':'lmc_30dorshell_001.fits',
              'lmcavg':'lmc_diffuse_002.fits',
              'mwdense':'milkyway_dense_001.fits',
              'mwavg':'milkyway_diffuse_001.fits',
              'smcbar':'smc_bar_001.fits',
              'xgalsb':'xgal_starburst_003.fits'}
              
  for name in shouldbe:
    assert shouldbe[name] == os.path.basename(locations.RedLaws[name])

# test that we can add a new conversion to the CONVERTDICT and 
# irafconvert will find and use it.
def test_CONVERTDICT():
  import pysynphot.locations as locations
  
  locations.CONVERTDICT['testjref'] = './data/cdbs/jref/'
  
  refpath = './data/cdbs/jref/empty_test_file.txt'
  
  filename = locations.irafconvert('testjref$empty_test_file.txt')
  
  assert refpath == filename
