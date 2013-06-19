"""

Tests for pysynphot using bin edges as the primary reference instead of bin
centers.


# Test coverage domain
    * obs(sp,bp)
    * obs(sp, bp, binset)
    * obs(binned_sp,bp)
    * obs(binned_sp,bp, binset)
    * some hst vs. generic bandpasses
    * some analytics vs. tabular spectra


"""

from __future__ import division, print_function
import numpy as np
import pysynphot as pysyn
from pysynphot.spectrum import FlatSpectrum


def result(obs, max, min, number):
    """
    result helper function

    """
    print(int(obs.flux.max()))
    print(int(obs.flux.min()))
    print(obs.flux.size)
    assert int(obs.flux.max()) == max
    assert int(obs.flux.min()) == min
    assert obs.flux.size == number


def test_hst_analytic():
    bp = pysyn.FileBandpass("data/test_bp_acs_hrc_f555w.fits",
                            thrucol="THROUGHPUT")
    spec = FlatSpectrum(10000, fluxunits='flam')
    obs = pysyn.Observation(spec, bp)
    result(obs, 2439, 0, 17023)


def test_hst_tabular_spectra():
    bp = pysyn.FileBandpass("data/test_bp_acs_hrc_f555w.fits",
                            thrucol="THROUGHPUT")
    sp = pysyn.FileSpectrum("data/test_sp_vega.fits")
    obs = pysyn.Observation(sp, bp)
    obs *= 1e20
    result(obs, 112231834769, 0, 15866)


def test_hst_analytic_binset():
    bp = pysyn.FileBandpass("data/test_bp_acs_hrc_f555w.fits",
                            thrucol="THROUGHPUT")
    spec = FlatSpectrum(10000, fluxunits='flam')
    binset = np.asarray([1000, 2000, 5000, 11000])
    obs = pysyn.Observation(spec, bp, binset=binset)
    result(obs, 2439, 0, 17023)


def test_hst_tabular_spectra_binset():
    bp = pysyn.FileBandpass("data/test_bp_acs_hrc_f555w.fits",
                            thrucol="THROUGHPUT")
    sp = pysyn.FileSpectrum("data/test_sp_vega.fits")

    binset = np.asarray([1000, 2000, 5000, 11000])
    obs = pysyn.Observation(sp, bp, binset=binset)
    obs *= 1e20
    result(obs, 112231834769, 0, 15866)


def test_johnson_v_analytic():
    bp = pysyn.FileBandpass("data/test_bp_johnson_v.fits",
                            thrucol="THROUGHPUT")
    spec = FlatSpectrum(10000, fluxunits='flam')
    obs = pysyn.Observation(spec, bp)
    result(obs, 10000, 0, 10047)


def test_johnson_v_tabular_spectra():
    bp = pysyn.FileBandpass("data/test_bp_johnson_v.fits",
                            thrucol="THROUGHPUT")
    sp = pysyn.FileSpectrum("data/test_sp_vega.fits")
    obs = pysyn.Observation(sp, bp)
    obs *= 1e20
    result(obs, 411896149580, 0, 8893)
