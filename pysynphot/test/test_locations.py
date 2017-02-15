from __future__ import absolute_import, division, print_function

import os

from astropy.utils.data import get_pkg_data_filename, _find_pkg_data_path

from .utils import use_cdbs
from .. import locations


class TestGetRedLaws(object):
    """
    Test the ability of pysynphot.locations to auto-gather extinction laws
    from $PYSYN_CDBS/extinction/
    """
    def setup_class(self):
        self.old_cdbs = os.environ['PYSYN_CDBS']
        locations.rootdir = _find_pkg_data_path(os.path.join('data', 'cdbs'))
        locations._get_RedLaws()

    def teardown_class(self):
        locations.rootdir = self.old_cdbs

    def test_get_RedLaws(self):
        redlaws = locations.RedLaws.copy()
        shouldbe = {'lmc30dor': 'lmc_30dorshell_001.fits',
                    'lmcavg': 'lmc_diffuse_002.fits',
                    'mwdense': 'milkyway_dense_001.fits',
                    'mwavg': 'milkyway_diffuse_001.fits',
                    'smcbar': 'smc_bar_001.fits',
                    'xgalsb': 'xgal_starburst_003.fits'}

        for name in shouldbe:
            assert shouldbe[name] == os.path.basename(redlaws[name]), \
                'actual={}'.format(redlaws[name])


def test_CONVERTDICT():
    """
    Test that we can add a new conversion to the CONVERTDICT and
    irafconvert will find and use it.
    """
    refpath = get_pkg_data_filename(
        os.path.join('data', 'cdbs', 'jref', 'empty_test_file.txt'))
    locations.CONVERTDICT['testjref'] = os.path.dirname(refpath)
    filename = locations.irafconvert('testjref$empty_test_file.txt')
    assert refpath == filename
