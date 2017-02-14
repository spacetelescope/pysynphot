from __future__ import absolute_import, division, print_function

import pytest

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..observationmode import _ThermalObservationMode


@use_cdbs
def test_exceptions():
    """
    Making a ThermalObservationMode for an obsmode that has no support
    for thermal calculations should raise an exception.
    """
    obsmode = 'acs,hrc,f555w'
    bp = ObsBandpass(obsmode)

    with pytest.raises(NotImplementedError):
        _ThermalObservationMode(obsmode)

    with pytest.raises(NotImplementedError):
        bp.thermback()


@use_cdbs
def test_therm():
    obsmode = 'nicmos,3,f222m'
    bp = ObsBandpass(obsmode)

    # No error
    _ThermalObservationMode(obsmode)

    assert bp.thermback() > 0
