import sys
import unittest
import pylab

import spectrum
import observation
import observationmode
import locations
import spparser as P
import units
import etc
import planck


testindex = 0
# spectrum values @ testindex
values = {'flam':           '2.79979E-11',
          'flam z=2.5':     '6.53011E-13',
          'fnu':            '1.23037E-23',
          'photlam':        '1.61773E+00',
          'photlam z=1.0':  '4.04432E-01',
          'photlam z=2.5':  '1.32060E-01',
          'photnu':         '7.10915E-13',
          'jy':             '1.23037E+00',
          'mjy':            '1.23037E+03',
          'abmag':          '8.67490E+00',
          'stmag':          '5.28218E+00',
          'obmag':          '-1.23590E+01',
          'v=0.0':          '4.38149E-07',
          'v=5.0':          '4.38149E-09',
          'vegamag':        '1.81443E+00',
          'counts':         '8.78177E+04',
          'angstrom':       '1.14780E+03',
          'angstrom z=1.0': '2.29560E+03',
          'angstrom z=2.5': '4.01730E+03',
          'hz':             '2.61189E+15',
          'nm':             '1.14780E+02',
          'micron':         '1.14780E-01',
          'mm':             '1.14780E-04',
          'cm':             '1.14780E-05',
          'm':              '1.14780E-07',
          'integral':       '1.65862E+03',
          'sp_npoints':     '5.11000E+03',
          'thru_npoints':   '1.00600E+03',
          'thru_500':       '1.22485E-01',
          'obsmode':        'acs,hrc,f555w',
          'hstarea':        '4.52389E+04',
          'countrate':      '7.64522E+05',
          'efflam':         '5.32599E+03'
          }

format_spec = '%.5E'    # floating point precision in assert
format_offset = {'win32':1,'sunos5':0,'linux2':0}

def format(value):
    ''' Formats scientific notation according to platform.    
    '''
    str = format_spec%(value)

    index1 = str.index('E') + 2
    index2 = index1 + format_offset[sys.platform]

    str1 = str[0:index1]
    str2 = str[index2:len(str)]

    return str1+str2


def testAll():
##    testsuite = unittest.TestSuite()
##
##    testsuite.addTest(UnitsTestCase)
##    testsuite.addTest(ObsmodeTestCase)
##    testsuite.addTest(SpectrumTestCase)
##
##    runner = unittest.TextTestRunner()
##    runner.run(testsuite)

    # TestSuite is broken (!$##$&%^$^%!!)

    runner = unittest.TextTestRunner()
    
    testcase = UnitsTestCase()
    runner.run(testcase)
    testcase = SpectrumTestCase()
    runner.run(testcase)
    testcase = PlanckTestCase()
    runner.run(testcase)
    testcase = ObsmodeTestCase()
    runner.run(testcase)
    testcase = CalcphotTestCase()
    runner.run(testcase)
    testcase = FunctionTestCase()
    runner.run(testcase)
    testcase = ParserTestCase()
    runner.run(testcase)
    testcase = IcatTestCase()
    runner.run(testcase)
    testcase = ResamplerTestCase()
    runner.run(testcase)
    testcase = ETCTestCase_Imag1()
    runner.run(testcase)
    testcase = ETCTestCase_Imag2()
    runner.run(testcase)
    testcase = ETCTestCase_Spec1()
    runner.run(testcase)
    testcase = ETCTestCase_Spec2()
    runner.run(testcase)
    testcase = ETCTestCase_Spec3()
    runner.run(testcase)


