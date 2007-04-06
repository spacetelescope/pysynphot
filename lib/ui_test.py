import sys
import math

import numpy as N
import pyfits
import testutil #from pytools

import units
import locations
import spectrum
from obsbandpass import ObsBandpass


## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import ui_test
## ui_test.FileTestCase('testwave').debug()


class FileTestCase(testutil.FPTestCase):
    def setUp(self):
        self.fname = locations.rootdir + 'calspec/feige66_002.fits'
        self.sp = spectrum.TabularSourceSpectrum(self.fname)
        self.openfits = pyfits.open(self.fname)

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

    def testresample(self):
        "ui_test.FileTestCase('testresample'): Tests #24"
        sp2=self.sp.resample(N.arange(10000,18000,2))
        self.failIf(sp2.fluxunits is None)
        #self.assertEqualNumpy(sp2.wave, N.arange(10000,18000,2))

    def testadd(self):
        "ui_test.FileTestCase('testadd'): Add two spectra"
        sp2=self.sp + self.sp
        sumflux = self.sp.flux + self.sp.flux
        self.assertEqualNumpy(sp2.flux,sumflux)

    def testsubtract(self):
        "ui_test.FileTestCase('testsub'): Subtract two spectra, #23"
        sp2=self.sp + self.sp
        sp3=sp2-self.sp
        self.assertEqualNumpy(sp3.flux,self.sp.flux)
        
    def tearDown(self):
        self.openfits.close()

class BandTestCase(testutil.FPTestCase):
    def testomfail(self):
        "ui_test.BandTestCase('testomfail'): Tests #30"
        bp1=ObsBandpass('johnson,v')

    def testompass(self):
        "ui_test.BandTestCase('testompass'): Tests r172"
        bp1=ObsBandpass('acs,hrc,f555w')
        self.assert_(len(bp1) == 6)

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
