""" Module to hold testutil-style test cases for tickets against non-UI
behaviors."""

import sys
import math
import os

import numpy as N
import pyfits
from pytools import testutil

import units
import locations

import wavetable
import etc,spectrum

import pysynphot as S
from pysynphot.newobservation import Observation as NewObservation
from pysynphot.observation import Observation as OldObservation
import tempfile

## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import tickettest
## tickettest.FileTestCase('testwave').debug()

class WavecatTestCase(testutil.FPTestCase):
    def setUp(self):
        self.w=wavetable.wavetable

    def testmatch(self):
        "tickettest.WavecatTestCase('testmatch'): nicmos,3,f220m"
        obs='nicmos,3,f220m'
        self.assertEqual(self.w[obs],'(7000.0,29996.0,1.0)')

    def testend(self):
        "tickettest WavecatTestCase('testend'): Ticket #20: acs,hrc,f550m"
        obs="acs,hrc,f550m"
        self.assertEqual(self.w[obs],self.w['acs,hrc'])

    def testmiddle1(self):
        "tickettest.WavecatTestCase('testmiddle1'): Ticket #37, stis,ccd,g750m"
        obs='stis,ccd,g750m'
        self.assertEqual(self.w[obs],self.w['stis,g750m'])

    def testmiddle2(self):
        "tickettest.WavecatTestCase('testmiddle2'): Ticket #37, stis,fuvmama,g140l,s52x2"
        obs='stis,fuvmama,g140l,s52x2'
        self.assertEqual(self.w[obs],self.w['stis,g140l'])

    def testmissing(self):
        "tickettest.WavecatTestCase('testmissing'): #37, stis,ccd"
        obs='stis,ccd'
        self.assertRaises(KeyError,self.w.__getitem__,obs)

    def testambig(self):
        "tickettest.WavecatTestCase('testambig'): #37, stis,nuvmama,e230h,c2263,s02x02"
        obs="stis,nuvmama,e230h,c2263,s02x02"
        self.assertEqual(self.w[obs],self.w['stis,e230h,c2263'])
            
class CalcspecTestCase(testutil.FPTestCase):
    """This is a stripped-down, for-ETC-use-only task that constructs
    a spectrum & writes it to a file. This is not equivalent to the synphot
    task calcspec."""
    def setUp(self):
        self.userdir   = os.environ['PYSYN_USERDATA']
        etc.debug = 0
        
    def test1(self):
        "tickettest.CalcspecTestCase('test1'): #38, rn(pl(4000.0,-1.0,flam),box(1500,1.0),1.00e-14,flam)"
        sp = 'spectrum="rn(pl(4000.0,-1.0,flam),box(1500,1.0),1.00E-14,flam)"'
        out = "output=%s"%os.path.join(self.userdir,'ticket38.fits')
        calculator = etc.Calcspec([sp,out])
        tst = calculator.run()
        
        ref = spectrum.TabularSourceSpectrum(os.path.join(self.userdir,'ticket38_ref.fits'))
        self.assertApproxNumpy(ref.wave, tst.wave)
        self.assertApproxNumpy(ref.flux, tst.flux)

class MergeTestCase(testutil.FPTestCase):
    """Demonstrate the problem described in ticket #34:
    Adding two identical tabular spectra loses a pixel in the resulting
    spectrum's table."""

    def testwave(self):
        """tickettest.MergeTestCase('testwave'): merge simple identical wavesets: #34"""
        foo=N.array(range(10,20),dtype=N.float64)
        x=spectrum.MergeWaveSets(foo,foo)
        self.assertEqualNumpy(foo,x)
            
