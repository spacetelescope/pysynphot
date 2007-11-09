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

from pytools import testutil 
from pysynphot import other_etc_test


class CalcphotTestCase(testutil.FPTestCase):
    """#33: Observations require a binset"""
    def setUp(self):
        self.sp = spectrum.TabularSourceSpectrum(testdata)
        self.obsmode = observationmode.ObservationMode(values['obsmode'])
        self.obs = observation.Observation(self.sp, self.obsmode)

    def testcountrate(self):
        countrate = self.obs.calcphot()
        self.assertApproxFP(countrate[0], values['countrate'])

    def testefflam(self):
        efflam = self.obs.calcphot(func='efflam')
        self.assertApproxFP(efflam, values['efflam'])

class ETCTestCase_Imag1(testutil.FPTestCase):
    """Ticket 21: parameterized keywords, Imag1"""

    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        self.expr = "(earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5)"
        os.chdir(locations.specdir)

    def test4cr1(self):
        spectrum = "spectrum=em(3880.0,10.0,1.0000000168623835E-16,flam)"
        instrument = "instrument=acs,wfc1,FR388N#3880"
        parameters = [spectrum, instrument]
        countrate = etc.countrate(parameters)
        self.assertApproxFP(countrate[0], 1.25658E-01)

    def test4cr2(self):
        """Ticket #71: discrepancy for (acs,sbc,f150lp) powerlaw case"""
        spectrum = "spectrum=rn(pl(4000,1.0,jy),box(5500.0,1),1e-18,flam)"
        instrument = "instrument=acs,sbc,F150LP"
        parameters = [spectrum, instrument]
        countrate = etc.countrate(parameters)
        self.assertApproxFP(countrate[0], 7.73334E-02)


class ETCTestCase_Imag2(testutil.FPTestCase):
    """Ticket 21: parameterized keywords, Imag2"""
    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        os.chdir(locations.specdir)
       
    def tearDown(self):
        os.chdir(self.oldpath)

    def test7(self):
        spectrum = "spectrum=rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15.0,vegamag)"
        instrument = "instrument=acs,hrc,FR388N#3880"
        parameters = [spectrum, instrument]
        countrate = etc.countrate(parameters)
        self.assertApproxFP(float(countrate[0]), 28.0668)

class ObsmodeTestCase(testutil.FPTestCase):
    """Ticket #21: parameterized keywords, ObsmodeTestCase"""
    def test2(self):
        obsmode = observationmode.ObservationMode("acs,hrc,FR388N#3880")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable
        self.assertApproxFP(throughput[5000], 2.8632756E-007)

    def test3(self):
        obsmode = observationmode.ObservationMode("acs,wfc1,FR647M#6470")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable
        self.assertApproxFP(throughput[5000], 5.647170E-3)

    def test6(self):
        obsmode = observationmode.ObservationMode("acs,hrc,FR388N#3880")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable
        self.assertApproxFP(throughput[5000], 2.863276E-7)


        

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__)


