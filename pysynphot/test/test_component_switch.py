"""
This tests whether the .components attribute of observationmode.ObservationMode
objects reflects the currently set COMPTABLE variable after the COMPTABLE
variable is switched within the same code.

"""
from __future__ import absolute_import, division, print_function

import os

import pytest

from .utils import use_cdbs
from .. import refs
from ..observationmode import ObservationMode


@use_cdbs
class TestCompSwitch(object):
    def setup_class(self):
        self.cdbs = os.environ['PYSYN_CDBS']
        self.old_refs = refs.getref()
        refs.GRAPHTABLE = os.path.join(
            self.cdbs, 'mtab', 'OLD_FILES', 'u921351jm_tmg.fits')

    def teardown_class(self):
        refs.setref(graphtable=self.old_refs['graphtable'])
        refs.setref(comptable=self.old_refs['comptable'])

    @pytest.mark.parametrize(
        ('filfile', 'ccdfile', 'tmcfile'),
        [('acs_f435w_005_syn.fits', 'acs_hrc_ccd_013_syn.fits',
          'ub31649mm_tmc.fits'),
         ('acs_f435w_004_syn.fits', 'acs_hrc_ccd_011_syn.fits',
          'r1j2146sm_tmc.fits')])
    def test_comp(self, filfile, ccdfile, tmcfile):
        refs.COMPTABLE = os.path.join(self.cdbs, 'mtab', 'OLD_FILES', tmcfile)

        obs = ObservationMode('acs,hrc,f435w')
        in_list = [c.throughput_name for c in obs.components]

        throughput_list = [os.path.join(self.cdbs, 'comp', 'acs', s)
                           for s in ['acs_hrc_m12_005_syn.fits',
                                     'acs_hrc_m3_005_syn.fits',
                                     filfile,
                                     'acs_hrc_win_005_syn.fits',
                                     ccdfile]]
        throughput_list.append(
            os.path.join(self.cdbs, 'comp', 'ota', 'hst_ota_007_syn.fits'))

        missing = []
        for x in throughput_list:
            if x not in in_list:
                missing.append(x)

        assert len(missing) == 0, 'missing: {}'.format(missing)
