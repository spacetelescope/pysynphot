import sys
import os
import testutil
import pysynphot as S
import pyfits

class Precision(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(5000)
        
        self.sp.writefits('/tmp/spdouble.fits',precision='double')
        self.sp.writefits('/tmp/spdefault.fits')

    def tearDown(self):
        os.unlink(self.fname)
        
    def testsingle(self):
        self.fname='/tmp/spsingle.fits'
        self.sp.writefits(self.fname,precision='single')
        f=pyfits.open(self.fname)
        self.assert_(f[1].header['tform2'].lower() == 'e')

    def testdouble(self):
        self.fname='/tmp/spdouble.fits'
        self.sp.writefits(self.fname,precision='double')
        f=pyfits.open(self.fname)
        self.assert_(f[1].header['tform2'].lower() == 'd')

    def testdefault(self):
        self.fname='/tmp/spdefault.fits'
        self.sp.writefits(self.fname)
        f=pyfits.open(self.fname)
        self.assert_(f[1].header['tform2'].lower() == 'd')

                                        
                                            
