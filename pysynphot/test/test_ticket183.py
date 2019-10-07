from __future__ import absolute_import, division, print_function

import pytest

from ..obsbandpass import ObsBandpass


@pytest.mark.remote_data
def test_no_thermback():
    bp = ObsBandpass('acs,wfc1,f555w')

    with pytest.raises(NotImplementedError):
        bp.thermback()
