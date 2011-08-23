import unittest
import nose.tools

import pysynphot as S
import pysynphot.exceptions as exceptions

# test the spectrum.ObsModeBandpass.pixel_range() method
class TestPixelRange(unittest.TestCase):
  def setUp(self):
    self.bp = S.ObsBandpass('acs,hrc,f555w')
    
  def test_round_exception(self):
    self.assertRaises(ValueError, self.bp.pixel_range, (5000,5001), round='up')
    
  def test_low_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, self.bp.pixel_range, (500,5001))
    
  def test_high_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, self.bp.pixel_range, (5000,50010))
    
  def test_pixel_range_round_return0(self):
    num = self.bp.pixel_range((5000,5000),round='round')
    self.assertEqual(num,0)
  
  def test_pixel_range_round_return1(self):
    num = self.bp.pixel_range((4999.5,5000.5),round='round')
    self.assertEqual(num,1)
  
  def test_pixel_range_round_return2(self):
    num = self.bp.pixel_range((5000,5002),round='round')
    self.assertEqual(num,2)
    
  def test_pixel_range_round_return9(self):
    num = self.bp.pixel_range((4999.6,5008.8),round='round')
    self.assertEqual(num,9)
  
  def test_pixel_range_min_return1(self):
    num = self.bp.pixel_range((5000,5002),round='min')
    self.assertEqual(num,1)
  
  def test_pixel_range_min_return2(self):
    num = self.bp.pixel_range((5000.5,5002.5),round='min')
    self.assertEqual(num,2)
    
  def test_pixel_range_min_return3(self):
    num = self.bp.pixel_range((5000.5,5004.4),round='min')
    self.assertEqual(num,3)
    
  def test_pixel_range_min_return4(self):
    num = self.bp.pixel_range((5000.2,5004.5),round='min')
    self.assertEqual(num,4)
    
  def test_pixel_range_max_return1(self):
    num = self.bp.pixel_range((5000,5000.1),round='max')
    self.assertEqual(num,1)
    
  def test_pixel_range_max_return2(self):
    num = self.bp.pixel_range((5000.5,5002.5),round='max')
    self.assertEqual(num,2)
    
  def test_pixel_range_max_return3(self):
    num = self.bp.pixel_range((5000.5,5002.6),round='max')
    self.assertEqual(num,3)
    
  def test_pixel_range_max_return4(self):
    num = self.bp.pixel_range((5001.2,5004.5),round='max')
    self.assertEqual(num,4)
    
  def test_pixel_range_None_return01(self):
    num = self.bp.pixel_range((5000,5000.1),round=None)
    nose.tools.assert_almost_equal(num,0.1)
    
  def test_pixel_range_None_return02(self):
    num = self.bp.pixel_range((4999.8,5000),round=None)
    nose.tools.assert_almost_equal(num,0.2)
    
  def test_pixel_range_None_return6(self):
    num = self.bp.pixel_range((5000.5,5006.5),round=None)
    nose.tools.assert_almost_equal(num,6)
    
  def test_pixel_range_None_return8(self):
    num = self.bp.pixel_range((5000,5008),round=None)
    nose.tools.assert_almost_equal(num,8)
    
  def test_waveunits(self):
    num = self.bp.pixel_range((499.95,500.05),waveunits='nm',round='round')
    self.assertEqual(num,1)
    
