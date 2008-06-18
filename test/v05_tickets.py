import sys
import os
import testutil
import pysynphot as S
import numpy as N
from pysynphot.units import Units
from pysynphot import extinction, spectrum, units

class ticket121(testutil.FPTestCase):
    def setUp(self):
        self.sp=S.BlackBody(30000)

    def testintegral(self):
        self.sp.convert('flam')
        self.sp.convert('Angstrom')
        wave,flux=self.sp.getArrays()
        self.ang=self.sp.trapezoidIntegration(wave,flux)
        self.sp.convert('fnu')
        self.sp.convert('hz')
        wave,flux=self.sp.getArrays()
        self.hz=self.sp.trapezoidIntegration(wave,flux)
        self.failUnlessAlmostEqual(self.ang/self.hz,1)


class AddInverseMicron(testutil.FPTestCase):
    def setUp(self):
        self.x=Units('1/um')
        self.mwave=extinction._buildDefaultWaveset()[0:10]
        self.awave=(spectrum.default_waveset.copy()[::10])[0:10]
        
    def teststr(self):
        self.failUnless(str(self.x)=='1/um')

    def testunittoang(self):
        test=self.x.Convert(self.mwave,'angstrom')
        self.assertApproxNumpy(test,self.awave)

    def testunitfromang1(self):
        ang=Units('angstrom')
        test=ang.Convert(self.awave,'1/um')
        self.assertApproxNumpy(test,self.mwave)

    def testunitfromang2(self):
        ang=Units('angstrom')
        test=ang.Convert(self.awave,'InverseMicron')
        self.assertApproxNumpy(test,self.mwave)

    def testunitfromang3(self):
        ang=Units('angstrom')
        test=ang.Convert(self.awave,'inversemicrons')
        self.assertApproxNumpy(test,self.mwave)
        
        
    def testfromang(self):

        test=S.ArraySpectrum(wave=self.awave,
                             flux=N.ones(self.awave.shape),
                             waveunits='angstrom',
                             fluxunits='flam')
        test.convert('1/um')
        self.failUnless(isinstance(test.waveunits,units.InverseMicron))
        self.assertApproxNumpy(test.wave,self.mwave)

    def testcreate(self):
        test=S.ArraySpectrum(wave=self.mwave,
                             flux=N.ones(self.mwave.shape),
                             waveunits='1/um',
                             fluxunits='flam')
        self.failUnless(isinstance(test.waveunits,units.InverseMicron))
        self.assertEqualNumpy(test.wave,self.mwave)
                        
    def testtoang(self):
        test=S.ArraySpectrum(wave=self.mwave,
                            flux=N.ones(self.mwave.shape),
                            waveunits='1/um',
                            fluxunits='flam')
        
        test.convert('angstrom')
        self.failUnless(isinstance(test.waveunits,units.Angstrom))
        self.assertApproxNumpy(test.wave,self.awave)
                                                
class AddMag(testutil.FPTestCase):
    "Ticket #122"
    def setUp(self):
        self.bright=S.UnitSpectrum(18.0,fluxunits='abmag')
        self.faint=S.UnitSpectrum(21.0,fluxunits='abmag')
        self.delta=3

    def testadd(self):
        test=self.bright.addmag(self.delta)
        self.assertEqualNumpy(test.flux,self.faint.flux)

    def testsubtract(self):
        test=self.faint.addmag(self.delta*-1.0)
        self.assertEqualNumpy(test.flux,self.bright.flux)

    def testtypecatch(self):
        self.assertRaises(TypeError,
                          self.faint.addmag,
                          self.bright)
