"""This will ultimately replace the observation.py module. It defines
a new Observation class, subclassed from CompositeSourceSpectrum,
that has some special methods and attributes and explicitly removes
certain other methods."""

import spectrum
import units

class Observation(spectrum.CompositeSourceSpectrum):
    """An Observation is the end point of a chain of spectral manipulation.
    The normal means of creating an Observation is by means of the .observe
    method on a SpectralElement."""

    def __init__(self,spec,band,binset=None):
        """The normal means of producing an Observation is by means of the
        .observe() method on the spectral element."""

        spectrum.CompositeSourceSpectrum.__init__(self, spec, band, 'multiply')
        self.spectrum = self.component1
        self.bandpass = self.component2


    def getBinnedArrays(self,binset=None):
        binwave = self.GetBinset(binset)
        binflux = self(binwave)

        binflux = units.Photlam().Convert(binwave,binflux,self.fluxunits.name)
        binwave = units.Angstrom().Convert(binwave, self.waveunits.name)

        return (binwave, binflux)

    def _getBinsetProp(self):
        binwave, binflux = self.getBinnedArrays()
        return binwave

    def _getBinfluxProp(self):
        binwave, binflux = self.getBinnedArrays()
        return binflux
    
    binwave = property(_getBinsetProp,doc='Binned wavelength property')
    binflux = property(_getBinfluxProp,doc='Flux on binned wavelength set property')
    def GetBinset(self,binset=None):
        if binset is None:
            try:
                binset = self.bandpass.obsmode.bandWave()
            except (KeyError, AttributeError), e:
                print "%s does not have a defined binset in the wavecat table. You must provide a binset."%self.bandpass
                raise e
        return binset

    #Disable methods that should not be supported by this class
    def __mul__(self, other):
        raise NotImplementedError('Observations cannot be multiplied')
    def __rmul__(self, other):
        raise NotImplementedError('Observations cannot be multiplied')
    def __add__(self, other):
        raise NotImplementedError('Observations cannot be added')
    def __radd__(self, other):
        raise NotImplementedError('Observations cannot be added')
    def redshift(self,z):
        raise NotImplementedError('Observations cannot be redshifted')
