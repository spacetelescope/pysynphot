from __future__ import division
import os
import testutil
import pysynphot as S
from pysynphot import etc
from pysynphot import locations, refs

        
class ETCTestCase(testutil.FPTestCase):

    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        os.chdir(locations.specdir)
        self.spectrum = "spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.obsmode = "cos,fuv,g140l,c1105"
        #These tests were defined using this graph table
        S.setref(comptable='$PYSYN_CDBS/mtab/tad1851am_tmc.fits')
        self.setup2()
        self.tda=dict(obsmode=self.obsmode,
                      spectrum=self.spectrum)
        self.tda.update(refs.getref())

    def setup2(self):
        try:
            self.oldpath=os.path.abspath(os.curdir)
            os.chdir(locations.specdir)
            self.sp=etc.parse_spec(self.spectrum)
            self.bp=S.ObsBandpass(self.obsmode)
            self.parameters=["spectrum=%s"%self.spectrum,
                             "instrument=%s"%self.obsmode,
                             "obsmode=%s"%self.obsmode]
        except AttributeError:
            pass
        
    def tearDown(self):
        os.chdir(self.oldpath)

    def testwarn(self):
        obs=S.Observation(self.sp,self.bp,force='taper')
        self.assert_('PartialOverlap' in obs.warnings)

    def testspecrate(self):
        result=etc.specrate(self.parameters)
        #ans structure is different
        ans=result.split(';')
        self.failUnless('partial' in ans[-1], 'error message: %s'%ans[-1])

    def testcalcphot(self):
        ans=etc.calcphot(self.parameters)
        try:
            self.failUnless('partial' in ans[-1])
        except IndexError, e:
            #Then we didn't get an error message: fail
            self.fail('No error message generated')
