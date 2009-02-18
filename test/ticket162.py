import os
import testutil
import pysynphot as S
from pysynphot import etc
from pysynphot import locations

        
class ETCTestCase(testutil.FPTestCase):

    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        os.chdir(locations.specdir)
        self.spectrum = "spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.obsmode = "cos,fuv,g140l,c1105"
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

    def testspecrate(self):
        ans=etc.specrate(self.parameters)
        self.failIf('partial' in ans[-1])

