from __future__ import division

import testutil
import os.path

import numpy as np

from pysynphot import Observation, ObsBandpass, FlatSpectrum
from pysynphot import locations

class BinFluxCase(testutil.FPTestCase):
  def setUp(self):
    tmg = locations._refTable(os.path.join('mtab','u921351jm_tmg.fits'))
    tmc = locations._refTable(os.path.join('mtab','ub31649mm_tmc.fits'))
    
    spec = FlatSpectrum(1,fluxunits='flam')
    bandpass = ObsBandpass('acs,hrc,f555w',graphtable=tmg,comptable=tmc)
    
    self.obs = Observation(spec,bandpass)
    self.obs.initbinflux()
    
  def test_binflux(self): 
    front10 = np.zeros(10)
    back10 = np.zeros(10)
    mid10 = np.array([ 0.12265425,  0.12226972,  0.12184207,  0.12141429,  0.12098646,
        0.1205586 ,  0.1201307 ,  0.11970269,  0.11927488,  0.11884699])
        
    binflux = self.obs.binflux
    
    self.assertEqualNumpy(front10,binflux[:10])
    self.assertEqualNumpy(back10,binflux[-10:])
    self.assertApproxNumpy(mid10,binflux[5000:5010])
    
  def test_binedges(self):
    front10 = np.array([  999.5,  1000.5,  1001.5,  1002.5,  1003.5,  1004.5,  1005.5,
        1006.5,  1007.5,  1008.5])
    back10 = np.array([ 10991.5,  10992.5,  10993.5,  10994.5,  10995.5,  10996.5,
        10997.5,  10998.5,  10999.5,  11000.5])
    mid10 = np.array([ 5999.5,  6000.5,  6001.5,  6002.5,  6003.5,  6004.5,  6005.5,
        6006.5,  6007.5,  6008.5])
        
    bin_edges = self.obs._bin_edges
    
    self.assertEqualNumpy(front10,bin_edges[:10])
    self.assertEqualNumpy(back10,bin_edges[-10:])
    self.assertEqualNumpy(mid10,bin_edges[5000:5010])
    