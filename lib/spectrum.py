## Automatically adapted for numpy.numarray Mar 05, 2007 by 

import string
import re
import os
import math

import pyfits
import numpy as N
from numpy import ma as MA

import units
import observationmode
import locations
import planck


# Renormalization constants from synphot:
PI = 3.14159265               # Mysterious math constant
RSUN = 6.9599E10              # Radius of sun
PC = 3.085678E18              # Parsec
RADIAN = RSUN / PC /1000.
RENORM = PI * RADIAN * RADIAN # Normalize to 1 solar radius @ 1 kpc


class Magnitude(object):

    def __init__(self, bandname, value):
        self.value = value
        self._throughputFile = locations.getBandFileName(bandname)
        self._throughput = TabularSpectralElement(self._throughputFile)

    def calcTotalFlux(self, inSpectrum):
        filteredflux = inSpectrum * self._throughput
        return filteredflux.integrate()
    
    def calcVegaFlux(self):
        vegaspec = TabularSourceSpectrum(locations.VegaFile)
        filteredvega = vegaspec * self._throughput
        return filteredvega.integrate()


def renormalize(spectrum, band, flux, unit):
    ''' renormalization function.'''
    if isinstance(band,Band):
        if unit.lower() == 'vegamag':
            mag = Magnitude(band.name,flux)
            return spectrum.setMagnitude(mag)
        else:
            raise ValueError("%s not supported yet."%unit)

            sp = spectrum * band
            cntrate = sp.integrate(fluxunits=unit)
            resp = band.unitResponse()
            factor = flux / (cntrate * resp)
            return spectrum * factor
    else:
        sp = spectrum * band
        cntrate = sp.integrate(fluxunits=unit)
        resp = band.unitResponse()
        factor = flux / (cntrate * resp)
        return spectrum * factor


def _computeDefaultWaveset():
    minwave = 500.
    maxwave = 26000.
    lenwave = 10000

    w1 = math.log10(minwave)
    w2 = math.log10(maxwave)

    result = N.zeros(shape=[lenwave,],dtype=N.float64)

    for i in range(lenwave):
        frac = float(i) / lenwave
        result[i] = 10 ** (w1 * (1.0 - frac) + w2 * frac)

    return result        

# Default waveset is computed at load time, once and for all.
# Note that this is not thread safe.
global default_waveset
default_waveset = _computeDefaultWaveset()


def MergeWaveSets(waveset1, waveset2):
    if waveset1 is None and waveset2 is not None:
        MergedWaveSet = waveset2
    elif waveset2 is None and waveset1 is not None:
        MergedWaveSet = waveset1
    elif waveset1 is None and Waveset2 is None:
        MergedWaveSet = None
    else:
        MergedWaveSet = N.concatenate((waveset1, waveset2))
        MergedWaveSet = N.sort(MergedWaveSet, 0)
        MergedWaveSet = N.compress(MergedWaveSet[:-1] !=
                                          MergedWaveSet[1:], MergedWaveSet)
    return MergedWaveSet


def trimSpectrum(sp, minw, maxw):
    ''' Creates a new spectrum with trimmed upper and lower ranges.
    '''
    wave = sp.GetWaveSet()
    flux = sp(wave)

    new_wave = N.compress(wave >= minw, wave)
    new_flux = N.compress(wave >= minw, flux)

    new_wave = N.compress(new_wave <= maxw, new_wave)
    new_flux = N.compress(new_wave <= maxw, new_flux)

    result = TabularSourceSpectrum()

    result._wavetable = new_wave
    result._fluxtable = new_flux

    result.waveunits = units.Units(sp.waveunits.name)
    result.fluxunits = units.Units(sp.fluxunits.name)

    return result


class Integrator(object):
    ''' Integrator engine.
    '''
    def trapezoidIntegration(self,x,y):
        npoints = x.size
        indices = N.arange(npoints)[:-1]
        deltas = x[indices+1] - x[indices]
        integrand = 0.5*(y[indices+1] + y[indices])*deltas

        return integrand.sum()


