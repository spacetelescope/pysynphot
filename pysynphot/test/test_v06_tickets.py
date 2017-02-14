from __future__ import absolute_import, division, print_function

import numpy as np

from .utils import use_cdbs
from ..catalog import Icat
from ..obsbandpass import ObsBandpass
from ..spectrum import (ArraySourceSpectrum,  ArraySpectralElement, Box,
                        UniformTransmission)


def test_box():
    bp = Box(10000, 100)

    assert bp(10000) == 1
    assert bp.sample(10000) == 1

    assert bp(3000) == 0
    assert bp.sample(3000) == 0

    bp2 = bp * 3
    assert bp2(10000) == 3


def test_flat():
    bp = UniformTransmission(0.5)
    assert bp.sample(3000) == 0.5


class TestTabular(object):
    def setup_class(self):
        self.wv = np.arange(1000, 2000)
        self.fl = np.zeros(self.wv.shape)
        self.fl[100:-100] = 10.0
        self.sp = ArraySourceSpectrum(self.wv, self.fl, fluxunits='photlam')

    def test_compsp(self):
        sp2 = ArraySourceSpectrum(self.wv[48:], self.fl[48:]*2.3,
                                  fluxunits='photlam')
        sp = self.sp + sp2
        assert self.sp(1500) == 10
        assert sp(1500) == 10 + (10 * 2.3)

    def test_bp(self):
        bp = ArraySpectralElement(self.wv, self.fl)
        assert bp(1500) == 10


@use_cdbs
def test_obsband():
    bp = ObsBandpass('acs,hrc,f555w')
    assert bp(3000) == 0


@use_cdbs
def test_icat():
    sp = Icat('k93models', 4500, 1, 2)
    assert sp(3000) > 0
