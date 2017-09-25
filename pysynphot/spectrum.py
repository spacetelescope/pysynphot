"""This module contains the basis for all spectra classes,
including source spectra and bandpasses.

It also pre-loads the built-in :ref:`pysynphot-vega-spec` spectrum to
``pysynphot.spectrum.Vega``.

"""
from __future__ import absolute_import, division, print_function

import re
import os
import math
import warnings

from astropy.io import fits as pyfits
from astropy.utils.data import get_file_contents
import numpy as N

from . import refs
from . import units
from . import locations
from . import planck
import pysynphot.exceptions as exceptions  # custom pysyn exceptions

try:
    from pysynphot import __version__
except ImportError:
    __version__ = 'unk'

try:
    from pysynphot import __svn_revision__
except ImportError:
    __svn_revision__ = 'unk'

# Renormalization constants from synphot:
PI = 3.14159265               # Mysterious math constant
RSUN = 6.9599E10              # Radius of sun
PC = 3.085678E18              # Parsec
RADIAN = RSUN / PC / 1000.
RENORM = PI * RADIAN * RADIAN  # Normalize to 1 solar radius @ 1 kpc

# MergeWaveSets "too close together" constant
MERGETHRESH = 1.e-12

# Single-precision epsilon value, taken from the synphot FAQ.
# This is the minimum separation in wavelength value necessary for
# synphot to read the entries as distinct single-precision numbers.
syn_epsilon = 0.00032


def MergeWaveSets(waveset1, waveset2):
    """Return the union of the two wavelength sets.

    The union is computed using `numpy.union1d`, unless one or
    both of them is `None`.

    The merged result may sometimes contain numbers which are nearly
    equal but differ at levels as small as 1E-14. Having values this
    close together can cause problems due to effectively duplicate
    wavelength values. Therefore, wavelength values having differences
    smaller than or equal to ``pysynphot.spectrum.MERGETHRESH``
    (defaults to 1E-12) are considered as the same.

    Parameters
    ----------
    waveset1, waveset2 : array_like or `None`
        Wavelength sets to combine.

    Returns
    -------
    MergedWaveSet : array_like or `None`
        Merged wavelength set. It is `None` if both inputs are such.

    """
    if waveset1 is None and waveset2 is not None:
        MergedWaveSet = waveset2
    elif waveset2 is None and waveset1 is not None:
        MergedWaveSet = waveset1
    elif waveset1 is None and waveset2 is None:
        MergedWaveSet = None
    else:
        MergedWaveSet = N.union1d(waveset1, waveset2)

        # The merged wave sets may sometimes contain numbers which are nearly
        # equal but differ at levels as small as 1e-14. Having values this
        # close together can cause problems down the line so here we test
        # whether any such small differences are present, with a small
        # difference defined as less than MERGETHRESH.
        #
        # If small differences are present we make a copy of the union'ed array
        # with the lower of the close together pairs removed.
        delta = MergedWaveSet[1:] - MergedWaveSet[:-1]

        if not (delta > MERGETHRESH).all():
            newlen = len(delta[delta > MERGETHRESH]) + 1
            newmerged = N.zeros(newlen, dtype=MergedWaveSet.dtype)
            newmerged[:-1] = MergedWaveSet[:-1][delta > MERGETHRESH]
            newmerged[-1] = MergedWaveSet[-1]

            MergedWaveSet = newmerged

    return MergedWaveSet


def trimSpectrum(sp, minw, maxw):
    """Create a new spectrum with trimmed upper and lower ranges.

    Parameters
    ----------
    sp : `SourceSpectrum`
        Spectrum to trim.

    minw, maxw : number
        Lower and upper limits (inclusive) for the wavelength set
        in the trimmed spectrum.

    Returns
    -------
    result : `TabularSourceSpectrum`
        Trimmed spectrum.

    """
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
    """Integrator engine, which is the base class for
    `SourceSpectrum` and `SpectralElement`.

    """
    def trapezoidIntegration(self, x, y):
        """Perform trapezoid integration.

        Parameters
        ----------
        x : array_like
            Wavelength set.

        y : array_like
            Integrand. For example, throughput or throughput
            multiplied by wavelength.

        Returns
        -------
        sum : float
            Integrated sum.

        """
        npoints = x.size
        if npoints > 0:
            indices = N.arange(npoints)[:-1]
            deltas = x[indices+1] - x[indices]
            integrand = 0.5*(y[indices+1] + y[indices])*deltas
            sum = integrand.sum()
            if x[-1] < x[0]:
                sum *= -1.0
            return sum
        else:
            return 0.0

    def _columnsFromASCII(self, filename):
        """Following synphot/TABLES, ASCII files may contain blank lines,
        comment lines (beginning with '#'), or terminal comments. This routine
        may be called by both Spectrum and SpectralElement objects to extract
        the first two columns from a file."""

        wlist = []
        flist = []
        lcount = 0
        if filename.lower().startswith('ftp://'):
            lines = get_file_contents(filename)
        else:
            with open(filename) as fs:
                lines = fs.readlines()
        for line in lines:
            lcount += 1
            cline = line.strip()
            if ((len(cline) > 0) and (not cline.startswith('#'))):
                try:
                    cols = cline.split()
                    if len(cols) >= 2:
                        wlist.append(float(cols[0]))
                        flist.append(float(cols[1]))
                except Exception as e:
                    raise exceptions.BadRow("Error reading %s: %s" % (
                        filename, str(e)), rows=lcount)

        return wlist, flist

    def validate_wavetable(self):
        """Enforce monotonic, ascending wavelength array with no zero or
        negative values.

        Raises
        ------
        pysynphot.exceptions.DuplicateWavelength
            Wavelength array contains duplicate entries.

        pysynphot.exceptions.UnsortedWavelength
            Wavelength array is not monotonic ascending or descending.

        pysynphot.exceptions.ZeroWavelength
            Wavelength array has zero or negative value(s).

        """
        # First check for invalid values
        wave = self._wavetable
        if N.any(wave <= 0):
            wrong = N.where(wave <= 0)[0]
            raise exceptions.ZeroWavelength(
                'Negative or Zero wavelength occurs in wavelength array',
                rows=wrong)

        # Now check for monotonicity & enforce ascending
        sorted = N.sort(wave)
        if not N.alltrue(sorted == wave):
            if N.alltrue(sorted[::-1] == wave):
                # monotonic descending is allowed
                pass
            else:
                wrong = N.where(sorted != wave)[0]
                raise exceptions.UnsortedWavelength(
                    'Wavelength array is not monotonic', rows=wrong)

        # Check for duplicate values
        dw = sorted[1:] - sorted[:-1]
        if N.any(dw == 0):
            wrong = N.where(dw == 0)[0]
            raise exceptions.DuplicateWavelength(
                "Wavelength array contains duplicate entries", rows=wrong)

    def validate_fluxtable(self):
        """Check for non-negative fluxes.
        If found, the negative flux values are set to zero, and
        a warning is printed to screen. This check is not done
        if flux unit is a magnitude because negative magnitude
        values are legal.

        """
        # neg. magnitudes are legal
        if ((not self.fluxunits.isMag) and (self._fluxtable.min() < 0)):
            idx = N.where(self._fluxtable < 0)
            self._fluxtable[idx] = 0.0
            print("Warning, %d of %d bins contained negative fluxes; they "
                  "have been set to zero." % (
                      len(idx[0]), len(self._fluxtable)))


