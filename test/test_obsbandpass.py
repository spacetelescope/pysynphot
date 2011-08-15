import unittest

import pysynphot as S

# test the spectrum.ObsModeBandpass.pixel_range() method
class TestPixelRange(unittest.TestCase):
  def setUp(self):
    self.bp = S.ObsBandpass('acs,hrc,f555w')
    
  def test_round_exception(self):
    self.assertRaises(ValueError, self.bp.pixel_range, (5000,5001), round='up')
    
  def test_low_wave_exception(self):
    self.assertRaises(ValueError, self.bp.pixel_range, (500,5001))
    
  def test_high_wave_exception(self):
    self.assertRaises(ValueError, self.bp.pixel_range, (5000,50010))
    
  def test_pixel_range_round_return0(self):
    num = self.bp.pixel_range((5000,5000),round='round')
    self.assertEqual(num,0)
  
  def test_pixel_range_round_return1(self):
    num = self.bp.pixel_range((4999.5,5000.5),round='round')
    self.assertEqual(num,1)
  
  def test_pixel_range_round_return2(self):
    num = self.bp.pixel_range((5000,5001),round='round')
    self.assertEqual(num,2)
    
  def test_pixel_range_round_return9(self):
    num = self.bp.pixel_range((4999.6,5008.8),round='round')
    self.assertEqual(num,9)
    
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
    self.assertRaises(ValueError, self.bp.wave_range, 1000, 100)
    
  def test_high_wave_exception(self):
    self.assertRaises(ValueError, self.bp.wave_range, 11000, 100)
