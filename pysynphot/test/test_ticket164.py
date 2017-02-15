from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pytest

from .utils import use_cdbs
from .. import refs, units
from ..locations import irafconvert
from ..obsbandpass import ObsBandpass
from ..refs import getref, setref

startup = None


def setup_module(module):
    global startup
    setref()
    startup = getref()


class TestSet(object):
    @classmethod
    def teardown_class(cls):
        setref()

    @pytest.mark.parametrize(
        ('ttype', 'ref'),
        [('graphtable', 'mtab$foobar.fits'),
         ('comptable', 'mtab$foobar.fits'),
         ('area', 12345.6)])
    def test_set(self, ttype, ref):
        kwargs = {ttype: ref}
        setref(**kwargs)
        tst = getref()[ttype]
        msg = '(ref,tst)=({},{})'.format(ref, tst)

        if ttype == 'area':
            assert ref == tst, msg
        else:
            assert irafconvert(ref) == irafconvert(tst), msg

    def test_refs_area(self):
        setref(area=100)
        assert refs.PRIMARY_AREA == 100

    def test_counts(self):
        """
        Area is used to convert to counts.
        So, changing the area should change the resulting counts.
        """
        w = np.arange(1, 10)
        p = units.Photlam()
        ref = p.ToCounts(w, w)

        setref(area=10)
        tst = p.ToCounts(w, w)

        assert not np.allclose(ref, tst)

    def test_reset(self):
        setref()
        tst = getref()
        assert startup == tst, '(ref,tst)=({},{})'.format(startup, tst)


class TestMulti(object):
    def setup_class(self):
        self.gref = os.path.join(os.environ['PYSYN_CDBS'], 'mtab',
                                 'OLD_FILES', 't2605492m_tmg.fits')
        self.cref = os.path.join(os.environ['PYSYN_CDBS'], 'mtab',
                                 'OLD_FILES', 't260548pm_tmc.fits')
        setref(graphtable=self.gref, comptable=self.cref)
        self.pick = getref()

    def teardown_class(self):
        setref()

    def test_ref(self):
        assert self.pick['graphtable'] == self.gref
        assert self.pick['comptable'] == self.cref

    @use_cdbs
    def test_bp(self):
        bp = ObsBandpass('acs,hrc,f555w')
        assert bp.obsmode.gtname == self.gref
        assert bp.obsmode.ctname == self.cref