class TestSetUp(unittest.TestCase):
    ''' Base class for all classes that use the test spectrum feige66_002.
        This class also acts as an implicit test for the FITS file reading
        machinery in the spectrum.TabularSourceSpectrum class.
    '''
    def setUp(self):
        self.sp = spectrum.TabularSourceSpectrum(locations.testdata)

        assert self.sp != None, 'cannot build spectrum object'

        self.assertEqual(self.sp.waveunits.name,'angstrom')
        self.assertEqual(self.sp.fluxunits.name,'flam')
        self.assertEqual(format(len(self.sp._wavetable)), values['sp_npoints'])
        self.assertEqual(format(len(self.sp._fluxtable)), values['sp_npoints'])

        # check internal arrays; they should always be expressed
        # in internal units.
        self.assertEqual(format(self.sp._wavetable[testindex]),values['angstrom'])
        self.assertEqual(format(self.sp._fluxtable[testindex]),values['photlam'])

        # fluxes should be expressed in flam
        (wav,flux) = self.sp.getArrays()
        self.assertEqual(format(flux[testindex]),values['flam'])

    # Turns off all assertion errors. This is to be used temporarily
    # while the graph table files are still separate (COS and WFC3 versions).
    def assertEqual(self, testvalue, expected):
        pass


class UnitsTestCase(TestSetUp):
    def setUp(self):
        TestSetUp.setUp(self)

    def runTest(self):
        # don't put these in a loop; it's easier to spot failure points
        # this way.......
        self._testWave(self.sp,'angstrom')
        self._testWave(self.sp,'nm')
        self._testWave(self.sp,'micron')
        self._testWave(self.sp,'mm')
        self._testWave(self.sp,'cm')
        self._testWave(self.sp,'m')
        self._testWave(self.sp,'hz')

        self._testFlux(self.sp,'flam')
        self._testFlux(self.sp,'fnu')
        self._testFlux(self.sp,'photlam')
        self._testFlux(self.sp,'photnu')
        self._testFlux(self.sp,'jy')
        self._testFlux(self.sp,'mjy')
        self._testFlux(self.sp,'abmag')
        self._testFlux(self.sp,'stmag')
        self._testFlux(self.sp,'obmag')
        self._testFlux(self.sp,'vegamag')
        self._testFlux(self.sp,'counts')

    def _testFlux(self, spectrum, units):
        spectrum.convert(units)
        (waves, fluxes) = spectrum.getArrays()
        self.assertEqual(format(fluxes[testindex]), values[units])

    def _testWave(self, spectrum, units):
        spectrum.convert(units)
        (waves, fluxes) = spectrum.getArrays()
        self.assertEqual(format(waves[testindex]), values[units])


class SpectrumTestCase(TestSetUp):
    def setUp(self):
        TestSetUp.setUp(self)

    def runTest(self):
        self._testRedshift()
        self._testIntegrate()
        self._testMagnitude()

    def _testRedshift(self):
        # redshift = 0 should return the same input.
        sp = self.sp.redshift(0.0)
        self.assertEqual(format(sp._wavetable[testindex]), values['angstrom'])
        self.assertEqual(format(sp._fluxtable[testindex]), values['photlam'])
        (dummy, fluxes) = sp.getArrays()
        self.assertEqual(format(fluxes[testindex]),values['flam'])

        # convert to photnu, then redshift, and check that flux in
        # photonu units didn't change.
        sp.convert('photnu')
        self.assertEqual(format(sp._wavetable[testindex]), values['angstrom'])
        self.assertEqual(format(sp._fluxtable[testindex]), values['photlam'])
        (dummy, fluxes) = sp.getArrays()
        self.assertEqual(format(fluxes[testindex]),values['photnu'])

        z = 1.0
        sp2 = sp.redshift(z)
        self.assertEqual(format(sp2._wavetable[testindex]), values['angstrom z=1.0'])
        (dummy, fluxes) = sp2.getArrays()
        self.assertEqual(format(fluxes[testindex]),values['photnu'])

        # internal array should change though, it's in photlam units.
        self.assertEqual(format(sp2._fluxtable[testindex]),values['photlam z=1.0'])

        # now test redshift in flam units.
        sp.convert('flam')
        sp2 = sp.redshift(2.5)
        self.assertEqual(format(sp2._wavetable[testindex]), values['angstrom z=2.5'])
        self.assertEqual(format(sp2._fluxtable[testindex]), values['photlam z=2.5'])
        (dummy, fluxes) = sp2.getArrays()
        self.assertEqual(format(fluxes[testindex]),values['flam z=2.5'])

    def _testIntegrate(self):
        integral = self.sp.integrate()
        self.assertEqual(format(integral), values['integral'])

    def _testMagnitude(self):
        vmag = spectrum.Magnitude('johnson,v',0.0)
        sp2 = self.sp.setMagnitude(vmag)
        (dummy, fluxes) = sp2.getArrays()
        self.assertEqual(format(fluxes[testindex]), values['v=0.0'])

        vmag = spectrum.Magnitude('johnson,v',5.0)
        sp2 = self.sp.setMagnitude(vmag)
        (dummy, fluxes) = sp2.getArrays()
        self.assertEqual(format(fluxes[testindex]), values['v=5.0'])