class SourceSpectrum(Integrator):
    '''Base class for the Source Spectrum object.
    '''
    
    def __add__(self, other):
        '''Source Spectra can be added.  Delegate the work to the
        CompositeSourceSpectrum class.
        '''
        if not isinstance(other, SourceSpectrum):
            raise TypeError("Can only add two SourceSpectrum objects")

        return CompositeSourceSpectrum(self, other, 'add')

    def __mul__(self, other):
        '''Source Spectra can be multiplied, by constants or by
        SpectralElement objects.
        '''
        #Ack!! There has to be a better way to do this
        if type(other) in [type(1), type(1.0),N.float64]:
            other = UniformTransmission(other)
        if not isinstance(other, SpectralElement):
            raise TypeError("SourceSpectrum objects can only be multiplied by SpectralElement objects or constants; %s type detected"%type(other))


        ## Delegate the work of multiplying to CompositeSourceSpectrum

        return CompositeSourceSpectrum(self, other, 'multiply')

    def __rmul__(self, other):
        return self.__mul__(other)

    def getArrays(self):
        '''Returns wavelength and flux arrays as a tuple, performing
           units conversion.
        '''
        wave = self.GetWaveSet();
        flux = self(wave)

        flux = units.Photlam().Convert(wave, flux, self.fluxunits.name)
        wave = units.Angstrom().Convert(wave, self.waveunits.name)

        return (wave, flux)

    #Define properties for consistent UI
    def _getWaveProp(self):
        wave,flux=self.getArrays()
        return wave

    def _getFluxProp(self):
        wave,flux=self.getArrays()
        return flux

    wave=property(_getWaveProp,doc="Wavelength property")
    flux=property(_getFluxProp,doc="Flux property")

    def writefits(self, filename, clobber=True, trimzero=True):
        """Write the spectrum to a FITS file."""

        if clobber:
            try:
                os.remove(filename)
            except OSError:
                pass

        first,last=0,len(self.flux)
        if trimzero:
            #Keep one zero at each end
            nz = self.flux.nonzero()[0]
            try:
                first=max(nz[0]-1,first)
                last=min(nz[-1]+2,last)
            except IndexError:
                pass

        #Construct the columns and HDUlist
        cw = pyfits.Column(name='WAVELENGTH',
                           array=self.wave[first:last],
                           unit=self.waveunits.name,
                           format='E')
        cf = pyfits.Column(name='FLUX',
                           array=self.flux[first:last],
                           unit=self.fluxunits.name,
                           format='E')
        hdu = pyfits.PrimaryHDU()
        hdulist = pyfits.HDUList([hdu])

        #Write the file
        cols = pyfits.ColDefs([cw, cf])
        hdu = pyfits.new_table(cols)
        hdulist.append(hdu)
        hdu.writeto(filename)
                                                 
    def integrate(self,fluxunits=None):
        wavelengths = self.GetWaveSet()
        fluxes = self(wavelengths)

        if fluxunits != None:
            sp = TabularSourceSpectrum()
            sp.waveunits = self.waveunits
            sp.fluxunits = units.Units(fluxunits)
            sp._wavetable = wavelengths
            sp._fluxtable = self(wavelengths)
            w,fluxes = sp.getArrays()

        return self.trapezoidIntegration(wavelengths,fluxes)

    def convert(self, targetunits):
        '''Convert to other units. This method actually just changes the
        wavelength and flux units objects, it does not recompute the
        internally kept wave and flux data; these are kept always in internal
        units. Method getArrays does the actual computation.
        '''
        nunits = units.Units(targetunits)
        if nunits.isFlux:
            self.fluxunits = nunits
        else:
            self.waveunits = nunits

    def redshift(self, z):
        ''' Returns a new redshifted spectrum.
        '''
        # begin by building a copy of self, but in Tabular format.
        copy = TabularSourceSpectrum()
        copy.fluxunits = self.fluxunits
        copy.waveunits = self.waveunits
        copy._wavetable = self.GetWaveSet()
        copy._fluxtable = self(copy._wavetable)

        # flux expressed in photnu is invariant wrt redshift; convert
        # the copy to photnu and extract its flux array.
        copy.convert('photnu')
        (dummy, flux_photnu) = copy.getArrays()

        # convert wavelenght array in the copy, to the redshifted frame.
        copy._wavetable *= 1.0 + z

        # now comes the trick: put back the flux array in photnu units
        # into the copy, and convert it back to internal units.
        copy._fluxtable = flux_photnu
        copy.fluxunits = units.Units('photnu')
        copy.ToInternal()
        copy.fluxunits = self.fluxunits

        return copy

    def setMagnitude(self, mag):
        '''Makes the magnitude of the source equal to mag.
        mag is a Magnitude object.
        '''
        objectFlux = mag.calcTotalFlux(self)
        vegaFlux = mag.calcVegaFlux()
        magDiff = -2.5*math.log10(objectFlux/vegaFlux)
        factor = 10**(-0.4*(mag.value - magDiff))

        '''Object returned is a CompositeSourceSpectrum'''

        return self * factor

