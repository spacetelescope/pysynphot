from __future__ import absolute_import, division, print_function

import numpy as np
import pytest
from numpy.testing import assert_array_equal

from ..spectrum import ArraySpectralElement, ArraySourceSpectrum


class TestFlip(object):
    def setup_class(self):
        self.waveup = np.arange(10000, 10100, 10)
        self.wavedown = self.waveup[::-1]
        self.t_up = np.arange(10) + 5
        self.t_flip = self.t_up.copy()[::-1]

    @pytest.mark.parametrize(
        'cls', [ArraySpectralElement, ArraySourceSpectrum])
    def test_flip(self, cls):
        up = cls(self.waveup, self.t_up)
        down = cls(self.wavedown, self.t_up[::-1])

        assert_array_equal(up(self.waveup), self.t_up)
        assert_array_equal(up(self.wavedown), self.t_flip)
        assert_array_equal(down(self.waveup), self.t_up)
        assert_array_equal(down(self.wavedown), self.t_flip)


class TestNumpyInterp(object):
    def setup_class(self):
        self.Y = np.arange(10) + 5

    def test1(self):
        A = np.arange(10)
        X = np.arange(10)
        ans = np.interp(A, X, self.Y)
        assert_array_equal(ans, self.Y)

    def test2(self):
        A = np.arange(10)[::-1]
        X = np.arange(10)[::-1]
        ans = np.interp(A[::-1], X[::-1], self.Y[::-1])
        assert_array_equal(ans, self.Y[::-1])

    def test3(self):
        A = np.arange(10)
        X = np.arange(10)[::-1]
        ans = np.interp(A, X[::-1], self.Y[::-1])
        assert_array_equal(ans, self.Y[::-1])

    def test4(self):
        A = np.arange(10)[::-1]
        X = np.arange(10)
        ans = np.interp(A[::-1], X, self.Y)
        assert_array_equal(ans, self.Y)
