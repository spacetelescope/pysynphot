"""This module handle bandpass of observation modes."""
from __future__ import division, print_function
import numpy as np

from .observationmode import ObservationMode
from .spectrum import CompositeSpectralElement, TabularSpectralElement
from . import units
from . import exceptions


def ObsBandpass(obstring, graphtable=None, comptable=None, component_dict={}):
    """Generate a bandpass object from observation mode.

    If the bandpass consists of multiple throughput files
    (e.g., "acs,hrc,f555w"), then `ObsModeBandpass` is returned.
    Otherwise, if it consists of a single throughput file
    (e.g., "johnson,v"), then `~pysynphot.spectrum.TabularSpectralElement`
    is returned.

    See :ref:`pysynphot-obsmode-bandpass` and :ref:`pysynphot-appendixb`
    for more details.

    Parameters
    ----------
    obstring : str
        Observation mode.

    graphtable, comptable, component_dict
        See `~pysynphot.observationmode.ObservationMode`.

    Returns
    -------
    bp : `~pysynphot.spectrum.TabularSpectralElement` or `ObsModeBandpass`

    Examples
    --------
    >>> bp1 = S.ObsBandpass('acs,hrc,f555w')
    >>> bp2 = S.ObsBandpass('johnson,v')

    """
    ##Temporarily create an Obsmode to determine whether an
    ##ObsModeBandpass or a TabularSpectralElement will be returned.
    ob=ObservationMode(obstring,graphtable=graphtable,
                       comptable=comptable,component_dict=component_dict)
    if len(ob) > 1:
        return ObsModeBandpass(ob)
    else:
        return TabularSpectralElement(ob.components[0].throughput_name)


