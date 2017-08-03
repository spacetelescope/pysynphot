"""Tests for the observation.Observation class."""
from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_equal

from .utils import use_cdbs
from ..observation import Observation
from ..obsbandpass import ObsBandpass
from ..spectrum import ArraySourceSpectrum, Box, FlatSpectrum
from ..spparser import parse_spec


@use_cdbs
class TestBinFlux(object):
    """Test the Observation.initbinflux method."""
    def setup_class(self):
        path = os.environ['PYSYN_CDBS']
        tmg = os.path.join(path, 'mtab', 'OLD_FILES', 'u921351jm_tmg.fits')
        tmc = os.path.join(path, 'mtab', 'OLD_FILES', 'ub31649mm_tmc.fits')

        spec = FlatSpectrum(1, fluxunits='flam')
        self.bp = ObsBandpass('acs,hrc,f555w', graphtable=tmg, comptable=tmc)

        self.obs = Observation(spec, self.bp)
        self.obs.initbinflux()

    def test_binflux(self):
        front10 = np.zeros(10)
        back10 = np.zeros(10)
        mid10 = np.array([
            0.12265425, 0.12226972, 0.12184207, 0.12141429, 0.12098646,
            0.1205586, 0.1201307, 0.11970269, 0.11927488, 0.11884699])

        assert_array_equal(front10, self.obs.binflux[:10])
        assert_array_equal(back10, self.obs.binflux[-10:])
        assert_allclose(mid10, self.obs.binflux[5000:5010])

    def test_binedges(self):
        front10 = np.array([
            999.5, 1000.5, 1001.5, 1002.5, 1003.5, 1004.5, 1005.5, 1006.5,
            1007.5, 1008.5])
        back10 = np.array([
            10991.5, 10992.5, 10993.5, 10994.5, 10995.5, 10996.5, 10997.5,
            10998.5, 10999.5, 11000.5])
        mid10 = np.array([
            5999.5, 6000.5, 6001.5, 6002.5, 6003.5, 6004.5, 6005.5, 6006.5,
            6007.5, 6008.5])
        bin_edges = self.obs._bin_edges

        assert_array_equal(front10, bin_edges[:10])
        assert_array_equal(back10, bin_edges[-10:])
        assert_array_equal(mid10, bin_edges[5000:5010])

    def test_obs_binset_roundtrip(self):
        """
        Test for changes in Trac Ticket #198.
        Test the bandpass.binset is the same as the Observation.binwave.
        Should be since one comes from the other.
        Also verifies that the bandpass has the .binset attribute,
        which is new in the fix to this ticket.
        """
        assert_array_equal(self.bp.binset, self.obs.binwave)


@use_cdbs
class TestPixelWaveRangeMethods(object):
    """Test the Observation.pixel_range() and .wave_range() methods."""
    def setup_class(self):
        bp = ObsBandpass('acs,hrc,f555w')
        spec = FlatSpectrum(1)
        self.obs = Observation(spec, bp)

    def test_pixel_range_waveunits(self):
        num = self.obs.pixel_range(
          (499.95, 500.05), waveunits='nm', round='round')
        assert num == 1

    def test_wave_range_waveunits(self):
        w = self.obs.wave_range(500, 2, waveunits='nm', round=None)
        assert_array_equal(w, (499.9, 500.1))


class TestArithmetic(object):
    """Test the multiplication (supported) and addition (disabled)."""
    def setup_class(self):
        sp = FlatSpectrum(1, fluxunits='counts')
        bp = Box(5000, 100)

        # It has been found that obs.binflux is very sensitive to Box
        # waveset for this sp and bp combo. It is best to use the larger
        # Box waveset rather than some arbitrary array.
        # In fact, the answers in this test do not look correct (even
        # prior to fixing Box in Sep 2016), but at least they are
        # consistently wrong.
        # Since such a combo is not used in science, we do not really care.
        self.bigbox = Box(5000, 1000)

        self.obs = Observation(sp, bp, binset=self.bigbox.wave)
        self.obs.convert('counts')

    def test_cls(self):
        assert isinstance(self.obs, Observation)

    def test_mult_scalar(self):
        tst = self.obs * 3
        assert_allclose(tst.sample(5000), 3 * self.obs.sample(5000))
        assert tst.sample(4499.99) == 0

    def test_mult_band(self):
        tst = self.obs * (self.bigbox * 5)
        assert_allclose(tst.sample(5000), 5 * self.obs.sample(5000))
        assert tst.sample(4499.99) == 0

    def test_not_allowed(self):
        # Scalar
        with pytest.raises(NotImplementedError):
            self.obs + 3

        # Another spectrum
        wv = np.arange(1000, 10000, 1)
        other = ArraySourceSpectrum(
            wave=wv, flux=np.zeros(wv.shape)+10,
            waveunits='angstroms', fluxunits='counts')
        with pytest.raises(NotImplementedError):
            self.obs + other


@use_cdbs
def test_no_neg_leak():
    """
    Test that negative leak is no longer possible.
    https://github.com/spacetelescope/pysynphot/issues/43
    """
    sp = parse_spec(
        'rn(icat(k93models,44500,0.0,5.0),box(2000.000000,1.),1e-10,flam)')
    bp = ObsBandpass('stis,fuvmama,mirror,F25NDQ2,MJD#58300.0822774')
    obs = Observation(sp, bp)
    c_all = obs.countrate()
    c_sub = obs.countrate(range=[1160.22, 12000.0])
    assert c_sub <= c_all
