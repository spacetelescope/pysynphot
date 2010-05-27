# New file to hold tests for the Unit class and its subclasses.
from __future__ import division
import sys
import os
import testutil
import numpy as N

from pysynphot.spectrum import ArraySourceSpectrum as ArraySpectrum
from pysynphot import extinction, spectrum

#Code under test
from pysynphot import units

class AddInverseMicron(testutil.FPTestCase):
    def setUp(self):
        self.x=units.Units('1/um')
        self.mwave=extinction._buildDefaultWaveset()[0:10]
        self.awave=(spectrum.default_waveset.copy()[::10])[0:10]
        
    def teststr(self):
        self.failUnless(str(self.x)=='1/um')

    def testunittoang(self):
        test=self.x.Convert(self.mwave,'angstrom')
        self.assertApproxNumpy(test,self.awave)

    def testunitfromang1(self):
        ang=units.Units('angstrom')
        test=ang.Convert(self.awave,'1/um')
        self.assertApproxNumpy(test,self.mwave)

    def testunitfromang2(self):
        ang=units.Units('angstrom')
        test=ang.Convert(self.awave,'InverseMicron')
        self.assertApproxNumpy(test,self.mwave)

    def testunitfromang3(self):
        ang=units.Units('angstrom')
        test=ang.Convert(self.awave,'inversemicrons')
        self.assertApproxNumpy(test,self.mwave)
        
        
    def testfromang(self):

        test=ArraySpectrum(wave=self.awave,
                             flux=N.ones(self.awave.shape),
                             waveunits='angstrom',
                             fluxunits='flam')
        test.convert('1/um')
        self.failUnless(isinstance(test.waveunits,units.InverseMicron))
        self.assertApproxNumpy(test.wave,self.mwave)

    def testcreate(self):
        test=ArraySpectrum(wave=self.mwave,
                             flux=N.ones(self.mwave.shape),
                             waveunits='1/um',
                             fluxunits='flam')
        self.failUnless(isinstance(test.waveunits,units.InverseMicron))
        self.assertEqualNumpy(test.wave,self.mwave)
                        
    def testtoang(self):
        test=ArraySpectrum(wave=self.mwave,
                            flux=N.ones(self.mwave.shape),
                            waveunits='1/um',
                            fluxunits='flam')
        
        test.convert('angstrom')
        self.failUnless(isinstance(test.waveunits,units.Angstrom))
        self.assertApproxNumpy(test.wave,self.awave)
                                                
