# It defines a new Observation class, subclassed from CompositeSourceSpectrum,
# that has some special methods and attributes and explicitly removes
# certain other methods.
"""This module handles an observation and related calculations."""
from __future__ import division

import numpy as np
import math

from . import spectrum
from . import units
from . import binning
from . import exceptions

from .obsbandpass import pixel_range, wave_range
from .spectrum import ArraySourceSpectrum


try:
    import pysynphot_utils
    utils_imported = True
except ImportError:
    utils_imported = False


def check_overlap(a, b):
    """Check for wavelength overlap between two spectra.

    .. note::

        Generalized from
        :meth:`pysynphot.spectrum.SpectralElement.check_overlap`.

    Parameters
    ----------
    a, b : `~pysynphot.spectrum.SourceSpectrum` or `~pysynphot.spectrum.SpectralElement`
       Typically a source spectrum, spectral element, observation,
       or bandpass from observation mode.

    Returns
    -------
    result : {'full', 'partial', 'none'}
        Full, partial, or no overlap.

    Raises
    ------
    AttributeError
        Given spectrum does not have flux or throughput.

    """
    if a.isAnalytic or b.isAnalytic:
        #then it's defined everywhere
        result = 'full'
    else:
        #get the wavelength arrays
        waves = list()
        for x in (a, b):
            if hasattr(x,'throughput'):
                wv = x.wave[np.where(x.throughput != 0)]
            elif hasattr(x,'flux'):
                wv = x.wave
            else:
                raise AttributeError("neither flux nor throughput in %s"%x)
            waves.append(wv)

        #get the endpoints
        a1,a2 = waves[0].min(), waves[0].max()
        b1,b2 = waves[1].min(), waves[1].max()

        #do the comparison
        if (a1>=b1 and a2<=b2):
            result = 'full'
        elif (a2<b1) or (b2<a1):
            result = 'none'
        else:
            result = 'partial'

    return result


def validate_overlap(comp1, comp2, force):
    """Validate the overlap between the wavelength sets
    of the two given components.

    Parameters
    ----------
    comp1, comp2 : `~pysynphot.spectrum.SourceSpectrum` or `~pysynphot.spectrum.SpectralElement`
        Source spectrum and bandpass of an observation.

    force : {'extrap', 'taper', `None`}
        If not `None`, the components may be adjusted by
        extrapolation or tapering.

    Returns
    -------
    comp1, comp2
        Same as inputs. However, ``comp1`` might be tapered
        if that option is selected.

    warnings : dict
        Maps warning keyword to its description.

    Raises
    ------
    KeyError
        Invalid ``force``.

    pysynphot.exceptions.DisjointError
        No overlap detected when ``force`` is `None`.

    pysynphot.exceptions.PartialOverlap
        Partial overlap detected when ``force`` is `None`.

    """
    warnings = dict()
    if force is None:
        stat = comp2.check_overlap(comp1)
        if stat=='full':
            pass
        elif stat == 'partial':
            raise(exceptions.PartialOverlap('Spectrum and bandpass do not fully overlap. You may use force=[extrap|taper] to force this Observation anyway.'))
        elif stat == 'none':
            raise(exceptions.DisjointError('Spectrum and bandpass are disjoint'))

    elif force.lower() == 'taper':
        try:
            comp1=comp1.taper()
        except AttributeError:
            comp1=comp1.tabulate().taper()
            warnings['PartialOverlap']=force

    elif force.lower().startswith('extrap'):
        #default behavior works, but check the overlap so we can set the warning
        stat=comp2.check_overlap(comp1)
        if stat == 'partial':
            warnings['PartialOverlap']=force

    else:
        raise(KeyError("Illegal value force=%s; legal values=('taper','extrap')"%force))
    return comp1, comp2, warnings


