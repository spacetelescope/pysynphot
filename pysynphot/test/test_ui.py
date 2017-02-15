from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest
from astropy.io import fits
from numpy.testing import assert_array_equal, assert_allclose

from .utils import use_cdbs
from .. import units, refs
from ..obsbandpass import ObsBandpass
from ..spectrum import (MergeWaveSets, ArraySourceSpectrum, BlackBody, Box,
                        FileSourceSpectrum, FlatSpectrum,
                        TabularSourceSpectrum)


def test_merge_wave():
    """
    Demonstrate the problem described in Trac Ticket #34:
    Adding two identical tabular spectra loses a pixel in the resulting
    spectrum's table.
    """
    foo = np.arange(10, 20, dtype=np.float64)
    x = MergeWaveSets(foo, foo)
    assert_array_equal(foo, x)


def test_unit():
    """
    Converted to fnu, it should not be flat.
    Can't test against 1.0 because there's computations & some
    numerical issues.
    """
    uspec = FlatSpectrum(1.0, fluxunits='flam')
    uspec.convert('fnu')
    assert uspec.flux.mean() != 1.0


def test_units_exceptions():
    sp = BlackBody(30000)

    # Make sure waveunits are really waveunits
    with pytest.raises(TypeError):
        ArraySourceSpectrum(sp.wave, sp.flux, 'flam')

    # Make sure fluxunits are really fluxunits
    with pytest.raises(TypeError):
        ArraySourceSpectrum(sp.wave, sp.flux, 'angstrom', 'angstrom')


@use_cdbs
def test_band():
    """Comparison results were computed with r1j2146sm_tmc.fits"""
    old_comptable = refs.COMPTABLE
    refs.COMPTABLE = os.path.join(
        os.environ['PYSYN_CDBS'], 'mtab', 'OLD_FILES', 'r1j2146sm_tmc.fits')

    # Tests Trac Ticket #30 -- no error
    ObsBandpass('johnson,v')

    # Tests SVN commit r172
    bp1 = ObsBandpass('acs,hrc,f555w')
    assert len(bp1) == 6

    # Reset
    refs.COMPTABLE = old_comptable


@use_cdbs
class TestFile(object):
    def setup_class(self):
        self.fname = os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'feige66_002.fits')
        self.sp = FileSourceSpectrum(self.fname)
        self.openfits = fits.open(self.fname)

    def test_wave_flux(self):
        fitswave = self.openfits[1].data.field('wavelength')
        fitsflux = self.openfits[1].data.field('flux')
        assert_array_equal(self.sp.wave, fitswave)
        assert_allclose(self.sp.flux, fitsflux, rtol=1E-6)

    def test_name(self):
        assert str(self.sp) == self.fname
        assert self.sp.name == self.fname

    def test_resample(self):
        sp2 = self.sp.resample(np.arange(10000, 18000, 2))
        assert sp2.fluxunits is not None

    def test_add(self):
        sp2 = self.sp + self.sp
        sumflux = self.sp.flux + self.sp.flux
        assert_array_equal(sp2.flux, sumflux)

    def test_mul(self):
        bp = Box(3000, 50)
        sp1 = self.sp * bp
        sp2 = bp * self.sp
        assert_array_equal(sp1.flux, sp2.flux)

    def teardown_class(self):
        self.openfits.close()


class TestTabular(object):
    """Test new ArraySourceSpectrum inheriting from TabularSourceSpectrum"""
    def setup_class(self):
        self.inwave = np.arange(1300, 1800)
        self.influx = -2.5 * np.log10(self.inwave ** 2)
        self.sp = ArraySourceSpectrum(wave=self.inwave, flux=self.influx,
                                      fluxunits='abmag')

    def test_arrays(self):
        assert_allclose(self.inwave, self.sp.wave)
        assert_allclose(self.influx, self.sp.flux, rtol=1E-3)

    def test_units(self):
        assert isinstance(self.sp.waveunits, units.Angstrom)
        assert isinstance(self.sp.fluxunits, units.ABMag)

    def test_string(self):
        str(self.sp)  # No error

    def test_convert(self):
        old_unit = self.sp.fluxunits
        self.sp.convert('flam')
        assert not np.allclose(self.influx, self.sp.flux)
        self.sp.convert(old_unit)


class TestTab2(TestTabular):
    def setup_class(self):
        self.inwave = np.arange(1300, 1800)
        self.influx = np.random.lognormal(size=len(self.inwave)) * 1e-15
        self.sp = ArraySourceSpectrum(wave=self.inwave, flux=self.influx,
                                      waveunits='nm', fluxunits='fnu',
                                      name='Tab2 spectrum')

    def test_units(self):
        assert isinstance(self.sp.waveunits, units.Nm)
        assert isinstance(self.sp.fluxunits, units.Fnu)

    def test_string(self):
        assert str(self.sp) == 'Tab2 spectrum'


class BaseSpecComp(object):
    """Base class for the tests to follow."""
    def test_wave_flux(self):
        assert_array_equal(self.new_sp.wave, self.old_sp.wave)
        assert_array_equal(self.new_sp.flux, self.old_sp.flux)

        assert isinstance(self.new_sp.waveunits,
                          self.old_sp.waveunits.__class__)
        assert isinstance(self.new_sp.fluxunits,
                          self.old_sp.fluxunits.__class__)

        assert_array_equal(self.new_sp._wavetable, self.old_sp._wavetable)
        assert_array_equal(self.new_sp._fluxtable, self.old_sp._fluxtable)

    def testconvertflux(self):
        self.old_sp.convert('vegamag')
        self.new_sp.convert('vegamag')
        assert_array_equal(self.new_sp.flux, self.old_sp.flux)


@use_cdbs
class TestTab(BaseSpecComp):
    def setup_class(self):
        self.fname = os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'feige66_002.fits')
        self.old_sp = FileSourceSpectrum(self.fname)
        self.openfits = fits.open(self.fname)
        fdata = self.openfits[1].data
        self.new_sp = ArraySourceSpectrum(
            wave=fdata.field('wavelength'),
            flux=fdata.field('flux'),
            waveunits=self.openfits[1].header['tunit1'],
            fluxunits=self.openfits[1].header['tunit2'],
            name='table from feige66')

    def teardown_class(self):
        self.openfits.close()


@use_cdbs
class TestFSS(BaseSpecComp):
    """Test operations on a FileSource."""
    def setup_class(self):
        self.fname = os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'feige66_002.fits')
        self.old_sp = TabularSourceSpectrum(self.fname)
        self.new_sp = FileSourceSpectrum(self.fname)