class SourceSpectrum(Integrator):
    """This is the base class for all
    :ref:`source spectra <pysynphot-spectrum>`.

    """
    def __add__(self, other):
        """Source Spectra can be added.  Delegate the work to the
        CompositeSourceSpectrum class.
        """
        if not isinstance(other, SourceSpectrum):
            raise TypeError("Can only add two SourceSpectrum objects")

        return CompositeSourceSpectrum(self, other, 'add')

    def __sub__(self, other):
        """Source Spectra can be subtracted, which is just another way
        of adding.
        """
        return self.__add__(-1.0*other)

    def __mul__(self, other):
        """Source Spectra can be multiplied, by constants or by
        SpectralElement objects.
        """
        # Multiplying by numeric constants is allowed
        if isinstance(other, (int, float)):
            other = UniformTransmission(other)
        # so is by SpectralElements. Otherwise, raise an exception.
        if not isinstance(other, SpectralElement):
            raise TypeError("SourceSpectrum objects can only be multiplied "
                            "by SpectralElement objects or constants; %s "
                            "type detected" % type(other))

        # Delegate the work of multiplying to CompositeSourceSpectrum
        return CompositeSourceSpectrum(self, other, 'multiply')

    def __rmul__(self, other):
        return self.__mul__(other)

    def addmag(self, magval):
        """Add a scalar magnitude to existing flux values.

        .. math::

            \\textnormal{flux}_{\\textnormal{new}} = 10^{-0.4 \\; \\textnormal{magval}} \\; \\textnormal{flux}

        Parameters
        ----------
        magval : number
            Magnitude value.

        Returns
        -------
        sp : `CompositeSourceSpectrum`
            New source spectrum with adjusted flux values.

        Raises
        ------
        TypeError
            Magnitude value is not a scalar number.

        """
        if N.isscalar(magval):
            factor = 10**(-0.4*magval)
            return self*factor
        else:
            raise TypeError(".addmag() only takes a constant scalar argument")

    def getArrays(self):
        """Return wavelength and flux arrays in user units.

        Returns
        -------
        wave : array_like
            Wavelength array in ``self.waveunits``.

        flux : array_like
            Flux array in ``self.fluxunits``.
            When necessary, ``self.primary_area`` is used for unit conversion.

        """
        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        wave = self.GetWaveSet()
        flux = self(wave)

        flux = units.Photlam().Convert(
            wave, flux, self.fluxunits.name, area=area)
        wave = units.Angstrom().Convert(wave, self.waveunits.name)

        return wave, flux

    # Define properties for consistent UI
    def _getWaveProp(self):
        wave, flux = self.getArrays()
        return wave

    def _getFluxProp(self):
        wave, flux = self.getArrays()
        return flux

    wave = property(_getWaveProp, doc="Wavelength property.")
    flux = property(_getFluxProp, doc="Flux property.")

    def validate_units(self):
        """Ensure that wavelenth and flux units belong to the
        correct classes.

        Raises
        ------
        TypeError
            Wavelength unit is not `~pysynphot.units.WaveUnits` or
            flux unit is not `~pysynphot.units.FluxUnits`.

        """
        if (not isinstance(self.waveunits, units.WaveUnits)):
            raise TypeError("%s is not a valid WaveUnit" % self.waveunits)
        if (not isinstance(self.fluxunits, units.FluxUnits)):
            raise TypeError("%s is not a valid FluxUnit" % self.fluxunits)

    def writefits(self, filename, clobber=True, trimzero=True,
                  binned=False, precision=None, hkeys=None):
        """Write the spectrum to a FITS table.

        Primary header in EXT 0. ``FILENAME``,  ``ORIGIN``, and any
        extra keyword(s) from ``hkeys`` will also be added.

        Table header and data are in EXT 1. The table has 2 columns,
        i.e., ``WAVELENGTH`` and ``FLUX``. Data are stored in user units.
        Its header also will have these additional keywords:

        * ``EXPR`` - Description of the spectrum.
        * ``TDISP1`` and ``TDISP2`` - Columns display format,
          always "G15.7".
        * ``GRFTABLE`` and ``CMPTABLE`` - Graph and component
          table names to use with associated observation mode.
          These are only added if applicable.

        If data is already double-precision but user explicitly
        set output precision to single, ``pysynphot.spectrum.syn_epsilon``
        defines the allowed minimum wavelength separation.
        This limit (:math:`3.2 \\times 10^{-4}`) was taken from
        IRAF STSDAS SYNPHOT FAQ.
        Values equal or smaller than this limit are considered as the
        same, and duplicates are ignored, resulting in data loss.
        In the way that this comparison is coded, when such precision clash
        happens, even when no duplicates are detected, the last row is
        always omitted (also data loss). Therefore, it is *not* recommended
        for user to force single-precision when the data is in
        double-precision.

        Parameters
        ----------
        filename : str
            Output filename.

        clobber : bool
            Overwrite existing file. Default is `True`.

        trimzero : bool
            Trim off duplicate rows with flux values of zero from both ends
            of the spectrum. This keeps one row of zero-flux at each end,
            if it exists; However, it does not add a zero-flux row if it
            does not. Default is `True`.

        binned : bool
            Write ``self.binwave`` and ``self.binflux`` (binned) dataset,
            instead of ``self.wave`` and ``self.flux`` (native). Using
            this option when object does not have binned data will cause
            an exception to be raised. Default is `False`.

        precision : {'s', 'd', `None`}
            Write data out in single (``'s'``) or double (``'d'``)
            precision. Default is `None`, which will enforce native
            precision from ``self.flux``.

        hkeys : dict
            Additional keyword(s) to be added to primary FITS header,
            in the format of ``{keyword:(value,comment)}``.

        """
        pcodes={'d':'D', 's':'E'}
        if precision is None:
            precision = self.flux.dtype.char
        _precision = precision.lower()[0]
        pcodes = {'d':'D','s':'E','f':'E'}

        if clobber:
            try:
                os.remove(filename)
            except OSError:
                pass

        if binned:
            wave = self.binwave
            flux = self.binflux
        else:
            wave = self.wave
            flux = self.flux

        # Add a check for single/double precision clash, so
        # that if written out in single precision, the wavelength table
        # will still be sorted with no duplicates
        # The value of epsilon is taken from the Synphot FAQ.

        if wave.dtype == N.float64 and _precision == 's':
            idx = N.where(abs(wave[1:]-wave[:-1]) > syn_epsilon)
        else:
            idx = N.where(wave) #=> idx=[:]

        wave = wave[idx]
        flux = flux[idx]

        first, last = 0, len(flux)

        if trimzero:
            # Keep one zero at each end
            nz = flux.nonzero()[0]
            try:
                first = max(nz[0] - 1, first)
                last = min(nz[-1] + 2, last)
            except IndexError:
                pass

        # Construct the columns and HDUlist
        cw = pyfits.Column(name='WAVELENGTH',
                           array=wave[first:last],
                           unit=self.waveunits.name,
                           format=pcodes[_precision])
        cf = pyfits.Column(name='FLUX',
                           array=flux[first:last],
                           unit=self.fluxunits.name,
                           format=pcodes[_precision])

        # Make the primary header
        hdu = pyfits.PrimaryHDU()
        hdulist = pyfits.HDUList([hdu])

        # User-provided keys are written to the primary header
        # so are filename and origin
        bkeys = dict(filename=(os.path.basename(filename), 'name of file'),
                     origin=('pysynphot', 'Version (%s, %s)' %
                             (__version__, __svn_revision__)))
        # User-values if present may override default values
        if hkeys is not None:
            bkeys.update(hkeys)

        # Now update the primary header
        for key, val in bkeys.items():
            hdu.header[key] = val

        # Make the extension HDU
        cols = pyfits.ColDefs([cw, cf])
        hdu = pyfits.BinTableHDU.from_columns(cols)

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = dict(expr=(str(self), 'pysyn expression'),
                     tdisp1=('G15.7',),
                     tdisp2=('G15.7',))

        try:
            bkeys['grftable'] = (self.bandpass.obsmode.gtname,)
            bkeys['cmptable'] = (self.bandpass.obsmode.ctname,)
        except AttributeError:
            pass  # Not all spectra have these

        for key, val in bkeys.items():
            hdu.header[key] = val

        # Add the header to the list, and write the file
        hdulist.append(hdu)
        hdulist.writeto(filename)

    def integrate(self, fluxunits='photlam'):
        """Integrate the flux in given unit.

        Integration is done using :meth:`~Integrator.trapezoidIntegration`
        with ``x=wave`` and ``y=flux``, where flux has been
        convert to given unit first.

        .. math::

            \\textnormal{result} = \\int F_{\\lambda} d\\lambda

        Parameters
        ----------
        fluxunits : str
            Flux unit to integrate in.

        Returns
        -------
        result : float
            Integrated sum.

        """
        # Extract the flux in the desired units
        u = self.fluxunits
        self.convert(fluxunits)
        wave, flux = self.getArrays()
        self.convert(u)
        # then do the integration
        return self.trapezoidIntegration(wave, flux)

    def sample(self, wave, interp=True):
        """Sample the spectrum at given wavelength(s).

        This method has two behaviors:

        * When ``interp=True``, wavelength(s) must be provided
          as a Numpy array. Interpolation is done in internal units
          (Angstrom and ``photlam``).
        * When ``interp=False``, wavelength must be a scalar number.
          The flux that corresponds to the closest matching wavelength
          value is returned. This option should only be used for sampling
          binned data in `~pysynphot.observation.Observation`.

        Parameters
        ----------
        wave : number or array_like
            Wavelength(s) to sample, given in user unit.

        interp : bool
            Allow flux interpolation. Default is `True`.

        Returns
        -------
        ans : number or array_like
            Sampled flux in user unit.

        Raises
        ------
        NotImplementedError
            Non-scalar wavelength set provided when interpolation
            is not allowed.

        """
        if interp:
            # convert input wavelengths to Angstroms since the __call__ method
            # will be expecting that
            angwave = self.waveunits.ToAngstrom(wave)

            # First use the __call__ to get it in photlam
            flux = self(angwave)

            if hasattr(self, 'primary_area'):
                area = self.primary_area
            else:
                area = None

            # Then convert to the desired units
            ans = units.Photlam().Convert(angwave, flux,
                                          self.fluxunits.name, area=area)

        else:
            # Get the arrays in the proper units
            wave_array, flux_array = self.getArrays()
            if N.isscalar(wave):
                # Find the correct index
                diff = abs(wave-wave_array)
                idx = diff.argmin()

                ans = flux_array[idx]

            else:
                raise NotImplementedError(
                    "Interp=False not yet supported for non-scalars")

        return ans

    def convert(self, targetunits):
        """Set new user unit, for either wavelength or flux.

        This effectively converts the spectrum wavelength or flux
        to given unit. Note that actual data are always kept in
        internal units (Angstrom and ``photlam``), and only converted
        to user units by :meth:`getArrays` during actual computation.
        User units are stored in ``self.waveunits`` and ``self.fluxunits``.

        Parameters
        ----------
        targetunits : str
            New unit name, as accepted by `~pysynphot.units.Units`.

        """
        nunits = units.Units(targetunits)

        if nunits.isFlux:
            self.fluxunits = nunits
        else:
            self.waveunits = nunits

    def redshift(self, z):
        """Apply :ref:`redshift <pysynphot-redshift>` to the spectrum.

        Redshifted spectrum is never analytic even if the input
        spectrum is. Output units are always Angstrom and PHOTLAM
        regardless of user units.

        Parameters
        ----------
        z : number
            Redshift value.

        Returns
        -------
        copy : `ArraySourceSpectrum`
            Redshifted spectrum.

        """
        # By default, apply only the doppler shift.

        waveunits = self.waveunits
        fluxunits = self.fluxunits
        self.convert('angstrom')
        self.convert('photlam')
        newwave = self.wave.astype(N.float64) * (1.0 + z)
        copy = ArraySourceSpectrum(wave=newwave,
                                   flux=self.flux,
                                   waveunits=self.waveunits,
                                   fluxunits=self.fluxunits,
                                   name="%s at z=%g" % (self.name, z))

        self.convert(waveunits)
        self.convert(fluxunits)
        return copy

    def setMagnitude(self, band, value):
        """Makes the magnitude of the source in the band equal to value.
        band is a SpectralElement.
        This method is marked for deletion once the .renorm method is
        well tested.

        Object returned is a CompositeSourceSpectrum.

        .. warning:: DO NOT USED

        """
        objectFlux = band.calcTotalFlux(self)
        vegaFlux = band.calcVegaFlux()
        magDiff = -2.5*math.log10(objectFlux/vegaFlux)
        factor = 10**(-0.4*(value - magDiff))
        return self * factor

    # Calls a function in another module to alleviate circular import
    # issues.
    def renorm(self, RNval, RNUnits, band, force=False):
        """:ref:`Renormalize <pysynphot-renorm>` the spectrum to the
        specified value, unit, and bandpass.

        This wraps :func:`~pysynphot.renorm.StdRenorm` for convenience.
        Basically, the spectrum is multiplied by a numeric factor so that
        the total integrated flux will be the given value in the given
        unit in the given bandpass.

        When ``force=False``, if spectrum is not fully defined within the
        given bandpass, but the overlap is at least 99%, a warning is
        printed to screen and ``self.warnings['PartialRenorm']`` is set
        to `True`.

        Parameters
        ----------
        RNval : number
            Flux value for renormalization.

        RNUnits : str
            Unit name, as accepted by `~pysynphot.units.Units`, for ``RNval``.

        band : `SpectralElement`
            Bandpass that ``RNval`` is based on.

        force : bool
            Force renormalization regardless of overlap status with given
            bandpass. If `True`, overlap check is skipped. Default is `False`.

        Returns
        -------
        newsp : `~pysynphot.spectrum.CompositeSourceSpectrum`
            Renormalized spectrum.

        Raises
        ------
        ValueError
            Integrated flux is zero, negative, NaN, or infinite.

        pysynphot.exceptions.DisjointError
            Spectrum and bandpass are disjoint.

        pysynphot.exceptions.OverlapError
            Spectrum and bandpass do not fully overlap.

        """
        from .renorm import StdRenorm
        return StdRenorm(self, band, RNval, RNUnits, force=force)

    def effstim(self, fluxunits='photlam'):
        """Not implemented."""
        print("?? %s" % fluxunits)
        raise NotImplementedError(
            "Ticket #140: calcphot.effstim functionality")