class Observation(spectrum.CompositeSourceSpectrum):
    """Class to handle an :ref:`observation <pysynphot-observation>`.
    An observation is the end point of a chain of spectral manipulation.

    Most `~pysynphot.obsbandpass.ObsBandpass` objects have a built-in
    ``binset`` that is optimized for use with the specified observing
    mode (also see :ref:`pysynphot-wavelength-table`).
    Specifying the ``binset`` here would override the built-in one.

    Parameters
    ----------
    spec : `~pysynphot.spectrum.SourceSpectrum`
        Source spectrum.

    band : `~pysynphot.spectrum.SpectralElement`
        Bandpass.

    binset : array_like or `None`
        Wavelength values to be used for binning when converting to counts.
        See :meth:`initbinset`.

    force
        See :meth:`~pysynphot.observation.Observation.validate_overlap`.

    Attributes
    ----------
    spectrum
        Same as input ``spec``.

    bandpass
        Same as input ``band``.

    binset
        Same as input ``binset``.

    component1, component2 : `~pysynphot.spectrum.SourceSpectrum` or `~pysynphot.spectrum.SpectralElement`
        Components and sub-components that belong to the observation.

    operation : str
        This is always "multiply".

    name : str
        Short description of the observation.

    warnings : dict
        To store warnings, which are inherited from all inputs. If they have the same warning keyword, the one from most recently read component is used.

    isAnalytic : bool
        Flag to indicate whether this is an analytic spectrum. This is only `True` if both inputs are analytic.

    primary_area : number or `None`
        :ref:`pysynphot-area` of the telescope. This is inherited from either of the inputs, if available (not `None`). If inputs have different values, an exception is raised.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units inherited from source spectrum.

    wave, flux : array_like
        Wavelength set and associated flux in user units. This is the native dataset.

    binwave, binflux : array_like
        Binned dataset.

    Raises
    ------
    pysynphot.exceptions.IncompatibleSources
        Input spectra have different telescope areas defined.

    """
    def __init__(self,spec,band,binset=None,force=None):
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
        """Validate that spectrum and bandpass overlap.
        Warnings are stored in ``self.warnings``.

        Parameters
        ----------
        force : {'extrap', 'taper', `None`}
            If `None`, it is required that the spectrum and bandpass fully
            overlap. Partial overlap is allowed if this is set to
            ``'extrap'`` or ``'taper'``. See :func:`validate_overlap`.

        """

        #Wrap the function for convenience
        self.spectrum, self.bandpass, warn = validate_overlap(self.spectrum,
                                                              self.bandpass, force)
        self.warnings.update(warn)

    def initbinset(self,binset=None):
        """Set ``self.binwave``.

        By default, wavelength values for binning are inherited
        from bandpass. If the bandpass has no binning information,
        then source spectrum wavelengths are used. However, if
        user provides values, then those are used without question.

        Parameters
        ----------
        binset : array_like or `None`
            Wavelength values to be used for binning when converting to counts.

        """
        if binset is None:
            msg="(%s) does not have a defined binset in the wavecat table. The waveset of the spectrum will be used instead."%str(self.bandpass)

            try:
                self.binwave = self.bandpass.binset
            except (KeyError, AttributeError):
                self.binwave = self.spectrum.wave
                print(msg)

            if self.binwave is None:
                self.binwave = self.spectrum.wave
                print(msg)
        else:
            self.binwave=binset

    def initbinflux(self):
        """Calculate binned flux and edges.

        Flux is computed by integrating the spectrum
        on the specified binned wavelength set, using
        information from the natural wavelength set.

        Native wave/flux arrays should be considered samples
        of a continuous function, but not their binned counterparts.
        Thus, it makes sense to interpolate ``(wave, flux)`` but not
        ``(binwave, binflux)``.

        .. note::

            Assumes that the wavelength values in the binned
            wavelength set are the *centers* of the bins.

            Uses ``pysynphot.pysynphot_utils.calcbinflux()`` C-extension,
            if available, for binned flux calculation.

        """
        endpoints = binning.calculate_bin_edges(self.binwave)

        # merge these endpoints in with the natural waveset
        spwave = spectrum.MergeWaveSets(self.wave, endpoints)
        spwave = spectrum.MergeWaveSets(spwave,self.binwave)

        # compute indices associated to each endpoint.
        indices = np.searchsorted(spwave, endpoints)
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
            self._binflux = np.empty(shape=self.binwave.shape,dtype=np.float64)
            self._intwave = np.empty(shape=self.binwave.shape,dtype=np.float64)
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

        if hasattr(self.bandpass, 'primary_area'):
            area = self.bandpass.primary_area
        else:
            area = None

        binflux = units.Photlam().Convert(self.binwave,
                                          self._binflux,
                                          self.fluxunits.name,
                                          area=area)
        return binflux

    def _getBinwaveProp(self):
        if self._binwave is None:
            self.initbinset(self.binset)
        return self._binwave

    binflux = property(_getBinfluxProp,doc='Flux of binned wavelength set.')
