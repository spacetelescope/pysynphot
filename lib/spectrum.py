import pyfits
import numarray
import math
import units
import magnitudes



def waveset(minwave=500.,maxwave=26000.,lenwave=10000):
    ''' Default waveset.'''
    w1 = math.log10(minwave)
    w2 = math.log10(maxwave)

    result = numarray.zeros(shape=[lenwave,],type='Float32')

    for i in range(lenwave):
        frac = float(i) / lenwave
        result[i] = 10 ** (w1 * (1.0 - frac) + w2 * frac)

    return result


def renormalize(spectrum, band, flux, units):
    ''' renormalization function.'''
    sp = spectrum * band
    f1 = sp.integrate(fluxunits=units)
    factor = flux/f1
    return spectrum * factor


def MergeWaveSets(waveset1, waveset2):
    '''Global function to merge 2 wavesets.
    Used by CompositeSourceFunction and CompositeSpectralElement'''

    if waveset1 is None and waveset2 is not None:
        MergedWaveSet = waveset2
    elif waveset2 is None and waveset1 is not None:
        MergedWaveSet = waveset1
    elif waveset1 is None and Waveset2 is None:
        MergedWaveSet = None
    else:
        MergedWaveSet = numarray.concatenate((waveset1, waveset2))
        MergedWaveSet = numarray.sort(MergedWaveSet, 1)
        MergedWaveSet = numarray.compress(MergedWaveSet[:-1] !=
                                          MergedWaveSet[1:], MergedWaveSet)
    return MergedWaveSet

class SourceSpectrum(object):
    '''Base class for the Source Spectrum object.'''

    def __add__(self, other):
        '''Source Spectra can be added.  Delegate the work to the
        CompositeSourceSpectrum class'''

        if not isinstance(other, SourceSpectrum):
            print "Can only add two SourceSpectrum objects"
            raise TypeError
        return CompositeSourceSpectrum(self, other, 'add')

    def __mul__(self, other):
        '''Source Spectra can be multiplied, by constants or by SpectralElement
        objects'''

        if type(other) in [type(1), type(1.0)]:
            other = UniformTransmission(other)
        if not isinstance(other, SpectralElement):
            print "SourceSpectrum objects can only be multiplied by' + \
            'SpectralElement objects or constants"
            raise TypeError

        ## Delegate the work of multiplying to CompositeSourceSpectrum

        return CompositeSourceSpectrum(self, other, 'multiply')

    def __rmul__(self, other):
        '''Order doesnt matter'''

        return self.__mul__(other)

    def getArrays(self):
        '''Returns wavelength and flux arrays as a tuple, performing
           units conversion.
        '''
        wave = self.GetWaveSet();
        flux = self(wave)

        flux = units.Photlam().Convert(wave, flux, self.fluxunits.name)
        wave = units.Angstrom().Convert(wave, None, self.waveunits.name)

        return (wave, flux)
    
    def integrate(self,fluxunits=None):
        '''Integrate using the Trapezoid rule.'''

        wavelengths = self.GetWaveSet()
        fluxes = self(wavelengths)

        if fluxunits != None:
            sp = TabularSourceSpectrum()
            sp.waveunits = self.waveunits
            sp.fluxunits = units.Units(fluxunits)
            sp._wavetable = wavelengths
            sp._fluxtable = self(wavelengths)
            w,fluxes = sp.getArrays()

        npoints = wavelengths.nelements()
        indices = numarray.arange(npoints)[:-1]
        dlambda = wavelengths[indices+1] - wavelengths[indices]
        integrand = 0.5*(fluxes[indices+1] + fluxes[indices])*dlambda

        return integrand.sum()

    def convert(self, targetunits):
        '''Convert to other units. This method actually just changes the
        wavelength and flux units objects, it does not recompute the
        internally kept wave and flux data; these are kept always in internal
        units. Method getArrays does the actual computation.'''

        nunits = units.Units(targetunits)
        if nunits.isFlux:
            self.fluxunits = nunits
        else:
            self.waveunits = nunits

    def redshift(self, z):
        ''' Returns a new redshifted spectrum'''

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
        # into the copy, and convert it to internal units.
        copy._fluxtable = flux_photnu
        copy.fluxunits = units.Units('photnu')

        copy.ToInternal()

        copy.fluxunits = self.fluxunits

        return copy

    def setMagnitude(self, mag):
        '''Makes the magnitude of the source equal to mag.
        mag is a magnitudes.Magnitude object'''

        objectFlux = mag.calcTotalFlux(self)
        vegaFlux = mag.calcVegaFlux()
        magDiff = -2.5*math.log10(objectFlux/vegaFlux)
        factor = 10**(-0.4*(mag.value - magDiff))

        '''Object returned is a CompositeSourceSpectrum'''

        return self * factor