class ObsModeBandpass(CompositeSpectralElement):
    """Bandpass instantiated from an ``obsmode`` string.
    Also see :ref:`pysynphot-obsmode-bandpass`, :ref:`pysynphot-appendixb`,
    and :ref:`pysynphot-appendixc`.

    Parameters
    ----------
    ob : str
        Observation mode.

    Attributes
    ----------
    obsmode, name
        Same as input ``ob``.

    component1, component2 : `CompositeSpectralElement` or `SpectralElement`
        Components and sub-components that belong to the observation mode.

    isAnalytic : bool
        This is always `False`.

    warnings : dict
        To store warnings, which are inherited from all inputs. If they have the same warning keyword, the one from most recently read component is used.

    primary_area : float
        See :ref:`pysynphot-area` for how this is set.

    binset : array_like
        This is set with :meth:`~pysynphot.observationmode.BaseObservationMode.bandWave`, as described in :ref:`pysynphot-refdata`.

    waveunits : `~pysynphot.units.Units`
        User unit inherited from inputs, where all inputs are required to have the same unit or an exception will be raised.

    throughputunits : `None`
        This is only to inform user that throughput is unitless.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless throughput.

    Raises
    ------
    NotImplementedError
        Inputs have different wavelength units.

    TypeError
        Both input spectra must be bandpasses.

    pysynphot.exceptions.IncompatibleSources
        Input spectra have different telescope areas defined.

    """
    # Instantiate a COmpositeSpectralElement by means of an
    # ObservationMode (which the caller must have already created from
    # an  obstring
    def __init__(self,ob):
        #Chain the individual components
        chain=ob.components[0].throughput*ob.components[1].throughput

        for i in range(2,len(ob)-1):
            chain = chain*ob.components[i].throughput

        CompositeSpectralElement.__init__(self,chain,
                                          ob.components[-1].throughput)


        self.obsmode = ob
        self.name = self.obsmode._obsmode #str(self.obsmode)
        self.primary_area = ob.primary_area

        #Check for valid bounds
        self._checkbounds()

        try:
            self.binset = self.obsmode.bandWave()
        except AttributeError:
            # this is to catch an error raised when the self.obsmode object does not
            # have a binset attribute because of some problem with the obsmode
            # used to instatiate it.
            pass

    def __str__(self):
        """Defer to ObservationMode component """
        return self.name #self.obsmode._obsmode

    def __len__(self):
        """Defer to ObservationMode component """
        return len(self.obsmode)

    def showfiles(self):
        """Same as
        :meth:`pysynphot.observationmode.BaseObservationMode.showfiles`.

        """
        return self.obsmode.showfiles()

    def _checkbounds(self):
        thru=self.throughput
        if thru[0] != 0 or thru[-1] != 0:
            print("Warning: throughput for this obsmode is not bounded by zeros. Endpoints: thru[0]=%g, thru[-1]=%g"%(thru[0],thru[-1]))

    def thermback(self):
        """Calculate thermal background count rate for ``self.obsmode``.

        Calculation uses
        :func:`~pysynphot.observationmode.ObservationMode.ThermalSpectrum`
        to extract thermal component source spectrum in
        ``photlam`` per square arcsec. Then this spectrum is
        integrated and multiplied by detector pixel scale
        and telescope collecting area to produce a count rate
        in count/s/pix. This unit is non-standard but used widely
        by STScI Exposure Time Calculator.

        .. note::

            Similar to IRAF STSDAS SYNPHOT ``thermback`` task.

        Returns
        -------
        ans : float
            Thermal background count rate.

        Raises
        ------
        NotImplementedError
            Bandpass has no thermal information in graph table.

        """
        #The obsmode.ThermalSpectrum method will raise an exception if there is
        #no thermal information, and that will just propagate up.
        sp=self.obsmode.ThermalSpectrum()

        #Thermback is always provided in this non-standard set of units.
        #This code was copied from etc.py.
        ans = sp.integrate() * (self.obsmode.pixscale**2 *
                                self.obsmode.primary_area)
        return ans

    def pixel_range(self, waverange, waveunits=None, round='round'):
        """Returns the number of wavelength bins within ``waverange``.

        .. note::

            This calls :func:`pixel_range` with ``self.binset`` as
            the first argument.

        Parameters
        ----------
        waverange, round
            See :func:`pixel_range`.

        waveunits : str, optional
            The units of the wavelengths given in ``waverange``.
            If `None` (default), the wavelengths are assumed to be
            in the units of ``self.waveunits``.

        Returns
        -------
        num : int or float
            Number of wavelength bins within ``waverange``.

        Raises
        ------
        pysynphot.exceptions.UndefinedBinset
            If ``self.binset`` is `None`.

        """
        # make sure we have a binset to work with
        if self.binset is None:
            raise exceptions.UndefinedBinset('No binset specified for this bandpass.')

        # start by converting waverange to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)

            if not isinstance(waverange,np.ndarray):
                waverange = np.array(waverange)

            # convert to angstroms and then whatever self.waveunits is
            waverange = waveunits.ToAngstrom(waverange)

            waverange = units.Angstrom().Convert(waverange, self.waveunits.name)

        return pixel_range(self.binset, waverange, round=round)

    def wave_range(self, cenwave, npix, waveunits=None, round='round'):
        """Get the wavelength range covered by the given number of pixels
        centered on the given wavelength.

        .. note::

           This calls :func:`wave_range` with ``self.binset``
           as the first argument.

        Parameters
        ----------
        cenwave, npix, round
            See :func:`wave_range`.

        waveunits : str, optional
            Wavelength units of ``cenwave`` and the returned wavelength range.
            If `None` (default), the wavelengths are assumed to be in
            the units of ``self.waveunits``.

        Returns
        -------
        waverange : tuple of floats
            The range of wavelengths spanned by ``npix`` centered on
            ``cenwave``.

        Raises
        ------
        pysynphot.exceptions.UndefinedBinset
            If ``self.binset`` is None.

        """
        # make sure we have a binset to work with
        if self.binset is None:
            raise exceptions.UndefinedBinset('No binset specified for this bandpass.')

        # convert cenwave from waveunits to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)

            # convert to angstroms and then whatever self.waveunits is
            cenwave = waveunits.ToAngstrom(cenwave)
            cenwave = units.Angstrom().Convert(cenwave, self.waveunits.name)

        wave1, wave2 = wave_range(self.binset, cenwave, npix, round=round)

        # translate ends to waveunits, if necessary
        if waveunits is not None:
            # convert to angstroms
            wave1 = self.waveunits.ToAngstrom(wave1)
            wave2 = self.waveunits.ToAngstrom(wave2)

            # then to waveunits
            wave1 = units.Angstrom().Convert(wave1, waveunits.name)
            wave2 = units.Angstrom().Convert(wave2, waveunits.name)

        return wave1, wave2


