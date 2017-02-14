from __future__ import absolute_import, division, print_function

import os

from ..locations import irafconvert


class TestVarString(object):
    def setup_class(self):
        self.old_cdbs = os.environ['PYSYN_CDBS']
        os.environ['PYSYN_CDBS'] = os.path.join('fake', 'path')

    def teardown_class(self):
        os.environ['PYSYN_CDBS'] = self.old_cdbs

    def test_path(self):
        fname = os.path.join('etc', 'background', 'Zodi.fits')
        ref = os.path.normcase(os.path.normpath(os.path.join(
            os.environ['PYSYN_CDBS'], fname)))
        ans = os.path.normcase(os.path.normpath(irafconvert(os.path.join(
            '$PYSYN_CDBS', fname))))
        assert ref == ans