class CompositeSourceSpectrum(SourceSpectrum):
    """Class to handle :ref:`composite spectrum <pysynphot-composite-spectrum>`
    involving source spectra.

    Parameters
    ----------
    source1, source2 : `SourceSpectrum` or `SpectralElement`
        One or both of the inputs must be source spectrum.

    operation : {'add', 'multiply'}
        Math operation to perform.

    Attributes
    ----------
    component1, component2
        Same as input ``source1`` and ``source2``.

    operation
        Same as input.

    name : str
        Short description of the spectrum.

    warnings : dict
        To store warnings, which are inherited from both input sources. If inputs have the same warning keyword, the one from ``source2`` is used.

    isAnalytic : bool
        Flag to indicate whether this is an analytic spectrum. This is only `True` if both inputs are analytic.

    primary_area : number or `None`
        :ref:`pysynphot-area` of the telescope. This is inherited from either of the inputs, if available (not `None`). If inputs have different values, an exception is raised.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units inherited from ``source1`` (if available) or ``source2`` (if not).

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    Raises
    ------
    pysynphot.exceptions.IncompatibleSources
        Input spectra have different telescope areas defined.

    """
    def __init__(self, source1, source2, operation):
        self.component1 = source1
        self.component2 = source2
        self.operation = operation

        self.name = str(self)

        # Propagate warnings
        self.warnings = {}
        self.warnings.update(source1.warnings)
        self.warnings.update(source2.warnings)

        # for now we keep these attributes here, in spite of the internal
        # units model. There is code that still breaks down if these attributes
        # are not here.
        try:
            self.waveunits = source1.waveunits
            self.fluxunits = source1.fluxunits
        except AttributeError:
            self.waveunits = source2.waveunits
            self.fluxunits = source2.fluxunits

        self.isAnalytic = source1.isAnalytic and source2.isAnalytic

        # check areas
        if hasattr(source1, 'primary_area'):
            source1_area = source1.primary_area
        else:
            source1_area = None

        if hasattr(source2, 'primary_area'):
            source2_area = source2.primary_area
        else:
            source2_area = None

        if not source1_area and not source2_area:
            self.primary_area = None

        elif source1_area and not source2_area:
            self.primary_area = source1_area

        elif not source1_area and source2_area:
            self.primary_area = source2_area

        else:
            if source1_area == source2_area:
                self.primary_area = source1_area

            else:
                err = ('Components have different area attributes: '
                       '%s: %f, %s: %f')
                err = err % (str(source1), source1_area,
                             str(source2), source2_area)
                raise exceptions.IncompatibleSources(err)

    def __str__(self):
        opdict = {'add': '+', 'multiply': '*'}
        return "%s %s %s" % (str(self.component1), opdict[self.operation],
                             str(self.component2))

    def __call__(self, wavelength):
        """Add or multiply components, delegating the function calculation
        to the individual objects.
        """
        if self.operation == 'add':
            return self.component1(wavelength) + self.component2(wavelength)

        if self.operation == 'multiply':
            return self.component1(wavelength) * self.component2(wavelength)

    def __iter__(self):
        """Allow iteration over each component."""
        complist = self.complist()
        return complist.__iter__()

    def complist(self):
        """Return a list of all components and sub-components.
        This is for use with :py:meth:`~object.__iter__`.

        """
        ans = []
        for comp in (self.component1, self.component2):
            try:
                ans.extend(comp.complist())
            except AttributeError:
                ans.append(comp)
        return ans

    def GetWaveSet(self):
        """Obtain the wavelength set for the composite spectrum.
        This is done by using :func:`MergeWaveSets` to form a union of
        wavelength sets from its components.

        Returns
        -------
        waveset : array_like
            Composite wavelength set.

        """
        waveset1 = self.component1.GetWaveSet()
        waveset2 = self.component2.GetWaveSet()
        return MergeWaveSets(waveset1, waveset2)

    def tabulate(self):
        """Return a simplified version of the spectrum.

        Composite spectrum can be overly complicated when it
        has too many components and sub-components. This method
        copies the following into a simple (tabulated) source spectrum:

        * Name
        * Wavelength array and unit
        * Flux array and unit

        Returns
        -------
        sp : `ArraySourceSpectrum`
            Tabulated source spectrum.

        """
        sp = ArraySourceSpectrum(wave=self.wave,
                                 flux=self.flux,
                                 waveunits=self.waveunits,
                                 fluxunits=self.fluxunits,
                                 name='%s (tabulated)' % self.name)
        return sp


class TabularSourceSpectrum(SourceSpectrum):
    """Base class for `ArraySourceSpectrum` and `FileSourceSpectrum`.

    Parameters
    ----------
    filename : str or `None`
        File with spectral data (can be ASCII or FITS). If not `None`,
        data will be loaded from file at initialization.

    fluxname : str or `None`
        Column name containing flux data. This is only used if filename
        is given and is of FITS format.

    keepneg : bool
        Keep negative flux values instead of setting them to zero with
        a warning. Default is `False`.

    Attributes
    ----------
    filename, name
        Same as input.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    """
    def __init__(self, filename=None, fluxname=None, keepneg=False):
        self.isAnalytic = False
        self.warnings = {}
        if filename:
            self._readSpectrumFile(filename, fluxname)
            self.filename = filename
            self.validate_units()
            self.validate_wavetable()
            if not keepneg:
                self.validate_fluxtable()
            self.ToInternal()
            self.name = self.filename
            self.isAnalytic = False
        else:
            self._wavetable = None
            self._fluxtable = None
            self.waveunits = None
            self.fluxunits = None
            self.filename = None
            self.name = self.filename

    def _reverse_wave(self):
        self._wavetable = self._wavetable[::-1]

    def __str__(self):
        return str(self.name)

    def _readSpectrumFile(self, filename, fluxname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, fluxname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, fluxname):
        fs = pyfits.open(filename)

        # pyfits cannot close the file on .close() if there are still
        # references to mmapped data
        self._wavetable = fs[1].data.field('wavelength').copy()
        if fluxname is None:
            fluxname = 'flux'
        self._fluxtable = fs[1].data.field(fluxname).copy()

        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.fluxunits = units.Units(fs[1].header['tunit2'].lower())

        fs.close()

    def _readASCII(self, filename):
        """ASCII files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is flux in Flam.

        """
        self.waveunits = units.Units('angstrom')
        self.fluxunits = units.Units('flam')
        wlist, flist = self._columnsFromASCII(filename)
        self._wavetable = N.array(wlist, dtype=N.float64)
        self._fluxtable = N.array(flist, dtype=N.float64)

    def __call__(self, wavelengths):
        """This is where the flux array is actually calculated given a
        wavelength array. Returns an array of flux values calculated at
        the wavelength values input.

        """
        if N.isscalar(wavelengths):
            delta = 0.0001
            ww = N.array([wavelengths - delta, wavelengths,
                          wavelengths + delta])
            tmp = self.resample(ww)
            return tmp._fluxtable[1]
        else:
            return self.resample(wavelengths)._fluxtable

    def taper(self):
        """Taper the spectrum by adding zero flux to each end.
        This is similar to :meth:`SpectralElement.taper`.

        There is no check to see if the spectrum is already tapered.
        Hence, calling this on a tapered spectrum will result in
        multiple zero-flux entries at both ends.

        The wavelengths to use for the new first and last points are
        calculated by using the same ratio as for the two interior points
        used at each end.

        Returns
        -------
        OutSpec : `TabularSourceSpectrum`
            Tapered spectrum.

        """
        OutSpec = TabularSourceSpectrum()
        wcopy = N.zeros(self._wavetable.size+2, dtype=N.float64)
        fcopy = N.zeros(self._fluxtable.size+2, dtype=N.float64)
        wcopy[1:-1] = self._wavetable
        fcopy[1:-1] = self._fluxtable
        fcopy[0] = 0.0
        fcopy[-1] = 0.0

        # The wavelengths to use for the first and last points are
        # calculated by using the same ratio as for the 2 interior points
        wcopy[0] = wcopy[1]*wcopy[1]/wcopy[2]
        wcopy[-1] = wcopy[-2]*wcopy[-2]/wcopy[-3]

        OutSpec._wavetable = wcopy
        OutSpec._fluxtable = fcopy
        OutSpec.waveunits = units.Units(str(self.waveunits))
        OutSpec.fluxunits = units.Units(str(self.fluxunits))

        return OutSpec

    def resample(self, resampledWaveTab):
        """Resample the spectrum for the given wavelength set.

        Given wavelength array must be monotonically increasing
        or decreasing. Flux interpolation is done using :func:`numpy.interp`.

        Parameters
        ----------
        resampledWaveTab : array_like
            Wavelength set for resampling.

        Returns
        -------
        resampled : `ArraySourceSpectrum`
            Resampled spectrum.

        """
        # Check whether the input wavetab is in descending order
        if resampledWaveTab[0] < resampledWaveTab[-1]:
            newwave = resampledWaveTab
            newasc = True
        else:
            newwave = resampledWaveTab[::-1]
            newasc = False

        # Use numpy interpolation function
        if self._wavetable[0] < self._wavetable[-1]:
            oldasc = True
            ans = N.interp(newwave, self._wavetable, self._fluxtable)
        else:
            oldasc = False
            rev = N.interp(newwave, self._wavetable[::-1],
                           self._fluxtable[::-1])
            ans = rev[::-1]

        # If the new and old waveset don't have the same parity,
        # the answer has to be flipped again
        if (newasc != oldasc):
            ans = ans[::-1]

        # Finally, make the new object
        # NB: these manipulations were done using the internal
        # tables in Angstrom and photlam, so those are the units
        # that must be fed to the constructor.
        resampled = ArraySourceSpectrum(wave=resampledWaveTab.copy(),
                                        waveunits='angstroms',
                                        flux=ans.copy(),
                                        fluxunits='photlam',
                                        keepneg=True)

        # Use the convert method to set the units desired by the user.
        resampled.convert(self.waveunits)
        resampled.convert(self.fluxunits)

        return resampled

    def GetWaveSet(self):
        """Return the wavelength set for the spectrum.

        Returns
        -------
        waveset : array_like
            Wavelength set (a copy of the internal wavelength table).

        """
        # For a TabularSource Spectrum, the WaveSet is just the _wavetable
        # member.  Return a copy so that there is no reference to the original
        # object.
        return self._wavetable.copy()

    def ToInternal(self):
        """Convert to the internal representation of (angstroms, photlam).
        This is for internal use only.

        """
        self.validate_units()

        savewunits = self.waveunits
        savefunits = self.fluxunits

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        angwave = self.waveunits.Convert(self.GetWaveSet(), 'angstrom')
        phoflux = self.fluxunits.Convert(angwave, self._fluxtable, 'photlam',
                                         area=area)

        self._wavetable = angwave.copy()
        self._fluxtable = phoflux.copy()

        self.waveunits = savewunits
        self.fluxunits = savefunits