def pixel_range(bins, waverange, round='round'):
    """Returns the number of wavelength bins within ``waverange``.

    Parameters
    ----------
    bins : ndarray
        Wavelengths of pixel centers.
        Must be in the same units as ``waverange``.

    waverange : array_like
        A sequence containing the wavelength range of interest. Only the
        first and last elements are used. Assumed to be in increasing order.
        Must be in the same units as ``bins``.

    round : {'round', 'min', 'max', `None`}, optional
        How to deal with pixels at the edges of the wavelength range. All
        of the options, except `None`, will return an integer number of pixels.
        Defaults to ``'round'``.

            * ``'round'`` - Wavelength ends that fall in the middle of a
              pixel are counted if more than half of the pixel is within
              ``waverange``. Ends that fall in the center of a pixel are
              rounded up to the nearest pixel edge.
            * ``'min'`` - Only pixels wholly within ``waverange`` are counted.
            * ``'max'`` - End pixels that are within ``waverange`` by any
              margin are counted.
            * `None` - The exact number of encompassed pixels, including
              fractional pixels, is returned.

    Returns
    -------
    num : int or float
        Number of wavelength bins within ``waverange``.

    Raises
    ------
    ValueError
        If ``round`` is not an allowed value.

    pysynphot.exceptions.OverlapError
        If ``waverange`` exceeds the bounds of ``bins``.

    """
    # make sure that the round keyword is valid
    if round not in ('round','min','max',None):
        raise ValueError("round keyword must be one of ('round','ciel','floor',None)")

    wave1 = waverange[0]
    wave2 = waverange[-1]

    # make sure the specified waverange is within our .binset
    minwave = bins[0] - (bins[0:2].mean() - bins[0])
    if wave1 < minwave:
        raise exceptions.OverlapError("Lower bound of waverange is outside of binset. Min = %f" % minwave)

    maxwave = bins[-1] + (bins[-1] - bins[-2:].mean())
    if wave2 > maxwave:
        raise exceptions.OverlapError("Upper bound of waverange is outside of binset. Max = %f" % maxwave)

    # if the wavelength ends are the same return 0
    if wave1 == wave2:
        return 0

    # find where the wavelength endpoints fall.
    if round == 'round':
        ind1 = bins.searchsorted(wave1, side='right')
        ind2 = bins.searchsorted(wave2, side='right')

        num = ind2 - ind1

    elif round == 'min':
        ind1 = bins.searchsorted(wave1, side='left')
        ind2 = bins.searchsorted(wave2, side='left')

        # for ind1, figure out if pixel ind1 is wholly included or not.
        # do this by figuring out where wave1 is between ind1 and ind1-1.
        frac = (bins[ind1] - wave1) / (bins[ind1] - bins[ind1-1])

        if frac < 0.5:
            # ind1 is only partially included
            ind1 += 1

        # similar but reversed procedure for ind2
        frac = (wave2 - bins[ind2-1]) / (bins[ind2] - bins[ind2-1])

        if frac < 0.5:
            # ind2 is only partially included
            ind2 -= 1

        num = ind2 - ind1

    elif round == 'max':
        ind1 = bins.searchsorted(wave1, side='left')
        ind2 = bins.searchsorted(wave2, side='left')

        # for ind1, figure out if pixel ind1-1 is partially included or not.
        # do this by figuring out where wave1 is between ind1 and ind1-1.
        frac = (wave1 - bins[ind1-1]) / (bins[ind1] - bins[ind1-1])

        if frac < 0.5:
            # ind1 is partially included
            ind1 -= 1

        # similar but reversed procedure for ind2
        frac = (bins[ind2] - wave2) / (bins[ind2] - bins[ind2-1])

        if frac < 0.5:
            # ind2 is partially included
            ind2 += 1

        num = ind2 - ind1

    elif round is None:
        ind1 = bins.searchsorted(wave1, side='left')
        ind2 = bins.searchsorted(wave2, side='left')

        # calculate fractional indices
        frac1 = ind1 - (bins[ind1] - wave1) / (bins[ind1] - bins[ind1-1])

        frac2 = ind2 - (bins[ind2] - wave2) / (bins[ind2] - bins[ind2-1])

        num = frac2 - frac1

    return num


