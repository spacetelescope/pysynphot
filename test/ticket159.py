from __future__ import division
import os
import testutil
import pysynphot as S
from pysynphot import etc
from pysynphot import locations

class SuccessCase(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(5000)
        self.bp=S.ObsBandpass('Johnson,V')
        S.setref(comptable='$PYSYN_CDBS/mtab/t260548pm_tmc.fits')
        self.tda=dict(spectrum=str(self.sp),
                      bp=str(self.bp)
                      )
        self.tda.update(S.observationmode.getref())
                     

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
        S.setref(comptable='$PYSYN_CDBS/mtab/t260548pm_tmc.fits')
        self.tda=dict(spectrum=str(self.spectrum),
                      bp=str(self.obsmode)
                      )
        self.tda.update(S.observationmode.getref())
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
        S.setref()

    def testwarn(self):
        obs=S.Observation(self.sp,self.bp,force='taper')
        self.assert_('PartialOverlap' in obs.warnings)

    def testcrwarn(self):
        ans=etc.countrate(self.parameters)
        self.tra=dict(ans=ans)
        self.assert_('partial' in ans[-1])

    def testcountrate(self):
        ans=etc.countrate(self.parameters)
        q=(float(ans[0])-self.refrate)/self.refrate
        self.tra=dict(ans=ans, discrep=q)
        self.failIf(abs(q)>0.01)
