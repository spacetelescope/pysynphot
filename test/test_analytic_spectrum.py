import numpy as np

import testutil

import pysynphot as S

class TestPowerLaw(testutil.FPTestCase):
  def setUp(self):
    self.wave = S.Waveset(3000,5000,10)
  
  def test_conversion1(self):
    pl = S.PowerLaw(6000,-4,'angstrom','photlam')
    
    angflux = pl.sample(self.wave)
    
    pl.convert('nm')
    
    nmflux = pl.sample(self.wave/10.)
    
    self.assertEqualNumpy(nmflux,angflux)
    
  def test_conversion2(self):
    pl = S.PowerLaw(6000,-4,'angstrom','photlam')
    
    self.assertEqualNumpy(pl.sample(self.wave)[:10],pl.sample(self.wave[:10]))
    
    pl.convert('nm')
    
    self.assertEqualNumpy(pl.sample(self.wave)[:10],pl.sample(self.wave[:10]))
    

class TestGaussian(testutil.FPTestCase):
  def setUp(self):
    self.wave = S.Waveset(3000,5000,10)
  
  def test_conversion1(self):
    g = S.GaussianSource(1,4000,100,'angstrom','photlam')
    
    angflux = g.sample(self.wave)
    
    g.convert('nm')
    
    nmflux = g.sample(self.wave/10.)
    
    self.assertEqualNumpy(nmflux,angflux)
    
  def test_conversion2(self):
    g = S.GaussianSource(1,4000,100,'angstrom','photlam')
    
    self.assertEqualNumpy(g.sample(self.wave)[:10],g.sample(self.wave[:10]))
    
    g.convert('nm')
    
    self.assertEqualNumpy(g.sample(self.wave)[:10],g.sample(self.wave[:10]))
    
  def test_conversion3(self):
    g = S.GaussianSource(1,4000,100,'angstrom','photlam')
    
    tf1 = g.total_flux
    
    g.convert('nm')
    
    tf2 = g.factor * g.sigma * np.sqrt(2.0 * np.pi)
    
    self.assertEqual(tf1,tf2)
    
class TestFlatSpec(testutil.FPTestCase):
  def setUp(self):
    self.wave = S.Waveset(3000,5000,10)
  
  def test_conversion1(self):
    f = S.FlatSpectrum(1,'angstrom','photlam')
    
    angflux = f.sample(self.wave)
    
    f.convert('nm')
    
    nmflux = f.sample(self.wave/10.)
    
    self.assertEqualNumpy(nmflux,angflux)
    
  def test_conversion2(self):
    f = S.FlatSpectrum(1,'angstrom','photlam')
    
    self.assertEqualNumpy(f.sample(self.wave)[:10],f.sample(self.wave[:10]))
    
    f.convert('nm')
    
    self.assertEqualNumpy(f.sample(self.wave)[:10],f.sample(self.wave[:10]))
