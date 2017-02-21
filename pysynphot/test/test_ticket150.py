from __future__ import absolute_import, division, print_function

import os
import sys

import numpy as np
import pytest
from numpy.testing import assert_allclose

from .utils import use_cdbs
from .. import locations, refs
from ..exceptions import OverlapError
from ..obsbandpass import ObsBandpass
from ..spectrum import (ArraySpectralElement, ArraySourceSpectrum, Box,
                        FileSourceSpectrum, SourceSpectrum)
from ..spparser import parse_spec

old_comptable = None
old_vegafile = None


def setup_module(module):
    """
    Freeze the version of the comptable so tests are not susceptible to
    updates to CDBS. Also set the version of Vega for similar reasons.
    """
    global old_comptable, old_vegafile

    old_comptable = refs.COMPTABLE
    refs.COMPTABLE = os.path.join(
        os.environ['PYSYN_CDBS'], 'mtab', 'OLD_FILES', 't260548pm_tmc.fits')

    old_vegafile = locations.VegaFile
    locations.VegaFile = os.path.join(
        os.environ['PYSYN_CDBS'], 'crcalspec', 'alpha_lyr_stis_003.fits')


def teardown_module(module):
    refs.COMPTABLE = old_comptable
    locations.VegaFile = old_vegafile


@use_cdbs
class TestRenormOverlap(object):
    """Tests for strict rejection."""

    def setup_class(self):
        """(re)discovery case: stis_rn_cases/stisC94"""
        self.sp = FileSourceSpectrum(os.path.join(
            os.environ['PYSYN_CDBS'], 'grid', 'kc96', 'starb2_template.fits'))
        self.bp = ObsBandpass('cos,fuv,g130m,c1300')
        self.cmd = ('rn(crgridkc96$starb2_template.fits,'
                    'band(cos,fuv,g130m,c1300),16.0,stmag)')
        self.ref = 0.00718543  # expected renorm factor

    def test_raise(self):
        with pytest.raises(OverlapError):
            self.sp.renorm(16.0, 'stmag', self.bp)

    def test_force(self):
        sp2 = self.sp.renorm(16.0, 'stmag', self.bp, force=True)
        ratio = sp2.flux / self.sp.flux
        assert np.all((1 - abs(ratio / self.ref)) < 0.0001)

    def test_parse(self):
        sp2 = parse_spec(self.cmd)
        ratio = sp2.flux / self.sp.flux
        assert np.all((1 - abs(ratio / self.ref)) < 0.0001)

    @pytest.mark.parametrize('obsmode', ['johnson,v', 'acs,hrc,f555w'])
    def test_renorm(self, obsmode):
        """
        ACS: If 99% of throughput on spectrum, go ahead but print warning.
        Does not yet test warning.
        """
        sp2 = self.sp.renorm(17.0, 'abmag', ObsBandpass(obsmode))
        assert isinstance(sp2, SourceSpectrum)


@use_cdbs
class TestCornerCase(object):
    def setup_class(self):
        """
        This is deliberately constructed to have a waveset that partially
        overlaps, but for which all the flux is fully contained.
        """
        self.bp = ObsBandpass('acs,hrc,f555w')
        w = np.arange(1000, 10000)
        f = np.zeros(w.shape)
        f[4000:4010] = 1.0
        self.sp = ArraySourceSpectrum(wave=w, flux=f, fluxunits='flam')

    def test_partial(self):
        assert self.bp.check_overlap(self.sp) == 'partial'

    def test_smart(self):
        sp2 = self.sp.renorm(17.0, 'abmag', self.bp)
        assert isinstance(sp2, SourceSpectrum)


class TestBPIntegrate(object):
    def setup_class(self):
        # Box 100 A wide, centered at 1000
        self.bp = Box(1000, 100)
        self.ref = 100.0

    def test_integrate(self):
        tst = self.bp.integrate()
        assert_allclose(tst, self.ref, rtol=0.01)

    def test_subint(self):
        w = self.bp.wave
        tst = self.bp.integrate(w[0:int(len(w)/2)])

        # epsilon due to the nature of trapezoid integration
        assert abs(self.ref / 2.0 - tst) <= 0.025


