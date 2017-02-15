from __future__ import absolute_import, division, print_function
from astropy.extern.six import iteritems

import os

import pytest
from astropy.io import fits

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..spectrum import BlackBody


class TestSpecHdr(object):
    @pytest.fixture(autouse=True)
    def setup_class(self, tmpdir):
        # Write the file
        self.sp = BlackBody(5500)
        self.fname = str(tmpdir.join('t163_spcase.fits'))
        self.keys = dict(sptype=('blackbody', 'Type of spectrum'),
                         bbtemp=(5500, ))
        self.sp.writefits(self.fname, hkeys=self.keys)

        # Read the header
        with fits.open(self.fname) as f:
            self.h0 = f[0].header
            self.h1 = f[1].header

    def test_header(self):
        assert 'origin' in self.h0
        assert os.path.basename(self.fname) == self.h0['filename']

        assert str(self.sp) == self.h1['expr']
        assert 'G15.7' == self.h1['tdisp1'].strip().upper()

    def test_keys(self):
        for k, v in iteritems(self.keys):
            assert self.h0[k] == v[0]


@use_cdbs
class TestBandHdr(TestSpecHdr):
    @pytest.fixture(autouse=True)
    def setup_class(self, tmpdir):
        # Write the file
        self.sp = ObsBandpass('acs,hrc,f555w')  # Is actually bp
        self.fname = str(tmpdir.join('t163_bpcase.fits'))
        self.sp.writefits(self.fname)

        # Read the header
        with fits.open(self.fname) as f:
            self.h0 = f[0].header
            self.h1 = f[1].header

    def test_keys(self):
        assert 'grftable' in self.h1
        assert 'cmptable' in self.h1
