"""
Tests for pysynphot using bin edges as the primary reference instead of bin
centers.

Test coverage domain:

* obs(sp,bp)
* obs(sp, bp, binset)
* obs(binned_sp,bp)
* obs(binned_sp,bp, binset)
* some hst vs. generic bandpasses
* some analytics vs. tabular spectra

"""
from __future__ import absolute_import, division, print_function

import numpy as np
import pytest
from astropy.utils.data import get_pkg_data_filename

from ..observation import Observation
from ..spectrum import FileSourceSpectrum, FileSpectralElement, FlatSpectrum


def result(obs, maxval, minval, number):
    """Result helper function."""
    msg = ('{}\n{}\n{}'.format(
        int(obs.flux.max()), int(obs.flux.min()), obs.flux.size))
    assert int(obs.flux.max()) == maxval, msg
    assert int(obs.flux.min()) == minval, msg
    assert obs.flux.size == number, msg


class TestBinEdgesRef(object):
    def setup_class(self):
        self.acs = FileSpectralElement(
            get_pkg_data_filename('data/test_bp_acs_hrc_f555w.fits'),
            thrucol='THROUGHPUT')
        self.v = FileSpectralElement(
            get_pkg_data_filename('data/test_bp_johnson_v.fits'),
            thrucol='THROUGHPUT')
        self.flat = FlatSpectrum(10000, fluxunits='flam')
        self.vega = FileSourceSpectrum(
            get_pkg_data_filename('data/test_sp_vega.fits'))

    @pytest.mark.parametrize(
        'binset', [None, np.array([1000, 2000, 5000, 11000])])
    def test_hst_acs_analytic(self, binset):
        obs = Observation(self.flat, self.acs, binset=binset)
        result(obs, 2439, 0, 17023)

    @pytest.mark.parametrize(
        'binset', [None, np.array([1000, 2000, 5000, 11000])])
    def test_hst_acs_tabular(self, binset):
        obs = Observation(self.vega, self.acs, binset=binset)
        obs *= 1e20
        result(obs, 112231834769, 0, 15866)

    def test_johnson_v_analytic(self):
        obs = Observation(self.flat, self.v)
        result(obs, 10000, 0, 10047)

    def test_johnson_v_tabular(self):
        obs = Observation(self.vega, self.v)
        obs *= 1e20
        result(obs, 411896149580, 0, 8893)