class ObservationTestCase(testutil.FPTestCase):
    """These test cases will be used to test implementation of Ticket #33"""
    def setUp(self):
        self.userdir = os.environ['PYSYN_USERDATA']
        self.cdbs = locations.rootdir
        self.sp = S.FileSpectrum(os.path.join(self.cdbs,'calspec','gd71_mod_005.fits'))
        self.bp = S.ObsBandpass('acs,hrc,f555w')
        self.oldobs=OldObservation(self.sp,self.bp.obsmode)
        self.ref_specval=self.oldobs.calcphot('spec')

        self.ref=self.oldobs.observed_spectrum
        self.effstim,self.pivot = self.oldobs.calcphot()

        calculator = etc.Countrate(['spectrum=%s'%self.sp,
                                    'instrument=acs,hrc,f555w'])
        self.countrate,self.pivot = calculator.run()
#.........................................................................
        #Effective wavelength calculation is tested against synphot,
        #not old pysynphot observation.calcphot('efflam')
##       --> calcphot acs,hrc,f555w crcalspec$gd71_mod_005.fits flam func=efflerg
##     Mode = band(acs,hrc,f555w)
##        Pivot       Equiv Gaussian
##      Wavelength         FWHM
##       5355.947        841.1204    band(acs,hrc,f555w)
##     Spectrum:  crcalspec$gd71_mod_005.fits
##         VZERO            EFFLERG     Mode: band(acs,hrc,f555w)
##            0.           5309.066
##     --> lpar refdata
##             (area = 45238.93416)    Telescope area in cm^2
##            (grtbl = "mtab$*_tmg.fits") Instrument graph table
##           (cmptbl = "mtab$r1j2146sm_tmc.fits") Instrument component table
##             (mode = "a")
      
        self.efflam = 5309.066
#.........................................................................
        self.idx = self.ref.flux.nonzero()[0]
        self.lx=30
        self.ux=-110

        
    def testobsmost(self):
        "tickettest.ObservationTestCase('testobsmost'): (acs,hrc,f555w)*gd71"
        tst=NewObservation(self.sp,self.bp)
        tst.convert('counts')
        self.assertApproxNumpy(tst.binwave, self.ref.wave)
        self.assertApproxNumpy(tst.binflux[self.idx[self.lx:self.ux]],
                               self.ref.flux[self.idx[self.lx:self.ux]])

    def testlowedge(self):
        "tickettest.ObservationTestCase('testlowedge'): (acs,hrc,f555w)*gd71"
        tst=NewObservation(self.sp,self.bp)
        tst.convert('counts')
        self.assertApproxNumpy(tst.binflux[self.idx[0:self.lx]],
                               self.ref.flux[self.idx[0:self.lx]])
 
    def testhighedge(self):
        "tickettest.ObservationTestCase('testhighedge'): (acs,hrc,f555w)*gd71"
        tst=NewObservation(self.sp,self.bp)
        tst.convert('counts')
        self.assertApproxNumpy(tst.binflux[self.idx[self.ux:]],
                               self.ref.flux[self.idx[self.ux:]])
        
    def testpivot(self):
        "tickettest.ObservationTestCase('testpivot'):"
        tst=NewObservation(self.sp,self.bp)
        ans=tst.pivot()
        self.effstim,self.pivot = self.oldobs.calcphot()
        self.assertApproxFP(self.pivot,ans)

    def testcountrate(self):
        "tickettest.ObservationTestCase('testcountrate'):"
        tst=NewObservation(self.sp,self.bp)
        ans=tst.countrate()
        self.assertApproxFP(self.countrate,ans)

    def testefflam(self):
        "tickettest.ObservationTestCase('testefflam'):"
        tst=NewObservation(self.sp,self.bp)
        ans=tst.efflam()
        self.assertApproxFP(self.efflam,ans)

    def testwrite(self):
        "tickettest.ObservationTestCase('testwrite'):"
        tst=NewObservation(self.sp,self.bp)
        tst.convert('counts')
        fname=os.path.join(tempfile.gettempdir(),'newobs_tstwrite.fits')
        tst.writefits(fname,trimzero=False,clobber=True)
        out=S.FileSpectrum(fname)
        self.assertApproxNumpy(tst.binflux,out.flux)
            
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
