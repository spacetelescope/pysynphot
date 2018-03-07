from __future__ import absolute_import, division, print_function

import os

import numpy as np
from astropy.utils.data import get_pkg_data_filename

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..reddening import Extinction
from ..refs import getref, setref
from ..spectrum import BlackBody, FileSourceSpectrum, MergeWaveSets, MERGETHRESH

orig_graphtable = None
orig_comptable = None


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


@use_cdbs
class TestQSOCountrate(object):
    """
    Extinction curve waveset should not be merged into composite spectrum
    when applied. See https://github.com/spacetelescope/pysynphot/issues/44 .
    """
    @classmethod
    def setup_class(cls):
        global orig_graphtable, orig_comptable
        cfg = getref()
        orig_graphtable = cfg['graphtable']
        orig_comptable = cfg['comptable']

        # Answers computed using specified tables
        mtab = os.path.join(os.environ['PYSYN_CDBS'], 'mtab')
        setref(graphtable=os.path.join(mtab, '14l1632sm_tmg.fits'),
               comptable=os.path.join(mtab, 'OLD_FILES', '16n1832tm_tmc.fits'))

    def test_countrate(self):
        bp = ObsBandpass('acs,hrc,f850lp')

        fname = get_pkg_data_filename(os.path.join('data', 'qso_template.fits'))
        qso = FileSourceSpectrum(fname)
        sp_ext = qso * Extinction(1.0, 'mwavg')
        sp = sp_ext.renorm(20, 'vegamag', ObsBandpass('johnson,v'), force=True)

        obs = Observation(sp, bp, force='taper')
        c = obs.countrate()
        np.testing.assert_allclose(c, 2.3554364232173565e-05)

    @classmethod
    def teardown_class(cls):
        setref(graphtable=orig_graphtable, comptable=orig_comptable)
