from __future__ import division
import os
import testutil
import pysynphot as S
import numpy as N

class Handmade(testutil.FPTestCase):
    def setUp(self):
        #Hand-make an observation with well defined ranges
        w=N.arange(1000,1100,0.5)
        self.sp=S.ArraySpectrum(wave=w,
                                flux=(w-1000),
                                fluxunits='counts',
                                name='slope1')
        #Hand make a box so it has fewer points
        self.bp=S.ArrayBandpass(wave=N.array([1000,1009.95,1010,
                                              1030,1030.05,1100]),
                                throughput=N.array([0,0,1,1,0,0]),
                                name='HandBox')
        #self.bp=S.Box(1020,20)
        self.obs=S.Observation(self.sp,self.bp,
                               binset=N.arange(w[6],w[40]))

    def tearDown(self):
        self.tda=dict(sp=str(self.sp))
        try:
            self.tra=dict(ref=self.ref,tst=self.tst)
        except AttributeError:
            pass

    def testallbin(self):
        #Specifying the entire exact range should be identical to the
        #results without any such specification
        self.ref=self.obs.countrate()
        self.tst=self.obs.countrate(range=[self.obs.binwave[0],
                                      self.obs.binwave[-1]],
                               )
        self.assertApproxFP(self.ref,self.tst)

    def testexactbin(self):
        #Specifying an exact range
##         >>> idx=slice(10,14)
##         >>> print x.obs.binwave[idx]
##         [ 1013.  1014.  1015.  1016.]
##         >>> print x.obs.binflux[idx]
##         [ 26.  28.  30.  32.]
##         >>> print x.obs.binflux[idx].sum()
##         116.0

        self.ref=116.0
        self.tst=self.obs.countrate(range=[1013,1016])
        self.assertApproxFP(self.ref,self.tst)

    def testofflowbin(self):
        #Specifying a wholly contained range but at slightly
        #offset sampling
        self.ref=116.0
        self.tst=self.obs.countrate(range=[1012.8,1016])
        self.assertApproxFP(self.ref,self.tst)

    def testoffhibin(self):
        #Specifying a wholly contained range but at slightly
        #offset sampling
        self.ref=116.0
        self.tst=self.obs.countrate(range=[1013.2,1016])
        self.assertApproxFP(self.ref,self.tst)

    def testdisjointbin(self):
        #Ask for something outside the bin range
        self.assertRaises(ValueError,
                          self.obs.countrate,
                          dict(range=[1025,1030])
                          )

    def testovlphibin(self):
        #Ask for something _partly_ outside the bin range
        self.ref=140
        try:
            self.tst=self.obs.countrate(range=[1016,1026])
            self.assert_(False, "No exception raised")
        except ValueError, e:
            print "Exception: ",str(e)
            self.failUnless(str(self.ref) in str(e))
            
    def testovlplobin(self):
        #Ask for something _partly_ outside the bin range
        self.ref=172.75
        try:
            self.tst=self.obs.countrate(range=[1000,1016])
            self.assert_(False, "No exception raised")
        except ValueError, e:
            print "Exception: ",str(e)
            self.failUnless(str(self.ref) in str(e))

class TestRange(object):
    def setUp(self):
        self.sp=S.BlackBody(5500)
        self.bp=S.ObsBandpass('johnson,v')

        self.range = (10000,11000)
        self.getanswer()

    def getanswer(self):
        #The right answer is defined by countrate of a Box covering
        #the range
        self.obs = S.Observation(self.sp,self.bp)
        
        lx,ux=self.range
        center=lx + (ux-lx)/2.0
        range=ux-lx
        ref=S.Observation(self.sp,self.bp*S.Box(center, range))
        self.ref=ref.countrate()

    def testrange(self):
        tst=self.obs.countrate(range=self.range)
        q=(tst-self.ref)/self.ref
        assert abs(q)<0.00001, 'tst, ref, discrep: %g, %g, %g'%(tst,
                                                                self.ref,
                                                                q)