class ArraySourceSpectrum(TabularSourceSpectrum):
    """Class to handle
    :ref:`source spectrum from arrays <pysynphot-empirical-source>`.

    Parameters
    ----------
    wave, flux : array_like
        Wavelength and flux arrays.

    waveunits, fluxunits : str
        Wavelength and flux units, as accepted by `~pysynphot.units.Units`.
        Defaults are Angstrom and ``photlam``.

    name : str
        Description of the spectrum. Default is "UnnamedArraySpectrum".

    keepneg : bool
        Keep negative flux values instead of setting them to zero with
        a warning. Default is `False`.

    Attributes
    ----------
    name
        Same as input.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    Raises
    ------
    ValueError
        Mismatched wavelength and flux arrays.

    """
    def __init__(self, wave=None, flux=None,
                 waveunits='angstrom', fluxunits='photlam',
                 name='UnnamedArraySpectrum',
                 keepneg=False):
        if len(wave) != len(flux):
            raise ValueError("wave and flux arrays must be of equal length")

        self._wavetable = wave
        self._fluxtable = flux
        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)
        self.name = name
        self.isAnalytic = False
        self.warnings = {}

        # must do before validate_fluxtable because it tests against unit type
        self.validate_units()
        # must do before ToInternal in case of descending
        self.validate_wavetable()
        if not keepneg:
            self.validate_fluxtable()

        self.ToInternal()


class FileSourceSpectrum(TabularSourceSpectrum):
    """Class to handle
    :ref:`source spectrum loaded from ASCII or FITS table <pysynphot-source-from-file>`.
    Also see :ref:`pysynphot-io`.

    Parameters
    ----------
    filename : str
        File with spectral data (can be ASCII or FITS).

    fluxname : str or `None`
        Column name containing flux data. This is only used if the given
        file is in FITS format.

    keepneg : bool
        Keep negative flux values instead of setting them to zero with
        a warning. Default is `False`.

    Attributes
    ----------
    name : str
        Resolved filename; i.e., IRAF-style directory name is expanded to actual path name.

    fheader : dict
        For FITS file, this contains headers from both extensions 0 and 1. If the extensions have the same keyword, the one from the latter is used.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    """
    def __init__(self, filename, fluxname=None, keepneg=False):
        self.name = locations.irafconvert(filename)
        self._readSpectrumFile(self.name, fluxname)
        self.validate_units()
        self.validate_wavetable()
        if not keepneg:
            self.validate_fluxtable()
        self.ToInternal()
        self.isAnalytic = False
        self.warnings = {}

    def _readSpectrumFile(self, filename, fluxname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, fluxname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, fluxname):
        fs = pyfits.open(filename)

        # pyfits cannot close the file on .close() if there are still
        # references to mmapped data
        self._wavetable = fs[1].data.field('wavelength').copy()
        if fluxname is None:
            fluxname = 'flux'
        self._fluxtable = fs[1].data.field(fluxname).copy()
        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.fluxunits = units.Units(fs[1].header['tunit2'].lower())

        # Retain the header information as a convenience for the user.
        # If duplicate keywords exist, the value in the extension
        # header will override that in the primary.
        self.fheader = dict(fs[0].header)
        self.fheader.update(dict(fs[1].header))

        fs.close()

    def _readASCII(self, filename):
        """ASCII files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is flux in Flam."""

        self.waveunits = units.Units('angstrom')
        self.fluxunits = units.Units('flam')
        wlist, flist = self._columnsFromASCII(filename)
        self._wavetable = N.array(wlist, dtype=N.float64)
        self._fluxtable = N.array(flist, dtype=N.float64)

        # We don't support headers from ascii files
        self.fheader = dict()


class AnalyticSpectrum(SourceSpectrum):
    """Base class for analytic source spectrum.
    This includes `BlackBody`, `FlatSpectrum`, `GaussianSource`, and
    `Powerlaw`.

    Parameters
    ----------
    waveunits, fluxunits : str
        Wavelength and flux units, as accepted by `~pysynphot.units.Units`.
        Defaults are Angstrom and ``photlam``.

    Attributes
    ----------
    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `True`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    """
    def __init__(self, waveunits='angstrom', fluxunits='photlam'):
        # All AnalyticSpectra must set wave & flux units; do it here
        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)
        self.validate_units()
        self.isAnalytic = True
        self.warnings = {}

    def GetWaveSet(self):
        """Return the wavelength set for the spectrum.

        Returns
        -------
        waveset : array_like
            Wavelength set (a copy of the default wavelength table).

        """
        return refs._default_waveset.copy()


class GaussianSource(AnalyticSpectrum):
    """Class to handle a :ref:`Gaussian source <pysynphot-gaussian>`.

    Parameters
    ----------
    flux : float
        Total flux under the Gaussian curve, in given flux unit.

    center : float
        Central wavelength of the Gaussian curve, in given wavelength unit.

    fwhm : float
        FWHM of the Gaussian curve, in given wavelength unit.

    waveunits, fluxunits : str
        Wavelength and flux units, as accepted by `~pysynphot.units.Units`.
        Defaults are Angstrom and ``flam``.

    Attributes
    ----------
    total_flux
        Same as input ``flux``.

    center, fwhm
        Same as inputs.

    sigma, factor : float
        These are :math:`\\sigma` and :math:`A` as defined in :ref:`pysynphot-gaussian`.

    name : str
        Description of the spectrum.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `True`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    """
    def __init__(self, flux, center, fwhm, waveunits='angstrom',
                 fluxunits='flam'):
        AnalyticSpectrum.__init__(self, waveunits, fluxunits)

        self.center = center

        self.fwhm = fwhm

        self.total_flux = flux

        self._input_flux_units = self.fluxunits
        self._input_wave_units = self.waveunits

        self.sigma = fwhm / math.sqrt(8.0 * math.log(2.0))

        self.factor = flux / (math.sqrt(2.0 * math.pi) * self.sigma)

        self.name = ('Gaussian: mu=%g %s,fwhm=%g %s, total flux=%g %s' %
                     (self.center, self._input_wave_units, self.fwhm,
                      self._input_wave_units, self.total_flux,
                      self._input_flux_units))

    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        # wavelength comes in as Angstom but Gaussian properties are stored
        # in user defined units
        wave = units.Angstrom().Convert(
            wavelength, self._input_wave_units.name)

        # calculate flux
        flux = (self.factor *
                N.exp(-0.5 * ((wave - self.center) / self.sigma) ** 2))

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        # convert flux to photlam before returning
        return self._input_flux_units.ToPhotlam(wave, flux, area=area)

    def GetWaveSet(self):
        """Return the wavelength set that optimally samples the Gaussian curve.
        It has 101 values, as defined below:

        .. math::

            x_{\\textnormal{first,last}} = x_{0} \\; \\pm \\; 5 \\; \\sigma

            \\delta x = 0.1 \\; \\sigma

        Returns
        -------
        waveset : array_like
            Wavelength set in internal unit.

        """
        increment = 0.1*self.sigma
        first = self.center - 50.0*increment
        last = self.center + 50.0*increment
        waveset = N.arange(first, last, increment)
        return self._input_wave_units.Convert(waveset, 'angstrom')


class FlatSpectrum(AnalyticSpectrum):
    """Class to handle a :ref:`flat source spectrum <pysynphot-flat-spec>`.

    Parameters
    ----------
    fluxdensity : float
        The constant flux value in the given flux unit.

    waveunits, fluxunits : str
        Wavelength and flux units, as accepted by `~pysynphot.units.Units`.
        Defaults are Angstrom and ``photlam``.

    Attributes
    ----------
    name : str
        Description of the spectrum.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `True`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    """
    def __init__(self, fluxdensity, waveunits='angstrom', fluxunits='photlam'):
        AnalyticSpectrum.__init__(self, waveunits, fluxunits)
        self.wavelength = None
        self._fluxdensity = fluxdensity
        self._input_flux_units = self.fluxunits
        self.name = "Flat spectrum of %g %s" % (self._fluxdensity,
                                                self._input_flux_units)

    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        if hasattr(wavelength, 'shape'):
            flux = self._fluxdensity * N.ones(wavelength.shape,
                                              dtype=N.float64)
        else:
            flux = self._fluxdensity

        # __call__ is supposed to return photflam so we need to do the
        # conversion here since it doesn't make sense to store the _fluxdensity
        # attribute in photlam
        wave = units.Angstrom().Convert(wavelength, self.waveunits.name)

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        return self._input_flux_units.ToPhotlam(wave, flux, area=area)

    def redshift(self, z):
        """Apply redshift to the flat spectrum.

        Unlike :meth:`SourceSpectrum.redshift`, the redshifted spectrum
        remains an analytic flat source.

        Parameters
        ----------
        z : number
            Redshift value.

        Returns
        -------
        ans : `FlatSpectrum`

        """
        tmp = SourceSpectrum.redshift(self, z)
        ans = FlatSpectrum(tmp.flux.max(), fluxunits=tmp.fluxunits)
        return ans

# This change produces 5 errors and 17 failures in cos_etc_test.py
#     def GetWaveSet(self):
#         return N.array([_default_waveset[0],_default_waveset[-1]])


class Powerlaw(AnalyticSpectrum):
    """Class to handle a :ref:`power-law source spectrum <pysynphot-powerlaw>`.

    Parameters
    ----------
    refwave : number
        Reference wavelength in the given unit.

    index : number
        Power-law index.

    waveunits, fluxunits : str
        Wavelength and flux units, as accepted by `~pysynphot.units.Units`.
        Defaults are Angstrom and ``photlam``.

    Attributes
    ----------
    name : str
        Description of the spectrum.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `True`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    """
    def __init__(self, refwave, index, waveunits='angstrom',
                 fluxunits='photlam'):
        AnalyticSpectrum.__init__(self, waveunits, fluxunits)
        self.wavelength = None

        self._input_flux_units = self.fluxunits
        self._input_wave_units = self.waveunits

        self._refwave = refwave

        self._index = index

        self.name = ("Power law: refwave %g %s, index %g" % (
                self._refwave, self._input_wave_units, self._index))

    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        # input wavelength is assumed to be angstroms
        # and either a scalar or a numpy array

        # need to first convert input wavelength to the units the user
        # specified when creating this object
        wave = units.Angstrom().Convert(
            wavelength, self._input_wave_units.name)

        flux = (wave / self._refwave) ** self._index

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        # convert flux to photlam before returning
        return self._input_flux_units.ToPhotlam(wave, flux, area=area)


