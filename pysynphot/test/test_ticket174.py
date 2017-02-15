from __future__ import absolute_import, division, print_function

import pytest

from .utils import use_cdbs
from ..exceptions import PartialOverlap
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..spparser import parse_spec


@use_cdbs
def test_force_partial():
    rband = (1146, 1213)
    bp = ObsBandpass('cos,fuv,g130m,c1318,psa')
    sp = parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1330.000000,1.),'
                    '2e-013,flam)')
    obs = Observation(sp, bp)

    # Force
    assert obs.countrate(range=rband, force=True) > 0

    # No force
    with pytest.raises(PartialOverlap):
        obs.countrate(range=rband)
