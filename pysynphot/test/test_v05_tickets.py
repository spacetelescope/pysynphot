from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest
from numpy.testing import assert_array_equal, assert_allclose

from .utils import use_cdbs
from .. import Cache, extinction
from ..obsbandpass import ObsBandpass
from ..reddening import Extinction, RedLaw
from ..spectrum import (ArraySourceSpectrum, ArraySpectralElement, BlackBody,
                        FlatSpectrum, SourceSpectrum, SpectralElement)
from ..spparser import parse_spec


@use_cdbs
def test_0000():
    """
    Some of the tests below will fail if this is not the FIRST
    set of tests to be run;they probe side effects on the Cache.
    """
    xt = Extinction(0.3, 'mwdense')
    assert isinstance(xt, SpectralElement)

    # test sideeffect of above
    xt = Cache.RedLaws['mwdense']
    assert isinstance(xt, RedLaw)

    xt = Cache.RedLaws['smcbar']
    if not xt.startswith('ftp'):
        assert os.path.isfile(xt)

    xt = Extinction(0.2, Cache.RedLaws['smcbar'])
    assert isinstance(xt, SpectralElement)

    xt = Extinction(0.3)
    assert isinstance(xt, SpectralElement)
    assert 'mwavg' in xt.name.lower()

    with pytest.raises(ValueError):
        Extinction(0.2, '/foo/bar.fits')


@use_cdbs
def test_smcbar():
    newsmc = Extinction(0.2, 'smcbar')
    tst = newsmc(np.array([5500, 5550, 5600]))
    assert tst[-1] > tst[0]
    assert_array_equal(newsmc.throughput, newsmc._throughputtable)


def test_integral():
    sp = BlackBody(30000)

    sp.convert('flam')
    sp.convert('Angstrom')
    wave, flux = sp.getArrays()
    ang = sp.trapezoidIntegration(wave, flux)

    sp.convert('fnu')
    sp.convert('hz')
    wave, flux = sp.getArrays()
    hz = sp.trapezoidIntegration(wave, flux)

    assert_allclose(ang, hz)


class TestTicket135Ordering(object):
    def setup_class(self):
        self.ascending = np.arange(10000, 10100, 10)
        self.thru = np.arange(10) + 5

    @pytest.mark.parametrize('step', [1, -1])
    def test_order(self, step):
        wave = self.ascending[::step]
        bp = ArraySpectralElement(wave=wave, throughput=self.thru)
        t = bp(wave[::-1])

        assert_array_equal(bp.throughput, bp._throughputtable)
        assert_array_equal(t, bp._throughputtable[::-1])
        assert_array_equal(bp.throughput, bp(bp.wave))


def test_ticket135_flip_sp():
    sp = BlackBody(30000)

    # create a spectrum with wavelength in descending order
    sp2 = ArraySourceSpectrum(wave=sp.wave[::-1],
                              flux=sp.flux[::-1],
                              waveunits=sp.waveunits,
                              fluxunits=sp.fluxunits)

    # .flux calls __call__ calls resample
    ref = sp.flux[::-1]
    tst = sp2.flux
    assert_allclose(ref, tst)


@use_cdbs
def test_ticket135_flip_bp():
    bp = ObsBandpass('johnson,v')
    T = bp.throughput

    # create a bandpass with wavelength in descending order
    bp2 = ArraySpectralElement(wave=bp.wave[::-1],
                               throughput=T[::-1],
                               waveunits=bp.waveunits)

    # .throughput calls __call__ calls resample
    ref = bp.throughput[::-1]
    tst = bp2.throughput
    idxr = np.where(ref != 0)[0]
    idxt = np.where(tst != 0)[0]
    assert_array_equal(idxr, idxt)
    assert_allclose(ref[idxr], tst[idxr])


@use_cdbs
@pytest.mark.parametrize(
    'pstr',
    ['rn(icat(k93models,44500,0.0,5.0),band(nicmos,2,f222m),18,vegamag)',
     'rn(icat(k93models,44500,0.0,5.0),band(v),18,vegamag)',
     'rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)'])
def test_parse_spec(pstr):
    sp = parse_spec(pstr)
    assert isinstance(sp, SourceSpectrum)


class TestAddMag(object):
    """Ticket #122"""
    def setup_class(self):
        self.bright = FlatSpectrum(18.0, fluxunits='abmag')
        self.faint = FlatSpectrum(21.0, fluxunits='abmag')
        self.delta = 3

    def test_add(self):
        test = self.bright.addmag(self.delta)
        assert_array_equal(test.flux, self.faint.flux)

    def test_subtract(self):
        test = self.faint.addmag(self.delta * -1.0)
        assert_array_equal(test.flux, self.bright.flux)

    def testtypecatch(self):
        with pytest.raises(TypeError):
            self.faint.addmag(self.bright)


def test_sample():
    """Ticket #99"""
    sp = FlatSpectrum(10, fluxunits='flam')
    wave = np.arange(1000, 11000, 1000)
    ref = ArraySourceSpectrum(wave=wave,
                              flux=sp.flux[0]*np.ones(wave.shape),
                              fluxunits=sp.fluxunits)
    tst = sp.sample(wave)
    assert_array_equal(tst, ref.flux)


@use_cdbs
def test_ticket104():
    """
    Use the extinction laws to test and make sure the conversion to
    SpectralElements works ok.
    """
    sp = Extinction(0.2, 'gal1')  # Make an extinction law
    sp.convert('1/um')  # convert to inverse microns
    refwave = extinction._buildDefaultWaveset()
    testwave = sp.wave
    assert_allclose(testwave, refwave)