class BlackBody(AnalyticSpectrum):
    """Class to handle a :ref:`blackbody source <pysynphot-planck-law>`.

    Flux is evaluated with :func:`~pysynphot.planck.bbfunc` and
    normalized with ``pysynphot.spectrum.RENORM``, which is:

    .. math::

      \\textnormal{RENORM} = \\pi \\; (\\frac{R_{\\odot}}{1 \\; \\textnormal{kpc}})^{2}

    Parameters
    ----------
    temperature : number
        Blackbody temperature in Kelvin.

    Attributes
    ----------
    temperature
        Same as input.

    name : str
        Description of the spectrum.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `True`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        User units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in user units.

    """
    def __init__(self, temperature):
        waveunits = units.Units('angstrom')
        fluxunits = units.Units('photlam')
        AnalyticSpectrum.__init__(self, waveunits, fluxunits)
        self.wavelength = None
        self.temperature = temperature
        self.name = 'BB(T=%d)' % self.temperature

    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        return planck.bbfunc(wavelength, self.temperature) * RENORM


class SpectralElement(Integrator):
    """This is the base class for all :ref:`bandpasses <pysynphot-bandpass>`
    and spectral elements (e.g., filter and detector response curves).

    Attributes
    ----------
    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    """
    def __init__(self):
        self.binset = None

    def validate_units(self):
        """Ensure that wavelenth unit belongs to the correct class.
        There is no check for throughput because it is unitless.

        Raises
        ------
        TypeError
            Wavelength unit is not `~pysynphot.units.WaveUnits`.

        """
        if (not isinstance(self.waveunits, units.WaveUnits)):
            raise TypeError("%s is not a valid WaveUnit" % self.waveunits)

    def __mul__(self, other):
        """Permitted to multiply a SpectralElement by another
        SpectralElement, or by a SourceSpectrum.  In the former
        case we return a CompositeSpectralElement, while in the
        latter case a CompositeSourceSpectrum.
        """
        if isinstance(other, SpectralElement):
            return CompositeSpectralElement(self, other)

        if isinstance(other, SourceSpectrum):
            return CompositeSourceSpectrum(self, other, 'multiply')

        # Multiplying by a constant is the same as multiplying by a
        # UniformTransmission object
        if isinstance(other, (int, float)):
            return CompositeSpectralElement(self, UniformTransmission(other))

        else:
            print("SpectralElements can only be multiplied by other " +
                  "SpectralElements or SourceSpectrum objects")

    def __rmul__(self, other):
        return self.__mul__(other)

    def integrate(self, wave=None):
        """Integrate the throughput over the specified wavelength set.
        If no wavelength set is specified, the built-in one is used.

        Integration is done using :meth:`~Integrator.trapezoidIntegration`
        with ``x=wave`` and ``y=throughput``.
        Also see :ref:`pysynphot-formula-equvw`.

        Parameters
        ----------
        wave : array_like or `None`
            Wavelength set for integration.

        Returns
        -------
        ans : float
            Integrated sum.

        """

        if wave is None:
            wave = self.wave
        ans = self.trapezoidIntegration(wave, self(wave))
        return ans

# ..................................................................
# Methods to implement bandpar functionality go here
# ..................................................................
    def avgwave(self):
        """Calculate :ref:`pysynphot-formula-avgwv`.

        Returns
        -------
        ans : float
            Average wavelength.

        """
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave = self.wave
        thru = self.throughput
        self.convert(mywaveunits)

        num = self.trapezoidIntegration(wave, thru*wave)
        den = self.trapezoidIntegration(wave, thru)

        if 0.0 in (num, den):
            return 0.0
        else:
            return num/den

    # This is the calculation performed when the ETC invokes calcphot.
    # Does this need to be calculated on binned waveset, or may
    # it be calculated on native waveset?
    def pivot(self, binned=False):
        """Calculate :ref:`pysynphot-formula-pivwv`.

        Parameters
        ----------
        binned : bool
            This is reserved for use by `~pysynphot.observation.Observation`.
            If `True`, binned wavelength set is used. Default is `False`.

        Returns
        -------
        ans : float
            Pivot wavelength.

        Raises
        ------
        AttributeError
            Binned wavelength set requested but not found.

        """
        if binned:
            try:
                wave = self.binwave
            except AttributeError:
                raise AttributeError('Class ' + str(type(self)) +
                                     ' does not support binning.')
        else:
            wave = self.wave

        countmulwave = self(wave)*wave
        countdivwave = self(wave)/wave

        num = self.trapezoidIntegration(wave, countmulwave)
        den = self.trapezoidIntegration(wave, countdivwave)

        if num == 0.0 or den == 0.0:
            return 0.0

        return math.sqrt(num/den)

    def rmswidth(self, floor=0):
        """Calculate :ref:`pysynphot-formula-rmswidth`.

        Parameters
        ----------
        floor : float
            Throughput values equal or below this threshold are not
            included in the calculation. By default (0), all points
            are included.

        Returns
        -------
        ans : float
            RMS band width.

        """
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave = self.wave
        thru = self.throughput
        self.convert(mywaveunits)

        if floor != 0:
            idx = N.where(thru >= floor)
            wave = wave[idx]
            thru = thru[idx]

        integrand = (wave-self.avgwave())**2 * thru
        num = self.trapezoidIntegration(wave, integrand)
        den = self.trapezoidIntegration(wave, thru)

        if 0.0 in (num, den):
            return 0.0
        else:
            ans = math.sqrt(num/den)
            return ans

    def photbw(self, floor=0):
        """Calculate :ref:`pysynphot-formula-bandw`.

        .. note:: For backward-compatibility with IRAF STSDAS SYNPHOT only.

        Parameters
        ----------
        floor : float
            Same as :meth:`rmswidth`.

        Returns
        -------
        ans : float
            RMS band width (deprecated).

        """
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave = self.wave
        thru = self.throughput
        self.convert(mywaveunits)

        # calculate the average wavelength
        num = self.trapezoidIntegration(wave, thru * N.log(wave) / wave)
        den = self.trapezoidIntegration(wave, thru / wave)

        if num == 0 or den == 0:
            return 0.0

        avg_wave = N.exp(num/den)

        if floor != 0:
            idx = N.where(thru >= floor)
            wave = wave[idx]
            thru = thru[idx]

        # calcualte the rms width
        integrand = thru * N.log(wave / avg_wave)**2 / wave
        num = self.trapezoidIntegration(wave, integrand)

        if num == 0 or den == 0:
            return 0.0

        return avg_wave * N.sqrt(num/den)

    def rectwidth(self):
        """Calculate :ref:`pysynphot-formula-rectw`.

        Returns
        -------
        ans : float
            Bandpass rectangular width.

        """
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave = self.wave
        thru = self.throughput
        self.convert(mywaveunits)

        num = self.trapezoidIntegration(wave, thru)
        den = thru.max()

        if 0.0 in (num, den):
            return 0.0
        else:
            return num/den

    def equivwidth(self):
        """Calculate :ref:`pysynphot-formula-equvw`.
        This basically just calls :meth:`integrate`.

        Returns
        -------
        ans : float
            Bandpass equivalent width.

        """
        return self.integrate()

    def efficiency(self):
        """Calculate :ref:`pysynphot-formula-qtlam`.

        Returns
        -------
        ans : float
            Bandpass dimensionless efficiency.

        """
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave = self.wave
        thru = self.throughput
        self.convert(mywaveunits)

        ans = self.trapezoidIntegration(wave, thru/wave)
        return ans