@pytest.mark.xfail(sys.version_info < (3, 0),
                   reason='defarrays not compatible with Python 2')
class OVBase(object):
    """
    Base class to test for the variants we can imagine.
    Implement all methods here.
    """
    def defarrays(self):
        """Supposes that the range variables have already been set."""
        w = np.arange(*self.sprange)
        f = np.zeros(w.shape)
        f[slice(*(self.spnonzero - w[0]))] += 1.0
        self.sp = ArraySourceSpectrum(wave=w, flux=f)

        w = np.arange(*self.bprange)
        t = np.zeros(w.shape)
        t[slice(*(self.bpnonzero - w[0]))] += 1
        self.bp = ArraySpectralElement(w, t)

    def test_current(self):
        ans = self.bp.check_overlap(self.sp)
        assert ans == self.cref

    def test_sig(self):
        if self.cref == 'partial':
            ans = self.bp.check_sig(self.sp)
            assert ans == self.sref
        else:
            pytest.skip('Not applicable')


class TestSpBp(OVBase):
    """SPdef fully encloses BPdef: "full" overlap. Pass."""
    def setup_class(self):
        self.sprange = (1000, 10000)
        self.spnonzero = self.sprange
        self.bprange = (5000, 6000)
        self.bpnonzero = self.bprange
        super(TestSpBp, self).defarrays(self)
        self.cref = 'full'
        self.sref = True


class TestBpSp(OVBase):
    """BPdef fully encloses SPdef: Insufficient overlap. Fail."""
    def setup_class(self):
        self.sprange = (5000, 6000)
        self.spnonzero = self.sprange
        self.bprange = (1000, 10000)
        self.bpnonzero = self.bprange
        super(TestBpSp, self).defarrays(self)
        self.cref = 'partial'
        self.sref = False


class TestSpPartial(OVBase):
    """Partial overlap: return partial, require further processing."""
    def setup_class(self):
        self.sprange = (1000, 8000)
        self.bprange = (4000, 10000)
        self.spnonzero = self.sprange
        self.bpnonzero = self.bprange
        super(TestSpPartial, self).defarrays(self)
        self.cref = 'partial'
        self.sref = False  # assuming they're all ones


# Now do variants where nonzero is different from range

class TestSpBpNz(OVBase):
    """BP defined zero some places: still acceptable."""
    def setup_class(self):
        self.sprange = (1000, 10000)
        self.spnonzero = self.sprange
        self.bprange = (5000, 6000)
        self.bpnonzero = (5500, 5550)
        super(TestSpBpNz, self).defarrays(self)
        self.cref = 'full'
        self.sref = True


class TestBpSpNz(OVBase):
    """Passes per current defn that looks at bp.nonzero, sp.def."""
    def setup_class(self):
        self.sprange = (5000, 6000)
        self.spnonzero = self.sprange
        self.bprange = (1000, 10000)
        self.bpnonzero = (5500, 5700)
        super(TestBpSpNz, self).defarrays(self)
        self.cref = 'full'
        self.sref = True


class TestSpPartialNz1(OVBase):
    """Passes per current defn that looks at bp.nonzero, sp.def."""
    def setup_class(self):
        self.sprange = (1000, 8000)
        self.spnonzero = self.sprange
        self.bprange = (4000, 10000)
        self.bpnonzero = (5000, 6000)
        super(TestSpPartialNz1, self).defarrays(self)
        self.cref = 'full'
        self.sref = True


class TestSpPartialNz2(OVBase):
    """
    This is still not acceptable:
    the bandpass is nonzero in places where the spectrum is undefined.
    """
    def setup_class(self):
        self.sprange = (1000, 8000)
        self.spnonzero = (5000, 6000)
        self.bprange = (4000, 10000)
        self.bpnonzero = self.bprange
        super(TestSpPartialNz2, self).defarrays(self)
        self.cref = 'partial'
        self.sref = False
