"""
Applies to both #125 and #126.
Test raises an error if the bug has not been fixed.
"""
from __future__ import absolute_import, division, print_function

from .utils import use_cdbs
from ..spectrum import SourceSpectrum
from ..spparser import parse_spec


@use_cdbs
def test_ticket125():
    sp = parse_spec('rn(icat(k93models,44500,0.0,5.0),band(nicmos,2,f222m),'
                    '18,vegamag)')
    assert isinstance(sp, SourceSpectrum)
