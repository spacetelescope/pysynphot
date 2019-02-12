"""
Applies to both #125 and #126.
Test raises an error if the bug has not been fixed.
"""
from __future__ import absolute_import, division, print_function

import pytest

from ..spectrum import SourceSpectrum
from ..spparser import parse_spec


@pytest.mark.remote_data
def test_ticket125():
    sp = parse_spec('rn(icat(k93models,44500,0.0,5.0),band(nicmos,2,f222m),'
                    '18,vegamag)')
    assert isinstance(sp, SourceSpectrum)
