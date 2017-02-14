from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest
from numpy.testing import assert_allclose

from .utils import use_cdbs
from ..spectrum import FileSourceSpectrum, FileSpectralElement, FlatSpectrum


def test_flat_redshift():
    sp = FlatSpectrum(1)
    tst = sp.redshift(2.5)
    tstpt = tst(np.array([550]))[0]
    assert tst.flux.max() == tstpt, 'tstpt={}'.format(tstpt)


@use_cdbs
def test_file_feige():
    """Subtract two spectra, Trac Ticket #23"""
    sp = FileSourceSpectrum(os.path.join(
        os.environ['PYSYN_CDBS'], 'calspec', 'feige66_002.fits'))
    sp2 = sp + sp
    sp3 = sp2 - sp
    assert_allclose(sp3.flux, sp.flux)


@use_cdbs
@pytest.mark.parametrize(
    ('cls', 'fname', 'realpath'),
    [(FileSourceSpectrum, 'crcalspec$hz2_005.fits',
      os.path.join(os.environ['PYSYN_CDBS'], 'calspec', 'hz2_005.fits')),
     (FileSourceSpectrum, '$PYSYN_CDBS/calspec/hz2_005.fits',
      os.path.join(os.environ['PYSYN_CDBS'], 'calspec', 'hz2_005.fits')),
     (FileSpectralElement, 'crotacomp$hst_ota_007_syn.fits',
      os.path.join(os.environ['PYSYN_CDBS'], 'comp', 'ota',
                   'hst_ota_007_syn.fits')),
     (FileSpectralElement, '$PYSYN_CDBS/comp/ota/hst_ota_007_syn.fits',
      os.path.join(os.environ['PYSYN_CDBS'], 'comp', 'ota',
                   'hst_ota_007_syn.fits'))])
def test_file_iraf(cls, fname, realpath):
    tst = cls(fname)
    ref = cls(realpath)
    assert os.path.normpath(tst.name) == os.path.normpath(ref.name)