class CompositeSourceSpectrum(SourceSpectrum):
    '''Composite Source Spectrum object, handles addition, multiplication
    and keeping track of the wavelength set.
    '''
    def __init__(self, source1, source2, operation):
        self.component1 = source1
        self.component2 = source2
        self.operation = operation

        # for now we keep these attributes here, in spite of the internal
        # units model. There is code that still breaks down if these attributes
        # are not here.
        self.fluxunits = source1.fluxunits
        self.waveunits = source1.waveunits

    def __str__(self):
        opdict = {'add':'+','multiply':'*'}
        return "%s %s %s"%(str(self.component1),opdict[self.operation],str(self.component2))
    
    def __call__(self, wavelength):
        '''Add or multiply components, delegating the function calculation
        to the individual objects.
        '''
        if self.operation == 'add':
            return self.component1(wavelength) + self.component2(wavelength)
        if self.operation == 'multiply':
            return self.component1(wavelength) * self.component2(wavelength)

    def GetWaveSet(self):
        '''Obtain the wavelength set for the composite source by forming
        the union of wavelengths from each component.
        '''
        waveset1 = self.component1.GetWaveSet()
        waveset2 = self.component2.GetWaveSet()

        return MergeWaveSets(waveset1, waveset2)

class TabularSourceSpectrum(SourceSpectrum):
    '''Class for a source spectrum that is read in from a table.
    '''
    def __init__(self, filename=None, fluxname=None):
        if filename:
            self._readSpectrumFile(filename, fluxname)
            self.filename=filename
            self.ToInternal()

        else:
            self._wavetable = None
            self._fluxtable = None
            self.waveunits = None
            self.fluxunits = None
            self.filename = None
        

    def __str__(self):
        return self.filename

    def _readSpectrumFile(self, filename, fluxname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, fluxname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, fluxname):
        fs = pyfits.open(filename)

        self._wavetable = fs[1].data.field('wavelength')
        if fluxname == None:
            fluxname = 'flux'
        self._fluxtable = fs[1].data.field(fluxname)

        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.fluxunits = units.Units(fs[1].header['tunit2'].lower())

        fs.close()

    def _readASCII(self, filename):
        fs = open(filename,mode='r')
        lines = fs.readlines()

        self._wavetable = N.ones(shape=[len(lines),],dtype=N.float64)
        self._fluxtable = N.ones(shape=[len(lines),],dtype=N.float32)

        regx = re.compile(r'\S+', re.IGNORECASE)
        i = 0
        for line in lines:
            try:
                [w,f] = regx.findall(line)
                self._wavetable[i] = float(w)
                self._fluxtable[i] = float(f)
                i = i + 1
            except:
                pass

        self.waveunits = units.Units('angstrom')
        self.fluxunits = units.Units('flam')

        fs.close()

    def __call__(self, wavelengths):
        '''This is where the flux array is actually calculated given a
        wavelength array. Returns an array of flux values calculated at
        the wavelength values input.
        '''
        return self.resample(wavelengths)._fluxtable

    def taper(self):
        '''Taper the spectrum by adding zeros to each end.
        '''
        OutSpec = TabularSourceSpectrum()
        wcopy = N.zeros(self._wavetable.size+2,dtype=N.float64)
        fcopy = N.zeros(self._fluxtable.size+2,dtype=N.float32)
        wcopy[1:-1] = self._wavetable
        fcopy[1:-1] = self._fluxtable
        fcopy[0] = 0.0
        fcopy[-1] = 0.0

        ## The wavelengths to use for the first and last points are
        ## calculated by using the same ratio as for the 2 interior points
        wcopy[0] = wcopy[1]*wcopy[1]/wcopy[2]
        wcopy[-1] = wcopy[-2]*wcopy[-2]/wcopy[-3]

        OutSpec._wavetable = wcopy
        OutSpec._fluxtable = fcopy

        return OutSpec
        
    def resample(self, resampledWaveTab):
        '''Interpolate flux given a wavelength array that is monotonically
        increasing and the TabularSourceSpectrum object.
        '''
        ## Make a new object to hold the resampled spectrum
        resampled = TabularSourceSpectrum()

        ## First need to pad the ends of the spectrum with zeros
        tapered = self.taper()

        ## Linear interpolations from the Python tutorial
        indices = N.searchsorted(tapered._wavetable,resampledWaveTab)-1

        ## Make sure the indices containing the desired points don't go
        ## beyond the ends of the array
        indices = N.clip(indices, 0, tapered._wavetable.size-2)

        fraction = resampledWaveTab - tapered._wavetable[indices]
        fraction = fraction / (tapered._wavetable[indices+1] -
                               tapered._wavetable[indices])

        ## Make sure the fraction is calculated correctly for elements beyond
        ## the valid regions of the input spectrum
        fraction = N.clip(fraction, 0.0, 1.0)

        resampled._fluxtable = tapered._fluxtable[indices] + \
                               fraction * (tapered._fluxtable[indices+1] - \
                                           tapered._fluxtable[indices])

        resampled._wavetable = resampledWaveTab.copy()

        return resampled

    def GetWaveSet(self):
        '''For a TabularSource Spectrum, the WaveSet is just the _wavetable
        member.  Return a copy so that there is no reference to the original
        object.
        '''
        return self._wavetable.copy()

    def ToInternal(self):
        '''Convert to the internal representation of (angstroms, photlam).
        '''
        savewunits = self.waveunits
        savefunits = self.fluxunits
        angwave = self.waveunits.Convert(self.GetWaveSet(), 'angstrom')
        phoflux = self.fluxunits.Convert(angwave, self._fluxtable, 'photlam')
        self._wavetable = angwave.copy()
        self._fluxtable = phoflux.copy()
        self.waveunits = savewunits
        self.fluxunits = savefunits

