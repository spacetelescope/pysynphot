import sys
import os
import tempfile

from pysynphot import spectrum
from pysynphot import observation
from pysynphot.newobservation import Observation as NewObservation
from pysynphot import observationmode, locations, units, planck
from pysynphot import spparser as P
from pysynphot import etc, newetc
import pysynphot as S

import testutil 

etc.debug=0

localdir=os.path.abspath(os.curdir)

class SpecCase(testutil.FPTestCase):
    def setUp(self):
        os.chdir(locations.specdir)
        self.setparms()
        self.tda={'spectrum':self.spectrum,
                  'obsmode':self.obsmode}
        self.params=['spectrum=%s'%self.spectrum,'instrument=%s'%self.obsmode]
        self.init_countrate()
        self.sp=newetc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.obs=NewObservation(self.sp,self.bp)
        self.lx=100
        self.ux=100

        self.oldobs = self.calculator.observed_spectrum
        self.oldwave, self.oldflux = self.calculator.observed_spectrum.getArrays()
        self.idx = self.oldflux.nonzero()[0]

    def tearDown(self):
        os.chdir(localdir)
    def init_countrate(self):
        """This routine tailors whether the Specrate (on binned waveset) or
        Countrate (on native waveset) will be tested."""
        self.calculator=None
        self.newrate=None

        
    def setparms(self):
        """null method in parent class"""
        self.spectrum=None
        self.obsmode=None
        


    def testcountrate(self):
        self.assertApproxFP(self.oldrate,self.newrate,
                            "old: %f, new: %f"%(self.oldrate, self.newrate))


#    def testlowedge(self):
#
#        self.obs.convert('counts')
#        self.assertApproxNumpy(self.obs.flux[self.idx[0:self.lx]],
#                               self.oldflux[self.idx[0:self.lx]])
# 
#    def testhighedge(self):
#       
#        self.obs.convert('counts')
#        self.assertApproxNumpy(self.obs.flux[self.idx[self.ux:]],
#                               self.oldflux[self.idx[self.ux:]])
        
#    def testpivot(self):
#       
#        tst=NewObservation(self.sp,self.bp)
#        ans=self.obs.pivot()
#        self.effstim,self.pivot = self.oldobs.calcphot()
#        self.assertApproxFP(self.pivot,ans)

#    def testefflam(self):
#
#        tst=NewObservation(self.sp,self.bp)
#        ans=self.obs.efflam()
#        self.assertApproxFP(self.efflam,ans)

class BinnedCase(SpecCase):
    def init_countrate(self):
        self.calculator=etc.SpecSourcerateSpec(self.params)
        self.oldrate=float(self.calculator.run().split(';')[0])
        self.newrate=float(newetc.specrate(self.params).split(';')[0])

    def testobsmost(self):
        self.obs.convert('counts')
        self.assertApproxNumpy(self.obs.binwave, self.oldwave)
        self.assertApproxNumpy(self.obs.binflux[self.idx[self.lx:self.ux]],
                               self.oldflux[self.idx[self.lx:self.ux]])

class NativeCase(SpecCase):
    def init_countrate(self):
        self.calculator=etc.Countrate(self.params)
        self.oldrate=float(self.calculator.run()[0])
        self.newrate=float(newetc.countrate(self.params)[0])
        
    def testobsmost(self):
        self.obs.convert('counts')
        self.assertApproxNumpy(self.obs.wave, self.oldwave)
        self.assertApproxNumpy(self.obs.flux[self.idx[self.lx:self.ux]],
                               self.oldflux[self.idx[self.lx:self.ux]])
