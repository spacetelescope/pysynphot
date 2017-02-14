"""
Container for tests of newly added COS functionality such as new obsmode.
In general, these tests simply test for file integrity (i.e., if there
are no errors, the tests pass) rather than comparison results.
"""
from __future__ import absolute_import, division, print_function

import pytest

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..spectrum import BlackBody


@use_cdbs
class TestCOS(object):
    def setup_class(self):
        self.bb = BlackBody(5500)

    @pytest.mark.parametrize(
        'obsmode',
        ['cos,fuv,g130m,c1055',
         'cos,fuv,g130m,c1096',
         'cos,fuv,g140l,c1280'])
    def test_fuv_obsmode(self, obsmode):
        obs = Observation(self.bb, ObsBandpass(obsmode))  # noqa