# test the spectrum.ObsModeBandpass.wave_range() method
class TestWaveRange(unittest.TestCase):
  def setUp(self):
    self.bp = S.ObsBandpass('acs,hrc,f555w')
    
  def test_round_exception(self):
    self.assertRaises(ValueError, self.bp.wave_range, 5000, 100, round='up')
    
  def test_low_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, self.bp.wave_range, 1000, 100)
    
  def test_high_wave_exception(self):
    self.assertRaises(exceptions.OverlapError, self.bp.wave_range, 11000, 100)
    
  def test_wave_range_None_0(self):
    w1, w2 = self.bp.wave_range(5000.4,0,round=None)
    self.assertEqual(w1,w2)
    
  def test_wave_range_None_2(self):
    w1, w2 = self.bp.wave_range(5000,2,round=None)
    self.assertEqual(w1,4999)
    self.assertEqual(w2,5001)
    
  def test_wave_range_None_3(self):
    w1, w2 = self.bp.wave_range(5000.25,3,round=None)
    self.assertEqual(w1,4998.75)
    self.assertEqual(w2,5001.75)
    
  def test_wave_range_None_4(self):
    w1, w2 = self.bp.wave_range(5000.5,4,round=None)
    self.assertEqual(w1,4998.5)
    self.assertEqual(w2,5002.5)
  
  def test_wave_range_round_1(self):
    w1, w2 = self.bp.wave_range(5002,1,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5002.5)

  def test_wave_range_round_2(self):
    w1, w2 = self.bp.wave_range(5005,2,round='round')
    self.assertEqual(w1,5004.5)
    self.assertEqual(w2,5006.5)

  def test_wave_range_round_3(self):
    w1, w2 = self.bp.wave_range(5005,3,round='round')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5006.5)
    
  def test_wave_range_round_4(self):
    w1, w2 = self.bp.wave_range(5004.25,4,round='round')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5006.5)
    
  def test_wave_range_round_5(self):
    w1, w2 = self.bp.wave_range(5004.25,5,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5006.5)
    
  def test_wave_range_round_6(self):
    w1, w2 = self.bp.wave_range(5004.5,6,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5007.5)
    
  def test_wave_range_round_7(self):
    w1, w2 = self.bp.wave_range(5004.5,7,round='round')
    self.assertEqual(w1,5001.5)
    self.assertEqual(w2,5008.5)
    
  def test_wave_range_min_1(self):
    w1, w2 = self.bp.wave_range(5004,1,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5004.5)
    
  def test_wave_range_min_2(self):
    w1, w2 = self.bp.wave_range(5004,2,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5004.5)
    
  def test_wave_range_min_3(self):
    w1, w2 = self.bp.wave_range(5004,3,round='min')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5005.5)
    
  def test_wave_range_min_4(self):
    w1, w2 = self.bp.wave_range(5006.25,4,round='min')
    self.assertEqual(w1,5004.5)
    self.assertEqual(w2,5007.5)
    
  def test_wave_range_min_5(self):
    w1, w2 = self.bp.wave_range(5006.25,5,round='min')
    self.assertEqual(w1,5004.5)
    self.assertEqual(w2,5008.5)
    
  def test_wave_range_min_6(self):
    w1, w2 = self.bp.wave_range(5006.5,6,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)
    
  def test_wave_range_min_7(self):
    w1, w2 = self.bp.wave_range(5006.5,7,round='min')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)
    
  def test_wave_range_max_1(self):
    w1, w2 = self.bp.wave_range(5004,1,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5004.5)
    
  def test_wave_range_max_2(self):
    w1, w2 = self.bp.wave_range(5004,2,round='max')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5005.5)
    
  def test_wave_range_max_3(self):
    w1, w2 = self.bp.wave_range(5004,3,round='max')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5005.5)
    
  def test_wave_range_max_4(self):
    w1, w2 = self.bp.wave_range(5006.25,4,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5008.5)
    
  def test_wave_range_max_5(self):
    w1, w2 = self.bp.wave_range(5006.25,5,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)
    
  def test_wave_range_max_6(self):
    w1, w2 = self.bp.wave_range(5006.5,6,round='max')
    self.assertEqual(w1,5003.5)
    self.assertEqual(w2,5009.5)
    
  def test_wave_range_max_7(self):
    w1, w2 = self.bp.wave_range(5006.5,7,round='max')
    self.assertEqual(w1,5002.5)
    self.assertEqual(w2,5010.5)

  def test_waveunits(self):
    w1, w2 = self.bp.wave_range(500,2,waveunits='nm',round=None)
    self.assertEqual(w1,499.9)
    self.assertEqual(w2,500.1)