class CompositeSourceSpectrum(SourceSpectrum):
    '''Composite Source Spectrum object, handles addition, multiplication and
    keeping track of the wavelength set'''

    def __init__(self, source1, source2, operation):
        '''__init__ just populates data members'''

        self.component1 = source1
        self.component2 = source2
        self.operation = operation

        # for now we keep these attributes here, in spite of the internal
        # units model. There is code that still breaks down if these attributes
        # are not here.
        self.fluxunits = source1.fluxunits
        self.waveunits = source1.waveunits

    def __call__(self, wavelength):
        '''Add or multiply components, delegating the function calculation to
        the individual objects'''

        if self.operation == 'add':
            return self.component1(wavelength) + self.component2(wavelength)
        if self.operation == 'multiply':
            return self.component1(wavelength) * self.component2(wavelength)

    def GetWaveSet(self):
        '''Obtain the wavelength set for the composite source by forming the
        union of wavelengths from each component'''

        waveset1 = self.component1.GetWaveSet()
        waveset2 = self.component2.GetWaveSet()

        return MergeWaveSets(waveset1, waveset2)

class TabularSourceSpectrum(SourceSpectrum):
    '''Class for a source spectrum that is read in from a FITS table'''

    def __init__(self, SpectrumFile=None):
        '''__init__ takes a character string argument that contains the name
        of the FITS file with the spectrum'''

        if SpectrumFile:
            fs = pyfits.open(SpectrumFile)

            ## Assume that a source spectrum has columns named WAVELENGTH and FLUX
            self._wavetable = fs[1].data.field('wavelength')
            self._fluxtable = fs[1].data.field('flux')

            ## Units are stored in the header in these variables
            self.waveunits = units.Units(fs[1].header['tunit1'].lower())
            self.fluxunits = units.Units(fs[1].header['tunit2'].lower())

            ## Be nice and tidy up
            fs.close()

            ## Convert to internal representation of (angstroms, photlam)
            self.ToInternal()

        else:

            ## if there's no FITS file named, just create empty members
            self._wavetable = None
            self._fluxtable = None
            self.waveunits = None
            self.fluxunits = None

    def __call__(self, wavelengths):
        '''This is where the flux array is actually calculated given a
        wavelength array. Returns an array of flux values calculated at
        the wavelength values input.'''
        return self.resample(wavelengths)._fluxtable

    def taper(self):
        '''Taper the spectrum by adding zeros to each end.'''

        OutSpec = TabularSourceSpectrum()
        wcopy = numarray.zeros(self._wavetable.nelements()+2,type='Float32')
        fcopy = numarray.zeros(self._fluxtable.nelements()+2,type='Float32')
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
        increasing and the TabularSourceSpectrum object'''

        ## Make a new object to hold the resampled spectrum
        resampled = TabularSourceSpectrum()

        ## First need to pad the ends of the spectrum with zeros
        tapered = self.taper()

        ## Linear interpolations from the Python tutorial
        indices = numarray.searchsorted(tapered._wavetable,resampledWaveTab)-1

        ## Make sure the indices containing the desired points don't go
        ## beyond the ends of the array
        indices = numarray.clip(indices, 0, tapered._wavetable.nelements()-2)

        fraction = resampledWaveTab - tapered._wavetable[indices]
        fraction = fraction / (tapered._wavetable[indices+1] -
                               tapered._wavetable[indices])

        ## Make sure the fraction is calculated correctly for elements beyond
        ## the valid regions of the input spectrum
        fraction = numarray.clip(fraction, 0.0, 1.0)

        resampled._fluxtable = tapered._fluxtable[indices] + \
        fraction*(tapered._fluxtable[indices+1] - tapered._fluxtable[indices])

        resampled._wavetable = resampledWaveTab

        return resampled

    def GetWaveSet(self):
        '''For a TabularSource Spectrum, the WaveSet is just the _wavetable
        member.  Return a copy so that there is no reference to the original
        object'''

        return self._wavetable.copy()

    def ToInternal(self):
        '''Convert to the internal representation of (angstroms, photlam)'''
        savewunits = self.waveunits
        savefunits = self.fluxunits
        angwave = self.waveunits.Convert(self.GetWaveSet(), None, 'angstrom')
        phoflux = self.fluxunits.Convert(angwave, self._fluxtable, 'photlam')
        self._wavetable = angwave.copy()
        self._fluxtable = phoflux.copy()
        self.waveunits = savewunits
        self.fluxunits = savefunits
        return None

class GaussianSource(SourceSpectrum):
    '''Gaussian Source Function.'''

    def __init__(self, total, center, width, waveunits='angstrom',
                 fluxunits='flam'):
        '''The integrated flux is total, centered on center with a
        sigma of width.  Default wavelength units are Angstroms and
        default flux units are flam'''

        self.total = total
        self.center = center
        self.width = width
        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)

    def __call__(self, wavelength):
        '''This is where the actual Gaussian is calculated'''

        peak = self.total/self.width/math.sqrt(2.0*3.141592653589)
        return peak*numarray.exp(-(wavelength-self.center)**2/
                                 (2.0*self.width**2))

    def GetWaveSet(self):
        '''Return a wavelength set that describes the Gaussian.  Here
        101 values are calculated, from center - 5*sigma to
        center + 5*sigma, in units of 0.1*sigma'''

        increment = 0.1*self.width
        first = self.center - 50.0*increment
        last = self.center + 50.0*increment
        return numarray.arange(first, last, increment)


class UnitSpectrum(SourceSpectrum):
    '''Constant Source Function.'''
    def __init__(self, fluxdensity, waveunits='angstrom', fluxunits='photlam'):
        self.wavelength = None
        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)
        self._fluxdensity = fluxdensity

    def __call__(self, wavelength):
        sp = TabularSourceSpectrum()
        sp.waveunits = self.waveunits
        sp.fluxunits = self.fluxunits
        sp._wavetable = wavelength
        sp._fluxtable = numarray.ones(sp._wavetable.shape, type='Float32') * \
                        self._fluxdensity
        sp.ToInternal()

        return sp(wavelength)

    def GetWaveSet(self):
        return waveset()


class SpectralElement(object):
    '''Base class for a Spectral Element (e.g. Filter, Detector...)'''

    def __mul__(self, other):
        '''Permitted to multiply a SpectralElement by another
        SpectralElement, or by a SourceSpectrum.  In the former
        case we return a CompositeSpectralElement, while in the
        latter case a CompositeSourceSpectrum'''

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
        '''Order doesnt matter'''

        return self.__mul__(other)

    def convert(self, targetunits):
        '''Spectral elements are not convertible.'''
        return self

    def __call__(self, wavelengths):
        '''This is where the throughput array is calculated for a given
        input wavelength table'''

        return self.resample(wavelengths).throughputtable

    def taper(self):
        '''Taper the spectrum by adding zeros to each end.'''

        OutElement = TabularSpectralElement()

        wcopy = numarray.zeros(self.wavetable.nelements()+2,type='Float32')
        fcopy = numarray.zeros(self.throughputtable.nelements()+2,
                               type='Float32')
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
        monotonically increasing and the TabularSpectralElement object'''
        ## Make a new object to hold the resampled SpectralElement
        resampled = TabularSpectralElement()

        ## First need to pad the ends with zeros
        tapered = self.taper()

        ## Linear interpolations from the Python tutorial
        indices = numarray.searchsorted(tapered.wavetable, resampledWaveTab)-1

        ## Make sure the indices containing the desired points don't go
        ## beyond the ends of the array
        indices = numarray.clip(indices, 0, tapered.wavetable.nelements()-2)
        fraction = resampledWaveTab - tapered.wavetable[indices]
        fraction = fraction / (tapered.wavetable[indices+1] -
                               tapered.wavetable[indices])

        ## Make sure the fraction is calculated correctly for elements beyond
        ## the valid regions of the input spectrum
        fraction = numarray.clip(fraction, 0.0, 1.0)
        resampled.throughputtable = tapered.throughputtable[indices] + \
        fraction*(tapered.throughputtable[indices+1] -
                  tapered.throughputtable[indices])

        resampled.wavetable = resampledWaveTab

        return resampled

    def GetWaveSet(self):
        return self.wavetable



