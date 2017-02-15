from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest
from astropy.utils.data import _find_pkg_data_path, get_pkg_data_filename
from numpy.testing import assert_allclose

from .utils import use_cdbs
from .. import locations, refs
from ..exceptions import PartialOverlap
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..spectrum import (ArraySourceSpectrum, ArraySpectralElement, BlackBody,
                        Box, FileSourceSpectrum, FlatSpectrum, GaussianSource,
                        Powerlaw)

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
        os.environ['PYSYN_CDBS'], 'mtab', 'OLD_FILES', 'r1j2146sm_tmc.fits')

    old_vegafile = locations.VegaFile
    locations.VegaFile = get_pkg_data_filename(
        os.path.join('data', 'alpha_lyr_stis_002.fits'))


def teardown_module(module):
    refs.COMPTABLE = old_comptable
    locations.VegaFile = old_vegafile


class TestOverlapBug(object):
    def setup_class(self):
        self.sp = ArraySourceSpectrum(wave=np.arange(3000, 4000),
                                      flux=np.ones((1000, ))*0.75,
                                      name='Short flat')
        self.bp = Box(4000, 100)
        self.refwave = 4005
        self.refval = 0.75
        self.rtol = 1e-7

    def test_overlap(self):
        ans = self.bp.check_overlap(self.sp)
        assert ans == 'partial'

        with pytest.raises(PartialOverlap):
            Observation(self.sp, self.bp)

    def test_taper(self):
        obs = Observation(self.sp, self.bp, force='taper')
        idx = np.searchsorted(obs.wave, self.refwave)
        tst = obs.flux[idx]
        assert tst == 0, 'Expected 0, got {}'.format(tst)

    def test_extrap(self):
        obs = Observation(self.sp, self.bp, force='extrap')
        idx = np.searchsorted(obs.wave, self.refwave)
        tst = obs.flux[idx]
        assert_allclose(tst, self.refval, rtol=self.rtol)


@use_cdbs
class TestDiscoveryCase(TestOverlapBug):
    def setup_class(self):
        # rn(z(spec(data/qso_template.fits),0.03),band(johnson,v),18,vegamag)
        spdat = FileSourceSpectrum(
            get_pkg_data_filename(os.path.join('data', 'qso_template.fits')))
        self.sp = spdat.redshift(0.03).renorm(
            18, 'vegamag', ObsBandpass('johnson,v'), force=True)
        self.sp.convert('photlam')
        self.bp = ObsBandpass('stis,ccd,g750l,c7751,s52x02')
        self.refwave = 6200
        self.refval = 2.97759742e-06
        self.rtol = 0.01


class TestBPOverlap(object):
    def setup_class(self):
        self.a = Box(4000, 50)
        self.disjoint = Box(6000, 100)
        self.full = Box(4000, 100)
        self.partial = Box(4050, 50)

    def test_disjoint(self):
        assert self.a.check_overlap(self.disjoint) == 'none'

    def test_full(self):
        assert self.a.check_overlap(self.full) == 'full'

    def test_partial(self):
        assert self.a.check_overlap(self.partial) == 'partial'


class TestBP03(TestBPOverlap):
    def setup_class(self):
        self.a = ArraySpectralElement(wave=np.arange(4000, 5000),
                                      throughput=np.ones(1000))
        self.disjoint = Box(1000, 100)
        self.full = ArraySpectralElement(wave=np.arange(3000, 6000),
                                         throughput=np.ones(3000))
        self.partial = ArraySpectralElement(wave=np.arange(500, 4500),
                                            throughput=np.ones(4000))


def test_analytic_to_file(tmpdir):
    fname = str(tmpdir.join('ac_pl.fits'))
    pl = Powerlaw(5000, -2)
    pl.writefits(fname)
    fspec = FileSourceSpectrum(fname)
    assert not fspec.isAnalytic


def test_analytic_flat():
    flat = FlatSpectrum(10)
    x = flat * 2.6
    assert x.isAnalytic


class TestAnalyticCase(object):
    def setup_class(self):
        self.bb = BlackBody(5000)

    def test_bb_gauss(self):
        em = GaussianSource(3300, 1, 1)
        x = self.bb + em
        assert x.isAnalytic

    def test_bb_arr(self):
        tspec = ArraySourceSpectrum(self.bb.wave, self.bb.flux,
                                    fluxunits=self.bb.fluxunits)
        x = self.bb + tspec
        assert self.bb.isAnalytic
        assert not tspec.isAnalytic
        assert not x.isAnalytic


# These tests were part of the original nightly pysynphot test suite
# that began failing when #157 was implemented because they really
# did have partial overlap.

@use_cdbs
class TestCalcphot(object):
    # Loosened accuracy for r618 (no taper)
    def setup_class(self):
        self.sp = FileSourceSpectrum(os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'feige66_002.fits'))
        self.bandpass = ObsBandpass('acs,hrc,f555w')

    def test_raises(self):
        with pytest.raises(PartialOverlap):
            Observation(self.sp, self.bandpass)

    def test_efflam(self):
        obs = Observation(self.sp, self.bandpass, force='extrap')
        tst = obs.efflam()
        assert_allclose(tst, 5304.462, rtol=1e-4)

    def test_countrate(self):
        obs = Observation(self.sp, self.bandpass, force='taper')
        tst = obs.countrate()
        assert_allclose(tst, 8.30680E+5, rtol=1e-4)


@use_cdbs
class TestETC_Imag2(object):
    def setup_class(self):
        # (earthshine.fits * 0.5) +
        # rn(spec(Zodi.fits), band(V), 22.7, vegamag) +
        # (el1215a.fits * 0.5) +
        # (el1302a.fits * 0.5) +
        # (el1356a.fits * 0.5) +
        # (el2471a.fits * 0.5)
        path = _find_pkg_data_path(os.path.join('data', 'generic'),
                                   package='pysynphot')
        spz = FileSourceSpectrum(os.path.join(path, 'Zodi.fits')).renorm(
            22.7, 'vegamag', ObsBandpass('V'))
        self.sp = ((FileSourceSpectrum(os.path.join(path, 'earthshine.fits')) +
                    FileSourceSpectrum(os.path.join(path, 'el1215a.fits')) +
                    FileSourceSpectrum(os.path.join(path, 'el1302a.fits')) +
                    FileSourceSpectrum(os.path.join(path, 'el1356a.fits')) +
                    FileSourceSpectrum(os.path.join(path, 'el2471a.fits'))) *
                   0.5 + spz)
        self.bp = ObsBandpass('acs,sbc,F140LP')

    def test_raises(self):
        # Replaced answer for r618 (no tapering).
        # The throughput files used in this case don't actually go
        # all the way to zero.
        with pytest.raises(PartialOverlap):
            Observation(self.sp, self.bp)

    def test_flux(self):
        """Moved from old ticket159.py"""
        obs = Observation(self.sp, self.bp, force='taper')
        assert 'PartialOverlap' in obs.warnings


class TestETC_Spec2a(TestETC_Imag2):
    def setup_class(self):
        self.sp = FileSourceSpectrum(os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'grw_70d5824_stis_001.fits'))
        self.bp = ObsBandpass('stis,fuvmama,g140l,s52x2')
        self.refrate = 28935.7

    def test_flux(self):
        obs = Observation(self.sp, self.bp, force='taper')
        obs.convert('counts')
        assert_allclose(obs.binflux[500], 35.5329, rtol=1e-4)
