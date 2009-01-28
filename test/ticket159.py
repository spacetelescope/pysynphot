import os
import testutil
import pysynphot as S
from pysynphot import etc
from pysynphot import locations

class SuccessCase(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(5000)
        self.bp=S.ObsBandpass('Johnson,V')

    def testok(self):
        obs=S.Observation(self.sp,self.bp)
        self.assert_('PartialOverlap' not in obs.warnings)
        
class ETCTestCase(testutil.FPTestCase):

    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        os.chdir(locations.specdir)
        self.spectrum = "((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        self.obsmode = "acs,sbc,F140LP"
        self.refrate=0.0877036
        self.setup2()
        
    def setup2(self):
        try:
            self.oldpath=os.path.abspath(os.curdir)
            os.chdir(locations.specdir)
            self.sp=etc.parse_spec(self.spectrum)
            self.bp=S.ObsBandpass(self.obsmode)
            self.parameters=["spectrum=%s"%self.spectrum,
                             "instrument=%s"%self.obsmode]
        except AttributeError:
            pass
        
    def tearDown(self):
        os.chdir(self.oldpath)

    def testwarn(self):
        obs=S.Observation(self.sp,self.bp,force='taper')
        self.assert_('PartialOverlap' in obs.warnings)

    def testcountrate(self):
        ans=etc.countrate(self.parameters)
        self.assert_('partial' in ans[-1])

