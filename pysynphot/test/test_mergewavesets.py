from __future__ import absolute_import, division, print_function

import numpy as np

from .utils import use_cdbs
from ..reddening import Extinction
from ..spectrum import BlackBody, MergeWaveSets, MERGETHRESH


@use_cdbs
def test_merge_wave_sets():
    """
    The function S.spectrum.MergeWaveSets is designed so that merged wave sets
    have no two adjacent values which differ by less than
    S.spectrum.MERGETHRESH. This tests that.
    """
    bb = BlackBody(20000)
    ext = Extinction(0.04, 'gal1')
    new_wave = MergeWaveSets(bb.wave, ext.wave)
    delta = new_wave[1:] - new_wave[:-1]
    assert np.all(delta > MERGETHRESH), \
        'Deltas should be < {}, min delta = {}'.format(MERGETHRESH, delta.min())  # noqa
