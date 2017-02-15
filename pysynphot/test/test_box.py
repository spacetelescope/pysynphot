from __future__ import absolute_import, division, print_function

from ..spectrum import Box
from ..units import Angstrom


def test_basic_box():
    bp = Box(5000, 100)
    assert bp.sample(5000) == 1  # test inside
    assert bp.sample(4000) == 0  # test outside
    assert bp.sample(4949) == 0  # test bound
    assert isinstance(bp.waveunits, Angstrom)  # test units


def test_ticket114():
    bp = Box(500, 10, waveunits='nm')
    assert str(bp.waveunits) == 'nm'  # test units
    assert bp.sample(500) == 1  # test inside