def wave_range(bins, cenwave, npix, round='round'):
    """Get the wavelength range covered by the given number of pixels
    centered on the given wavelength.

    Parameters
    ----------
    bins : ndarray
        Wavelengths of pixel centers. Must be in the same units as
        ``cenwave``.

    cenwave : float
        Central wavelength of range. Must be in the same units as ``bins``.

    npix : int
        Number of pixels in range, centered on ``cenwave``.

    round : {'round', 'min', 'max', `None`}, optional
        How to deal with pixels at the edges of the wavelength range. All
        of the options, except `None`, will return wavelength ends that
        correpsonds to pixel edges. Defaults to ``'round'``.

            * ``'round'`` - A wavelength range is returned such that the
              ends are pixel edges and the range spans exactly ``npix`` pixels.
              Ends that fall in the center of bins are rounded up to the nearest
              pixel edge.
            * ``'min'`` - The returned wavelength range is shrunk so that
              it includes an integer number of pixels and the ends fall on pixel
              edges. May not span exactly ``npix`` pixels.
            * ``'max'`` - The returned wavelength range is expanded so that
              it includes an integer number of pixels and the ends fall on pixel
              edges. May not span exactly ``npix`` pixels.
            * `None` - An exact wavelength range is returned.
              The wavelength ends returned may not correspond to pixel edges,
              but will cover exactly ``npix`` pixels.

    Returns
    -------
    waverange : tuple of floats
        The range of wavelengths spanned by ``npix`` centered on ``cenwave``.

    Raises
    ------
    ValueError
        If ``round`` is not an allowed value.

    pysynphot.exceptions.OverlapError
        If ``cenwave`` is not within ``bins``, or the returned ``waverange``
        would exceed the limits of ``bins``.

    """
    # make sure that the round keyword is valid
    if round not in (None,'round','min','max'):
        raise ValueError("round keyword must be one of (None,'round','min','max')")

    # make sure cenwave is within binset
    if cenwave < bins[0]:
        raise exceptions.OverlapError("cenwave is not within binset. Min = %f" % bins[0])
    elif cenwave > bins[-1]:
        raise exceptions.OverlapError("cenwave is not within binset. Max = %f" % bins[-1])

    # first figure out what index the central wavelength falls at
    diff = cenwave - bins
    ind = np.where(np.abs(diff) == np.abs(diff).min())[0][0]

    # now figure out the fractional index
    if diff[ind] < 0:
        frac_ind = float(ind) + diff[ind] / (bins[ind] - bins[ind-1])
    elif diff[ind] > 0:
        frac_ind = float(ind) + diff[ind] / (bins[ind+1] - bins[ind])
    else:
        frac_ind = float(ind)

    # then figure out the fractional indices of the ends
    frac_ind1 = frac_ind - npix/2.
    frac_ind2 = frac_ind + npix/2.

    # check ends
    if frac_ind1 < -0.5:
        raise exceptions.OverlapError("Lower wavelength range is below allowed binset.")

    if frac_ind2 > bins.shape[0] - 0.5:
        raise exceptions.OverlapError("Upper wavelength range is above allowed binset.")

    frac1, int1 = np.modf(frac_ind1)
    frac2, int2 = np.modf(frac_ind2)

    # translate ends to wavelength
    if round is None:
        # translate ends directly to wavelength without regard to bin edges
        f, i = frac1, int(int1)

        wave1 = bins[i] + frac1 * (bins[i+1] - bins[i])

        f, i = frac2, int(int2)

        wave2 = bins[i] + frac2 * (bins[i+1] - bins[i])

    elif round == 'round':
        # calculate lower end of wavelength range
        f, i = frac1, int(int1)

        if f >= 0:
            # end is somewhere greater than binset[0] so we can just
            # interpolate between two neighboring values going with upper edge
            wave1 = bins[i:i+2].mean()
        else:
            # end is below the lowest binset value, but not by enough to
            # trigger an exception
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])

        # calculate upper end of wavelength range
        f, i = frac2, int(int2)

        if i < bins.shape[0] - 1:
            # end is somewhere below binset[-1] so we can just interpolate
            # between two neighboring values, going with the upper edge.
            wave2 = bins[i:i+2].mean()
        else:
            # end is above highest binset value but not by enough to
            # trigger an exception
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())

    elif round == 'min':
        # calculate lower end of wavelength range
        f, i = frac1, int(int1)

        if f <= 0.5 and i < bins.shape[0] - 1:
            # not at the lowest possible edge and pixel i included
            wave1 = bins[i:i+2].mean()
        elif f > 0.5 and i < bins.shape[0] - 2:
            # not at the lowest possible edge and pixel i not included
            wave1 = bins[i+1:i+3].mean()
        elif f == -0.5:
            # at the lowest possible edge
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])

        # calculate upper end of wavelength range
        f, i = frac2, int(int2)

        if f >= 0.5 and i < bins.shape[0] - 1:
            # not out at the end and pixel i included
            wave2 = bins[i:i+2].mean()
        elif f < 0.5 and i < bins.shape[0]:
            # not out at end and pixel i not included
            wave2 = bins[i-1:i+1].mean()
        elif f == 0.5 and i == bins.shape[0] - 1:
            # at the very end
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())

    elif round == 'max':
        # calculate lower end of wavelength range
        f, i = frac1, int(int1)

        if f < 0.5 and i < bins.shape[0]:
            # not at the lowest possible edge and pixel i included
            wave1 = bins[i-1:i+1].mean()
        elif f >= 0.5 and i < bins.shape[0] - 1:
            # not at the lowest possible edge and pixel i not included
            wave1 = bins[i:i+2].mean()
        elif f == -0.5:
            # at the lowest possible edge
            wave1 = bins[0] - (bins[0:2].mean() - bins[0])

        # calculate upper end of wavelength range
        f, i = frac2, int(int2)

        if f > 0.5 and i < bins.shape[0] - 2:
            # not out at the end and pixel i included
            wave2 = bins[i+1:i+3].mean()
        elif f <= 0.5 and i < bins.shape[0] - 1:
            # not out at end and pixel i not included
            wave2 = bins[i:i+2].mean()
        elif f == 0.5 and i == bins.shape[0] - 1:
            # at the very end
            wave2 = bins[-1] + (bins[-1] - bins[-2:].mean())

    return wave1, wave2