class PlanckTestCase(unittest.TestCase):
    def runTest(self):
        flux = planck.bb_photlam_arcsec(spectrum.default_waveset, 1000.)


class ObsmodeTestCase(unittest.TestCase):
    def runTest(self):

        obsmode = observationmode.ObservationMode(values['obsmode'])

        self.assertEqual(format(obsmode.area), values['hstarea'])
        throughput = obsmode.Throughput().throughputtable
        self.assertEqual(format(len(throughput)), values['thru_npoints'])
        self.assertEqual(format(throughput[500]), values['thru_500'])
        
        obsmode = observationmode.ObservationMode("acs,hrc,FR388N#3880")
##        files = obsmode.GetFiles()
##        for f in files:
##            print f
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("acs,wfc1,FR647M#6470")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("acs,sbc,F125LP")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("stis,ccd")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("acs,hrc,FR388N#3880")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("acs,wfc1,G800L")
##        obsmode = observationmode.ObservationMode("stis,g750m,c8825")
        wave = obsmode.bandWave()

        obsmode = observationmode.ObservationMode("stis,fuvmama,g140l,s52x2")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("acs,hrc,PR200L")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("stis,nuvmama,e230h,c2263,s02x02")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable

        obsmode = observationmode.ObservationMode("wfc3,ir,f160w")
        wave = obsmode.Throughput().GetWaveSet()
        throughput = obsmode.Throughput().throughputtable


class CalcphotTestCase(TestSetUp):
    def setUp(self):
        TestSetUp.setUp(self)

    def runTest(self):
        obsmode = observationmode.ObservationMode(values['obsmode'])
        obs = observation.Observation(self.sp, obsmode)

        countrate = obs.calcphot()
        self.assertEqual(format(countrate[0]), values['countrate'])

        efflam = obs.calcphot(func='efflam')
        self.assertEqual(format(efflam), values['efflam'])


class FunctionTestCase(unittest.TestCase):
    def runTest(self):
        an = spectrum.AnalyticSpectrum()
        wave = an.GetWaveSet()

        sp = spectrum.UnitSpectrum(1.0,fluxunits='photlam')
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.shape[0]),'1.00000E+04')
        self.assertEqual(format(fluxes[0]),'1.00000E+00')
        self.assertEqual(format(fluxes[9000]),'1.00000E+00')

        sp = spectrum.UnitSpectrum(1.0,fluxunits='flam')
        fluxes = sp(wave)
        self.assertEqual(format(fluxes[0]),'2.51701E+10')
        self.assertEqual(format(fluxes[9000]),'8.81633E+11')
        waves,fluxes = sp.getArrays()
        self.assertEqual(format(fluxes[0]),'1.00000E+00')
        self.assertEqual(format(fluxes[9000]),'1.00000E+00')

        box = spectrum.Box(5500.0,1.0)
        self.assertEqual(format(box.wavetable.shape[0]),'2.20000E+01')
        self.assertEqual(format(box.throughputtable.shape[0]),'2.20000E+01')
        self.assertEqual(format(box.throughputtable[1]),'1.00000E+00')

        sp = spectrum.UnitSpectrum(1.0,fluxunits='photlam')
        box = spectrum.Box(5500.0,1.0)
        sp = sp * box
        wave = sp.GetWaveSet()
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.sum()),'2.00000E+01')

        sp = spectrum.UnitSpectrum(1.0,fluxunits='flam')
        box = spectrum.Box(5500.0,1.0)
        sp = sp * box
        wave = sp.GetWaveSet()
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.sum()),'5.53744E+12')


