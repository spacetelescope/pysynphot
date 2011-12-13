import os

# test the ability of pysynphot.locations to auto-gather extinction laws
# from $PYSYN_CDBS/grid/extinction/
def test_get_RedLaws():
    cdbs = os.environ['PYSYN_CDBS']
    mydir = os.path.abspath(os.path.dirname(__file__))
    os.environ['PYSYN_CDBS'] = os.path.join(mydir, 'data', 'cdbs')

    import pysynphot.locations as locations
    reload(locations)
    RedLaws = locations.RedLaws.copy()

    # Reset to the default
    os.environ['PYSYN_CDBS'] = cdbs
    reload(locations)

    shouldbe = {'lmc30dor': 'lmc_30dorshell_001.fits',
                'lmcavg': 'lmc_diffuse_002.fits',
                'mwdense': 'milkyway_dense_001.fits',
                'mwavg': 'milkyway_diffuse_001.fits',
                'smcbar': 'smc_bar_001.fits',
                'xgalsb': 'xgal_starburst_003.fits'}

    for name in shouldbe:
      assert shouldbe[name] == os.path.basename(RedLaws[name])
