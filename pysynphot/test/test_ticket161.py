from __future__ import absolute_import, division, print_function

import numpy as np

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass


@use_cdbs
def test_err_col():
    """Test that this obsmode does not raise exception."""
    obs = ObsBandpass('stis,ccd,50ccd,mjd#55000')
    assert np.any(obs.throughput > 0)