class NewTabularSpectrum(TabularSourceSpectrum):
    """ Replacement class """
    def __init__(self, wave=None, flux=None,
                 waveunits='angstrom', fluxunits='photlam',
                 name='TabularSourceSpectrum'):
        self._wavetable=wave
        self._fluxtable=flux
        self.waveunits=units.Units(waveunits)
        self.fluxunits=units.Units(fluxunits)
        self.name=name
        
        self.ToInternal()

class FileSourceSpectrum(TabularSourceSpectrum):
    '''Class for a source spectrum that is read in from a table.'''
    def __init__(self, filename, fluxname=None):
        self._readSpectrumFile(filename, fluxname)
        self.name=filename
        self.ToInternal()

    def _readSpectrumFile(self, filename, fluxname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, fluxname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, fluxname):
        fs = pyfits.open(filename)
        
        self._wavetable = fs[1].data.field('wavelength')
        if fluxname == None:
            fluxname = 'flux'
            self._fluxtable = fs[1].data.field(fluxname)
            self.waveunits = units.Units(fs[1].header['tunit1'].lower())
            self.fluxunits = units.Units(fs[1].header['tunit2'].lower())
            fs.close()

    def _readASCII(self, filename):
        fs = open(filename,mode='r')
        lines = fs.readlines()
        
        self._wavetable = N.ones(shape=[len(lines),],dtype=N.float64)
        self._fluxtable = N.ones(shape=[len(lines),],dtype=N.float32)
        
        regx = re.compile(r'\S+', re.IGNORECASE)
        i = 0
        for line in lines:
            try:
                [w,f] = regx.findall(line)
                self._wavetable[i] = float(w)
                self._fluxtable[i] = float(f)
                i = i + 1
            except:
                pass
            
        self.waveunits = units.Units('angstrom')
        self.fluxunits = units.Units('flam')
                            
        fs.close()
            
                                
                                                        
class AnalyticSpectrum(SourceSpectrum):
    ''' Base class for analytic functions. These are spectral forms
    which are defined, by default, on top of the default synphot
    waveset. 
    '''
    def GetWaveSet(self):
        global default_waveset
        return default_waveset.copy()


