from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest

from .utils import use_cdbs
from ..catalog import Icat
from ..obsbandpass import ObsBandpass
from ..spectrum import (ArraySourceSpectrum, BlackBody, Box,
                        FileSourceSpectrum, FileSpectralElement, FlatSpectrum,
                        GaussianSource, Powerlaw, UniformTransmission)
from ..spparser import interpret, parse, scan

root = os.environ['PYSYN_CDBS']


@pytest.mark.parametrize(
    'obj',
    [ArraySourceSpectrum(np.arange(1, 10000), np.arange(9999) * 2.5),
     BlackBody(10000),
     Box(7000, 13.5),
     FlatSpectrum(10.0, fluxunits='flam'),
     GaussianSource(1e14, 10000, 10),
     Powerlaw(10000, 0.5),
     UniformTransmission(0.7)])
def test_write(tmpdir, obj):
    fname = tmpdir.join(os.path.basename(obj.name) + '.fits')
    obj.writefits(str(fname))


@use_cdbs
@pytest.mark.parametrize(
    'obj',
    [interpret(parse(scan('ebmvx(0.5,gal1)'))),
     FileSourceSpectrum(os.path.join(root, 'calspec', 'feige66_002.fits')),
     FileSpectralElement(os.path.join(root, 'comp', 'nonhst',
                                      'johnson_v_003_syn.fits')),
     ObsBandpass('acs,hrc,f555w'),
     ObsBandpass('acs,hrc,f555w,mjd#54000'),
     BlackBody(10000) * ObsBandpass('acs,hrc,f555w'),
     Icat('k93models', 3500, 0.0, 4.6)])
def test_write_cdbs(tmpdir, obj):
    fname = tmpdir.join(os.path.basename(obj.name) + '.fits')
    obj.writefits(str(fname))