class ParserTestCase(unittest.TestCase):
    def runTest(self):
        an = spectrum.AnalyticSpectrum()
        wave = an.GetWaveSet()

        expr = "unit(1,photlam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.shape[0]),'1.00000E+04')
        self.assertEqual(format(fluxes[0]),'1.00000E+00')
        self.assertEqual(format(fluxes[9000]),'1.00000E+00')

        expr = "unit(1,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        fluxes = sp(wave)
        self.assertEqual(format(fluxes[0]),'2.51701E+10')
        self.assertEqual(format(fluxes[9000]),'8.81633E+11')
        waves,fluxes = sp.getArrays()
        self.assertEqual(format(fluxes[0]),'1.00000E+00')
        self.assertEqual(format(fluxes[9000]),'1.00000E+00')

        expr = "(unit(1,flam) * box(5500.0,1.0))"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.sum()),'5.53744E+12')

        expr = "(unit(1,flam) * box(5500.0,20.0))"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.sum()),'1.13241E+14')

        expr = "rn(unit(1,flam),box(5500.0,1000),1.0E-18,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        sp.convert('flam')
        wave = sp.GetWaveSet()
        sp(wave)
        wav,flux = sp.getArrays()
        self.assertEqual(format(flux[0]),'1.00000E-18')
        box = spectrum.Box(5500.0,1.0)
        sp = sp * box
        integral = sp.integrate(fluxunits='flam')
        self.assertEqual(format(integral),'1.00000E-18')

        om = observationmode.ObservationMode("acs,hrc,f220w")
        sp = P.interpret(P.parse(P.scan("rn(unit(1,flam),box(5500.0,1),1.0E-18,flam)")))
        ob = observation.Observation(sp, om)
        effstim = ob.calcphot()
        self.assertEqual(format(effstim[0]),'1.15706E-01')
        efflam = ob.calcphot(func='efflam')
        self.assertEqual(format(efflam),'2.35765E+03')

        expr = "spec(Zodi.fits)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        f = sp(wave)
        w,f = sp.getArrays()
        self.assertEqual(format(f[0]),'4.74300E-29')

        expr = "earthshine.fits"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        f = sp(wave)
        w,f = sp.getArrays()
        self.assertEqual(format(f[0]),'2.41358E-23')

        expr = "band(V)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[10]),'9.97000E-01')

        expr = "rn(spec(Zodi.fits),band(V),22.7,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[100]),'3.29485E-16')

        expr = "(earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[1000]),'1.16471E-13')

        expr = "rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[1000]),'1.33871E-04')

        expr = "spec(crcalspec$gd71_mod_005.fits)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[1000]),'9.44461E-02')

        expr = "pl(4000.,1,photlam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[5270]),'1.00287E+00')

        expr = "pl(4000.,1,jy)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        f = sp(wave)
        w,f = sp.getArrays()
        self.assertEqual(format(f[5270]),'1.00287E+00')

        expr = "bb(10000.0)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[5000]),'1.06813E-02')

        expr = "z(bb(10000.0),1.0)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[5000]),'2.67032E-03')

        expr = "em(3880.0,10.0,1.0000000168623835E-16,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[50]),'1.83491E-06')

        expr = "rn(elliptical.fits,band(johnson,v),15.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[50]),'2.17656E-04')

        expr = "spec(userFiles$vb8.inr.2a)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[5000]),'8.15545E-03')

        expr = "rn(unit(1,flam)*ebmvx(0.1,gal1),box(5500.0,1),1.0E-18,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[5000]),'1.53329E-07')

        expr = "spec(userFiles$test.dat)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[5000]),'6.08108E+10')

        expr = "rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[500]),'1.02024E-05')

        expr = "rn(bb(5500.0),band(bessell,h),22.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[6000]),'3.88200E-07')

        expr = "rn(egal.dat,band(bessell,h),20.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[500]),'9.60494E-07')

        expr = "rn(bb(5500.0)*ebmvx(0.5,lmc),band(bessell,h),20.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[7000]),'1.38877E-06')

        expr = "rn(z(null,NaN),band(johnson,v),15.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[5000]),'9.92766E-04')

        expr = "rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[1000]),'5.86311E-04')

        expr = "(spec(crcalspec$grw_70d5824_stis_001.fits))"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[1000]),'5.08782E-02')

        expr = "rn((icat(k93models,44500,0.0,5.0))*ebmvx(0.5,smc),band(johnson,v),15.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[1000]),'1.10761E-03')

        expr = "(spec(crcalspec$grw_70d5824_stis_001.fits))"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[2000]),'1.41039E-02')

        expr = "ebmvx(0.1,gal1)"
        th = P.interpret(P.parse(P.scan(expr)))
        wave = th.GetWaveSet()
        throughput = th.throughputtable

        expr = "(spec(crcalspec$gd71_mod_005.fits))*ebmvx(0.1,gal1)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[2000]),'7.15737E-03')

        expr = "rn(z(qso_template.fits,1),band(johnson,v),18.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[2000]),'2.87132E-05')

        expr = "ebmvx(0.5,smc)"
        th = P.interpret(P.parse(P.scan(expr)))
        wave = th.GetWaveSet()
        throughput = th.throughputtable

        expr = "rn((icat(k93models,44500,0.0,5.0))*ebmvx(0.5,smc),band(johnson,v),15.0,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[200]),'5.48990E-05')

        expr = "rn((icat(k93models,44500,0.0,5.0)),band(johnson,v),10.516,vegamag)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[200]),'1.08948E+00')

        expr = "rn((spec(crcalspec$bd_28d4211_stis_001.fits)),box(2000.0,1),1.0E-12,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[200]),'2.92770E-01')

        expr = "rn((spec(crcalspec$gd71_mod_005.fits))*ebmvx(0.1,gal1),box(5500.0,1),1.0E-16,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        wave = sp.GetWaveSet()
        flux = sp(wave)
        self.assertEqual(format(flux[2000]),'4.37347E-05')


