from __future__ import absolute_import, division, print_function

import os

import pytest
from numpy.testing import assert_allclose, assert_array_equal

from .utils import use_cdbs
from ..exceptions import OverlapError
from ..obsbandpass import ObsBandpass, pixel_range, wave_range
from ..refs import setref


@use_cdbs
class TestObsBandpass(object):
    def setup_class(self):
        self.bp = ObsBandpass('acs,hrc,f555w')
        self.bins = self.bp.binset

    def test_exceptions(self):
        with pytest.raises(ValueError):
            pixel_range(self.bins, (5000, 5001), round='up')  # rounding
        with pytest.raises(OverlapError):
            pixel_range(self.bins, (500, 5001))  # low wave
        with pytest.raises(OverlapError):
            pixel_range(self.bins, (5000, 50010))  # high wave

        with pytest.raises(ValueError):
            wave_range(self.bins, 5000, 100, round='up')  # rounding
        with pytest.raises(OverlapError):
            wave_range(self.bins, 1000, 100)  # low wave
        with pytest.raises(OverlapError):
            wave_range(self.bins, 11000, 100)  # high wave

    @pytest.mark.parametrize(
      ('args', 'rnd', 'ans'),
      [((5000, 5000), 'round', 0),
       ((4999.5, 5000.5), 'round', 1),
       ((5000, 5002), 'round', 2),
       ((4999.6, 5008.8), 'round', 9),
       ((5000, 5002), 'min', 1),
       ((5000.5, 5002.5), 'min', 2),
       ((5000.5, 5004.4), 'min', 3),
       ((5000.2, 5004.5), 'min', 4),
       ((5000, 5000.1), 'max', 1),
       ((5000.5, 5002.5), 'max', 2),
       ((5000.5, 5002.6), 'max', 3),
       ((5001.2, 5004.5), 'max', 4)])
    def test_pixel_range(self, args, rnd, ans):
        num = pixel_range(self.bins, args, round=rnd)
        assert num == ans

    @pytest.mark.parametrize(
      ('args', 'ans'),
      [((5000, 5000.1), 0.1),
       ((4999.8, 5000), 0.2),
       ((5000.5, 5006.5), 6),
       (((5000, 5008), 8))])
    def test_pixel_range_none(self, args, ans):
        num = pixel_range(self.bins, args, round=None)
        assert_allclose(num, ans)

    def test_wave_range_eq_out(self):
        w1, w2 = wave_range(self.bins, 5000.4, 0, round=None)
        assert w1 == w2

    @pytest.mark.parametrize(
        ('cenwave', 'npix', 'rnd', 'ans'),
        [(5000, 2, None, (4999, 5001)),
         (5000.25, 3, None, (4998.75, 5001.75)),
         (5000.5, 4, None, (4998.5, 5002.5)),
         (5002, 1, 'round', (5001.5, 5002.5)),
         (5005, 2, 'round', (5004.5, 5006.5)),
         (5005, 3, 'round', (5003.5, 5006.5)),
         (5004.25, 4, 'round', (5002.5, 5006.5)),
         (5004.25, 5, 'round', (5001.5, 5006.5)),
         (5004.5, 6, 'round', (5001.5, 5007.5)),
         (5004.5, 7, 'round', (5001.5, 5008.5)),
         (5004, 1, 'min', (5003.5, 5004.5)),
         (5004, 2, 'min', (5003.5, 5004.5)),
         (5004, 3, 'min', (5002.5, 5005.5)),
         (5006.25, 4, 'min', (5004.5, 5007.5)),
         (5006.25, 5, 'min', (5004.5, 5008.5)),
         (5006.5, 6, 'min', (5003.5, 5009.5)),
         (5006.5, 7, 'min', (5003.5, 5009.5)),
         (5004, 1, 'max', (5003.5, 5004.5)),
         (5004, 2, 'max', (5002.5, 5005.5)),
         (5004, 3, 'max', (5002.5, 5005.5)),
         (5006.25, 4, 'max', (5003.5, 5008.5)),
         (5006.25, 5, 'max', (5003.5, 5009.5)),
         (5006.5, 6, 'max', (5003.5, 5009.5)),
         (5006.5, 7, 'max', (5002.5, 5010.5))])
    def test_wave_range(self, cenwave, npix, rnd, ans):
        w = wave_range(self.bins, cenwave, npix, round=rnd)
        assert_array_equal(w, ans)

    def test_pixel_range_method(self):
        num = self.bp.pixel_range(
            (499.95, 500.05), waveunits='nm', round='round')
        assert num == 1

    def test_wave_range_method(self):
        w = self.bp.wave_range(500, 2, waveunits='nm', round=None)
        assert_array_equal(w, (499.9, 500.1))


@use_cdbs
class TestUnitResponse(object):
    """
    Test the spectrum.SpectralElement.unit_response method as
    it is run by obsbandpass.ObsModeBandpass objects.
    Results are compared to synphot bandpar.
    """
    def setup_class(self):
        path = os.environ['PYSYN_CDBS']
        graphtab = os.path.join(
            path, 'mtab', 'OLD_FILES', 'u921351jm_tmg.fits')
        comptab = os.path.join(
            path, 'mtab', 'OLD_FILES', 'v8h1925fm_tmc.fits')
        thermtab = os.path.join(
            path, 'mtab', 'OLD_FILES', 'tae17277m_tmt.fits')
        setref(graphtable=graphtab, comptable=comptab, thermtable=thermtab)

    def teardown_class(self):
        setref()

    @pytest.mark.parametrize(
        ('obsmode', 'ans'),
        [('acs,hrc,f555w', 3.0074E-19),
         ('acs,wfc1,f555w,f814w', 1.7308E-13),
         ('acs,sbc,f125lp', 1.7218E-17),
         ('wfc3,uvis1,f395n', 5.9579E-18),
         ('wfc3,uvis2,fq924n', 6.9039E-18),
         ('wfc3,ir,f140w', 1.4574E-20),
         ('wfpc2,f555w', 4.8968E-19),
         ('cos,boa,fuv,g130m,c1309', 3.5520E-15),
         ('stis,ccd,f25ndq1,a2d4,mjd#55555', 3.0650E-18)])
    def test_uresp(self, obsmode, ans):
        bp = ObsBandpass(obsmode)
        val = bp.unit_response()
        assert_allclose(val, ans, rtol=1E-4)