# ..................................................................
    def check_sig(self, other):
        """Check overlap insignificance with another spectrum.
        Also see :ref:`pysynphot-command-checko`.

        .. note::

            Only use when :meth:`check_overlap` returns "partial".

        Parameters
        ----------
        other : `SourceSpectrum` or `SpectralElement`
            The other spectrum.

        Returns
        -------
        ans : bool
            `True` means the *lack* of overlap is *insignificant*
            (i.e., okay to proceed).

        """
        swave = self.wave[N.where(self.throughput != 0)]
        s1, s2 = swave.min(), swave.max()

        owave = other.wave
        o1, o2 = owave.min(), owave.max()

        lorange = sorted([s1, o1])
        hirange = sorted([s2, o2])

        # Get the full throughput
        total = self.integrate()

        # Now get the other two pieces
        # We cannot yet do
        # low = self[slice(*lowrange)].integrate()
        wave = self.wave
        idxs = [N.searchsorted(wave, lorange, 'left'),
                N.searchsorted(wave, hirange, 'left')]

        excluded = 0.0
        for idx in idxs:
            try:
                excluded += self.integrate(wave=wave[slice(*idx)])
            except IndexError:
                pass  # If the range is zero, do nothing

        if excluded/total < 0.01:
            return True
        else:
            return False

    def check_overlap(self, other):
        """Check overlap with another spectrum.
        Also see :ref:`pysynphot-command-checko`.

        This checks whether the wavelength set of the given spectrum
        is defined everywhere within ``self``.
        Wavelength values where throughput is zero are excluded from the check.
        Typical use case is for checking whether a source spectrum
        is fully defined over the range of a bandpass.
        This check is asymmetric in the sense that if ``self`` is fully
        defined within the given spectrum, but not the other way around,
        it will still only return "partial".
        If the given spectrum is analytic, the result is always "full".

        Example of full overlap::

            |---------- other ----------|
               |------ self ------|

        Examples of partial overlap::

            |---------- self ----------|
               |------ other ------|

            |---- other ----|
               |---- self ----|

            |---- self ----|
               |---- other ----|

        Examples of no overlap::

            |---- self ----|  |---- other ----|

            |---- other ----|  |---- self ----|

        Parameters
        ----------
        other : `SourceSpectrum` or `SpectralElement`
            The other spectrum.

        Returns
        -------
        ans : {'full', 'partial', 'none'}
            Overlap status.

        """
        if other.isAnalytic and not isinstance(other, Box):
            # then it's defined everywhere, except for Box
            return 'full'

        swave = self.wave[N.where(self.throughput != 0)]
        s1, s2 = swave.min(), swave.max()

        owave = other.wave
        o1, o2 = owave.min(), owave.max()

        if (s1 >= o1 and s2 <= o2):
            ans = 'full'

        elif (s2 < o1) or (o2 < s1):
            ans = 'none'

        else:
            ans = 'partial'

        return ans

    def convert(self, targetunits):
        """Set new user unit, for wavelength only.

        This effectively converts the spectrum wavelength
        to given unit. Note that actual data are always kept in
        internal unit (Angstrom), and only converted
        to user unit by :meth:`GetWaveSet` during actual computation.
        User unit is stored in ``self.waveunits``.
        Throughput is unitless and cannot be converted.

        Parameters
        ----------
        targetunits : str
            New unit name, as accepted by `~pysynphot.units.Units`.

        """
        nunits = units.Units(targetunits)
        self.waveunits = nunits

    def ToInternal(self):
        """Convert wavelengths to the internal representation of angstroms.
        Note: This is not yet used, but should be for safety when creating
        TabularSpectralElements from files. It will also be necessary for the
        ArraySpectralElement class that we want to create RSN.

        .. note:: For internal use only.

        """
        self.validate_units()
        savewunits = self.waveunits
        angwave = self.waveunits.Convert(self.GetWaveSet(), 'angstrom')
        self._wavetable = angwave.copy()
        self.waveunits = savewunits

    def __call__(self, wavelengths):
        """This is where the throughput array is calculated for a given
        input wavelength table.

        Parameters
        ----------
        wavelengths : ndarray
            An array of wavelengths in Angstrom at which the
            throughput should be sampled.

        """
        if N.isscalar(wavelengths):
            delta = 0.0001
            ww = N.array([wavelengths - delta, wavelengths,
                          wavelengths + delta])
            tmp = self.resample(ww)
            return tmp._throughputtable[1]
        else:
            return self.resample(wavelengths)._throughputtable

    def sample(self, wave):
        """Sample the spectrum.

        This uses :meth:`resample` to do the actual computation.

        Parameters
        ----------
        wave : number or array_like
            Wavelength set for sampling, given in user unit.

        Returns
        -------
        throughput : number or array_like
            Sampled throughput.

        """
        angwave = self.waveunits.ToAngstrom(wave)
        return self.__call__(angwave)

    def taper(self):
        """Taper the spectrum by adding zero throughput to each end.
        This is similar to :meth:`TabularSourceSpectrum.taper`.

        There is no check to see if the spectrum is already tapered.
        Hence, calling this on a tapered spectrum will result in
        multiple zero-throughput entries at both ends.

        The wavelengths to use for the new first and last points are
        calculated by using the same ratio as for the two interior points
        used at each end.

        Returns
        -------
        OutElement : `TabularSpectralElement`
            Tapered spectrum.

        """
        OutElement = TabularSpectralElement()

        wcopy = N.zeros(self._wavetable.size + 2, dtype=N.float64)
        fcopy = N.zeros(self._throughputtable.size + 2, dtype=N.float64)

        wcopy[1:-1] = self._wavetable
        fcopy[1:-1] = self._throughputtable

        fcopy[0] = 0.0
        fcopy[-1] = 0.0

        # The wavelengths to use for the first and last points are
        # calculated by using the same ratio as for the 2 interior points
        wcopy[0] = wcopy[1]*wcopy[1]/wcopy[2]
        wcopy[-1] = wcopy[-2]*wcopy[-2]/wcopy[-3]

        OutElement._wavetable = wcopy
        OutElement._throughputtable = fcopy

        return OutElement

    def writefits(self, filename, clobber=True, trimzero=True,
                  precision=None, hkeys=None):
        """Write the spectrum to a FITS table.

        Primary header in EXT 0. ``FILENAME``,  ``ORIGIN``, and any
        extra keyword(s) from ``hkeys`` will also be added.

        Table header and data are in EXT 1. The table has 2 columns,
        i.e., ``WAVELENGTH`` and ``THROUGHPUT``.
        Wavelength data are stored in user unit.
        Its header also will have these additional keywords:

        * ``EXPR`` - Description of the spectrum.
        * ``TDISP1`` and ``TDISP2`` - Columns display format,
          always "G15.7".
        * ``GRFTABLE`` and ``CMPTABLE`` - Graph and component
          table names to use with associated observation mode.
          These are only added if applicable.

        If data is already double-precision but user explicitly
        set output precision to single, ``pysynphot.spectrum.syn_epsilon``
        defines the allowed minimum wavelength separation.
        This limit (:math:`3.2 \\times 10^{-4}`) was taken from
        IRAF STSDAS SYNPHOT FAQ.
        Values equal or smaller than this limit are considered as the
        same, and duplicates are ignored, resulting in data loss.
        In the way that this comparison is coded, when such precision clash
        happens, even when no duplicates are detected, the last row is
        always omitted (also data loss). Therefore, it is *not* recommended
        for user to force single-precision when the data is in
        double-precision.

        Parameters
        ----------
        filename : str
            Output filename.

        clobber : bool
            Overwrite existing file. Default is `True`.

        trimzero : bool
            Trim off duplicate rows with flux values of zero from both ends
            of the spectrum. This keeps one row of zero-flux at each end,
            if it exists; However, it does not add a zero-flux row if it
            does not. Default is `True`.

        precision : {'s', 'd', `None`}
            Write data out in single (``'s'``) or double (``'d'``)
            precision. Default is `None`, which will enforce native
            precision from ``self.throughput``.

        hkeys : dict
            Additional keyword(s) to be added to primary FITS header,
            in the format of ``{keyword:(value,comment)}``.

        """
        if precision is None:
            precision = self.throughput.dtype.char
        _precision = precision.lower()[0]
        pcodes = {'d':'D', 's':'E', 'f':'E'}

        if clobber:
            try:
                os.remove(filename)
            except OSError:
                pass

        wave = self.wave
        thru = self(wave)

        # Add a check for single/double precision clash, so
        # that if written out in single precision, the wavelength table
        # will still be sorted with no duplicates
        # The value of epsilon is taken from the Synphot FAQ.

        if wave.dtype == N.float64 and _precision == 's':
            idx = N.where(abs(wave[1:] - wave[:-1]) > syn_epsilon)
        else:
            idx = N.where(wave)  # => idx=[:]

        wave = wave[idx]
        thru = thru[idx]

        first, last = 0, len(thru)
        if trimzero:
            # Keep one zero at each end
            nz = thru.nonzero()[0]
            try:
                first = max(nz[0] - 1, first)
                last = min(nz[-1] + 2, last)
            except IndexError:
                pass

        # Construct the columns and HDUlist
        cw = pyfits.Column(name='WAVELENGTH',
                           array=wave[first:last],
                           unit=self.waveunits.name,
                           format=pcodes[_precision])
        cf = pyfits.Column(name='THROUGHPUT',
                           array=thru[first:last],
                           unit='         ',
                           format=pcodes[_precision])

        # Make the primary header
        hdu = pyfits.PrimaryHDU()
        hdulist = pyfits.HDUList([hdu])

        # User-provided keys are written to the primary header;
        # so are filename and origin
        bkeys = dict(filename=(os.path.basename(filename), 'name of file'),
                     origin=('pysynphot', 'Version (%s, %s)' %
                             (__version__, __svn_revision__)))
        # User-values if present may override default values
        if hkeys is not None:
            bkeys.update(hkeys)

        # Now update the primary header
        for key, val in bkeys.items():
            hdu.header[key] = val

        # Make the extension HDU
        cols = pyfits.ColDefs([cw, cf])
        hdu = pyfits.BinTableHDU.from_columns(cols)

        # There are also some keys to be written to the extension header
        bkeys = dict(expr=(str(self), 'pysyn expression'),
                     tdisp1=('G15.7',),
                     tdisp2=('G15.7',))

        try:
            bkeys['grftable'] = (os.path.basename(self.obsmode.gtname),
                                 'graph table used')
            bkeys['cmptable'] = (os.path.basename(self.obsmode.ctname),
                                 'component table used')
        except AttributeError:
            pass  # Not all bandpasses have these

        for key, val in bkeys.items():
            hdu.header[key] = val

        # Add the extension to the list, and write to file.
        hdulist.append(hdu)
        hdulist.writeto(filename)

    def resample(self, resampledWaveTab):
        """Resample the spectrum for the given wavelength set.

        Given wavelength array must be monotonically increasing or decreasing.
        Throughput interpolation is done using :func:`numpy.interp`.

        Parameters
        ----------
        resampledWaveTab : array_like
            Wavelength set for resampling.

        Returns
        -------
        resampled : `ArraySpectralElement`
            Resampled spectrum.

        """
        # Check whether the input wavetab is in descending order
        if resampledWaveTab[0] < resampledWaveTab[-1]:
            newwave = resampledWaveTab
            newasc = True
        else:
            newwave = resampledWaveTab[::-1]
            newasc = False

        # Use numpy interpolation function
        if self._wavetable[0] < self._wavetable[-1]:
            oldasc = True
            ans = N.interp(newwave, self._wavetable, self._throughputtable)
        else:
            oldasc = False
            rev = N.interp(newwave, self._wavetable[::-1],
                           self._throughputtable[::-1])
            ans = rev[::-1]

        # If the new and old waveset don't have the same parity,
        # the answer has to be flipped again
        if (newasc != oldasc):
            ans = ans[::-1]

        # Finally, make the new object.
        # NB: these manipulations were done using the internal
        # tables in Angstrom, so those are the units
        # that must be fed to the constructor.
        resampled = ArraySpectralElement(wave=resampledWaveTab.copy(),
                                         waveunits='angstroms',
                                         throughput=ans.copy())
        # Use the convert method to set the units desired by the user.
        resampled.convert(self.waveunits)

        return resampled

    def unit_response(self):
        """Calculate :ref:`pysynphot-formula-uresp`.

        .. warning::

            Result is correct only if ``self.waveunits`` is in Angstrom.

        Returns
        -------
        ans : float
            Bandpass unit response.

        """
        hc = units.HC

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = refs.PRIMARY_AREA

        wave = self.GetWaveSet()
        thru = self(wave)

        return hc / (area * self.trapezoidIntegration(wave, thru*wave))

    def GetWaveSet(self):
        """Obtain the wavelength set for the spectrum.

        Returns
        -------
        wave : array_like
            Wavelength set in internal unit.

        """
        return self._wavetable

    # Define properties for consistent UI
    def _getWaveProp(self):
        """Return wavelength in user units."""
        wave = self.GetWaveSet()
        wave = units.Angstrom().Convert(wave, self.waveunits.name)
        return wave

    wave = property(_getWaveProp, doc="Wavelength property.")

    # NB: Throughput never changes units no matter what the
    # wavelength does. There is an implicit assumption here that
    # the units of the input waveset to the __call__ are always
    # Angstroms.
    def GetThroughput(self):
        """Obtain throughput for the spectrum.

        Returns
        -------
        throughput : array_like
            Throughput values.

        """
        # See https://aeon.stsci.edu/ssb/trac/astrolib/ticket/169
        return self.__call__(self.GetWaveSet())

    throughput = property(GetThroughput, doc='Throughput property.')

    def fwhm(self):
        """Not implemented."""
        raise NotImplementedError("#139: Implement calcband functionality")


