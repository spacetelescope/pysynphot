from __future__ import absolute_import, division, print_function

import numpy as np
import pytest

from ..obsbandpass import ObsBandpass


@pytest.mark.remote_data
def test_err_col():
    """Test that this obsmode does not raise exception."""
    obs = ObsBandpass('stis,ccd,50ccd,mjd#55000')
    assert np.any(obs.throughput > 0)
