from __future__ import absolute_import, division, print_function

import pytest

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass


@use_cdbs
def test_no_thermback():
    bp = ObsBandpass('acs,sbc,f150lp')

    with pytest.raises(NotImplementedError):
        bp.thermback()
