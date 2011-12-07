from __future__ import division
"""This will ultimately replace the observation.py module. It defines
a new Observation class, subclassed from CompositeSourceSpectrum,
that has some special methods and attributes and explicitly removes
certain other methods."""

import os
import types

import numpy as N
import math

import spectrum
import units

from obsbandpass import pixel_range, wave_range
from spectrum import ArraySourceSpectrum

import pysynphot.exceptions as exceptions

try:
  import pysynphot_utils
  utils_imported = True
except ImportError:
  utils_imported = False

class Observation(spectrum.CompositeSourceSpectrum):
    """ obs = Observation(Spectrum object, Bandpass object,
    binset=numpy array to be used for binning when converting to counts.)
    
    Most ObsBandpass objects have a built-in binset that is optimized
    for use with the specified observing mode; specifying the binset
    in the Observation constructor would overrirde that binset.

    An Observation is the end point of a chain of spectral manipulation."""
    

    def __init__(self,spec,band,binset=None,force=None):
        """The normal means of producing an Observation is by means of the
        .observe() method on the spectral element."""

        self.spectrum = spec
        self.bandpass = band
        self.warnings={}
        self.validate_overlap(force)
        self.binset = binset
        
        keep=self.warnings
        spectrum.CompositeSourceSpectrum.__init__(self,
                                                  self.spectrum,
                                                  self.bandpass,
                                                  'multiply')

        self.warnings.update(keep)
        
        #The natural waveset of the observation is the merge of the
        #natural waveset of the spectrum with the natural waveset of the
        #bandpass. Because the Observation inherits from a
        #CompositeSourceSpectrum, this will be handled correctly.
#        self._binwave = None
        self._binflux = None

        self.initbinset(binset)
        #self.initbinflux()

        
    def validate_overlap(self,force):
        """By default, it is required that the spectrum and bandpass fully
        overlap. Partial overlap will raise an error in the absence of the
        force keyword, which may be set to "taper" or "extrap". """

       
        if force is None:
            stat=self.bandpass.check_overlap(self.spectrum)
            if stat=='full':
                pass
            elif stat == 'partial':
                raise(ValueError('Spectrum and bandpass do not fully overlap. You may use force=[extrap|taper] to force this Observation anyway.'))
            elif stat == 'none':
                raise(ValueError('Spectrum and bandpass are disjoint'))
            
        elif force.lower() == 'taper':
            try:
                self.spectrum=self.spectrum.taper()
            except AttributeError:
                self.spectrum=self.spectrum.tabulate().taper()
                self.warnings['PartialOverlap']=True
                
        elif force.lower().startswith('extrap'):
            #default behavior works, but check the overlap so we can set the warning
            stat=self.bandpass.check_overlap(self.spectrum)
            if stat == 'partial':
                self.warnings['PartialOverlap']=True

        else:
            raise(KeyError("Illegal value force=%s; legal values=('taper','extrap')"%force))

    def initbinset(self,binset=None):
        if binset is None:
            msg="(%s) does not have a defined binset in the wavecat table. The waveset of the spectrum will be used instead."%str(self.bandpass)

            try:
                self.binwave = self.bandpass.binset
            except (KeyError, AttributeError), e:
                self.binwave = self.spectrum.wave
                print(msg)
            
            if self.binwave is None:
                self.binwave = self.spectrum.wave
                print(msg)
        else:
            self.binwave=binset

    def initbinflux(self):
        """This routine performs the integration of the spectrum
        on the specified binned waveset. It uses the natural waveset
        of the spectrum in performing this integration.

        NOTE: This method is implemented under the assumption that the
        wavelength values in the binned waveset are the *centers* of the bins.

        By contrast, the native wave/flux arrays should be considered
        samples of a continuous function.

        Thus, it makes sense to interpolate .wave/.flux; it does not
        make sense to interpolate .binwave/.binflux.
        
        """

        # compute endpoints of each summation bin from their centers.
        bin_edges = (self.binwave[1:] + self.binwave[:-1]) / 2.0
        endpoints = N.empty(shape=[len(bin_edges)+2,],
                            dtype=N.float64)
        endpoints[1:-1] = bin_edges
        
        #compute the first and last by making them symmetric
        endpoints[0]  = self.binwave[0]  - (bin_edges[0]   - self.binwave[0])
        endpoints[-1] = self.binwave[-1] + (self.binwave[-1] - bin_edges[-1])
        
        # merge these endpoints in with the natural waveset 
        spwave = spectrum.MergeWaveSets(self.wave, endpoints)
        spwave = spectrum.MergeWaveSets(spwave,self.binwave)

        # compute indices associated to each endpoint.
        indices = N.searchsorted(spwave, endpoints)
        self._indices = indices[:-1]
        self._indices_last = indices[1:]

        # prepare integration variables.
        flux = self(spwave) 
        avflux = (flux[1:] + flux[:-1]) / 2.0
        self._deltaw = spwave[1:] - spwave[:-1]
        
        # sum over each bin.
        if utils_imported is True:
            self._binflux, self._intwave = \
              pysynphot_utils.calcbinflux(len(self.binwave),
                                          self._indices,
                                          self._indices_last,
                                          avflux,
                                          self._deltaw)
        else:
            #Note that, like all Python striding, the range over which
            #we integrate is [first:last).
            self._binflux = N.empty(shape=self.binwave.shape,dtype=N.float64)
            self._intwave = N.empty(shape=self.binwave.shape,dtype=N.float64)
            for i in range(len(self._indices)):
                first = self._indices[i]
                last = self._indices_last[i]
                self._binflux[i]=(avflux[first:last]*self._deltaw[first:last]).sum()/self._deltaw[first:last].sum()
                self._intwave[i]=self._deltaw[first:last].sum()
        
        #Save the endpoints for future use
        self._bin_edges = endpoints

    def _getBinfluxProp(self):
        if self._binflux is None:
            self.initbinflux()
            
        binflux = units.Photlam().Convert(self.binwave,
                                          self._binflux,
                                          self.fluxunits.name)
        return binflux
    
    def _getBinwaveProp(self):
        if self._binwave is None:
            self.initbinset(self.binset)
        return self._binwave
    
    binflux = property(_getBinfluxProp,doc='Flux on binned wavelength set property')
