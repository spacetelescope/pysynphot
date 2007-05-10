""" Module to hold testutil-style test cases for tickets against non-UI
behaviors."""

import sys
import math
import os

import numpy as N
import pyfits
import testutil #from pytools

import units
import locations

import wavetable
import etc,spectrum

import pysynphot as S

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

class ObservationTestCase(testutil.FPTestCase):
    """These test cases will be used to test implementation of Ticket #33"""
    def setUp(self):
        self.userdir = os.environ['PYSYN_USERDATA']
        self.sp = S.FileSpectrum(os.path.join(self.userdir,'alpha_lyr_stis_003.fits'))
        self.bp = S.ObsBandpass('acs,hrc,f555w')
        
    def testobs1(self):
        "tickettest.ObservationTestCase('testobs1'): #30, (acs,hrc,f555w)*vega"
        tst=self.bp.observe(self.sp)
        ref=S.FileSpectrum(os.path.join(self.userdir,'testobs1.fits'))
        self.assertEqualNumpy(tst.wave, ref.wave)
        self.assertEqualNumpy(tst.flux, ref.flux)
                           
                                 

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
