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
        ans=self.bp.check_overlap(self.sp)
        self.failUnless(ans=='partial')
        
    def testtaper(self):
        self.obs=S.Observation(self.sp,self.bp,force='taper')
        idx=N.where(self.obs.wave==self.refwave)
        test=self.obs.flux.item(idx[0])
        self.assert_(test==0,'Expected 0, got %f'%test)

    def testextrap(self):
        self.obs=S.Observation(self.sp,self.bp,force='extrap')
        idx=N.where(self.obs.wave==self.refwave)
        test=self.obs.flux.item(idx[0])
        self.assertAlmostEqual(test,self.refval,msg='Expected %f, got %f'%(self.refval,test))
        
##     def testrange(self):
##         self.wt=N.array([3090, 3095, 4000,4005, 4010])
##         ans=self.sp(self.wt)
##         self.ref=N.array( [1.0, 1.0, 1.0, 0.0, 0.0])
##         self.assertEqualNumpy(self.ref,ans)

    def testraise(self):
        self.assertRaises(ValueError,
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
        self.refval=2.97759742e-06

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
        self.a=S.Box(4000,50)
        self.disjoint=S.Box(6000,100)
        self.full=S.Box(4000,100)
        self.partial=S.Box(4050,50)
        
    def testdisjoint(self):
        stat=self.a.check_overlap(self.disjoint)
        self.failUnless(stat == 'none')

    def testfull(self):
        stat=self.a.check_overlap(self.full)
        self.failUnless(stat == 'full')

    def testpartial(self):
        stat=self.a.check_overlap(self.partial)
        self.failUnless(stat == 'partial')


class BP03(BPOverlap):
    def setUp(self):
        self.a=S.ArrayBandpass(wave=N.arange(4000,5000),
                               throughput=N.ones(1000))
        self.disjoint=S.Box(1000,100)
        self.full=S.ArrayBandpass(wave=N.arange(3000,6000),
                                  throughput=N.ones(3000))
        self.partial=S.ArrayBandpass(wave=N.arange(500,4500),
                                     throughput=N.ones(4000))


class AnalyticCase(testutil.FPTestCase):
    def setUp(self):
        self.bb=S.BlackBody(5000)
        self.em=S.GaussianSource(3300,1,1)
        self.flat=S.FlatSpectrum(10)
        self.pl=S.PowerLaw(5000,-2)
        self.tspec=S.ArraySpectrum(self.bb.wave,self.bb.flux,
                                   fluxunits=self.bb.fluxunits)
        self.pl.writefits('ac_pl.fits')
        self.fspec=S.FileSpectrum('ac_pl.fits')

    def tearDown(self):
        os.unlink('ac_pl.fits')

    def testbb(self):
        self.assert_(self.bb.isAnalytic)

    def testfile(self):
        self.failIf(self.fspec.isAnalytic)

    def testtab(self):
        self.failIf(self.tspec.isAnalytic)

    def testcomp1(self):
        x=self.bb+self.em
        self.assert_(x.isAnalytic)

    def testcomp2(self):
        x=self.bb+self.tspec
        self.failIf(x.isAnalytic)

    def testcomp3(self):
        x=self.flat*2.6
        self.assert_(x.isAnalytic)

## class ETC01(OverlapBug):

                                     
##         self.spectrum = "em(4300.0,1.0,9.999999960041972E-13,flam)"
##         self.obsmode = "stis,ccd,g430l"

 
##         self.spectrum = "em(4000.0,10.0,1.0000000168623835E-16,flam)"
##         self.obsmode = "acs,hrc,PR200L"

##         self.spectrum = "(spec(crcalspec$grw_70d5824_stis_001.fits))"
##         self.obsmode = "stis,fuvmama,g140l,s52x2"

##         spectrum = "spectrum= rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
##         instrument = "instrument=stis,ccd"

##         spectrum = "spectrum=((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
##         instrument = "instrument=acs,sbc,F140LP"

##         spectrum = "spectrum=em(3880.0,10.0,1.0000000168623835E-16,flam)"
##         instrument = "instrument=acs,wfc1,FR388N#3880"

##         testdata  = os.path.join(locations.rootdir,'calspec','feige66_002.fits')
##         'obsmode':        'acs,hrc,f555w',
