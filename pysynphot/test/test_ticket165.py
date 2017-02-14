from __future__ import absolute_import, division, print_function

import pytest

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..spectrum import SpectralElement


@use_cdbs
@pytest.mark.parametrize(
    'obsmode',
    ['wfc3,uvis1,f218w,aper#0.60',
     'wfc3,uvis1,f218w,aper#1.38',
     'wfc3,uvis1,f218w,aper#1.98',
     'wfc3,uvis2,f218w'])
def test_aper(obsmode):
    """Test that WFC3/UVIS aper does not raise exception."""
    bp = ObsBandpass(obsmode)
    assert isinstance(bp, SpectralElement)
