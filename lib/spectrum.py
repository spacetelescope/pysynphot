import pyfits
import numarray
import math
import units
import magnitudes

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

class SourceSpectrum:
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

        ## Delegate the work of multiplying to the CompositeSourceSpectrum
        ## class

        return CompositeSourceSpectrum(self, other, 'multiply')

    def __rmul__(self, other):
        '''Order doesnt matter'''

        return self.__mul__(other)

    def integrate(self):
        '''Integrate using the Trapezoid rule'''

        wavelengths = self.GetWaveSet()
        fluxes = self(wavelengths)
        npoints = wavelengths.nelements()
        indices = numarray.arange(npoints)[:-1]
        dlambda = wavelengths[indices+1] - wavelengths[indices]
        integrand = 0.5*(fluxes[indices+1] + fluxes[indices])*dlambda
        return integrand.sum()

    def convert(self, targetunits):
        '''Convert to other units.  Delegate to methods in the
        Units class'''
        if targetunits == 'angstroms' or targetunits == 'hz':
            return self.waveunits.Convert(self, targetunits)
        return self.fluxunits.Convert(self, targetunits)

    def SetMagnitude(self, Mag):
        '''SetMagnitude makes the magnitude of the source equal to Mag
        Mag is a magnitudes.Magnitude object'''
        
        ObjectFlux = Mag.CalcTotalFlux(self)
        VegaFlux = Mag.CalcVegaFlux()
        MagDiff = -2.5*math.log10(ObjectFlux/VegaFlux)
        Factor = 10**(-0.4*(Mag.value - MagDiff))

        '''Object returned is a CompositeSourceSpectrum'''
        
        return self*Factor

class CompositeSourceSpectrum(SourceSpectrum):
    '''Composite Source Spectrum object, handles addition, multiplication and
    keeping track of the wavelength set'''

    def __init__(self, source1, source2, operation):
        '''__init__ just populates data members'''

        self.component1 = source1
        _fluxunits = self.component1.fluxunits.name
        _waveunits = self.component1.waveunits.name
        self.component2 = source2.convert(_fluxunits)
        self.component2 = self.component2.convert(_waveunits)
        self.fluxunits = source1.fluxunits
        self.waveunits = source1.waveunits
        self.operation = operation

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

            ## Assume that a source spectrum has columns named WAVELENGTH and
            ## FLUX

            self.wavetable = fs[1].data.field('wavelength')
            self.fluxtable = fs[1].data.field('flux')

            ## Units are stored in the header in these variables

            self.fluxunits = units.Units(fs[1].header['tunit2'].lower())
            self.waveunits = units.Units(fs[1].header['tunit1'].lower())

            ## Be nice and tidy up

            fs.close()

        else:

            ## if there's no FITS file named, just create empty members

            self.wavetable = None
            self.fluxtable = None
            self.waveunits = None
            self.fluxunits = None

    def __call__(self, wavelengths):
        '''This is where the flux array is actually calculated given a
        wavelength array.  Returns an array of flux values calculated at
        the wavelength values input'''

        return self.resample(wavelengths).fluxtable

    def taper(self):
        '''Taper the spectrum by adding zeros to each end.'''

        OutSpec = TabularSourceSpectrum()
        wcopy = numarray.zeros(self.wavetable.nelements()+2,type='Float32')
        fcopy = numarray.zeros(self.fluxtable.nelements()+2,type='Float32')
        wcopy[1:-1] = self.wavetable
        fcopy[1:-1] = self.fluxtable
        fcopy[0] = 0.0
        fcopy[-1] = 0.0

        ## The wavelengths to use for the first and last points are
        ## calculated by using the same ratio as for the 2 interior points

        wcopy[0] = wcopy[1]*wcopy[1]/wcopy[2]
        wcopy[-1] = wcopy[-2]*wcopy[-2]/wcopy[-3]

        OutSpec.wavetable = wcopy
        OutSpec.fluxtable = fcopy

        return OutSpec
        
    def resample(self, resampledWaveTab):
        '''Interpolate flux given a wavelength array that is monotonically
        increasing and the TabularSourceSpectrum object'''

        ## Make a new object to hold the resampled spectrum

        resampled = TabularSourceSpectrum()

        ## First need to pad the ends of the spectrum with zeros

        tapered = self.taper()

        ## Linear interpolations from the Python tutorial

        indices = numarray.searchsorted(tapered.wavetable,resampledWaveTab)-1

        ## Make sure the indices containing the desired points don't go
        ## beyond the ends of the array

        indices = numarray.clip(indices, 0, tapered.wavetable.nelements()-2)

        fraction = resampledWaveTab - tapered.wavetable[indices]
        fraction = fraction / (tapered.wavetable[indices+1] -
                               tapered.wavetable[indices])

        ## Make sure the fraction is calculated correctly for elements beyond
        ## the valid regions of the input spectrum

        fraction = numarray.clip(fraction, 0.0, 1.0)

        resampled.fluxtable = tapered.fluxtable[indices] + \
        fraction*(tapered.fluxtable[indices+1] - tapered.fluxtable[indices])

        resampled.wavetable = resampledWaveTab

        return resampled

    def GetWaveSet(self):
        '''For a TabularSource Spectrum, the WaveSet is just the wavetable
        member'''

        return self.wavetable

class GaussianSource(SourceSpectrum):
    '''Gaussian Source Function.'''

    def __init__(self, total, center, width, waveunits='angstroms',
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

class SpectralElement:
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

        return MergeWaveSets(waveset1, waveset2)

class UniformTransmission(SpectralElement):
    '''Uniform Transmission Spectral Element.
    Need to add a GetWaveSet method (or just return None)'''

    def __init__(self, value, waveunits='angstroms'):
        '''The __init__ method just populates the waveunits and value
        members'''

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

            self.wavetable = None
            self.throughputtable = None
            self.waveunits = None
            self.throughputunits = None

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
        '''For a TabularSpectralElement, the WaveSet is just the wavelength
        table'''

        return self.wavetable
