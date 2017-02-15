"""Test that exceptions really are raised when they should be."""
from __future__ import absolute_import, division, print_function

import os

import pytest

from .utils import use_cdbs
from .. import refs
from ..obsbandpass import ObsBandpass
from ..observationmode import ObservationMode
from ..spectrum import FlatSpectrum


@use_cdbs
class TestTMCMismatch(object):
    """Can arise with mismatched graph & component tables."""
    def setup_class(self):
        self.oldrefs = refs.getref()
        self.obsmode = 'acs,hrc,f555w,mjd#54000'

        path = os.environ['PYSYN_CDBS']
        refs.COMPTABLE = os.path.join(
            path, 'mtab', 'OLD_FILES', 'r1j2146sm_tmc.fits')
        refs.GRAPHTABLE = os.path.join(
            path, 'mtab', 'OLD_FILES', 'rbg2236im_tmg.fits')

    def teardown_class(self):
        refs.COMPTABLE = self.oldrefs['comptable']
        refs.GRAPHTABLE = self.oldrefs['graphtable']

    def test_exception(self):
        """compname not found in TMC file."""
        with pytest.raises(IndexError):
            ObservationMode(self.obsmode)


@use_cdbs
def test_renorm_exception():
    """Can arise with zero, negative, or NaN spectra."""
    sp = FlatSpectrum(1) * -10
    bp = ObsBandpass('johnson,v')

    with pytest.raises(ValueError):
        sp.renorm(15, 'vegamag', bp)