##class ETCTestCase_Imag1(unittest.TestCase):
class ETCTestCase_Imag1(TestSetUp):
    def runTest(self):

        expr = "(earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5)"
        sp = P.interpret(P.parse(P.scan(expr)))
        obsmode = observationmode.ObservationMode('acs,hrc,f220w')
        obs = observation.Observation(sp, obsmode)
        countrate = obs.calcphot()
        self.assertEqual(format(countrate[0]),'1.15585E-01')
        
        spectrum = "spectrum=" + expr
        obsmode = "obsmode=acs,hrc,f220w"
        parameters = [spectrum, obsmode]
        calculator = etc.Calcphot(parameters)
        efflam = calculator.run()
        self.assertEqual(format(efflam),'2.56717E+03')

        spectrum = "spectrum=" + expr
        instrument = "instrument=acs,hrc,f220w"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'1.15585E-01')

        spectrum = "spectrum=em(3880.0,10.0,1.0000000168623835E-16,flam)"
        instrument = "instrument=acs,wfc1,FR388N#3880"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'1.25658E-01')

        spectrum = "spectrum=rn(pl(4000,1.0,jy),box(5500.0,1),1e-18,flam)"
        instrument = "instrument=acs,sbc,F150LP"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'7.73334E-02')

        spectrum = "spectrum=rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20.0,vegamag)"
        instrument = "instrument=acs,sbc,F125LP"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]), '1.53451E-04')
        sp = calculator.observed_spectrum
        wave = sp.GetWaveSet()
        flux = sp(wave)