class CompositeSpectralElement(SpectralElement):
    '''CompositeSpectralElement Class, which knows how to calculate
    its throughput by delegating the calculating the calculating to
    its components'''

    def __init__(self, component1, component2):
        '''__init__ populates the component1 and component2 data members'''

        if (not isinstance(component1, SpectralElement) or
            not isinstance(component2, SpectralElement)):
            print "Arguments must be SpectralElements"
            raise TypeError
        self.component1 = component1
        self.component2 = component2

    def __call__(self, wavelength):
        '''This is where the throughput calculation is delegated'''

        return self.component1(wavelength) * self.component2(wavelength)

    def GetWaveSet(self):
        '''This method returns a wavelength set appropriate for a composite
        object by forming the union of the wavelengths of the components'''

        wave1 = self.component1.GetWaveSet()
        wave2 = self.component2.GetWaveSet()

        return MergeWaveSets(wave1, wave2)


class UniformTransmission(SpectralElement):
    '''Uniform Transmission Spectral Element.
    Need to add a GetWaveSet method (or just return None)'''

    def __init__(self, value, waveunits='angstrom'):
        '''The __init__ method just populates the waveunits and value members'''

        self.waveunits = units.Units(waveunits)
        self.value = value

    def GetWaveSet(self):
        '''A UniformTransmission object has no wavelength set'''

        return None

    def __call__(self, wavelength):
        '''__call__ returns the constant value as an array, given a
        wavelength array as argument'''

        return 0.0*wavelength + self.value


