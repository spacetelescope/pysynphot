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
class TestWriteParse(object):
    """
    pytest.mark.parametrize gives URLError for FTP connection, so we have
    to do it this way instead.
    """
    def setup_class(self):
        self.obj = interpret(parse(scan('ebmvx(0.5,gal1)')))

    def test_write_obj(self, tmpdir):
        fname = tmpdir.join(os.path.basename(self.obj.name) + '.fits')
        self.obj.writefits(str(fname))


class TestWriteFeige(TestWriteParse):
    def setup_class(self):
        self.obj = FileSourceSpectrum(
            os.path.join(root, 'calspec', 'feige66_002.fits'))


class TestWriteV(TestWriteParse):
    def setup_class(self):
        self.obj = FileSpectralElement(
            os.path.join(root, 'comp', 'nonhst', 'johnson_v_003_syn.fits'))


class TestWriteACS(TestWriteParse):
    def setup_class(self):
        self.obj = ObsBandpass('acs,hrc,f555w')


class TestWriteMJD(TestWriteParse):
    def setup_class(self):
        self.obj = ObsBandpass('acs,hrc,f555w,mjd#54000')


class TestWriteMult(TestWriteParse):
    def setup_class(self):
        self.obj = BlackBody(10000) * ObsBandpass('acs,hrc,f555w')


class TestWriteIcat(TestWriteParse):
    def setup_class(self):
        self.obj = Icat('k93models', 3500, 0.0, 4.6)
