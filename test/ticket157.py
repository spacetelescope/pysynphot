import pysynphot as S
from pysynphot.observation import Observation
from pysynphot import etc
import os, sys
import testutil
import numpy as N

class OverlapBug(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.ArraySpectrum(wave=N.arange(3000,4000),
                                flux=N.ones((1000,))*0.75,
                                name="Short flat")
        self.bp=S.Box(4000,100)
        self.refwave=4005
        self.refval=0.75

    def testoverlap(self):
        ans=self.sp.overlap(self.bp)
        self.failUnless(ans='partial')
        
    def testtaper(self):
        self.obs=S.Observation(self.sp,self.bp,force='taper')
        idx=N.where(self.obs.wave==self.refwave)
        test=self.obs.flux[idx[0]]
        self.assert_(test==0,'Expected 0, got %f'%test)

    def testextrap(self):
        self.obs=S.Observation(self.sp,self.bp,force='extrap')
        idx=N.where(self.obs.wave==self.refwave)
        test=self.obs.flux[idx[0]]
        self.assert_(test==self.refval,'Expected %f, got %f'%(self.refval,test))
        
##     def testrange(self):
##         self.wt=N.array([3090, 3095, 4000,4005, 4010])
##         ans=self.sp(self.wt)
##         self.ref=N.array( [1.0, 1.0, 1.0, 0.0, 0.0])
##         self.assertEqualNumpy(self.ref,ans)

    def testraise(self):
        self.assertRaises(KeyError,
                          S.Observation,
                          self.sp, self.bp)


class DiscoveryCase(OverlapBug):
    def setUp(self):
        fname='qso_template.fits'
        self.spstring='rn(z(spec(%s),0.03),band(johnson,v),18,vegamag)' %fname
        self.sp=etc.parse_spec(self.spstring)
        self.sp.convert('photlam')
        self.bp=S.ObsBandpass('stis,ccd,g750l,c7751,s52x02')
        self.refwave=6200
        self.refval=4.44878989e-05

##     def testorig(self):
##         #This test fails unless the Observation has the "expected"
##         #behavior. Pre-fix, it will fail because that's the bug.
##         #Post-fix, it will have an error and end with an exception.
##           #It can be uncommented as a sanity check, but will never pass.
##           
##         self.obs=S.Observation(self.sp,self.bp)
##         idx=N.where(self.obs.wave==self.refwave)
##         testval=self.obs.flux[idx[0]]
##         self.failUnless(testval == 0,'obs[%d]==%g'%(self.refwave,testval))
        
class BPOverlap(testutil.FPTestCase):
    def setUp(self):
        self.a=S.Box(4000,100)
        self.disjoint=S.Box(6000,100)
        self.full=S.Box(4000,50)
        self.partial=S.Box(4050,200)
        
    def testdisjoint(self):
        stat=self.a.overlapstat(self.disjoint)
        self.failUnless(stat == 'none')

    def testfull(self):
        stat=self.a.overlapstat(self.full)
        self.failUnless(stat == 'full')

    def testpartial(self):
        stat=self.a.overlapstat(self.partial)
        self.failUnless(stat == 'partial')
