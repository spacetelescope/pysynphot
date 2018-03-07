"""Tests for the catalog module."""
from __future__ import absolute_import, division, print_function

import os

import pytest
import numpy as np
from numpy.testing import assert_allclose, assert_array_equal

from .utils import use_cdbs
from .. import Cache
from ..exceptions import ParameterOutOfBounds
from ..catalog import Icat


@use_cdbs
class ICatK93Test(object):
    """
    This test passes before changes, and should pass after the changes.
    """
    def setup_class(self):
        self.sp = Icat('k93models', 6440, 0, 4.3)

    def test_wave(self):
        ref_wave1 = np.array([
            90.90000153, 93.50000763, 96.09999847, 97.70000458, 99.59999847,
            102, 103.80000305, 105.6000061, 107.70000458, 110.40000153, 114,
            117.79999542, 121.30000305, 124.79999542, 127.09999847,
            128.40000916, 130.5, 132.3999939, 133.90000916, 136.6000061,
            139.80000305, 143.30000305, 147.19999695, 151, 155.20001221,
            158.80000305, 162.00001526, 166, 170.30000305, 173.40000916,
            176.80000305, 180.20001221, 181.69999695, 186.1000061, 191,
            193.8999939, 198.40000916, 201.80000305, 205, 210.5, 216.20001221,
            219.80000305, 223, 226.80000305, 230, 234, 240, 246.5, 252.3999939,
            256.80001831], dtype=np.float32)
        assert_allclose(self.sp.wave[:50], ref_wave1)

        ref_wave2 = np.array([
            83800, 84200, 84600, 85000, 85400, 85800, 86200, 86600, 87000,
            87400, 87800, 88200, 88600, 89000, 89400, 89800, 90200, 90600,
            91000, 91400, 91800, 92200, 92600, 93000, 93400, 93800, 94200,
            94600, 95000, 95400, 95800, 96200, 96600, 97000, 97400, 97800,
            98200, 98600, 99000, 99400, 99800, 100200, 200000, 400000, 600000,
            800000, 1000000, 1200000, 1400000, 1600000], dtype=np.float32)
        assert_allclose(self.sp.wave[-50:], ref_wave2)

    def test_flux(self):
        assert_array_equal(self.sp.flux[:50], 0)

        ref_flux2 = np.array([
            2.52510792e+03, 2.47883842e+03, 2.43311637e+03, 2.38843415e+03,
            2.34455095e+03, 2.30190141e+03, 2.25982266e+03, 2.21930715e+03,
            2.17950029e+03, 2.14031198e+03, 2.10216378e+03, 2.06411734e+03,
            2.02789000e+03, 1.99191291e+03, 1.95752853e+03, 1.92259620e+03,
            1.88976666e+03, 1.85768178e+03, 1.82475330e+03, 1.79369145e+03,
            1.76356796e+03, 1.73377904e+03, 1.70432192e+03, 1.67572220e+03,
            1.64739969e+03, 1.61997833e+03, 1.59299008e+03, 1.56657219e+03,
            1.54066436e+03, 1.51508799e+03, 1.49065412e+03, 1.46606232e+03,
            1.44255637e+03, 1.41922753e+03, 1.39555249e+03, 1.37360936e+03,
            1.35179525e+03, 1.33041182e+03, 1.30944458e+03, 1.28851215e+03,
            1.26828580e+03, 1.24841065e+03, 8.04744247e+01, 5.03657385,
            9.88851448e-01, 3.10885179e-01, 1.26599425e-01, 6.07383728e-02,
            3.26344365e-02, 1.90505413e-02])
        assert_allclose(self.sp.flux[-50:], ref_flux2)


@use_cdbs
@pytest.mark.parametrize(
    ('teff', 'z', 'logg'),
    [(6440, 0, 10),
     (6440, 0, -1),
     (1.e6, 0, 4.3),
     (100, 0, 4.3),
     (6440, 2, 4.3),
     (6440, -6, 4.3)])
def test_Icat_exceptions(teff, z, logg):
    """
    Tests for changes related to Trac ticket #211.
    Test that an exception is raised when making out of bounds requests.
    """
    with pytest.raises(ParameterOutOfBounds):
        Icat('k93models', teff, z, logg)


@use_cdbs
def test_phoenix_gap():
    """
    https://github.com/spacetelescope/pysynphot/issues/68
    """
    Icat('phoenix', 2700, -1, 5.1)  # OK
    with pytest.raises(ParameterOutOfBounds):
        Icat('phoenix', 2700, -0.5, 5.1)
    with pytest.raises(ParameterOutOfBounds):
        Icat('phoenix', 2700, -0.501, 5.1)


@use_cdbs
class TestCatalogCache(object):
    """
    Test changes for Trac ticket #131.
    Test that the Cache.CATALOG_CACHE variable works as intended.
    """
    def test_things_in_cache(self):
        Cache.reset_catalog_cache()

        sp = Icat('k93models', 6440, 0, 4.3)  # noqa
        assert len(Cache.CATALOG_CACHE) == 1

        k = next(key for key in Cache.CATALOG_CACHE.keys())
        if k.startswith('ftp'):
            fixed_k = k
        else:
            fixed_k = os.path.normpath(os.path.normcase(k))
        f = os.path.join(
            os.environ['PYSYN_CDBS'], 'grid', 'k93models', 'catalog.fits')
        msg = ('cache_found={}, cache_found_fixed={}, cache_expect={}, '
               'cache_type_mismatch={}'.format(k, fixed_k, f,
                                               type(Cache.CATALOG_CACHE[k])))
        assert fixed_k == f, msg
        assert isinstance(Cache.CATALOG_CACHE[k], list), msg

    def test_reset_catalog_cache(self):
        sp = Icat('k93models', 6440, 0, 4.3)  # noqa
        assert len(Cache.CATALOG_CACHE) != 0

        Cache.reset_catalog_cache()
        assert len(Cache.CATALOG_CACHE) == 0
