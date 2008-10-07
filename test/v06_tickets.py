import sys
import os
import testutil
import pysynphot as S
import numpy as N

class Ticket128(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.FlatSpectrum(10)
        self.bp=S.Box(10000,100)

    def testsp(self):
        tst=self.sp(5000)
        self.assert_(tst == 10)

    def testbp1(self):
        tst=self.bp(10000)
        self.assert_(tst == 1.0)

    def testbp2(self):
        tst=self.bp(3000)
        self.assert_(tst == 0.0)