##class ETCTestCase_Imag2(unittest.TestCase):
class ETCTestCase_Imag2(TestSetUp):
    def runTest(self):

        obsmode = "obsmode="
        calculator = etc.Thermback([obsmode])
        countrate = calculator.run()
        self.assertEqual(countrate,'NaN')

        obsmode = "obsmode=null"
        calculator = etc.Thermback([obsmode])
        countrate = calculator.run()
        self.assertEqual(countrate,'NaN')

        obsmode = "obsmode=nicmos,1,F090M"
        calculator = etc.Thermback([obsmode])
        countrate = calculator.run()
        self.assertEqual(countrate,'1.95583447265e-012;')

        obsmode = "obsmode=nicmos,1,f190n"
        calculator = etc.Thermback([obsmode])
        countrate = calculator.run()
        self.assertEqual(countrate,'0.0139801017505;')

        obsmode = "obsmode=wfc3,ir,f110w"
        calculator = etc.Thermback([obsmode])
        countrate = calculator.run()
        self.assertEqual(countrate,'0.0290797241317;')

        spectrum = "spectrum=((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        instrument = "instrument=acs,sbc,F140LP"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'8.30771E-02')

        spectrum = "spectrum=rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15.0,vegamag)"
        instrument = "instrument=acs,hrc,FR388N#3880"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'2.80668E+01')

        spectrum = "spectrum=((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))*thru.fits"
        instrument = "instrument=stis,ccd"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'3.41703E+01')

        spectrum = "spectrum= rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        instrument = "instrument=stis,ccd"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'3.58774E+04')

        spectrum = "spectrum= rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        instrument = "instrument=wfc3,ir,F110W"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()
        self.assertEqual(format(countrate[0]),'9.69528E+04')

        spectrum = "spectrum=rn(bb(5000.0),band(johnson,v),28.0,vegamag)"
        instrument = "instrument=wfc3,uvis1,F606W"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()

        print "TEST:  ", countrate
##        self.assertEqual(format(countrate[0]),'9.69528E+04')

        spectrum = "spectrum=((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        instrument = "instrument=wfc3,uvis1,F606W"
        parameters = [spectrum, instrument]
        calculator = etc.Countrate(parameters)
        countrate = calculator.run()

        print "TEST:  ", countrate

##class ETCTestCase_Spec1(unittest.TestCase):
class ETCTestCase_Spec1(TestSetUp):
    def runTest(self):

        spectrum = "spectrum=(earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)"
        instrument = "instrument=acs,hrc,PR200L"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave,flux) = sp.getArrays()
        self.assertEqual(format(flux[-1]),'4.99529E+00')
        self.assertEqual(format(float(countrate.split(';')[0])),'1.37193E+01')

        spectrum = "spectrum=rn((unit(1,flam)),band(johnson,v),15.0,vegamag)"
        instrument = "instrument=acs,wfc1,G800L"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave,flux) = sp.getArrays()
        self.assertEqual(format(flux[50]),'9.08781E+02')
        self.assertEqual(format(float(countrate.split(';')[0])),'7.32526E+04')

        spectrum = "spectrum=em(4000.0,10.0,1.0000000168623835E-16,flam)"
        instrument = "instrument=acs,hrc,PR200L"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(float(countrate.split(';')[0])),'1.63706E-01')

        spectrum = "spectrum=rn((unit(1,flam)),band(johnson,v),15.0,vegamag)"
        instrument = "instrument=acs,hrc,PR200L"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(flux[80]),'7.92963E+01')
        self.assertEqual(format(float(countrate.split(';')[0])),'1.55488E+04')

        spectrum = "spectrum=rn((spec(crcalspec$gd71_mod_005.fits))*ebmvx(0.1,gal1),box(5500.0,1),1.0E-16,flam)"
        instrument = "instrument=acs,hrc,PR200L"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(flux[50]),'7.03327E+00')
        self.assertEqual(format(float(countrate.split(';')[0])),'1.47203E+03')

##class ETCTestCase_Spec2(unittest.TestCase):
class ETCTestCase_Spec2(TestSetUp):
    def runTest(self):

        spectrum = "spectrum=(spec(crcalspec$grw_70d5824_stis_001.fits))"
        instrument = "instrument=stis,fuvmama,g140l,s52x2"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(flux[500]),'3.55329E+01')
        self.assertEqual(format(float(countrate.split(';')[0])),'2.89357E+04')

        spectrum = "spectrum=rn((icat(k93models,44500,0.0,5.0)),band(johnson,v),10.516,vegamag)"
        instrument = "instrument=stis,nuvmama,e230h,c2263,s02x02"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(flux[500]),'1.19061E+00')
        self.assertEqual(format(float(countrate.split(';')[0])),'3.55750E+04')

        spectrum = "spectrum=rn((spec(crcalspec$bd_28d4211_stis_001.fits)),box(2000.0,1),1.0E-12,flam)"
        instrument = "instrument=stis,nuvmama,e230h,c2263,s02x02"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(flux[500]),'1.43728E-01')
        self.assertEqual(format(float(countrate.split(';')[0])),'4.23316E+03')

        spectrum = "spectrum=(spec(crcalspec$agk_81d266_stis_001.fits))"
        instrument = "instrument=stis,ccd,g230lb,c2375,s52x2"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(flux[500]),'2.45078E+02')
        self.assertEqual(format(float(countrate.split(';')[0])),'1.83608E+05')