class TabularSpectralElement(SpectralElement):
    '''The TabularSpectralElement class handles spectral elements that are
    stored in FITS tables'''

    def __init__(self, ElementFile=None):
        '''__init__ takes a character string argument that contains the name
        of the FITS file with the spectral element'''

        if ElementFile:
            fs = pyfits.open(ElementFile)

            self.name = ElementFile

            ## Assume that the table has columns with names WAVELENGTH
            ## and THROUGHPUT
            self.wavetable = fs[1].data.field('wavelength')
            self.throughputtable = fs[1].data.field('throughput')

            ## Assume that the wavelength units are stored in this header
            ## parameter
            self.waveunits = units.Units(fs[1].header['tunit1'].lower())
            self.throughputunits = 'none'
            fs.close()
        else:

            ## If there's no FITS file, just make a TabularSpectralElement
            ## object with data members set to None
            self.name = None
            self.wavetable = None
            self.throughputtable = None
            self.waveunits = None
            self.throughputunits = None


class Box(SpectralElement):

    def __init__(self, center, width):
        ''' Both center and width are assumed to be in Angstrom
            units, according to the synphot definition.
        '''
        lower = center - width / 2.0
        upper = center + width / 2.0
        step = 0.05                     # fixed step for now (in A)

        waves = []
        nwaves = (upper - lower) / step
        for i in range(nwaves):
            waves.append(lower + step * i)
        
        self.wavetable = numarray.array(waves, type='Float32')
        self.throughputtable = numarray.ones(shape=self.wavetable.shape, \
                                        type='Float32')


