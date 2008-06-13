import sys
import os
import testutil
import pysynphot as S

class ticket121(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(30000)

    def testintegral(self):
        self.sp.convert('flam')
        self.sp.convert('Angstrom')
        wave,flux=self.sp.getArrays()
        self.ang=self.sp.trapezoidIntegration(wave,flux)
        self.sp.convert('fnu')
        self.sp.convert('hz')
        wave,flux=self.sp.getArrays()
        self.hz=self.sp.trapezoidIntegration(wave,flux)
        self.failUnlessAlmostEqual(self.ang/self.hz,1)
