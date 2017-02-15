from __future__ import absolute_import, division, print_function

import os

from astropy.utils.data import get_pkg_data_filename

from .utils import use_cdbs
from ..obsbandpass import ObsBandpass
from ..observation import Observation
from ..refs import getref, setref
from ..spectrum import BlackBody, FileSourceSpectrum, FlatSpectrum


def test_composite_warn():
    sp = BlackBody(5500)
    sp.warnings['FakeWarn'] = True

    for sp2 in (sp * 45, sp + FlatSpectrum(1)):
        assert 'FakeWarn' in sp2.warnings


@use_cdbs
class TestOverlapWarning(object):
    def setup_class(self):
        self.oldref = getref()
        setref(comptable=os.path.join(os.environ['PYSYN_CDBS'], 'mtab',
                                      'OLD_FILES', 't260548pm_tmc.fits'))

    def teardown_class(self):
        setref(comptable=self.oldref['comptable'])

    def test_ok(self):
        sp = BlackBody(5000)
        bp = ObsBandpass('Johnson,V')
        obs = Observation(sp, bp)
        assert 'PartialOverlap' not in obs.warnings

    def test_cos_qso(self):
        sp = FileSourceSpectrum(get_pkg_data_filename(
            os.path.join('data', 'qso_template.fits')))
        bp = ObsBandpass('cos,fuv,g140l,c1230,PSA')
        tst = sp.renorm(17.0, 'vegamag', bp)
        assert 'PartialRenorm' in tst.warnings, \
            'Warnings: {}'.format(tst.warnings)