#    binwave = property(_getBinwaveProp,doc='Waveset for binned flux')


    # Multiplication is handled by performing the operation on
    # the spectral component of the Observation, and then creating a
    # new Observation as the result.
    #
    # This is because Observation is a subclass of CompositeSourceSpectrum
    # but with *a lot* of extra functionality involved in handling the
    # binned wave and flux arrays. Simply inheriting the parent class's
    # methods for multiplication does not return an Observation.
    #
    # Note that the order of operations actually implemented therefore varies
    # from what is expected, which naively would be
    #    (self.spectrum*self.bandpass) * other
    #
    def __mul__(self, other):
        # If the original object has partial overlap warnings, then
        # the forcing behavior also needs to be propagated.

        force = self.warnings.get('PartialOverlap', None)

        result = Observation(self.spectrum,
                             self.bandpass * other,
                             binset=self.binwave,
                             force=force)
        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    #Disable methods that should not be supported by this class
    def __add__(self, other):
        raise NotImplementedError('Observations cannot be added')

    def __radd__(self, other):
        raise NotImplementedError('Observations cannot be added')


    def redshift(self,z):
        """Observations cannot be redshifted."""
        raise NotImplementedError('Observations cannot be redshifted')

    def writefits(self,fname,clobber=True, trimzero=True, binned=True,
                  hkeys=None):
        """Like :meth:`pysynphot.spectrum.SourceSpectrum.writefits`
        but with ``binned=True`` as default.

        """
        spectrum.CompositeSourceSpectrum.writefits(self,fname,
                                                   clobber=clobber,
                                                   trimzero=trimzero,
                                                   binned=binned,
                                                   hkeys=hkeys)

    def countrate(self,binned=True,range=None,force=False):
        """Calculate effective stimulus in count/s.
        Also see :ref:`pysynphot-formula-countrate` and
        :ref:`pysynphot-formula-effstim`.

        .. note::

            This is the calculation performed when the ETC invokes
            ``countrate``.

        Parameters
        -----------
        binned : bool
            If `True` (default), use binned data.
            Otherwise, use native data.

        range : tuple or `None`
            If not `None`, it must be a sequence with two floating-point
            elements specifying the wavelength range (*inclusive*) in the
            unit of ``self.waveunits`` in the form of ``(low, high)``;
            This is the range over which the integration will be performed.
            If the specified range does not exactly match a value in the
            wavelength set:

                * If ``binned=True``, the bin containing the range value will
                  be used. This assumes ``self.binwave`` contains bin centers.
                * If ``binned=False``, native dataset will be interpolated to
                  the specified values. (*Not Implemented.*)

        force : bool
            If `False` (default), partially overlapping ranges
            will raise an exception. If `True`, a partial overlap will
            return the calculated value instead. Disjoint ranges raise
            an exception regardless.

        Returns
        -------
        ans : float
            Count rate.

        Raises
        ------
        NotImplementedError
            Wavelength range is defined for unbinned data.

        pysynphot.exceptions.DisjointError
            Wavelength range does not overlap with observation.

        pysynphot.exceptions.PartialOverlap
            Wavelength range only partially overlaps with observation.

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
                raise exceptions.DisjointError("%s is disjoint from obs.binwave %s"%(range,
                                                                       [self.binwave[0],self.binwave[-1]]))
            #Partial overlap
            else:

                if range[0] < self._bin_edges[0]:
                    warn=True
                    lx=None
                else:
                    lx=np.searchsorted(self._bin_edges,range[0])-1

                if range[1] > self._bin_edges[-1]:
                    warn=True
                    ux=None
                else:
                    ux=np.searchsorted(self._bin_edges,range[1])


            ans = math.fsum(self.binflux[lx:ux])
            if warn and not force:
                raise exceptions.PartialOverlap("%s does not fully overlap binwave range %s. Countrate in overlap area is %f"%(range,[self.binwave[0],self.binwave[-1]],ans))

        else:
            if range is None:
                ans = math.fsum(self.flux)
            else:
                raise NotImplementedError("Sorry, range+binned=False not yet implemented")
        self.convert(myfluxunits)
        return ans

    def effstim(self,fluxunits='photlam'):
        """Compute :ref:`effective stimulus <pysynphot-formula-effstim>`.

        Calculations are done in given flux unit, and wavelengths
        in Angstrom. Native dataset is used.

        Parameters
        ----------
        fluxunits : str
            Flux unit.

        Returns
        -------
        ans : float
            Effective stimulus.

        Raises
        ------
        ValueError
            Invalid integrated flux.

        """
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
        if np.isnan(totalflux):
            raise ValueError('Integrated flux is NaN')
        if np.isinf(totalflux):
            raise ValueError('Integrated flux is infinite')


    def pivot(self,binned=True):
        """Calculate :ref:`pivot wavelength <pysynphot-formula-pivwv>`
        of the observation.

        .. note::

            This is the calculation performed when ETC invokes ``calcphot``.

        Parameters
        ----------
        binned : bool
            Use binned dataset for calculations. Otherwise, use native dataset.

        Returns
        -------
        ans : float
            Pivot wavelength.

        """
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
        """Calculate :ref:`effective wavelength <pysynphot-formula-efflam>`
        of the observation.
        Calculation is done in the flux unit of ``flam``.

        .. note::

            Similar to IRAF STSDAS SYNPHOT ``efflphot`` task.

        Parameters
        ----------
        binned : bool
            Use binned dataset for calculations. Otherwise, use native dataset.

        Returns
        -------
        ans : float
            Effective wavelength.

        """
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
        """Sample the observation at the given wavelength.
        Also see :ref:`pysynphot-command-sample`.

        Parameters
        ----------
        swave : float
            Wavelength to sample.

        binned : bool
            Sample binned dataset (no interpolation).
            Otherwise, native (perform interpolation).

        fluxunits : {'counts'}
            Only the unit of counts is supported for now.

        Returns
        -------
        ans : float
            Sampled flux in given unit.

        Raises
        ------
        NotImplementedError
            Flux unit is not supported or non-scalar wavelength is given.

        ValueError
            Given wavelength out of range.

        """
        if self._binflux is None:
          self.initbinflux()

        if fluxunits != 'counts':
            s = "Sorry, only counts are supported at this time"
            raise NotImplementedError(s)
        else:
            #Save current fluxunits, in case they're different
            saveunits = None
            if not units.ismatch('counts', self.fluxunits):
                saveunits = self.fluxunits
                self.convert('counts')


        if binned:
            #Then we don't interpolate, just return the appropriate values
            #from binflux
            if np.isscalar(swave):
                #Find the bin in which it belongs.
                #_bin_edge[i] is the low edge of the bin centered
                #at binwave[i].

                idx = np.where(swave >= self._bin_edges)[0]
                #idx[-1] is the largest edge that is still smaller
                #than swave
                try:
                    ans = self.binflux[idx[-1]]
                except IndexError:
                    s = 'Value out of range: wavelength %g not contained in range [%g, %g]'
                    s = s % (swave, self.binwave[0], self.binwave[-1])
                    raise ValueError(s)

            else:
                #The logic for this case doesn't yet work on arrays
                s = "Sorry, only scalar samples are supported at this time"
                raise NotImplementedError(s)

        else:
            #Then we do interpolate on wave/flux
            if np.isscalar(swave):
                delta = 0.00001
                wv = np.array([swave - delta, swave, swave + delta])
                ans = np.interp(wv, self.wave, self.flux)[1]
            else:
                # This raises UnboundLocalError -- needs to be fixed!
                ans = np.interp(wv, self.wave, self.flux)


        #Change units back, if necessary, then return
        if saveunits is not None:
            self.convert(saveunits)
        return ans

    def pixel_range(self, waverange, waveunits=None, round='round'):
        """Calculate the number of wavelength bins within given
        wavelength range.

        .. note::

            This calls :func:`pysynphot.obsbandpass.pixel_range` with
            ``self.binwave`` as the first argument.

        Parameters
        ----------
        waverange, round
            See :func:`pysynphot.obsbandpass.pixel_range`.

        waveunits : str, optional
            The unit of the wavelength range.
            If `None` (default), the wavelengths are assumed to be
            in the units of ``self.waveunits``.

        Returns
        -------
        num : int or float
            Number of wavelength bins within ``waverange``.

        Raises
        ------
        pysynphot.exceptions.UndefinedBinset
            No binned dataset.

        """
        # make sure we have a binset to work with
        if self.binwave is None:
            raise exceptions.UndefinedBinset('No binset specified for this bandpass.')

        # start by converting waverange to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)

            if not isinstance(waverange, np.ndarray):
                waverange = np.array(waverange)

            # convert to angstroms and then whatever self.waveunits is
            waverange = waveunits.ToAngstrom(waverange)

            waverange = units.Angstrom().Convert(waverange, self.waveunits.name)

        return pixel_range(self.binwave, waverange, round=round)

    def wave_range(self, cenwave, npix, waveunits=None, round='round'):
        """Calculate the wavelength range covered by the given
        number of pixels, centered on the given wavelength.

        .. note::

            This calls :func:`pysynphot.obsbandpass.wave_range` with
            ``self.binwave`` as the first argument.

        Parameters
        ----------
        cenwave, npix, round
            See :func:`pysynphot.obsbandpass.wave_range`.

        waveunits : str, optional
            Wavelength unit of the given and the returned wavelength values.
            If `None` (default), the wavelengths are assumed to be in
            the unit of ``self.waveunits``.

        Returns
        -------
        waverange : tuple of floats
            The range of wavelengths spanned by ``npix`` centered on
            ``cenwave``.

        Raises
        ------
        pysynphot.exceptions.UndefinedBinset
            No binned dataset.

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
        """Reduce the observation to a simple spectrum object.

        An observation is a complex object with some restrictions on its
        capabilities. At times, it would be useful to work with the
        simulated observation as a simple object that is easier to
        manipulate and takes up less memory.

        Parameters
        ----------
        binned : bool
            If `True` (default), export binned dataset. Otherwise, native.

        Returns
        -------
        result : `~pysynphot.spectrum.ArraySourceSpectrum`
            Observation dataset as a simple spectrum object.

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