class GaussianSource(AnalyticSpectrum):
    def __init__(self, flux, center, fwhm, waveunits='angstrom',
                 fluxunits='flam'):
        self.center = center
        self.input_fwhm = fwhm
        self.input_flux = flux
        self.input_units = fluxunits
        self.sigma = fwhm / math.sqrt(8.0 * math.log(2.0))
        self.factor = flux / (math.sqrt(2.0 * math.pi) * self.sigma)

        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)

    def __str__(self):
        return 'Gaussian: mu=%f,fwhm=%f,flux=%f %s'%(self.center,self.input_fwhm,self.input_flux,self.input_units)

    def __call__(self, wavelength):
        sp = TabularSourceSpectrum()
        sp.waveunits = self.waveunits
        sp.fluxunits = self.fluxunits
        sp._wavetable = wavelength
        sp._fluxtable = self.factor * N.exp( \
            -0.5 *((wavelength - self.center)/ self.sigma)**2)
        sp.ToInternal()

        return sp(wavelength)

    def GetWaveSet(self):
        '''Return a wavelength set that describes the Gaussian.
        Overrides the base class to compute 101 values, from
        center - 5*sigma to center + 5*sigma, in units of
        0.1*sigma
        '''
        increment = 0.1*self.sigma
        first = self.center - 50.0*increment
        last = self.center + 50.0*increment
        return N.arange(first, last, increment)


class UnitSpectrum(AnalyticSpectrum):
    def __init__(self, fluxdensity, waveunits='angstrom', fluxunits='photlam'):
        self.wavelength = None
        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)
        self._fluxdensity = fluxdensity
        self._input_units = self.fluxunits

    def __str__(self):
        return "Unit spectrum of %f %s"%(self._fluxdensity,self._input_units)
    
    def __call__(self, wavelength):
        sp = TabularSourceSpectrum()
        sp.waveunits = self.waveunits
        sp.fluxunits = self.fluxunits
        sp._wavetable = wavelength
        sp._fluxtable = N.ones(sp._wavetable.shape, dtype=N.float32) * \
                        self._fluxdensity
        sp.ToInternal()

        return sp(wavelength)


class Powerlaw(AnalyticSpectrum):
    def __init__(self, refwave, index, waveunits='angstrom', fluxunits='photlam'):
        self.wavelength = None
        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)
        self._refwave = refwave
        self._index = index

    def __str__(self):
        return "Power law: refwave %f, index %f"%(self._refwave,self._index)

    def __call__(self, wavelength):
        sp = TabularSourceSpectrum()
        sp.waveunits = self.waveunits
        sp.fluxunits = self.fluxunits
        sp._wavetable = wavelength
        sp._fluxtable = N.ones(sp._wavetable.shape, dtype=N.float32)

        for i in range(len(sp._fluxtable)):
            sp._fluxtable[i] = (sp._wavetable[i] / self._refwave) ** self._index

        sp.ToInternal()

        return sp(wavelength)


class BlackBody(AnalyticSpectrum):
    def __init__(self, temperature):
        self.wavelength = None
        self.waveunits = units.Units('angstrom')
        self.fluxunits = units.Units('photlam')
        self.temperature = temperature

    def __str__(self):
        return 'BlackBody(T=%d)'%self.temperature

    def __call__(self, wavelength):
        sp = TabularSourceSpectrum()
        sp.waveunits = self.waveunits
        sp.fluxunits = self.fluxunits
        sp._wavetable = wavelength

        sp._fluxtable = planck.bbfunc(wavelength, self.temperature)* RENORM

        return sp(wavelength)


