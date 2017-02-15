"""
Very preliminary tests of some bandpar functionality.
These answers were computed with pysynphot and eyeballed against
synphot answers. These tests are only to establish that the
functionality doesn't *break*. More rigorous tests should be added.
"""
from __future__ import absolute_import, division, print_function

import os

import pytest
from numpy.testing import assert_allclose

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..refs import getref, setref
from ..spectrum import FileSpectralElement

orig_graphtable = None
orig_comptable = None


def setup_module(module):
    global orig_graphtable, orig_comptable
    cfg = getref()
    orig_graphtable = cfg['graphtable']
    orig_comptable = cfg['comptable']

    # Answers computed using specified tables
    mtab = os.path.join(os.environ['PYSYN_CDBS'], 'mtab', 'OLD_FILES')
    setref(graphtable=os.path.join(mtab, '0661437lm_tmg.fits'),
           comptable=os.path.join(mtab, '0661429jm_tmc.fits'))


def teardown_module(module):
    setref(graphtable=orig_graphtable, comptable=orig_comptable)


@use_cdbs
@pytest.mark.parametrize(
    ('cls', 'om', 'avgw', 'effi', 'equiv', 'rectw', 'rmsw'),
    [(FileSpectralElement, 'crnonhstcomp$johnson_v_004_syn.fits',
      5490.5552003639823, 0.15678915809503616, 857.34999515116215,
      857.34999515116215, 357.13065617707804),
     (ObsBandpass, 'wfc3,uvis1,fq672n',
      6716.6253925114133, 0.00071479633888800855, 4.8006812790841318,
      19.373016584072371, 46.46729888277223)])
def test_bandpar(cls, om, avgw, effi, equiv, rectw, rmsw):
    bp = cls(om)
    assert_allclose(bp.avgwave(), avgw)
    assert_allclose(bp.efficiency(), effi)
    assert_allclose(bp.equivwidth(), equiv)
    assert_allclose(bp.rectwidth(), rectw)
    assert_allclose(bp.rmswidth(), rmsw)
