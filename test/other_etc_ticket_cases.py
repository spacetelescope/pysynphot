import sys
import os
import tempfile

from pysynphot import spectrum,observationmode
from pysynphot import newobservation as observation
from pysynphot import ObsBandpass
from pysynphot import locations
from pysynphot import spparser as P
from pysynphot import units, planck
from pysynphot import newetc as etc
import pysynphot as S

from pytools import testutil 
import other_etc_test

from other_etc_test import values

testdata  = os.path.join(locations.rootdir,'calspec','feige66_002.fits')


class ETC_Imag1(testutil.FPTestCase):
    """Ticket 21: parameterized keywords, Imag1"""

    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        self.expr = "(earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5)"
        os.chdir(locations.specdir)

    def test4cr2(self):
        """Ticket #71: discrepancy for (acs,sbc,f150lp) powerlaw case"""
        spectrum = "spectrum=rn(pl(4000,1.0,jy),box(5500.0,1),1e-18,flam)"
        instrument = "instrument=acs,sbc,F150LP"
        parameters = [spectrum, instrument]
        countrate = etc.countrate(parameters)
        self.assertApproxFP(countrate[0], 7.73334E-02)


class ETC_Imag2(testutil.FPTestCase):
    """Ticket 21: parameterized keywords, Imag2"""
    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        os.chdir(locations.specdir)
       
    def tearDown(self):
        os.chdir(self.oldpath)
        
    def test7(self):
        "test7: acs,hrc,fr488n#3880 discrep"
        spectrum = "spectrum=rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15.0,vegamag)"
        instrument = "instrument=acs,hrc,FR388N#3880"
        parameters = [spectrum, instrument]
        countrate = etc.countrate(parameters)
        self.assertApproxFP(float(countrate[0]), 28.56996)

    def testtherm3(self):
        obsmode = "obsmode=nicmos,1,F090M"
        countrate = etc.thermback([obsmode])
        synphot_ref=1.98635725923e-12
        self.assertApproxFP(float(countrate), synphot_ref)

    def testtherm4(self):
        obsmode = "obsmode=nicmos,1,f190n"
        countrate = etc.thermback([obsmode])
        synphot_ref=0.0142158651724
        self.assertApproxFP(float(countrate), synphot_ref)

    def testtherm5(self):
        obsmode = "obsmode=wfc3,ir,f110w"
        countrate = etc.thermback([obsmode])
        synphot_ref=0.0342143550515
        self.assertApproxFP(float(countrate), synphot_ref)


        

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)