class SpectralElement(Integrator):
    '''Base class for a Spectral Element (e.g. Filter, Detector...).
    '''
    def __mul__(self, other):
        '''Permitted to multiply a SpectralElement by another
        SpectralElement, or by a SourceSpectrum.  In the former
        case we return a CompositeSpectralElement, while in the
        latter case a CompositeSourceSpectrum.
        '''
        if isinstance(other, SpectralElement):
            return CompositeSpectralElement(self, other)

        if isinstance(other, SourceSpectrum):
            return CompositeSourceSpectrum(self, other, 'multiply')

        ## Multiplying by a constant is the same as multiplying by a
        ## UniformTransmission object
        if type(other) in [type(1), type(1.0)]:
            return CompositeSpectralElement(self, UniformTransmission(other))

        else:
            print "SpectralElements can only be multiplied by other " + \
                  "SpectralElements or SourceSpectrum objects"

    def __rmul__(self, other):
        return self.__mul__(other)

    def convert(self, targetunits):
        '''Spectral elements are not convertible.
        '''
        return self

    def __call__(self, wavelengths):
        '''This is where the throughput array is calculated for a given
        input wavelength table.
        '''
        return self.resample(wavelengths).throughputtable

    def taper(self):
        '''Taper the spectrum by adding zeros to each end.
        '''
        OutElement = TabularSpectralElement()

        wcopy = N.zeros(self.wavetable.size+2,dtype=N.float64)
        fcopy = N.zeros(self.throughputtable.size+2,dtype=N.float32)

        wcopy[1:-1] = self.wavetable
        fcopy[1:-1] = self.throughputtable

        fcopy[0] = 0.0
        fcopy[-1] = 0.0

        ## The wavelengths to use for the first and last points are
        ## calculated by using the same ratio as for the 2 interior points
        wcopy[0] = wcopy[1]*wcopy[1]/wcopy[2]
        wcopy[-1] = wcopy[-2]*wcopy[-2]/wcopy[-3]

        OutElement.wavetable = wcopy
        OutElement.throughputtable = fcopy

        return OutElement

    def resample(self, resampledWaveTab):
        '''Interpolate throughput given a wavelength array that is
        monotonically increasing and the TabularSpectralElement object.
        '''
        ## Make a new object to hold the resampled SpectralElement
        resampled = TabularSpectralElement()

        ## First need to pad the ends with zeros
        tapered = self.taper()

        ## Linear interpolations from the Python tutorial
        indices = N.searchsorted(tapered.wavetable, resampledWaveTab)-1

        ## Make sure the indices containing the desired points don't go
        ## beyond the ends of the array
        indices = N.clip(indices, 0, tapered.wavetable.size-2)
        fraction = resampledWaveTab - tapered.wavetable[indices]
        fraction = fraction / (tapered.wavetable[indices+1] -
                               tapered.wavetable[indices])

        ## Make sure the fraction is calculated correctly for elements beyond
        ## the valid regions of the input spectrum
        fraction = N.clip(fraction, 0.0, 1.0)
        resampled.throughputtable = tapered.throughputtable[indices] + \
                                    fraction*(tapered.throughputtable[indices+1] - \
                                              tapered.throughputtable[indices])

        resampled.wavetable = resampledWaveTab.copy()

        return resampled

    def unitResponse(self):
        wave = self.GetWaveSet()
        thru = self(wave)
        return 1.0 / self.trapezoidIntegration(wave,thru)

    def GetWaveSet(self):
        return self.wavetable

    def GetThroughput(self):
        """Return the throughput for the internal wavetable"""
        return self.__call__(self.wave)
    
    wave = property(GetWaveSet, doc='Waveset for bandpass')
    throughput = property(GetThroughput, doc='Throughput for bandpass')


class CompositeSpectralElement(SpectralElement):
    '''CompositeSpectralElement Class, which knows how to calculate
    its throughput by delegating the calculating the calculating to
    its components.
    '''
    def __init__(self, component1, component2):
        if (not isinstance(component1, SpectralElement) or
            not isinstance(component2, SpectralElement)):
            raise TypeError("Arguments must be SpectralElements")
        self.component1 = component1
        self.component2 = component2
        self.waveunits = "probably angstroms"
        self.throughputunits = None
        
    def __call__(self, wavelength):
        '''This is where the throughput calculation is delegated.
        '''
        return self.component1(wavelength) * self.component2(wavelength)

    def GetWaveSet(self):
        '''This method returns a wavelength set appropriate for a composite
        object by forming the union of the wavelengths of the components.
        '''
        wave1 = self.component1.GetWaveSet()
        wave2 = self.component2.GetWaveSet()

        return MergeWaveSets(wave1, wave2)

    wave = property(GetWaveSet,doc="wave for CompositeSpectralElement")


class UniformTransmission(SpectralElement):
    '''Uniform Transmission Spectral Element.
    Need to add a GetWaveSet method (or just return None).
    '''
    def __init__(self, value, waveunits='angstrom'):
        self.waveunits = units.Units(waveunits)
        self.value = value

    def GetWaveSet(self):
        return None

    def __call__(self, wavelength):
        '''__call__ returns the constant value as an array, given a
        wavelength array as argument.
        '''
        return 0.0 * wavelength + self.value


