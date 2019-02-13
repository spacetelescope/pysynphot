from __future__ import absolute_import, division, print_function

import pytest

from ..obsbandpass import ObsBandpass


@pytest.mark.remote_data
def test_no_thermback():
    bp = ObsBandpass('acs,sbc,f150lp')

    with pytest.raises(NotImplementedError):
        bp.thermback()
