from __future__ import absolute_import, division, print_function

import os

import numpy as np
from astropy.utils.data import get_pkg_data_filename
from numpy.testing import assert_array_equal

from .utils import use_cdbs
from ..spectrum import (ArraySourceSpectrum, BlackBody, FileSourceSpectrum,
                        FlatSpectrum, GaussianSource, Powerlaw)
from ..units import WaveUnits, FluxUnits


def test_fits_header():
    sp = FileSourceSpectrum(get_pkg_data_filename(os.path.join(
        'data', 'alpha_lyr_stis_002.fits')))
    # This also naturally tests for len(sp.fheader) > 0
    assert sp.fheader['TARGETID'] == 'ALPHA_LYR'


class BaseSpec(object):
    """Base class for source spectrum tests."""

    def test_attr_cls(self):
        assert isinstance(self.sp.wave, np.ndarray)
        assert isinstance(self.sp.flux, np.ndarray)
        assert isinstance(self.sp.waveunits, WaveUnits)
        assert isinstance(self.sp.fluxunits, FluxUnits)
        assert isinstance(self.sp(np.arange(3000, 10000)), np.ndarray)

    def test_call(self):
        self.sp.convert('fnu')
        midpoint = len(self.sp.flux) // 2
        assert self.sp.flux[midpoint] != self.sp(self.sp.wave)[midpoint]

        self.sp.convert('photlam')
        assert_array_equal(self.sp.flux, self.sp(self.sp.wave))


class TestZeroFlux(BaseSpec):
    def setup_class(self):
        self.sp = ArraySourceSpectrum(
            np.arange(3000, 6000, 500),
            np.array([1.0, 0.5, 0.2, 0.0, 0.0, 0.0]) * 1e-14,
            fluxunits='flam')

    def test_call(self):
        """0 flam does indeed equal 0 fnu"""
        self.sp.convert('fnu')
        midpoint = len(self.sp.flux) // 2
        assert self.sp.flux[midpoint] == self.sp(self.sp.wave)[midpoint]


class TestNegFlux(BaseSpec):
    def setup_class(self):
        self.sp = ArraySourceSpectrum(
            np.arange(3000, 6000, 500),
            np.array([1.0, 0.5, 0.2, 0.1, -0.1, -0.3]) * 1e-14,
            fluxunits='flam')


class TestGaussian(BaseSpec):
    def setup_class(self):
        self.sp = GaussianSource(1e-12, 5000, 30)


class TestUnitSpec(BaseSpec):
    def setup_class(self):
        self.sp = FlatSpectrum(10)


class TestPowerLaw(BaseSpec):
    def setup_class(self):
        self.sp = Powerlaw(6000, 3)


class TestBlackBody(BaseSpec):
    def setup_class(self):
        self.sp = BlackBody(60000)


class TestCompositeAnalytic(BaseSpec):
    def setup_class(self):
        self.sp = BlackBody(60000) + GaussianSource(1e-12, 5000, 30)


@use_cdbs
class TestFileSpec(BaseSpec):
    def setup_class(self):
        self.sp = FileSourceSpectrum(os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'alpha_lyr_stis_003.fits'))


@use_cdbs
class TestNegFlam(BaseSpec):
    def setup_class(self):
        self.sp = FileSourceSpectrum(os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'vb8_stisnic_001.fits'))


@use_cdbs
class TestNegMag(BaseSpec):
    def setup_class(self):
        self.sp = FileSourceSpectrum(os.path.join(
            os.environ['PYSYN_CDBS'], 'calobs', 'alpha_lyr_006.fits'))


@use_cdbs
class TestCompositeFile(BaseSpec):
    def setup_class(self):
        comp1 = FileSourceSpectrum(os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'alpha_lyr_stis_003.fits'))
        self.sp = comp1 + FlatSpectrum(10)
