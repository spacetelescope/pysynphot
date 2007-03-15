## Automatically adapted for numpy.numarray Mar 05, 2007 by 

import string
import math
import numpy as N
import observationmode
import spectrum
import units


class Spectrogram(spectrum.TabularSourceSpectrum):
    ''' Class that represents objects that are not unlike regular Spectrum
    objects, but differ from them in the fact that their flux variable is not
    represented in units of flux density (photlam by default), but in units
    of counts per detector pixel. A Spectrogram can only exist if associated
    to a physical detector.
    '''
    def __init__(self, sp, wave):
        ''' Constructor builds the spectrogram on top of a regular spectrum
        expressed in flux density units, and a set of wavelengths representing
        the central wavelenghts associated with the detector elements (pixels)
        on a detector array.
        '''
        # compute endpoints of each summation bin.
        midpoints = (wave[1:] + wave[:-1]) / 2.0
        endpoints = N.empty(shape=[len(midpoints)+2,],dtype=N.float64)
        endpoints[1:-1] = midpoints
        endpoints[0]  = wave[0] - (midpoints[0] - wave[0])
        endpoints[-1] = wave[-1] + (wave[-1] - midpoints[-1])

        # resample over natural wave set merged with endpoints waveset.
        spwave = spectrum.MergeWaveSets(sp.GetWaveSet(), endpoints)
        spwave = spectrum.MergeWaveSets(spwave, wave)

        # compute indices associated to each endpoint.
        indices = N.searchsorted(spwave, endpoints)
        diff = indices[1:] - indices[:-1]
        indices = indices[:-1]
        indices_last = indices + diff 

        # prepare integration variables.
        flux = sp(spwave)
        avflux = (flux[1:] + flux[:-1]) / 2.0
        deltaw = spwave[1:] - spwave[:-1]

        # sum over each bin.
        nflux = N.empty(shape=wave.shape,dtype=N.float64)
        for i in range(len(indices)):
            first = indices[i]
            last = indices_last[i]
            nflux[i] = (avflux[first:last] * deltaw[first:last]).sum() 

        self._wavetable = wave
        self._fluxtable = nflux * units.HSTAREA

        self.waveunits = sp.waveunits
        self.fluxunits = units.Units("counts")
        
        
    def getArrays(self):
        ''' This method overrides the base class to return wavelength
        and counts/s/pixel arrays as a tuple. Note that units conversion
        is ignored for the flux array, but can still take place on the
        wavelength array.
        '''
        wave = units.Angstrom().Convert(self._wavetable, \
                                        self.waveunits.name)
        return (wave, self._fluxtable)
        

class Observation(object):

    def __init__(self, source, observationmode):

        self.source = source
        self.observationmode = observationmode

        self._wave = None

    def calcphot(self,func='effstim'):
        calculator = _factory(func, self.source,
                              self.observationmode.Throughput(),
                              self.observationmode.bandWave(),
                              self.observationmode.area)

        result = calculator._compute()

        self.observed_spectrum = calculator.observed_spectrum

        return result


class _CalcphotCalculator(object):
    ''' Base class for all calcphot calculators.
    '''
    def __init__(self, source, throughput, wavelengths, area):
        self._area = area
        self.wave = wavelengths

        self.observed_spectrum = source * throughput


class _EffstimCalculator(_CalcphotCalculator):
    ''' Computes effstim result for calcphot function.
    Only 'counts' units are supported for now (result is
    expresed in counts/s units)
    '''
    def _compute(self):
        countrate = self.observed_spectrum.integrate() * self._area
        pivot = self._getPivot()

        return (countrate, pivot)

    def _getPivot(self):
        wave = self.observed_spectrum.GetWaveSet()

        countmulwave = self.observed_spectrum(wave) * wave
        countdivwave = self.observed_spectrum(wave) / wave

        num = _integrate(countmulwave, self.observed_spectrum)
        den = _integrate(countdivwave, self.observed_spectrum)

        return math.sqrt(num/den)


class _SpectrumCalculator(_CalcphotCalculator):
    ''' Generates a Spectrogram of counts per sec per detector pixel.
    '''
    def _compute(self):
        self.observed_spectrum = Spectrogram(self.observed_spectrum, self.wave)

        return self.observed_spectrum._fluxtable.sum()


class _EfflamCalculator(_CalcphotCalculator):
    ''' Computes efflam result for calcphot function.
    '''
    def _compute(self):
        wave = self.observed_spectrum.GetWaveSet()
        countwave = self.observed_spectrum(wave) * wave
        countwave2 = countwave * wave

        num = _integrate(countwave2, self.observed_spectrum)
        den = _integrate(countwave, self.observed_spectrum)

        return num / den


def _integrate(values, refspectrum):
        sp = spectrum.TabularSourceSpectrum()

        sp.waveunits = refspectrum.waveunits
        sp.fluxunits = refspectrum.fluxunits
        sp._wavetable = refspectrum.GetWaveSet()
        sp._fluxtable = values

        return sp.integrate()


_calculatorClasses = {'effstim': _EffstimCalculator,
                      'efflam' : _EfflamCalculator,
                      'spec'   : _SpectrumCalculator}

def _factory(func, *args, **kwargs):
    return apply(_calculatorClasses[string.lower(func)], args, kwargs)


