from __future__ import absolute_import, division, print_function

import numpy as np
from numpy.testing import assert_allclose

from ..spectrum import BlackBody, FlatSpectrum, GaussianSource, Powerlaw


class TestPowerLaw(object):
    def setup_class(self):
        self.pl = Powerlaw(6000, -4, 'angstrom', 'photlam')
        self.wave = np.arange(3000, 5000, 10)

    def test_values(self):
        ref = np.array([
            16, 15.78843266, 15.58035072, 15.37568551, 15.17436992,
            14.97633838, 14.78152682, 14.5898726, 14.40131453, 14.21579277])
        ans = self.pl.sample(self.wave[:10])
        assert_allclose(ans, ref)

    def test_conversion(self):
        angflux = self.pl.sample(self.wave)
        assert_allclose(self.pl.sample(self.wave)[:10],
                        self.pl.sample(self.wave[:10]))

        self.pl.convert('nm')
        nmflux = self.pl.sample(self.wave / 10)
        assert_allclose(nmflux, angflux)
        assert_allclose(self.pl.sample(self.wave)[:10],
                        self.pl.sample(self.wave[:10]))

        self.pl.convert('angstrom')


class TestGaussian(object):
    def setup_class(self):
        self.g = GaussianSource(1, 4000, 100, 'angstrom', 'photlam')
        self.wave = np.arange(3000, 5000, 10)

    def test_values(self):
        ref = np.array([
            3.63805721e-123, 9.05875032e-121, 2.13395205e-118, 4.75574568e-116,
            1.00269809e-113, 2.00004310e-111, 3.77421053e-109, 6.73799198e-107,
            1.13802672e-104, 1.81841090e-102])
        ans = self.g.sample(self.wave[:10])
        assert_allclose(ans, ref)

    def test_symmetry1(self):
        assert_allclose(self.g.sample(3950), self.g.sample(4050))

    def test_symmetry2(self):
        g = GaussianSource(1, 400, 100, 'nm', 'flam')
        assert_allclose(g.sample(395), g.sample(405))

    def test_conversion(self):
        tf1 = self.g.total_flux
        angflux = self.g.sample(self.wave)
        assert_allclose(self.g.sample(self.wave)[:10],
                        self.g.sample(self.wave[:10]))

        self.g.convert('nm')
        tf2 = self.g.factor * self.g.sigma * np.sqrt(2.0 * np.pi)
        assert_allclose(tf1, tf2)
        nmflux = self.g.sample(self.wave / 10.)
        assert_allclose(nmflux, angflux)
        assert_allclose(self.g.sample(self.wave)[:10],
                        self.g.sample(self.wave[:10]))

        self.g.convert('angstrom')


class TestFlatSpec(object):
    def setup_class(self):
        self.f = FlatSpectrum(1, 'angstrom', 'photlam')
        self.wave = np.arange(3000, 5000, 10)

    def test_values(self):
        ans = self.f.sample(self.wave[:10])
        assert_allclose(ans, 1)

    def test_conversion(self):
        angflux = self.f.sample(self.wave)
        assert_allclose(self.f.sample(self.wave)[:10],
                        self.f.sample(self.wave[:10]))

        self.f.convert('nm')

        nmflux = self.f.sample(self.wave / 10.)
        assert_allclose(nmflux, angflux)
        assert_allclose(self.f.sample(self.wave)[:10],
                        self.f.sample(self.wave[:10]))

        self.f.convert('angstrom')


class TestBlackBody(object):
    def setup_class(self):
        self.bb = BlackBody(5500)
        self.wave = np.arange(3000, 5000, 10)

    def test_values(self):
        ref = np.array([
            0.00019318, 0.00019623, 0.0001993, 0.00020238, 0.00020549,
            0.00020861, 0.00021175, 0.00021491, 0.00021809, 0.00022128])
        ans = self.bb.sample(self.wave[:10])
        assert_allclose(ans, ref, rtol=3e-5)