#    binwave = property(_getBinwaveProp,doc='Waveset for binned flux')
    

    # Multiplication and addition are handled by performing them on
    # the spectral component of the Observation, and then creating a
    # new Observation as the result.
    #
    # This is because Observation is a subclass of CompositeSourceSpectrum
    # but with *a lot* of extra functionality involved in handling the
    # binned wave and flux arrays. Simply inheriting the parent class's
    # methods for multiplication and addition does not return an Observation.
    #
    # Note that the order of operations actually implemented therefore varies
    # from what is expected, which naively would be
    #    (self.spectrum*self.bandpass) * other
    #
    def __mul__(self, other):
        result = Observation(self.spectrum,
                                 self.bandpass * other,
                                 binset=self.binset
                                 )
        return result
      
    def __rmul__(self, other):
        return __mul__(self, other)

    def __add__(self, other):
        result = Observation(self.spectrum + other,
                             self.bandpass,
                             binset = self.binset)
        return result
    def __radd__(self, other):
        return __add__(self, other)
      
    #Disable methods that should not be supported by this class
    def redshift(self,z):
        raise NotImplementedError('Observations cannot be redshifted')

    def writefits(self,fname,clobber=True, trimzero=True, binned=True,
                  hkeys=None):
        """All we really want to do here is flip the default value of
        'binned' from the vanilla spectrum case.
        """

        spectrum.CompositeSourceSpectrum.writefits(self,fname,
                                                   clobber=clobber,
                                                   trimzero=trimzero,
                                                   binned=binned,
                                                   hkeys=hkeys)
            
    def countrate(self,binned=True,range=None,force=False):
        """This is the calculation performed when the ETC invokes countrate.
        Essentially it wants the effstim in counts.

        binned: if True, operations will be performed on (binwave,binflux);
                otherwise on (wave,flux)

        range=[low,high]: if range is not None, it is expected to be a
            sequence with two floating-point elements specifying the low
            and high wavelength range (specified in self.waveunits) over 
            which the integration will be performed. 

            This is an _inclusive_ range.

            Disjoint or partially-overlapping ranges will raise an
            exception by default. If force=True is set, then a partial
            overlap will return the calculated value rather than raise
            an exception.

            If the specified range does not exactly match a value in the
            waveset:
               - if binned=True, the bin containing the range value will
                 be used. (Recall values of binwave specify bin centers.)
               - if binned=False, the wave and flux arrays will be
                 interpolated to the specified values.
        """

        if self._binflux is None:
          self.initbinflux()

        myfluxunits = self.fluxunits.name
        self.convert('counts')
        warn=False
        if binned:
            #No range specified - use full range
            if range is None:
                lx,ux=(None,None)
            #Range is disjoint from binwave
            elif (range[0]>self.binwave[-1] or
                  range[1]<self.binwave[0]):
                raise ValueError("%s is disjoint from obs.binwave %s"%(range,
                                                                       [self.binwave[0],self.binwave[-1]]))
            #Partial overlap                     
            else:
                
                if range[0] < self._bin_edges[0]:
                    warn=True
                    lx=None
                else:
                    lx=N.searchsorted(self._bin_edges,range[0])-1
                    
                if range[1] > self._bin_edges[-1]:
                    warn=True
                    ux=None
                else:
                    ux=N.searchsorted(self._bin_edges,range[1])
                

            ans = self.binflux[lx:ux].sum()
            if warn and not force:
                raise ValueError("%s does not fully overlap binwave range %s. Countrate in overlap area is %f"%(range,[self.binwave[0],self.binwave[-1]],ans))
                                                                                                             
        else:
            if range is None:
                ans = self.flux.sum()
            else:
                raise NotImplementedError("Sorry, range+binned=False not yet implemented")
        self.convert(myfluxunits)
        return ans

    def effstim(self,fluxunits='photlam'):
        """Compute effective stimulation in specified units"""

        oldunits=self.fluxunits
        self.convert(fluxunits)
        x=units.Units(fluxunits)
        try:
            if x.isDensity:
                rate=self.integrate()
                self._fluxcheck(rate)
                if x.isMag:
                    ans=x.unitResponse(self.bandpass) - 2.5*math.log10(rate)
                else:
                    ans=rate*x.unitResponse(self.bandpass)
            else:
                if x.isMag:
                    #its linear unit must be counts
                    self.convert('counts')
                    total=self.flux.sum()
                    self._fluxcheck(total)
                    ans=-2.5*math.log10(total)
                else:
                    ans=self.flux.sum()
                    self._fluxcheck(ans)
        finally:
            self.convert(oldunits)
            del x
            
        return ans

    def _fluxcheck(self,totalflux):
        if totalflux <= 0.0:
            raise ValueError('Integrated flux is <= 0')
        if N.isnan(totalflux):
            raise ValueError('Integrated flux is NaN')
        if N.isinf(totalflux):
            raise ValueError('Integrated flux is infinite')
                            
    
    def pivot(self,binned=True):
        """This is the calculation performed when the ETC invokes calcphot.
        Does this need to be calculated on binned waveset, or may
        it be calculated on native waveset?"""
        if binned:
            wave = self.binwave
        else:
            wave = self.wave

        countmulwave = self(wave)*wave
        countdivwave = self(wave)/wave

        num = self.trapezoidIntegration(wave,countmulwave)
        den = self.trapezoidIntegration(wave,countdivwave)

        if num == 0.0 or den == 0.0:
            return 0.0

        return math.sqrt(num/den)


    def efflam(self,binned=True):
        """Calculation performed based on observation.py
        _EfflamCalculator, which produces EFFLPHOT results!."""

        myfluxunits=self.fluxunits.name
        self.convert('flam')
        if binned:
            wave=self.binwave
            flux=self.binflux
        else:
            wave=self.wave
            flux=self.flux

        num = self.trapezoidIntegration(wave,flux*wave*wave)
        den = self.trapezoidIntegration(wave,flux*wave)
        self.convert(myfluxunits)

        if num == 0.0 or den == 0.0:
            return 0.0

        return num/den

    def sample(self, swave, binned=True, fluxunits='counts'):
        """Samples the observation at the wavelength(s) swave, specified in
        waveunits. The binned keyword determines whether the sampling is
        performed on binwave/binflux, in which case no interpolation is
        performed, or on the native wave/flux, in which case interpolation
        is performed.
        """

        if self._binflux is None:
          self.initbinflux()

        if fluxunits != 'counts':
            raise NotImplementedError("Sorry, only counts are supported at this time")
        else:
            #Save current fluxunits, in case they're different
            saveunits=None
            if not units.ismatch('counts', self.fluxunits):
                saveunits=self.fluxunits
                self.convert('counts')

                
        if binned:
            #Then we don't interpolate, just return the appropriate values
            #from binflux
            if not isinstance(swave,(types.IntType, types.FloatType)):
                #The logic for this case doesn't yet work on arrays
                raise NotImplementedError("Sorry, only scalar samples are supported at this time")
            else:
                #Find the bin in which it belongs.
                #_bin_edge[i] is the low edge of the bin centered
                #at binwave[i].

                idx = N.where(swave >= self._bin_edges)[0]
                #idx[-1] is the largest edge that is still smaller
                #than swave
                try:
                    ans = self.binflux[idx[-1]]
                except IndexError:
                    raise ValueError("Value out of range: wavelength %g not contained in range [%g, %g]"%(swave,self.binwave[0],self.binwave[-1]))

        else:
            #Then we do interpolate on wave/flux
            if isinstance(swave,(types.IntType, types.FloatType)):
                delta=0.00001
                wv=N.array([swave-delta, swave, swave+delta])
                ans = N.interp(wv, self.wave, self.flux)[1]
            else:
                ans = N.interp(wv, self.wave, self.flux)

            
        #Change units back, if necessary, then return
        if saveunits is not None:
            self.convert(saveunits)
        return ans
        
    def pixel_range(self, waverange, waveunits=None, round='round'):
        """
        Returns the number of wavelength bins within `waverange`.
        
        .. note:: This calls the `obsbandpass.pixel_range` function with
           `self.binwave` as the first argument. See
           `obsbandpass.pixel_range` for full documentation.
           
        Parameters
        ----------
        waveunits : str, optional
            The units of the wavelengths given in `waverange`. Defaults to None.
            If None, the wavelengths are assumed to be in the units of the
            `waveunits` attribute.
            
        Raises
        ------
        pysynphot.exceptions.UndefinedBinset
            If the `binwave` attribute is None.
           
        See Also
        --------
        `obsbandpass.pixel_range`
        
        """
        # make sure we have a binset to work with
        if self.binwave is None:
            raise exceptions.UndefinedBinset('No binset specified for this bandpass.')
        
        # start by converting waverange to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)
            
            if not isinstance(waverange,N.ndarray):
                waverange = N.array(waverange)
            
            # convert to angstroms and then whatever self.waveunits is
            waverange = waveunits.ToAngstrom(waverange)
            
            waverange = units.Angstrom().Convert(waverange, self.waveunits.name)
        
        return pixel_range(self.binwave, waverange, round=round)
        
        
    def wave_range(self, cenwave, npix, waveunits=None, round='round'):
        """
        Get the wavelength range covered by a number of pixels, `npix`, centered
        on wavelength `cenwave`.
        
        .. note:: This calls the `obsbandpass.wave_range` function with
           `self.binwave` as the first argument. See
           `obsbandpass.wave_range` for full documentation.
           
        Parameters
        ----------
        waveunits : str, optional
            Wavelength units of `cenwave` and the returned wavelength range.
            Defaults to None. If None, the wavelengths are assumed to be in 
            the units of the `waveunits` attribute.
        
        Raises
        ------
        pysynphot.exceptions.UndefinedBinset
            If the `binwave` attribute is None.
        
        See Also
        --------
        `obsbandpass.wave_range`
        
        """
        # make sure we have a binset to work with
        if self.binwave is None:
            raise exceptions.UndefinedBinset('No binset specified for this bandpass.')
        
        # convert cenwave from waveunits to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)
            
            # convert to angstroms and then whatever self.waveunits is
            cenwave = waveunits.ToAngstrom(cenwave)
            cenwave = units.Angstrom().Convert(cenwave, self.waveunits.name)
            
        wave1, wave2 = wave_range(self.binwave, cenwave, npix, round=round)    
            
        # translate ends to waveunits, if necessary
        if waveunits is not None:
            # convert to angstroms
            wave1 = self.waveunits.ToAngstrom(wave1)
            wave2 = self.waveunits.ToAngstrom(wave2)
            
            # then to waveunits
            wave1 = units.Angstrom().Convert(wave1, waveunits.name)
            wave2 = units.Angstrom().Convert(wave2, waveunits.name)
            
        return wave1, wave2

    def as_spectrum(self, binned=True):
        """ Reduce the Observation to a TabularSourceSpectrum.

        An Observation is a complex object with some restrictions on its
        capabilities. At times it would be useful to work with the
        simulated Observation as a simpler object that is easier to
        manipulate and takes up less memory. This method returns a
        TabularSourceSpectrum made from either the (wave, flux) or
        the (binwave, binflux) properties of the Observation.

        Parameters
        ----------
        binned: bool
          If True, use (binwave, binflux); otherwise use (wave, flux).

        Returns
        -------
        result: TabularSourceSpectrum

        """
        if binned:
            wave, flux = self.binwave, self.binflux
        else:
            wave, flux = self.wave, self.flux

        result = ArraySourceSpectrum(wave, flux,
                                     self.waveunits,
                                     self.fluxunits,
                                     name = self.name,
                                     keepneg = True)

        return result
