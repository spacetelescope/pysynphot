import sys
import math

import numpy as N
import pyfits
import testutil #from pytools

import units
import locations
import spectrum


## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import ui_test
## ui_test.FileTestCase('testwave').debug()


class FileTestCase(testutil.FPTestCase):
    def setUp(self):
        self.fname = locations.rootdir + 'calspec/feige66_002.fits'
        self.sp = spectrum.TabularSourceSpectrum(self.fname)
        self.openfits = pyfits.open(self.fname)
        self.failIf(self.sp == None, 'cannot build spectrum object')

    def testwave(self):
        "ui_test.FileTestCase('testwave'): r164 wave"
        fitswave=self.openfits[1].data.field('wavelength')
        self.assertEqualNumpy(self.sp.wave, fitswave)

    def testflux(self):
        "ui_test.FileTestCase('testflux'): r164 flux"
        fitsflux=self.openfits[1].data.field('flux')
        self.assertApproxNumpy(self.sp.flux, fitsflux)

    def testname(self):
        "ui_test.FileTestCase('testname'): Tests r163"
        self.assert_(str(self.sp) == self.fname)
        self.assert_(self.sp.filename == self.fname)

    def tearDown(self):
        self.openfits.close()

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
