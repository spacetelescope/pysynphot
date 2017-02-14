from __future__ import absolute_import, division, print_function

import os

import pytest
from numpy.testing import assert_array_equal, assert_allclose

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..refs import getref, setref
from ..spectrum import BlackBody


@use_cdbs
class TestDefault(object):
    def setup_class(self):
        self.sp = BlackBody(4400)

        # Note that this bandpass has a simple 1A-spacing binwave
        self.bp = ObsBandpass('acs,hrc,f555w')

        self.obs = Observation(self.sp, self.bp)
        self.obs.convert('counts')

    @pytest.mark.parametrize(
        ('wave', 'binwave'),
        [(5500, 5500),
         (5523.3, 5523.0),
         (5523.8, 5524.0)])
    def test_ref(self, wave, binwave):
        # Important note: binwave contains bin _centers_.
        ref = self.obs.binflux[self.obs.binwave == binwave]
        tst = self.obs.sample(wave, binned=True, fluxunits='counts')

        # Since we're getting the ref out of the same array, the
        # numbers really should be exactly the same
        assert_array_equal(tst, ref)


@use_cdbs
class TestStisDef(object):
    """Same tests as above but for an actual disperser."""
    def setup_class(self):
        # Use a defined comptab here: we're examining native arrays
        self.oldref = getref()
        setref(comptable=os.path.join(os.environ['PYSYN_CDBS'], 'mtab',
                                      'OLD_FILES', 'u4c18498m_tmc.fits'))
        self.sp = BlackBody(4400)
        self.bp = ObsBandpass('stis,fuvmama,g140m,c1470,s52x01')
        self.obs = Observation(self.sp, self.bp)

    def tearDown(self):
        setref(comptable=self.oldref['comptable'])

    @pytest.mark.xfail(reason='old test was written wrong')
    @pytest.mark.parametrize(
        ('ref', 'refwave', 'binned'),
        [(4.43311555e-08, 1450, True),
         (4.43311555e-08, 1450.03, True),
         (4.43461351e-08, 1450.08, True),
         (1.93621958e-07, 1450.03, False),
         (1.62642353e-07, 1450.1, False),
         (1.18385774e-07, 1450.2, False)])
    def test_ref(self, ref, refwave, binned):
        tst = self.obs.sample(refwave, binned=binned, fluxunits='counts')
        assert_allclose(tst, ref, rtol=0.001)

    def test_nativeref(self):
        refwave = 1450

        # Look up the reference in the correct units
        self.obs.convert('counts')
        ref = self.obs.flux[self.obs.wave == refwave]
        self.obs.convert('photlam')

        tst = self.obs.sample(refwave, binned=False, fluxunits='counts')
        assert_allclose(tst, ref, rtol=0.001)

    @pytest.mark.xfail(reason='old test was written wrong')
    def test_nlast(self):
        refwave = self.obs.binwave[-1]
        ref = self.obs.binflux[-1]
        tst = self.obs.sample(refwave, binned=False, fluxunits='counts')
        assert_allclose(tst, ref, rtol=0.001)
