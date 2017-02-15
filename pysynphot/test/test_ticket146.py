from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

from .utils import use_cdbs
from ..exceptions import DuplicateWavelength
from ..obsbandpass import ObsBandpass
from ..reddening import Extinction
from ..spectrum import (ArraySourceSpectrum, ArraySpectralElement, BlackBody,
                        FileSpectralElement, FileSourceSpectrum)


def test_dup_wave():
    with pytest.raises(DuplicateWavelength):
        ArraySourceSpectrum(wave=np.array([1, 2, 3, 4, 4, 5]), flux=np.ones(6))


def test_sorted_bp(tmpdir):
    fname = str(tmpdir.join('bpesp.fits'))
    bp = ArraySpectralElement(wave=np.array([1, 2, 3, 4, 4.0000001, 5]),
                              throughput=np.ones(6))
    bp.writefits(fname, precision='single')

    # Read back in
    bp = FileSpectralElement(fname)
    idx = np.where(bp.wave == 4)
    num = len(idx[0])
    assert num == 1, '{} occurrences found'.format(num)


@use_cdbs
def test_sorted(tmpdir):
    fname = str(tmpdir.join('epsilon.fits'))

    # rn(spec(data/bz_7.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)
    sp = FileSourceSpectrum(get_pkg_data_filename(
        os.path.join('data', 'bz_7.fits')))
    sp2 = (sp.renorm(28.0, 'vegamag', ObsBandpass('cousins,i')) *
           Extinction(0.04, 'gal1'))

    sp2.writefits(fname, precision='single')

    # Read back in
    sp = FileSourceSpectrum(fname)
    idx = np.where(sp.wave == 500)
    num = len(idx[0])
    assert num == 1, '{} occurrences found'.format(num)


class TestPrecision(object):
    def setup_class(self):
        self.sp = BlackBody(5000)

    @pytest.mark.parametrize(
        ('fname', 'precision', 'ans'),
        [('spsingle.fits', 'single', 'e'),
         ('spdouble.fits', 'double', 'd'),
         ('spdefault.fits', None, 'd')])
    def test_write(self, tmpdir, fname, precision, ans):
        f = str(tmpdir.join(fname))
        self.sp.writefits(f, precision=precision)
        hdr = fits.getheader(f, ext=1)
        assert hdr['tform2'].lower() == ans


@use_cdbs
class TestPrecisionBP(TestPrecision):
    def setup_class(self):
        self.sp = ObsBandpass('acs,hrc,f555w')
