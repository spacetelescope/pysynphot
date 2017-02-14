from __future__ import absolute_import, division, print_function

import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_equal

from .. import extinction, refs
from ..binning import calculate_bin_widths, calculate_bin_edges
from ..spectrum import ArraySourceSpectrum, BlackBody, FlatSpectrum
from ..units import Angstrom, Counts, InverseMicron, OBMag, Photlam, Units

awave = refs._default_waveset.copy()[::10][0:10]
aflux = np.ones(awave.shape)


class BaseUnitStr(object):
    """Base class to test unit string."""
    def test_str(self):
        assert str(self.x) == self.unit_str


class TestInverseMicron(BaseUnitStr):
    def setup_class(self):
        self.unit_str = '1/um'
        self.x = Units(self.unit_str)
        self.mwave = extinction._buildDefaultWaveset()[0:10]
        self.awave = awave

    def test_unittoang(self):
        tst = self.x.Convert(self.mwave, 'angstrom')
        assert_allclose(tst, self.awave)

    def test_unitfromang(self):
        ang = Units('angstrom')
        for s in ('1/um', 'InverseMicron', 'inversemicrons'):
            tst = ang.Convert(self.awave, s)
            assert_allclose(tst, self.mwave)

    def test_fromang(self):
        tst = ArraySourceSpectrum(wave=self.awave,
                                  flux=aflux,
                                  waveunits='angstrom',
                                  fluxunits='flam')
        tst.convert('1/um')
        assert isinstance(tst.waveunits, InverseMicron)
        assert_allclose(tst.wave, self.mwave)

    def test_create(self):
        tst = ArraySourceSpectrum(wave=self.mwave,
                                  flux=aflux,
                                  waveunits='1/um',
                                  fluxunits='flam')
        assert isinstance(tst.waveunits, InverseMicron)
        assert_array_equal(tst.wave, self.mwave)

        tst.convert('angstrom')
        assert isinstance(tst.waveunits, Angstrom)
        assert_allclose(tst.wave, self.awave)


class BasePfxJy(object):
    """Base class to test ujy and njy."""

    def test_unittophotlam(self):
        """Verify that the conversion from muJy to photlam is correct."""
        tst = self.x.ToPhotlam(self.awave, self.flux)
        assert_allclose(self.ref_photlam, tst)

    def test_fromphotlam1(self):
        """Verify that the conversion from photlam to muJy is correct."""
        photlam = Units('photlam')
        for s in self.aliases:
            tst = photlam.Convert(self.awave, self.flux, s)
            assert_allclose(tst, self.ref_val)


class TestmuJy(BasePfxJy, BaseUnitStr):
    """
    Tests certain attributes of the micro Jansky (muJy)
    class, including how the units are referenced, and
    the conversion to and from.

    Partial fulfillment of Trac Ticket #102.
    """
    def setup_class(self):
        self.unit_str = 'mujy'
        self.aliases = (self.unit_str, 'microjy', 'ujy')
        self.x = Units(self.unit_str)

        # Create a 10 element array of simulated wavelength values in Angstroms
        self.awave = awave

        # Creates a 10 element array of ones
        self.flux = aflux

        # Create reference values based on Jansky class to
        # be used in verifying the Micro Jansky class
        self.ref_photlam = (Units('jy').ToPhotlam(self.awave, self.flux) *
                            (1.0e-6))

        self.ref_val = Units('photlam').ToJy(self.awave, self.flux) * (1.0e6)


class TestnJy(BasePfxJy, BaseUnitStr):
    """
    Tests certain attributes of the nano Jansky (nJy)
    class, including how the units are referenced, and
    the conversion to and from.

    Partial fulfillment of Trac Ticket #102.
    """
    def setup_class(self):
        self.unit_str = 'njy'
        self.aliases = (self.unit_str, 'nanojy')
        self.x = Units(self.unit_str)

        # Create a 10 element array of simulated wavelength values in Angstroms
        self.awave = awave

        # Creates a 10 element array of ones
        self.flux = aflux

        # Create reference values based on Jansky class to
        # be used in verifying the Nano Jansky class
        self.ref_photlam = (Units('jy').ToPhotlam(self.awave, self.flux) *
                            (1.0e-9))

        self.ref_val = Units('photlam').ToJy(self.awave, self.flux) * (1.0e9)


