import os, sys
import math

import numpy as N
import pyfits
from pytools import testutil 
import units
import locations
import spectrum
from obsbandpass import ObsBandpass


## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import ui_test
## ui_test.FileTestCase('testwave').debug()


class FileTestCase(testutil.FPTestCase):
    def setUp(self):
        self.fname = os.path.join(locations.rootdir,'calspec','feige66_002.fits')
        self.sp = spectrum.TabularSourceSpectrum(self.fname)
        self.openfits = pyfits.open(self.fname)

    def testsubtract(self):
        "ui_test.FileTestCase('testsub'): Subtract two spectra, #23"
        sp2=self.sp + self.sp
        sp3=sp2-self.sp
        self.assertEqualNumpy(sp3.flux,self.sp.flux)

    def tearDown(self):
        self.openfits.close()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__)
