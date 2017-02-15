"""
Test various aspects of having an area keyword in graphtable headers and
propogating that area back to places where it's used.
"""
from __future__ import absolute_import, division, print_function

import os

import pytest
from astropy.utils.data import get_pkg_data_filename
from numpy.testing import assert_allclose

from .utils import use_cdbs
from .. import refs, units
from ..exceptions import IncompatibleSources
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..observationmode import ObservationMode
from ..spectrum import FlatSpectrum, Integrator
from ..tables import GraphTable

GT_FILE_NO = ''
GT_FILE_100 = ''


def setup_module(module):
    global GT_FILE_NO, GT_FILE_100

    # A stock graph table on CDBS
    path = os.environ['PYSYN_CDBS']
    GT_FILE_NO = os.path.join(path, 'mtab', 'OLD_FILES', 'n9i1408hm_tmg.fits')

    # This copy of a graph table has been modified to have PRIMAREA = 100.0
    GT_FILE_100 = get_pkg_data_filename(
        os.path.join('data', 'cdbs', 'mtab', 'n9i1408hm_tmg.fits'))


def teardown_module(module):
    refs.setref()


def test_gt100():
    gt = GraphTable(GT_FILE_100)
    assert gt.primary_area == 100.0


@use_cdbs
def test_gtno():
    gt = GraphTable(GT_FILE_NO)
    assert not hasattr(gt, 'primary_area')


@use_cdbs
@pytest.mark.parametrize('cls', [ObservationMode, ObsBandpass, Observation])
def test_obsmode_gt100(cls):
    """Same behavior for obsmode and bandpass."""
    if cls is Observation:
        sp = FlatSpectrum(1)
        bp = cls(sp, ObsBandpass('acs,hrc,f555w', graphtable=GT_FILE_100))
    else:
        bp = cls('acs,hrc,f555w', graphtable=GT_FILE_100)

    assert bp.primary_area != refs.PRIMARY_AREA
    assert bp.primary_area == 100.0

    # This should have no effect.
    refs.setref(area=1.)
    assert refs.PRIMARY_AREA == 1

    assert bp.primary_area != refs.PRIMARY_AREA
    assert bp.primary_area == 100.0


@use_cdbs
@pytest.mark.parametrize('cls', [ObservationMode, ObsBandpass, Observation])
def test_obsmode_gtno(cls):
    if cls is Observation:
        sp = FlatSpectrum(1)
        bp = cls(sp, ObsBandpass('acs,hrc,f555w', graphtable=GT_FILE_NO))
    else:
        bp = cls('acs,hrc,f555w', graphtable=GT_FILE_NO)

    assert bp.primary_area == refs.PRIMARY_AREA

    # This should change the obsmode area.
    refs.setref(area=1.)
    assert refs.PRIMARY_AREA == 1

    assert bp.primary_area == refs.PRIMARY_AREA


@use_cdbs
class TestObsBandpass(object):
    def setup_class(self):
        self.bp = ObsBandpass('acs,hrc,f555w', graphtable=GT_FILE_100)
        self.area = 100

    def test_composite_spectral_element(self):
        """You can't combine 2 bandpasses that don't have the same area."""
        bp2 = ObsBandpass('acs,hrc,f555w', graphtable=GT_FILE_NO)
        with pytest.raises(IncompatibleSources):
            self.bp * bp2

    def test_unit_response(self):
        """Test that the graph table's area gets used in a method."""
        tst = self.bp.unit_response()
        wave = self.bp.GetWaveSet()
        thru = self.bp(wave)
        intg = Integrator()
        ref = (units.HC /
               (self.area * intg.trapezoidIntegration(wave, thru * wave)))
        assert_allclose(ref, tst)
