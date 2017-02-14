from __future__ import absolute_import, division, print_function

import numpy as np
import pytest
from numpy.testing import assert_allclose

from ..exceptions import DisjointError, PartialOverlap
from ..observation import Observation
from ..spectrum import ArraySourceSpectrum, ArraySpectralElement


class TestHandmade(object):
    """Handmade observation with well defined ranges."""
    def setup_class(self):
        w = np.arange(1000, 1100, 0.5)
        self.sp = ArraySourceSpectrum(
            wave=w, flux=(w - 1000), fluxunits='counts', name='slope1')

        # Handmade box that has fewer points
        self.bp = ArraySpectralElement(
            wave=np.array([1000, 1009.95, 1010, 1030, 1030.05, 1100]),
            throughput=np.array([0, 0, 1, 1, 0, 0]), name='HandBox')

        self.obs = Observation(self.sp, self.bp, binset=np.arange(w[6], w[40]))

    def test_allbin(self):
        """
        Specifying the entire exact range should be identical to the
        results without any such specification.
        """
        ref = self.obs.countrate()
        tst = self.obs.countrate(range=[self.obs.binwave[0],
                                        self.obs.binwave[-1]])
        assert_allclose(tst, ref)

    @pytest.mark.parametrize(
        'wrange', [[1013, 1016], [1012.8, 1016], [1013.2, 1016]])
    def test_bin(self, wrange):
        """Ask for a bin with some slight offsets."""
        tst = self.obs.countrate(range=wrange)
        assert_allclose(tst, 116)

    @pytest.mark.parametrize(
        ('wrange', 'ans'),
        [([1016, 1026], '140'),
         ([1000, 1016], '172.75')])
    def test_ovlphibin(self, wrange, ans):
        """Ask for something _partly_ outside the bin range."""
        with pytest.raises(PartialOverlap) as e:
            self.obs.countrate(range=wrange)
            assert ans in str(e)

    def test_disjointbin(self):
        """Ask for something outside the bin range."""
        with pytest.raises(DisjointError):
            self.obs.countrate(range=[1025, 1030])
