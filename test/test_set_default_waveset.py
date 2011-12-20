import numpy.testing as nptest

from pysynphot import refs

def test_log_num():
  refs.set_default_waveset(10, 20, 10)
  
  testref = [ 10.        ,  10.80059739,  11.6652904 ,  12.5992105 ,
              13.6079    ,  14.69734492,  15.87401052,  17.14487966,
              18.51749425,  20.        ]
           
  nptest.assert_allclose(testref,refs._default_waveset)
  
  refs.setref(waveset=(10, 20, 10))
  
  nptest.assert_allclose(testref,refs._default_waveset)
  
  refs.setref(waveset=(10, 20, 10, 'log'))
  
  nptest.assert_allclose(testref,refs._default_waveset)


def test_log_delta():
  refs.set_default_waveset(10, 20, delta=0.05)
  
  testref = [ 10.        ,  11.22462048,  12.5992105 ,  14.14213562,
              15.87401052,  17.81797436,  20.        ]
              
  nptest.assert_allclose(testref,refs._default_waveset)
  
  
def test_linear_num():
  refs.set_default_waveset(10, 20, 11, log=False)
  
  testref = [ 10.,  11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.,  20.]
              
  nptest.assert_array_equal(refs._default_waveset, testref)
  
  refs.setref(waveset=(10, 20, 11, 'linear'))
  
  nptest.assert_allclose(testref,refs._default_waveset)


def test_linear_delta():
  refs.set_default_waveset(10, 20, delta=1, log=False)
  
  testref = [ 10.,  11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.,  20.]
              
  nptest.assert_array_equal(refs._default_waveset, testref)