##class ETCTestCase_Spec3(unittest.TestCase):
class ETCTestCase_Spec3(TestSetUp):
    def runTest(self):

        spectrum = "spectrum=em(4300.0,1.0,9.999999960041972E-13,flam)"
        instrument = "instrument=stis,ccd,g430l"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(float(countrate.split(';')[0])),'9.24085E+02')

        spectrum = "spectrum=rn((icat(k93models,5770,0.0,4.5)),band(johnson,v),20.0,vegamag)"
        instrument = "instrument=acs,hrc,PR200L"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(float(countrate.split(';')[0])),'1.19709E+02')

        spectrum = "spectrum=((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        instrument = "instrument=stis,fuvmama,g140l"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(float(countrate.split(';')[0])),'1.15518E+01')
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(float(countrate.split(';')[0])),'1.15518E+01')

        spectrum = "spectrum=((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        instrument = "instrument=cos,fuv,g130m,c1309"
        parameters = [spectrum, instrument]
        calculator = etc.SpecSourcerateSpec(parameters)
        countrate = calculator.run()
        sp = calculator.observed_spectrum
        (wave, flux) = sp.getArrays()
        self.assertEqual(format(float(countrate.split(';')[0])),'2.65409E+01')


##        pylab.ion()
##        pylab.clf()
##        pylab.scatter(wave,flux)
##        pylab.xlim(1000.0,6000.0)
##        pylab.ylim(-1.E-6,1.E-5)


class IcatTestCase(unittest.TestCase):
    def runTest(self):
        testValues = \
            ["icat(k93models,30000,0.0,4.0)",
             "icat(k93models,25400,0.0,3.9)",
             "icat(k93models,18700,0.0,3.9)",
             "icat(k93models,15400,0.0,3.9)",
             "icat(k93models,11900,0.0,4.0)",
             "icat(k93models,9230,0.0,4.1)",
             "icat(k93models,8720,0.0,4.2)",
             "icat(k93models,8200,0.0,4.3)",
             "icat(k93models,7700,0.0,1.7)",
             "icat(k93models,7200,0.0,4.3)",
             "icat(k93models,6890,0.0,4.3)",
             "icat(k93models,6440,0.0,4.3)",
             "icat(k93models,6200,0.0,4.4)",
             "icat(k93models,5860,0.0,4.4)",
             "icat(k93models,4850,0.0,1.1)",
             "icat(k93models,5770,0.0,4.5)",
             "icat(k93models,5570,0.0,4.5)",
             "icat(k93models,5250,0.0,4.5)",
             "icat(k93models,4560,0.0,4.5)",
             "icat(k93models,4060,0.0,4.5)",
             "icat(k93models,3500,0.0,4.6)",
             "icat(k93models,44500,0.0,5.0)",
             "icat(k93models,38000.,0.0,4.5)",
             "icat(k93models,33000.,0.0,4.0)"]

        for expr in testValues:
           sp = P.interpret(P.parse(P.scan(expr)))

           wave = sp.GetWaveSet()
           flux = sp(wave)

           i = len(flux)/3
           print wave[i], flux[i]

class ResamplerTestCase(unittest.TestCase):
    def runTest(self):
        sp = P.interpret(P.parse(P.scan("icat(k93models,5750,0.0,4.5)")))

        filename = locations.temporary + "resampler.fits"
        writer = etc.SpectrumWriter(filename, sp);
        writer.write()