class TestXJanskyTypicalUse(object):
    """
    Tests normal use attributes of the muJy and nJy classes in
    relation to a larger portion of the code base, to verify
    output, from a broader perspective, and values as they
    should appear, based on how the functions within the classes
    are referenced and how they are converted.

    Partial fulfillment of Trac Ticket #102.
    """
    def setup_class(self):
        self.bb = BlackBody(5500)
        self.bb.convert('jy')
        self.wave = self.bb.wave
        self.flux = self.bb.flux

    @pytest.mark.parametrize(
        ('fac', 'unit_str'),
        [(1.0e6, 'mujy'),
         (1.0e9, 'njy')])
    def test_convert(self, fac, unit_str):
        self.bb.convert(unit_str)
        assert_allclose(self.bb.wave, self.wave)
        assert_allclose(self.bb.flux, self.flux * fac)

    @pytest.mark.parametrize(
        ('unit_str', 'ref_units'),
        [('mujy', 'mujy'),
         ('microjy', 'mujy'),
         ('ujy', 'mujy'),
         ('njy', 'njy'),
         ('nanojy', 'njy')])
    def test_unitstring1(self, unit_str, ref_units):
        self.bb.convert(unit_str)
        assert str(self.bb.fluxunits) == ref_units

    def test_fluxattribute(self):
        self.bb.convert('mujy')
        mflux = self.bb.flux

        self.bb.convert('njy')
        nflux = self.bb.flux

        assert_allclose(np.mean(nflux / mflux), 1000)


def test_flat_spectrum():
    """Test unit conversion of a FlatSpectrum."""
    f = FlatSpectrum(1, fluxunits='photlam')
    f.convert('counts')
    delta_wave = calculate_bin_widths(calculate_bin_edges(f.wave))

    assert_allclose(delta_wave * refs.PRIMARY_AREA, f.sample(f.wave))

    f.primary_area = 100.0
    assert_allclose(delta_wave * 100, f.sample(f.wave))


class TestConvWithArea(object):
    """Test the flux unit conversion methods that take area arguments."""
    def setup_class(self):
        self.wave = refs._default_waveset
        self.flux = np.ones_like(self.wave)
        self.delta_wave = calculate_bin_widths(calculate_bin_edges(self.wave))

    @pytest.mark.parametrize(
        ('area', 'refs_area'),
        [(1.0, 1),
         (None, refs.PRIMARY_AREA)])
    def test_photlam(self, area, refs_area):
        p = Photlam()

        ref = -1.085736 * np.log(self.flux * self.delta_wave * refs_area)
        tst = p.ToOBMag(self.wave, self.flux, area=area)
        assert_allclose(ref, tst)

        ref = self.flux * self.delta_wave * refs_area
        tst = p.ToCounts(self.wave, self.flux, area=area)
        assert_allclose(ref, tst)

    @pytest.mark.parametrize(
        ('area', 'refs_area'),
        [(1.0, 1),
         (None, refs.PRIMARY_AREA)])
    def test_obmag(self, area, refs_area):
        ob = OBMag()

        ref = 10.0 ** (-0.4 * self.flux) / (self.delta_wave * refs_area)
        tst = ob.ToPhotlam(self.wave, self.flux, area=area)
        assert_allclose(ref, tst)

    @pytest.mark.parametrize(
        ('area', 'refs_area'),
        [(1.0, 1),
         (None, refs.PRIMARY_AREA)])
    def test_counts(self, area, refs_area):
        counts = Counts()

        ref = self.flux / (self.delta_wave * refs_area)
        tst = counts.ToPhotlam(self.wave, self.flux, area=area)
        assert_allclose(ref, tst)