class TabularSpectralElement(SpectralElement):
    '''The TabularSpectralElement class handles spectral elements that are
    stored in tables.
    '''
    def __init__(self, fileName=None, thrucol='throughput'):
        '''__init__ takes a character string argument that contains the name
        of the file with the spectral element table.
        '''
        if fileName:
            self.name = fileName

            fs = pyfits.open(self.name)

            self.wavetable = fs[1].data.field('wavelength')
            self.throughputtable = fs[1].data.field(thrucol)

            self.waveunits = units.Units(fs[1].header['tunit1'].lower())
            self.throughputunits = 'none'

            self.getHeaderKeywords(fs[1].header)

            fs.close()
        else:
            self.name = None
            self.wavetable = None
            self.throughputtable = None
            self.waveunits = None
            self.throughputunits = None

    def __str__(self):
        return self.name

    def getHeaderKeywords(self, header):
        ''' This is a placeholder for subclasses to get header keywords without
        having to reopen the file again. 
        '''
        pass


class InterpolatedSpectralElement(SpectralElement):
    '''The InterpolatedSpectralElement class handles spectral elements
    that are interpolated from columns stored in FITS tables
    '''
    def __init__(self, fileName, wavelength):
        ''' The file name contains a suffix with a column name specification
        in between square brackets, such as [fr388n#]. The wavelength
        parameter is used to interpolate between two columns in the file.
        '''
        self.name = fileName.split('[')[0]
        colSpec = fileName.split('[')[1][:-1]

        fs = pyfits.open(self.name)

        self.wavetable = fs[1].data.field('wavelength')

        colNames = fs[1].data.names[1:]
        colWaves = []
        for columnName in colNames:
            colWaves.append(float(columnName.split('#')[1]))

        waves = MA.array(colWaves)
        greater = MA.masked_less(waves, wavelength)
        less = MA.masked_greater(waves, wavelength)
        upper = MA.minimum(greater)
        lower = MA.maximum(less)
        lcol = (colSpec + str(lower)).upper()
        ucol = (colSpec + str(upper)).upper()

        lthr = fs[1].data.field(lcol)
        uthr = fs[1].data.field(ucol)

        if upper != lower:
            w = (wavelength - lower) / (upper - lower)
            self.throughputtable = uthr * w + lthr * (1.0 - w)
        else:
            self.throughputtable = uthr

        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.throughputunits = 'none'
        fs.close()


class ThermalSpectralElement(TabularSpectralElement):
    '''The ThermalSpectralElement class handles spectral elements
    that have associated thermal properties read from a FITS table.

    ThermalSpectralElements differ from regular SpectralElements in
    that they carry thermal parameters such as temperature and beam
    filling factor, but otherwise they operate just as regular
    SpectralElements. They don't know how to apply themselves to an
    existing beam, in the sense that their emissivities should be
    handled explictly, outside the objects themselves.
    '''
    def __init__(self, fileName):

        TabularSpectralElement.__init__(self, fileName=fileName, thrucol='emissivity')

    def getHeaderKeywords(self, header):
        ''' Overrides base class in order to get thermal keywords.
        '''
        self.temperature = header['DEFT']
        self.beamFillFactor = header['BEAMFILL']


class Box(SpectralElement):

    def __init__(self, center, width):
        ''' Both center and width are assumed to be in Angstrom
            units, according to the synphot definition.
        '''
        lower = center - width / 2.0
        upper = center + width / 2.0
        step = 0.05                     # fixed step for now (in A)

        nwaves = int(((upper - lower) / step)) + 2
        self.wavetable = N.zeros(shape=[nwaves,], dtype=N.float64)
        for i in range(nwaves):
            self.wavetable[i] = lower + step * i

        self.wavetable[0]  = self.wavetable[1]  - step
        self.wavetable[-1] = self.wavetable[-2] + step
        
        self.throughputtable = N.ones(shape=self.wavetable.shape, \
                                        dtype=N.float32)
        self.throughputtable[0]  = 0.0
        self.throughputtable[-1] = 0.0
        

class Band(SpectralElement):

    def __init__(self, args):
        ''' Band derived from a reference file.
        '''
        if len(args) == 1:
            self.name = 'band(johnson,' + args[0] + ')'
        else:
            self.name = 'band(' + args[0] + ',' + args[1] + ')'

        # first, check if the band is a valid obsmode taken from the graph table
        obsmode = observationmode.ObservationMode(self.name)
        band = obsmode.Throughput()

        # if not, try to build it from a locally kept throughput file.
        if band == None:
            self.name = self.name.split('(')[1][:-1].lower()
            filename = locations.getBandFileName(self.name)

            band = TabularSpectralElement(filename)

        self.wavetable = band.wavetable
        self.throughputtable = band.throughputtable





