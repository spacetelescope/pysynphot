from __future__ import absolute_import, division, print_function

import os

import numpy as np
from astropy.utils.data import get_pkg_data_filename
from numpy.testing import assert_allclose

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..refs import getref, setref
from ..spectrum import ArraySourceSpectrum, FileSourceSpectrum

orig_ref = None


def setup_module(module):
    global orig_ref
    orig_ref = getref()

    # Specify a TMC file
    setref(comptable=os.path.join(os.environ['PYSYN_CDBS'],
                                  'mtab', 'OLD_FILES', 't921857im_tmc.fits'))


def teardown_module(module):
    setref(comptable=orig_ref['comptable'])


class TestArrKeepneg(object):
    def setup_class(self):
        self.wave = np.arange(1000, 6000, 1000)
        self.flux = np.array([1.0, 0.5, -0.5, 0.75, 1.0])

    def test_array(self):
        sp = ArraySourceSpectrum(wave=self.wave, flux=self.flux.copy())
        assert sp.flux[2] == 0

    def test_arraykeep(self):
        sp = ArraySourceSpectrum(wave=self.wave, flux=self.flux, keepneg=True)
        assert sp.flux[2] == -0.5, self.flux

    def test_magarray(self):
        sp = ArraySourceSpectrum(wave=self.wave, flux=self.flux,
                                 fluxunits='ABMag')
        assert_allclose(sp.flux[2], -0.5, rtol=1E-4)


@use_cdbs
class TestObsKeepneg(object):
    def setup_class(self):
        self.fname = get_pkg_data_filename(os.path.join('data', 'us7.txt'))
        self.refrate = 2303.5  # provided by C. Oliveira
        self.bp = ObsBandpass('cos,fuv,g130m,c1309,psa')

    def test_clip(self):
        sp = FileSourceSpectrum(self.fname)
        obs = Observation(sp, self.bp)
        rate = obs.countrate()
        assert abs(rate - self.refrate) < 1, \
            'tst {} ref {}'.format(rate, self.refrate)

    def test_keep(self):
        sp = FileSourceSpectrum(self.fname, keepneg=True)
        obs = Observation(sp, self.bp)
        rate = obs.countrate()
        assert rate < self.refrate
        assert obs.flux.min() < 0
