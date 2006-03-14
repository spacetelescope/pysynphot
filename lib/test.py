import sys
import unittest
import spectrum
import magnitudes
import observation
import observationmode
import locations
import spparser as P
import etc

# import pylab as P

filename = locations.testdata
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
          'thru_npoints':   '1.10000E+04',
          'thru_5000':      '1.22327E-01',
          'obsmode':        'acs,hrc,f555w',
          'hstarea':        '4.52389E+04',
          'countrate':      '8.30681E+05', #Ctrate from synphot: 8.30679E+05
          'efflam':         '5.32587E+03'   #Efflam from synphot: 5.32812E+03
          }

format_spec = '%.5E'    # floating point precision in assert
format_offset = {'win32':1,'sunos5':0,'linux2':0}

def format(value):
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
    testcase = ObsmodeTestCase()
    runner.run(testcase)
    testcase = CalcphotTestCase()
    runner.run(testcase)
    testcase = FunctionTestCase()
    runner.run(testcase)
    testcase = ParserTestCase()
    runner.run(testcase)


class TestSetUp(unittest.TestCase):
    ''' Base class for all classes that use the test spectrum feige66_002.
        This class also acts as an implicit test for the FITS file reading
        machinery in the spectrum.TabularSourceSpectrum class.
    '''
    def setUp(self):
        self.sp = spectrum.TabularSourceSpectrum(filename)

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
        vmag = magnitudes.VMag(0.0)
        sp2 = self.sp.setMagnitude(vmag)
        (dummy, fluxes) = sp2.getArrays()
        self.assertEqual(format(fluxes[testindex]), values['v=0.0'])

        vmag = magnitudes.VMag(5.0)
        sp2 = self.sp.setMagnitude(vmag)
        (dummy, fluxes) = sp2.getArrays()
        self.assertEqual(format(fluxes[testindex]), values['v=5.0'])


class ObsmodeTestCase(unittest.TestCase):
    def runTest(self):
        obsmode = observationmode.ObservationMode(values['obsmode'])

        self.assertEqual(format(obsmode.area), values['hstarea'])

        throughput = obsmode.Throughput().throughputtable

        self.assertEqual(format(len(throughput)), values['thru_npoints'])
        self.assertEqual(format(throughput[5000]), values['thru_5000'])
        

class CalcphotTestCase(TestSetUp):
    def setUp(self):
        TestSetUp.setUp(self)

    def runTest(self):
        obsmode = observationmode.ObservationMode(values['obsmode'])
        obs = observation.Observation(self.sp, obsmode)

        countrate = obs.calcphot()
        self.assertEqual(format(countrate), values['countrate'])

        efflam = obs.calcphot(func='efflam')
        self.assertEqual(format(efflam), values['efflam'])


class FunctionTestCase(unittest.TestCase):
    def runTest(self):
        wave = spectrum.waveset()

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
        self.assertEqual(format(box.wavetable.shape[0]),'2.00000E+01')
        self.assertEqual(format(box.throughputtable.shape[0]),'2.00000E+01')
        self.assertEqual(format(box.throughputtable[0]),'1.00000E+00')

        sp = spectrum.UnitSpectrum(1.0,fluxunits='photlam')
        box = spectrum.Box(5500.0,1.0)



##        wave = box.GetWaveSet()
##        for i in range(len(wave)):
##            print i,wave[i]





        sp = sp * box
        fluxes = sp(wave)


        for i in range(6060,6080):
            print i,wave[i],fluxes[i]




        self.assertEqual(format(fluxes.sum()),'1.82681E+00')

        sp = spectrum.UnitSpectrum(1.0,fluxunits='flam')
        box = spectrum.Box(5500.0,1.0)
        sp = sp * box
        fluxes = sp(wave)





##        self.assertEqual(format(fluxes.sum()),'2.40938E+11')


class ParserTestCase(unittest.TestCase):
    def runTest(self):
        wave = spectrum.waveset()

        expr = "unit(1,photlam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.shape[0]),'1.00000E+04')
        self.assertEqual(format(fluxes[0]),'1.00000E+00')
        self.assertEqual(format(fluxes[9000]),'1.00000E+00')

        expr = "unit(1,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        fluxes = sp(wave)
        self.assertEqual(format(fluxes[0]),'2.51701E+10')
        self.assertEqual(format(fluxes[9000]),'8.81633E+11')
        waves,fluxes = sp.getArrays()
        self.assertEqual(format(fluxes[0]),'1.00000E+00')
        self.assertEqual(format(fluxes[9000]),'1.00000E+00')

        expr = "(unit(1,flam) * box(5500.0,1.0))"
        sp = P.interpret(P.parse(P.scan(expr)))
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.sum()),'2.40938E+11')

        expr = "(unit(1,flam) * box(5500.0,20.0))"
        sp = P.interpret(P.parse(P.scan(expr)))
        fluxes = sp(wave)
        self.assertEqual(format(fluxes.sum()),'5.09664E+12')

        expr = "rn(unit(1,flam),box(5500.0,1),1.0E-18,flam)"
        sp = P.interpret(P.parse(P.scan(expr)))
        sp.convert('flam')
        sp(wave)
        wav,flux = sp.getArrays()
        self.assertEqual(format(flux[0]),'3.86298E-19')








