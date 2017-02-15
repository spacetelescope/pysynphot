"""Tests varying legal cases for ASCII file spectrum data."""
from __future__ import absolute_import, division, print_function

import numpy as np
import pytest

from ..exceptions import BadRow
from ..spectrum import FileSourceSpectrum


def writedata(start=0, end=4000):
    """len = end - start"""
    s = ''
    for k in range(start, end):
        s += '{}   {}\n'.format(wave[k], flux[k])
    return s


def writeinline():
    """len = nwave"""
    s = ''
    for k in range(nwave):
        s += '{}   {}   # Line {}\n'.format(wave[k], flux[k], k)
    return s


def write3():
    """len = nwave"""
    s = ''
    for k in range(nwave):
        s += '{}   {}   {}\n'.format(wave[k], flux[k], wave[k])
    return s


wave = np.arange(10000, 14000, dtype=np.float64)
flux = np.ones(wave.shape, dtype=np.float64)
nwave = len(wave)
s_writedata = writedata()


@pytest.mark.parametrize(
    ('fn', 'dat', 'wlen'),
    [('goodfile.dat', s_writedata, 4000),
     ('head1.dat', '#   wave      flux\n\n' + s_writedata, 4000),
     ('head2.dat', '#  1   wave\n#  2  flux\n' + s_writedata, 4000),
     ('blank.dat', s_writedata + '\n\n\n\n\n', 4000),
     ('midcomment.dat', writedata(end=2000) +
      '#middle of the file\n#  yet more middle of the file\n' +
      writedata(start=2000), 4000),
     ('inline.dat', writeinline(), nwave),
     ('3col.dat', write3(), nwave)])
def test_writedata(tmpdir, fn, dat, wlen):
    fname = tmpdir.join(fn)
    fname.write(dat)
    wlen = 4000
    sp = FileSourceSpectrum(str(fname))

    # test length
    assert len(sp.wave) == wlen

    # test garbage
    assert np.all(np.isfinite(sp.flux))


def test_badline(tmpdir):
    fname = tmpdir.join('badline.dat')
    fname.write(s_writedata + 'Hello world')

    with pytest.raises(BadRow):
        FileSourceSpectrum(str(fname))
