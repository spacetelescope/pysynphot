from __future__ import absolute_import, division, print_function

import os

import pytest

from .utils import use_cdbs
from ..locations import irafconvert
from ..spparser import parse_spec


@use_cdbs
class TestTicket52(object):
    def setup_class(self):
        self.ref = os.path.join(
            os.environ['PYSYN_CDBS'], 'calspec', 'gd50_004.fits')

    @pytest.mark.parametrize(
        'fname',
        ['crcalspec$gd50_004.fits',
         '$PYSYN_CDBS/calspec/gd50_004.fits'])
    def test_iraf(self, fname):
        tst = irafconvert(fname)
        assert tst == self.ref, 'Expected {}, got {}'.format(self.ref, tst)

        sp = parse_spec(fname)
        assert str(sp) == self.ref

    @pytest.mark.xfail(reason='invalid test')
    def test_plain(self):
        tst = irafconvert('gd50_004.fits')
        assert tst == self.ref, 'Expected {}, got {}'.format(self.ref, tst)
