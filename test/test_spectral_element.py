import numpy as np

import pysynphot.spectrum as spec

# test that SpectralElement.sample respects internal units
def test_sample_units():
  defwave = np.linspace(0.1, 1, 10)
  defthru = defwave
  
  s = spec.ArraySpectralElement(defwave, defthru, 'm', 'TestArray')
  
  angwave = defwave * 1.e10
  
  np.testing.assert_allclose(s(angwave), s.sample(defwave))