class CompositeSpectralElement(SpectralElement):
    """Class to handle :ref:`composite spectrum <pysynphot-composite-spectrum>`
    involving bandpasses.

    Parameters
    ----------
    component1, component2 : `SpectralElement`
        Input bandpass.

    Attributes
    ----------
    component1, component2
        Same as inputs.

    name : str
        Short description of the spectrum.

    isAnalytic : bool
        Flag to indicate whether this is an analytic spectrum. This is only `True` if both inputs are analytic.

    warnings : dict
        To store warnings, which are inherited from both input sources. If inputs have the same warning keyword, the one from ``component2`` is used.

    primary_area : number or `None`
        :ref:`pysynphot-area` of the telescope. This is inherited from either of the inputs, if available (not `None`). If inputs have different values, an exception is raised.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit inherited from inputs, where both inputs are required to have the same unit or an exception will be raised.

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
    def __init__(self, component1, component2):
        SpectralElement.__init__(self)

        if (not isinstance(component1, SpectralElement) or
                not isinstance(component2, SpectralElement)):
            raise TypeError("Arguments must be SpectralElements")

        self.component1 = component1
        self.component2 = component2

        self.isAnalytic = component1.isAnalytic and component2.isAnalytic

        if component1.waveunits.name == component2.waveunits.name:
            self.waveunits = component1.waveunits
        else:
            msg = ("Components have different waveunits (%s and %s)" %
                   (component1.waveunits, component2.waveunits))
            raise NotImplementedError(msg)

        self.throughputunits = None

        self.name = "(%s * %s)" % (str(self.component1), str(self.component2))

        self.warnings = {}
        self.warnings.update(component1.warnings)
        self.warnings.update(component2.warnings)

        # check areas
        if hasattr(component1, 'primary_area'):
            comp1_area = component1.primary_area
        else:
            comp1_area = None

        if hasattr(component2, 'primary_area'):
            comp2_area = component2.primary_area
        else:
            comp2_area = None

        if not comp1_area and not comp2_area:
            self.primary_area = None

        elif comp1_area and not comp2_area:
            self.primary_area = comp1_area

        elif not comp1_area and comp2_area:
            self.primary_area = comp2_area

        else:
            if comp1_area == comp2_area:
                self.primary_area = comp1_area

            else:
                err = ('Components have different area attributes: '
                       '%s: %f, %s: %f')
                err = err % (str(component1), comp1_area,
                             str(component2), comp2_area)
                raise exceptions.IncompatibleSources(err)

    def __call__(self, wavelength):
        """This is where the throughput calculation is delegated."""
        return self.component1(wavelength) * self.component2(wavelength)

    def __str__(self):
        return self.name

    def complist(self):
        """Return a list of all components and sub-components."""
        ans = []
        for comp in (self.component1, self.component2):
            try:
                ans.extend(comp.complist())
            except AttributeError:
                ans.append(comp)
        return ans

    def GetWaveSet(self):
        """Obtain the wavelength set for the composite spectrum.
        This is done by using :func:`MergeWaveSets` to form a union of
        wavelength sets from its components.

        Returns
        -------
        waveset : array_like
            Composite wavelength set.

        """
        wave1 = self.component1.GetWaveSet()
        wave2 = self.component2.GetWaveSet()
        return MergeWaveSets(wave1, wave2)

    wave = property(GetWaveSet, doc='Wavelength property.')


class UniformTransmission(SpectralElement):
    """Class to handle a :ref:`uniform bandpass <pysynphot-bandpass-uniform>`.

    Parameters
    ----------
    value : number
        Constant throughput value for the bandpass.

    waveunits : str
        Wavelength unit, as accepted by `~pysynphot.units.Units`.
        Default is Angstrom.

    Attributes
    ----------
    value
        Same as input.

    name : str
        Short description of the spectrum.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `True`.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit for wavelength.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless throughput.

    """
    def __init__(self, value, waveunits='angstrom'):
        SpectralElement.__init__(self)

        self.waveunits = units.Units(waveunits)
        self.value = value
        self.name = str(self)
        self.isAnalytic = True
        self.warnings = {}
        # The ._wavetable is used only by the .writefits() method at this time
        # It is not for general use.
        self._wavetable = N.array([refs._default_waveset[0],
                                   refs._default_waveset[-1]])
        self._wave = self.GetWaveSet()

    # TODO: Find a less hacky way to do this?
    def writefits(self, *args, **kwargs):
        """Write to file using default waveset."""
        old_wave = self.wave
        self.wave = self._wavetable

        try:
            super(UniformTransmission, self).writefits(*args, **kwargs)
        finally:
            self.wave = old_wave

    @property
    def wave(self):
        """``waveset`` for uniform transmission."""
        return self._wave

    @wave.setter
    def wave(self, val):
        self._wave = val

    def GetWaveSet(self):
        """Obtain wavelength set for the spectrum.

        Returns
        -------
        waveset : `None`
            Due to the nature of uniform transmission,
            this is always undefined.

        """
        return None

# This produced 15 test failures in cos_etc_test.
#     def GetWaveSet(self):
#         return N.array([_default_waveset[0],_default_waveset[-1]])

    def __str__(self):
        return "%g" % self.value

    def check_overlap(self, spectrum):
        """Apply special overlap logic for UniformTransmission.

        By definition, a UniformTransmission is defined everywhere.
        Therefore, this is a special case for which the overlap check
        should be ignored (because the alternative is that it will
        always fail and always require users to override it, so it
        becomes meaningless).

        """
        pass

    def __call__(self, wavelength):
        """__call__ returns the constant value as an array, given a
        wavelength array as argument.
        """
        if wavelength is None:
            thru = N.array([self.value], dtype=N.float)
        else:
            thru = N.zeros_like(wavelength, dtype=N.float) + self.value

        return thru


class TabularSpectralElement(SpectralElement):
    """Base class for `ArraySpectralElement` and `FileSpectralElement`.

    Parameters
    ----------
    fileName : str or `None`
        File with spectral data (can be ASCII or FITS). If not `None`,
        data will be loaded from file at initialization.

    thrucol : str
        Column name containing throughput data.
        Default is "throughput" (case-insensitive).
        This is only used if filename is given and is of FITS format.

    Attributes
    ----------
    name
        Same as input ``fileName``.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit for wavelength.

    throughputunits : {'none', `None`}
        This is only to inform user that throughput is unitless.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless throughput.

    """
    def __init__(self, fileName=None, thrucol='throughput'):
        SpectralElement.__init__(self)

        self.isAnalytic = False
        self.warnings = {}
        if fileName:
            if fileName.endswith('.fits') or fileName.endswith('.fit'):
                self._readFITS(fileName, thrucol)
            else:
                self._readASCII(fileName)
            self.name = fileName

        else:
            self.name = None
            self._wavetable = None
            self._throughputtable = None
            self.waveunits = None
            self.throughputunits = None

    def _reverse_wave(self):
        self._wavetable = self._wavetable[::-1]

    def __str__(self):
        return str(self.name)

    def ToInternal(self):
        """Convert wavelengths to the internal representation of angstroms.
        For internal use only."""
        self.validate_units()
        savewunits = self.waveunits
        angwave = self.waveunits.Convert(self._wavetable, 'angstrom')
        self._wavetable = angwave.copy()
        self.waveunits = savewunits

    def _readASCII(self, filename):
        """ASCII files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is throughput (dimensionless)."""
        self.waveunits = units.Units('angstrom')
        self.throughputunits = 'none'
        wlist, tlist = self._columnsFromASCII(filename)
        self._wavetable = N.array(wlist, dtype=N.float64)
        self._throughputtable = N.array(tlist, dtype=N.float64)

    def _readFITS(self, filename, thrucol='throughput'):
        fs = pyfits.open(filename)

        # pyfits cannot close the file on .close() if there are still
        # references to mmapped data
        self._wavetable = fs[1].data.field('wavelength').copy()
        self._throughputtable = fs[1].data.field(thrucol).copy()

        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.throughputunits = 'none'

        self.getHeaderKeywords(fs[1].header)

        fs.close()

    def getHeaderKeywords(self, header):
        """This is a placeholder for subclasses to get header keywords without
        having to reopen the file again."""
        pass


class ArraySpectralElement(TabularSpectralElement):
    """Class to handle :ref:`bandpass from arrays <pysynphot-bandpass-arrays>`.

    Parameters
    ----------
    wave, throughput : array_like
        Wavelength and throughput arrays.

    waveunits : str
        Wavelength unit, as accepted by `~pysynphot.units.Units`.
        Default is Angstrom.

    name : str
        Description of the spectrum. Default is "UnnamedArrayBandpass".

    Attributes
    ----------
    name
        Same as input.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit for wavelength.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless throughput.

    Raises
    ------
    ValueError
        Mismatched wavelength and throughput arrays.

    """
    def __init__(self, wave=None, throughput=None,
                 waveunits='angstrom',
                 name='UnnamedArrayBandpass'):
        if len(wave) != len(throughput):
            raise ValueError("wave and throughput arrays must be of "
                             "equal length")

        self._wavetable = wave
        self._throughputtable = throughput
        self.waveunits = units.Units(waveunits)
        self.name = name
        self.isAnalytic = False
        self.warnings = {}

        # must do before validate_fluxtable because it tests against unit type
        self.validate_units()
        # must do before ToInternal in case of descending
        self.validate_wavetable()

        self.ToInternal()


class FileSpectralElement(TabularSpectralElement):
    """Class to handle
    :ref:`bandpass loaded from ASCII or FITS table <pysynphot-bandpass-from-file>`.
    Also see :ref:`pysynphot-io`.

    Parameters
    -----------
    filename : str
        File with spectral data (can be ASCII or FITS).

    thrucol : str or `None`
        Column name containing throughput data. This is only used if the given
        file is in FITS format.

    Attributes
    ----------
    name : str
        Resolved filename; i.e., IRAF-style directory name is expanded to actual path name.

    fheader : dict
        For FITS file, this contains headers from both extensions 0 and 1. If the extensions have the same keyword, the one from the latter is used.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit for wavelength.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless throughput.

    """
    def __init__(self, filename, thrucol=None):
        self.name = locations.irafconvert(filename)
        self._readThroughputFile(self.name, thrucol)

        self.validate_units()
        self.validate_wavetable()
        self.ToInternal()
        self.isAnalytic = False
        self.warnings = {}

    def _readThroughputFile(self, filename, throughputname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, throughputname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, throughputname):
        fs = pyfits.open(filename)

        # pyfits cannot close the file on .close() if there are still
        # references to mmapped data
        self._wavetable = fs[1].data.field('wavelength').copy()
        if throughputname is None:
            throughputname = 'throughput'
        self._throughputtable = fs[1].data.field(throughputname).copy()
        self.waveunits = units.Units(fs[1].header['tunit1'].lower())

        # Retain the header information as a convenience for the user.
        # If duplicate keywords exist, the value in the extension
        # header will override that in the primary.
        self.fheader = dict(fs[0].header)
        self.fheader.update(dict(fs[1].header))

        fs.close()

    def _readASCII(self, filename):
        """ Ascii files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is throughput in Flam."""

        self.waveunits = units.Units('angstrom')
        wlist, flist = self._columnsFromASCII(filename)
        self._wavetable = N.array(wlist, dtype=N.float64)
        self._throughputtable = N.array(flist, dtype=N.float64)

        # We don't support headers from asii files
        self.fheader = dict()


class InterpolatedSpectralElement(SpectralElement):
    """Class to handle :ref:`parameterized keyword <pysynphot-parameterized>`
    in an observation mode.

    Parameters
    ----------
    fileName : str
        Filename followed by a column name specification between square
        brackets. For example: "mythru_syn.fits[fr388n#]"

    wavelength : number
        Desired value to interpolate to. This is not restricted to wavelength,
        but rather whatever parameter the file is parameterized for.

    Attributes
    ----------
    name : str
        Expanded filename.

    interpval
        Same as input ``wavelength``.

    warnings : dict
        To store warnings. When extrapolation is not allowed but a default
        throughput column is present and used, ``warnings['DefaultThroughput']``
        is set to `True`.

    isAnalytic : bool
        This is always `False`.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit for wavelength.

    throughputunits : 'none'
        This is only to inform user that throughput is unitless.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless throughput.

    Raises
    ------
    Exception
        File does not have columns needed for interpolation.

    pysynphot.exceptions.ExtrapolationNotAllowed
        Extrapolation is not allowed and no default throughput column found.

    """
    def __init__(self, fileName, wavelength):
        SpectralElement.__init__(self)

        xre = re.search('\[(?P<col>.*?)\]', fileName)
        self.name = os.path.expandvars(fileName[0:(xre.start())])
        colSpec = xre.group('col')

        self.isAnalytic = False
        self.warnings = {}

        self.interpval = wavelength

        fs = pyfits.open(self.name)

        # if the file has the PARAMS header keyword and if it is set to
        # WAVELENGTH then we want to perform a wavelength shift before
        # interpolation, otherwise we don't want to shift.
        if ('PARAMS' in fs[0].header and
                fs[0].header['PARAMS'].lower() == 'wavelength'):
            doshift = True
        else:
            doshift = False

        # check whether we are supposed to extrapolate when we're given an
        # interpolation value beyond the columns of the table.
        # extrapolation is assumed to false if the EXTRAP keyword is missing.
        if 'EXTRAP' in fs[0].header and fs[0].header['EXTRAP'] is True:
            extrapolate = True
        else:
            extrapolate = False

        # The wavelength table will have to be adjusted before use.

        # pyfits cannot close the file on .close() if there are still
        # references to mmapped data
        wave0 = fs[1].data.field('wavelength').copy()

        # Determine the columns that bracket the desired value
        # grab all columns that beging with the parameter name (e.g. 'MJD#')
        # then split off the numbers after the '#'
        colNames = [n for n in fs[1].data.names
                    if n.startswith(colSpec.upper())]
        colWaves = [float(cn.split('#')[1]) for cn in colNames]

        if colNames == []:
            raise Exception(
                'File %s contains no interpolated columns.' % (fileName, ))

        # easy case: wavelength matches a column
        if self.interpval in colWaves:
            self._no_interp_init(
                wave0, fs[1].data[colNames[colWaves.index(wavelength)]])

        # need interpolation
        elif self.interpval > colWaves[0] and self.interpval < colWaves[-1]:
            upper_ind = N.searchsorted(colWaves, self.interpval)
            lower_ind = upper_ind - 1

            self._interp_init(wave0, colWaves[lower_ind], colWaves[upper_ind],
                              fs[1].data[colNames[lower_ind]],
                              fs[1].data[colNames[upper_ind]], doshift)

        # extrapolate below lowest columns
        elif extrapolate and self.interpval < colWaves[0]:
            self._extrap_init(wave0, colWaves[0], colWaves[1],
                              fs[1].data[colNames[0]],
                              fs[1].data[colNames[1]])

        # extrapolate above highest columns
        elif extrapolate and self.interpval > colWaves[-1]:
            self._extrap_init(wave0, colWaves[-2], colWaves[-1],
                              fs[1].data[colNames[-2]],
                              fs[1].data[colNames[-1]])

        # can't extrapolate, use default
        elif not extrapolate and 'THROUGHPUT' in fs[1].data.names:
            s = ('Extrapolation not allowed, using default throughput '
                 'for %s' % (fileName, ))
            warnings.warn(s, UserWarning)
            self.warnings['DefaultThroughput'] = True
            self._no_interp_init(wave0, fs[1].data['THROUGHPUT'])

        # can't extrapolate and no default
        elif not extrapolate and 'THROUGHPUT' not in fs[1].data.names:
            s = ('Cannot extrapolate and no default throughput '
                 'for %s' % (fileName, ))
            raise exceptions.ExtrapolationNotAllowed(s)

        # assign units
        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.throughputunits = 'none'

        fs.close()

    def __str__(self):
        return "%s#%g" % (self.name, self.interpval)

    def _no_interp_init(self, waves, throughput):
        self._wavetable = waves
        self._throughputtable = throughput

    def _interp_init(self, waves, lower_val, upper_val, lower_thru,
                     upper_thru, doshift):
        self._wavetable = waves

        if doshift:
            # Adjust the wavelength table to bracket the range
            lwave = waves + (lower_val - self.interpval)
            uwave = waves + (upper_val - self.interpval)

            # Interpolate the columns at those ranges
            lower_thru = N.interp(lwave, waves, lower_thru)
            upper_thru = N.interp(uwave, waves, upper_thru)

        # Then interpolate between the two columns
        w = (self.interpval - lower_val) / (upper_val - lower_val)
        self._throughputtable = (upper_thru * w) + lower_thru * (1.0 - w)

    def _extrap_init(self, waves, lower_val, upper_val, lower_thru,
                     upper_thru):
        self._wavetable = waves

        throughput = []

        for y1, y2 in zip(lower_thru, upper_thru):
            m = (y2 - y1) / (upper_val - lower_val)
            b = y1 - m * lower_val

            throughput.append(m*self.interpval + b)

        self._throughputtable = N.array(throughput)


class ThermalSpectralElement(TabularSpectralElement):
    """Class to handle
    :ref:`spectral element with thermal properties <pysynphot_thermal_em>`
    read from a FITS table.

    .. note::

        This class does not know how to apply itself to an existing beam.
        Its emissivity is handled by
        :meth:`~pysynphot.observationmode.ObservationMode.ThermalSpectrum`.

    Parameters
    ----------
    fileName : str
        Filename of the thermal emissivity table.

    Attributes
    ----------
    name
        Same as input ``fileName``.

    temperature : number
        Default temperature in Kelvin from header.

    beamFillFactor : number
        Beam filling factor from header.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit for wavelength.

    throughputunits : 'none'
        This is only to inform user that throughput is unitless.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless emissivity.

    """
    def __init__(self, fileName):

        TabularSpectralElement.__init__(self, fileName=fileName,
                                        thrucol='emissivity')
        self.warnings = {}

    def getHeaderKeywords(self, header):
        """Overrides base class in order to get thermal keywords.
        For internal use only."""
        self.temperature = header['DEFT']
        self.beamFillFactor = header['BEAMFILL']


class Box(SpectralElement):
    """Class to handle a :ref:`box-shaped bandpass <pysynphot-box-bandpass>`.

    Parameters
    ----------
    center, width : number
        Center and width of the box in the given wavelength unit.

    waveunits : str or `None`
        Wavelength unit, as accepted by `~pysynphot.units.Units`.
        If not given, assumed to be in Angstrom.

    Attributes
    ----------
    name : str
        Description of the spectrum.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    binset : `None`
        This is reserved to be used by `~pysynphot.obsbandpass.ObsModeBandpass`.

    waveunits : `~pysynphot.units.Units`
        User unit for wavelength.

    wave, throughput : array_like
        Wavelength set in user unit and associated unitless throughput.

    """
    def __init__(self, center, width, waveunits=None):
        SpectralElement.__init__(self)

        if waveunits is None:
            self.waveunits = units.Units('angstrom')  # per docstring: for now
            self.center = center
            self.width = width
        else:
            self.waveunits = units.Units(waveunits)
            self.center = self.waveunits.Convert(center, 'angstrom')
            self.width = self.waveunits.Convert(width, 'angstrom')

        self.name = 'Box at %g (%g wide)' % (self.center, self.width)
        self.isAnalytic = True
        self.warnings = {}

        # Construct some default lookup table
        self.lower = self.center - self.width / 2.0
        self.upper = self.center + self.width / 2.0
        step = 0.01  # fixed step for now (in A)
        self._wavetable = N.arange(
            self.lower - step, self.upper + step + step, step)
        self._throughputtable = self(self._wavetable)

    def __call__(self, wave):
        """Input wavelengths assumed to be in Angstrom."""

        if N.isscalar(wave):
            if (wave >= self.lower) & (wave <= self.upper):
                thru = 1.0
            else:
                thru = 0.0
        else:
            wave = N.asarray(wave)
            thru = N.zeros(wave.shape, dtype=N.float64)
            thru[(wave >= self.lower) & (wave <= self.upper)] = 1.0

        return thru

    def sample(self, wavelength):
        """Input wavelengths assumed to be in user unit."""
        wave = self.waveunits.Convert(wavelength, 'angstrom')
        return self(wave)

    def resample(self, resampledWaveTab):
        """Resample the spectrum for the given wavelength set.

        Given wavelength array must be monotonically increasing or decreasing.

        Parameters
        ----------
        resampledWaveTab : array_like
            Wavelength set for resampling.

        Returns
        -------
        resampled : `ArraySpectralElement`
            Resampled spectrum. This is no longer a real `Box` spectrum.

        """
        return ArraySpectralElement(
            wave=resampledWaveTab.copy(), waveunits='angstrom',
            throughput=self(resampledWaveTab).copy())


Vega = FileSourceSpectrum(locations.VegaFile)
