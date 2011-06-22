"""
This tests whether the .components attribute of observationmode.ObservationMode
objects reflects the currently set COMPTABLE variable after the COMPTABLE
variable is switched within the same code.

"""

from __future__ import division

import os.path
from unittest import TestCase

from pysynphot import observationmode

class TestCompSwitch(TestCase):
  def test_one(self):
    throughput_list = ['/grp/hst/cdbs/comp/ota/hst_ota_007_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_m12_005_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_m3_005_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_f435w_005_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_win_005_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_ccd_013_syn.fits']
    
    cmptb_name = os.path.join('mtab','ub31649mm_tmc.fits')
    observationmode.COMPTABLE = observationmode._refTable(cmptb_name)
    
    obs = observationmode.ObservationMode('acs,hrc,f435w')
    
    for c in obs.components:
      self.assertTrue(c.throughput_name in throughput_list)
      
  def test_two(self):
    throughput_list = ['/grp/hst/cdbs/comp/ota/hst_ota_007_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_m12_005_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_m3_005_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_f435w_004_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_win_005_syn.fits',
                       '/grp/hst/cdbs/comp/acs/acs_hrc_ccd_011_syn.fits']
    
    cmptb_name = os.path.join('mtab','r1j2146sm_tmc.fits')
    observationmode.COMPTABLE = observationmode._refTable(cmptb_name)
    
    obs = observationmode.ObservationMode('acs,hrc,f435w')
    
    for c in obs.components:
      self.assertTrue(c.throughput_name in throughput_list)
