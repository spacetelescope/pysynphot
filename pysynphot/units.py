"""This module handles :ref:`wavelength and flux units <pysynphot-units>`.
Constants used for unit conversion are also defined here.

"""
# WARNING: vegamag unit conversions require spectrum and
#          locations modules => circular imports
from __future__ import absolute_import, division

import math
import numpy as N
from . import binning
from . import refs  # needed for PRIMARY_AREA

# cannot just import the constant because it won't get updated
# when the setref() function is used to change it.

C = 2.99792458e18  # speed of light in Angstrom/sec
H = 6.62620E-27    # Planck's constant in ergs * sec

HC = H * C
ABZERO = -48.60    # magnitude zero points
STZERO = -21.10


# This needs to be a factory function in order to return an object
# of the correct subclass
def Units(uname):
    """Generate a unit object.

    Parameters
    ----------
    uname : str
        Wavelength or flux unit name.

    Returns
    -------
    unit : `BaseUnit` or `None`
        Unit object. `None` means unitless.

    Raises
    ------
    ValueError
        Unknown unit name.

    """
    if isinstance(uname,BaseUnit):
        return uname
    else:
        try:
            if issubclass(uname,BaseUnit):
                return uname()
        except TypeError:

            try:
                return factory(uname)
            except KeyError:
                if uname == str(None):
                    return None
                else:
                    raise ValueError("Unknown units %s"%uname)

#......................................................................
def ismatch(a,b):
    """Method to allow smart comparisons between classes, instances,
    and string representations of units and give the right answer.
    For internal use only."""
    #Try the easy case
    if a == b:
        return True
    else:
        #Try isinstance in both orders
        try:
            if isinstance(a,b):
                return True
        except TypeError:
            try:
                if isinstance(b,a):
                    return True
            except TypeError:
                #Try isinstance(a, type(b)) in both orders
                try:
                    if isinstance(a,type(b)):
                        return True
                except TypeError:
                    try:
                        if isinstance(b,type(a)):
                            return True
                    except TypeError:
                        #Try the string representation
                        if str(a).lower() == str(b).lower():
                            return True
                        else:
                            return False

#......................................................................
#Base classes

class BaseUnit(object):
    """Base class for all units.

    Parameters
    ----------
    uname : str
        Unit name.

    Attributes
    ----------
    name
        Same as input ``uname``.

    Dispatch : dict or `None`
        This is used by sub-classes for unit conversion by mapping target unit name to the relevant conversion method.

    """
    def __init__(self,uname):
        self.Dispatch=None
        self.name=uname

    def __str__(self):
        return self.name

    def Convert(self,wave,flux,target_units):
        """Perform unit conversion.

        .. note::

            This is only applicable to some of the available flux conversions.
            All other sub-classes must re-implement this method.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        target_units : str
            Unit to convert to.

        Returns
        -------
        result : number or array_like
            Converted values.

        Raises
        ------
        TypeError
            Conversion to given unit is not allowed.

        """
        #This signature is appropriate for fluxes, not waves
        try:
            return self.Dispatch[target_units.lower()](wave,flux)
        except KeyError:
            raise TypeError("%s cannot be converted to %s"%(self.name,
                                                            target_units))


class WaveUnits(BaseUnit):
    """Base unit for :ref:`wavelength <pysynphot-wave-units>`.

    Since Angstrom is the internal unit used by **pysynphot**
    calculations, a wavelength unit can always convert to/from
    Angstrom. Conversion between two arbitrary units uses
    Angstrom as the intermediate unit.

    Attributes
    ----------
    name : `None`
        To be set by sub-class of a specific wavelength unit.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    """
    def __init__(self):
        self.name=None
        self.isFlux = False
        self.Dispatch = {'angstrom' : self.ToAngstrom}

    def Convert(self,wave,target_units):
        """Perform unit conversion.

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        target_units : str
            Unit to convert to.

        Returns
        -------
        result : number or array_like
            Converted values.

        Raises
        ------
        TypeError
            Conversion to given unit is not allowed.

        """
        try:
            return self.Dispatch[target_units.lower()](wave)
        except KeyError:
            raise TypeError("%s cannot be converted to %s"%(self.name,
                                                            target_units))

    def ToAngstrom(self,wave):
        """This is implemented by sub-class."""
        raise NotImplementedError("Required method ToAngstrom not yet implemented")


class FluxUnits(BaseUnit):
    """Base unit for :ref:`flux <pysynphot-flux-units>`.

    Since ``photlam`` is the internal unit used by **pysynphot**
    calculations, a flux unit can always convert to/from
    ``photlam``. Conversion between two arbitrary units uses
    ``photlam`` as the intermediate unit.

    .. note::

        To support source spectrum :ref:`renormalization <pysynphot-renorm>`
        without introducing circular import, all supported flux units
        must have their ``StdSpectrum`` attributes defined separately
        in :func:`~pysynphot.renorm.DefineStdSpectraForUnits`.

    Attributes
    ----------
    name : `None`
        To be set by sub-class of a specific flux unit.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux : bool
        This is always `True`.

    isMag : bool
        This is `True` if this is a magnitude.

    isDensity : bool
        This is `True` *except* for counts and ``obmag``.

    nativewave : `WaveUnits`
        Native wavelength unit associated with the flux unit. This is for informational purpose only.

    """
    def __init__(self):
        self.isFlux = True
        self.isMag = False
        self.isDensity = True #False for counts and obmag
        self.name=None
        self.Dispatch = {'photlam':self.ToPhotlam}
        self.nativewave = Angstrom
        #self.StdSpectrum = None
        #...StdSpectrum is a placeholder. Actual values for the attributes
        # be defined in the renorm.py module; they can't be done here
        # because of a circular import problem. If you add a new fluxunit
        # in this file, you must define its StdSpectrum in renorm.py.

    def Convert(self, wave, flux, target_units, area=None):
        """Perform unit conversion.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        target_units : str
            Unit to convert to.

        area : number or `None`
            Telescope :ref:`area <pysynphot-area>`, if applicable.
            This is only needed for conversions involving counts or ``obmag``.

        Returns
        -------
        result : number or array_like
            Converted values.

        Raises
        ------
        TypeError
            Conversion to given unit is not allowed.

        """
        try:
            return self.Dispatch[target_units](wave, flux, area=area)
        except KeyError:
            raise TypeError("%s is not a valid flux unit" % (target_units))

    def ToPhotlam(self, wave, flux, area=None):
        """This is implemented by sub-class."""
        raise NotImplementedError("Required method ToPhotlam not yet implemented")


class LogFluxUnits(FluxUnits):
    """Base class for :ref:`magnitude <pysynphot-units-counts-mags>`,
    which often requires special handling.

    Attributes
    ----------
    name, zeropoint : `None`
        To be set by sub-class of a specific magnitude unit.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isMag : bool
        This is always `True`.

    isDensity : bool
        This is `True` *except* for ``obmag``.

    nativewave : `WaveUnits`
        Native wavelength unit associated with the flux unit. This is for informational purpose only.

    linunit : `None`
        Corresponding linear flux unit to be set by sub-class.

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.isMag=True
        self.linunit=None
        self.zeropoint=None


#.............................................................
# Internal wavelength units are Angstroms, so it is smarter than the others
class Angstrom(WaveUnits):
    """Class to handle Angstrom unit.

    Since Angstrom is the internal wavelength unit, it can convert
    to all the other supported units.

    Attributes
    ----------
    name : str
        This is always 'angstrom'.

    Dispatch : dict
        Defines conversion to all supported wavelength units.

    isFlux : bool
        This is always `False`.

    """
    def __init__(self):
        WaveUnits.__init__(self)
        self.name = 'angstrom'
        self.Dispatch = {'angstrom' : self.ToAngstrom,
                         'angstroms' : self.ToAngstrom,
                         'nm': self.ToNm,
                         'micron': self.ToMicron,
                         'microns': self.ToMicron,
                         '1/um': self.ToInverseMicron,
                         'inversemicron': self.ToInverseMicron,
                         'inversemicrons': self.ToInverseMicron,
                         'mm': self.ToMm,
                         'cm': self.ToCm,
                         'm': self.ToMeter,
                         'hz': self.ToHz}


    def ToAngstrom(self, wave):
        """Convert to Angstrom.

        Since there is no real conversion necessary, this returns
        a copy of input (if array) or just the input (if scalar).
        An input array is copied to avoid modifying the input
        in subsequent **pysynphot** processing.

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        if hasattr(wave,'copy'):
          return wave.copy()      # to avoid writing over any internal wave objects
        else:
          return wave             # probably a scalar

    def ToNm(self, wave):
        """Convert to nm.

        .. math::

            \\textnormal{nm} = 10^{-1} \\; \\AA

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return wave / 10.0

    def ToMicron(self, wave):
        """Convert to micron.

        .. math::

            \\mu \\textnormal{m} = 10^{-4} \\; \\AA

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return wave * 1.0e-4

    def ToInverseMicron(self, wave):
        """Convert to inverse micron.

        .. math::

            \\mu \\textnormal{m}^{-1} = 10^{4} \\; \\AA^{-1}

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return 1.0e4/wave

    def ToMm(self, wave):
        """Convert to mm.

        .. math::

            \\textnormal{mm} = 10^{-7} \\; \\AA

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return wave * 1.0e-7

    def ToCm(self, wave):
        """Convert to cm.

        .. math::

            \\textnormal{cm} = 10^{-8} \\; \\AA

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return wave * 1.0e-8

    def ToMeter(self, wave):
        """Convert to meter.

        .. math::

            \\textnormal{m} = 10^{-10} \\; \\AA

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return wave * 1.0e-10

    def ToHz(self, wave):
        """Convert to Hz.

        .. math::

            \\textnormal{Hz} = \\frac{c}{\\AA}

        where :math:`c` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return C / wave


#........................................................................
# Internal flux units = Photlam, so it is smarter than the others
class Photlam(FluxUnits):
    """Class to handle ``photlam`` unit.

    Since ``photlam`` is the internal flux unit, it can convert
    to all the other supported units.

    .. math::

        \\textnormal{photlam} = \\textnormal{photon} \\; \\textnormal{s}^{-1} \\; \\textnormal{cm}^{-2} \\; \\AA^{-1}

    Attributes
    ----------
    name : str
        This is always 'photlam'.

    Dispatch : dict
        Defines conversion to all supported flux units.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Angstrom` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'photlam'
        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'photnu': self.ToPhotnu,
                         'jy': self.ToJy,
                         'mjy': self.TomJy,
                         'mujy': self.TomuJy,
                         'microjy': self.TomuJy,
                         'ujy': self.TomuJy,
                         'njy': self.TonJy,
                         'nanojy': self.TonJy,
                         'abmag': self.ToABMag,
                         'stmag': self.ToSTMag,
                         'obmag': self.ToOBMag,
                         'vegamag': self.ToVegaMag,
                         'counts': self.ToCounts,
                         'counts': self.ToCounts}
        self.nativewave = Angstrom

    def unitResponse(self, band):
        """Put a flat spectrum of 1 photlam through this band and integrate.
        This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,0,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        total = band.trapezoidIntegration(band.wave, band.throughput)
        return 1.0/total

    def ToFlam(self, wave, flux, **kwargs):
        """Convert to ``flam``.

        .. math::

            \\textnormal{flam} = \\frac{hc}{\\lambda} \\; \\textnormal{photlam}

        where :math:`h` and :math:`c` are as defined in
        :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return HC * flux / wave

    def ToFnu(self, wave, flux, **kwargs):
        """Convert to ``fnu``.

        .. math::

            \\textnormal{fnu} = h \\lambda \\; \\textnormal{photlam}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return H * flux * wave

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        Since there is no real conversion necessary, this returns
        a copy of input flux (if array) or just the input (if scalar).
        An input array is copied to avoid modifying the input
        in subsequent **pysynphot** processing.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength (not used) and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        if hasattr(flux,'copy'):
          return flux.copy()  # No conversion, just copy the array.
        else:
          return flux         # probably a scalar

    def ToPhotnu(self, wave, flux, **kwargs):
        """Convert to ``photnu``.

        .. math::

            \\textnormal{photnu} = \\frac{\\lambda^{2}}{c} \\; \\textnormal{photlam}

        where :math:`c` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return flux * wave * wave / C

    def ToJy(self, wave, flux, **kwargs):
        """Convert to Jy.

        .. math::

            \\textnormal{Jy} = 10^{23} h \\lambda \\; \\textnormal{photlam}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return 1.0e+23 * H * flux * wave

    def TomJy(self, wave, flux, **kwargs):
        """Convert to mJy.

        .. math::

            \\textnormal{mJy} = 10^{26} h \\lambda \\; \\textnormal{photlam}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return 1.0e+26 * H * flux * wave

    def TomuJy(self, wave, flux, **kwargs):
        """Convert to :math:`\\mu \\textnormal{Jy}`.

        .. math::

            \\mu \\textnormal{Jy} = 10^{29} h \\lambda \\; \\textnormal{photlam}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return 1.0e+29 * H * flux * wave

    def TonJy(self, wave, flux, **kwargs):
        """Convert to nJy.

        .. math::

            \\textnormal{nJy} = 10^{32} h \\lambda \\; \\textnormal{photlam}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return 1.0e+32 * H * flux * wave

    def ToABMag(self, wave, flux, **kwargs):
        """Convert to ``abmag``.

        .. math::

            \\textnormal{AB}_{\\nu} = -2.5 \\; \\log(h \\lambda \\; \\textnormal{photlam}) - 48.6

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        arg = H * flux * wave
        return -1.085736 * N.log(arg) + ABZERO

    def ToSTMag(self, wave, flux, **kwargs):
        """Convert to ``stmag``.

        .. math::

            \\textnormal{ST}_{\\lambda} = -2.5 \\; \\log(\\frac{hc}{\\lambda} \\; \\textnormal{photlam}) - 21.1

        where :math:`h` and :math:`c` are as defined in
        :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        arg = H * C * flux / wave
        return -1.085736 * N.log(arg) + STZERO

    def ToOBMag(self, wave, flux, area=None):
        """Convert to ``obmag``.

        .. math::

            \\textnormal{obmag} = -2.5 \\; \\log(\\delta \\lambda \\; \\times \\; \\textnormal{area} \\; \\times  \\; \\textnormal{photlam})

        where :math:`\\delta \\lambda` represent bin widths derived from
        :func:`~pysynphot.binning.calculate_bin_edges` and
        :func:`~pysynphot.binning.calculate_bin_widths`, using the input
        wavelength values as bin centers.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        area : number or `None`
            Telescope collecting area. If not given, default value from
            :ref:`pysynphot-refdata` is used.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        area = area if area else refs.PRIMARY_AREA
        bin_widths = \
            binning.calculate_bin_widths(binning.calculate_bin_edges(wave))
        arg = flux * bin_widths * area
        return -1.085736 * N.log(arg)

    def ToVegaMag(self, wave, flux, **kwargs):
        """Convert to ``vegamag``.

        .. math::

            \\textnormal{vegamag} = -2.5 \\; \\log(\\frac{\\textnormal{photlam}}{f_{\\textnormal{Vega}}})

        where :math:`f_{\\textnormal{Vega}}` is the flux of
        :ref:`pysynphot-vega-spec` resampled at given wavelength values
        and converted to ``photlam``.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        from . import spectrum
        resampled = spectrum.Vega.resample(wave)
        normalized = flux / resampled._fluxtable
        return -2.5 * N.log10(normalized)

    def ToCounts(self, wave, flux, area=None):
        """Convert to counts.

        .. math::

            \\textnormal{counts} = \\delta \\lambda \\; \\times \\; \\textnormal{area} \\; \\times  \\; \\textnormal{photlam}

        where :math:`\\delta \\lambda` represent bin widths derived from
        :func:`~pysynphot.binning.calculate_bin_edges` and
        :func:`~pysynphot.binning.calculate_bin_widths`, using the input
        wavelength values as bin centers.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        area : number or `None`
            Telescope collecting area. If not given, default value from
            :ref:`pysynphot-refdata` is used.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        area = area if area else refs.PRIMARY_AREA
        bin_widths = \
            binning.calculate_bin_widths(binning.calculate_bin_edges(wave))
        return flux * bin_widths * area


#................................................................
#Other wavelength units

class Hz(WaveUnits):
    """Class to handle Hz unit.

    Attributes
    ----------
    name : str
        This is always 'hz'.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    """
    def __init__(self):
        WaveUnits.__init__(self)
        self.name='hz'

    def ToAngstrom(self, wave):
        """Convert to Angstrom.

        .. math::

            \\AA = \\frac{c}{\\textnormal{Hz}}

        where :math:`c` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return C / wave


class InverseMicron(WaveUnits):
    """Class to handle inverse micron unit.

    Attributes
    ----------
    name : str
        This is always '1/um'.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    """
    def __init__(self):
        WaveUnits.__init__(self)
        self.name = '1/um'

    def ToAngstrom(self, wave):
        """Convert to Angstrom.

        .. math::

            \\AA = \\frac{10^{4}}{\\mu \\textnormal{m}^{-1}}

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return 1.0e4/wave


# Encapsulates some easy unit-conversion machinery. Angstrom
# is not subclassed from here because it needs to be especially smart in
# other ways. (Although multiple inheritence might be possible.)
class _MetricWavelength(WaveUnits):
    """Class to handle meter unit and its prefixes.

    .. note::

        `Angstrom` is not a sub-class of this because as an
        internal unit, it requires special handling.

    Attributes
    ----------
    name : `None`
        To be set by sub-class of a specific wavelength unit.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    """
    def ToAngstrom(self,wave):
        """Convert to Angstrom.

        Conversion is simply the input values multiplied
        by a factor specific to its sub-class.

        Parameters
        ----------
        wave : number or array_like
            Wavelength values to be used for conversion.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return wave*self.factor


class Nm(_MetricWavelength):
    """Class to handle nm unit.

    Attributes
    ----------
    name : str
        This is always 'nm'.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    factor : float
        Conversion factor. This is always 10.

    """
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'nm'
        self.factor = 10.0


class Micron(_MetricWavelength):
    """Class to handle micron unit.

    Attributes
    ----------
    name : str
        This is always 'micron'.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    factor : float
        Conversion factor. This is always :math:`10^{4}`.

    """
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'micron'
        self.factor = 1.0e4


class Mm(_MetricWavelength):
    """Class to handle mm unit.

    Attributes
    ----------
    name : str
        This is always 'mm'.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    factor : float
        Conversion factor. This is always :math:`10^{7}`.

    """
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'mm'
        self.factor = 1.0e7


class Cm(_MetricWavelength):
    """Class to handle cm unit.

    Attributes
    ----------
    name : str
        This is always 'cm'.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    factor : float
        Conversion factor. This is always :math:`10^{8}`.

    """
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'cm'
        self.factor = 1.0e8


class Meter(_MetricWavelength):
    """Class to handle meter unit.

    Attributes
    ----------
    name : str
        This is always 'm'.

    Dispatch : dict
        Defines conversion to Angstrom.

    isFlux : bool
        This is always `False`.

    factor : float
        Conversion factor. This is always :math:`10^{10}`.

    """
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'm'
        self.factor = 1.0e10


#................................................................
#Other flux units

class Flam(FluxUnits):
    """Class to handle ``flam`` unit.

    .. math::

        \\textnormal{flam} = \\textnormal{erg} \\; \\textnormal{s}^{-1} \\; \\textnormal{cm}^{-2} \\; \\AA^{-1}

    Attributes
    ----------
    name : str
        This is always 'flam'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Angstrom` by default.  (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name='flam'
        self.nativewave = Angstrom

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{\\lambda}{hc} \\; \\textnormal{flam}

        where :math:`h` and :math:`c` are as defined in
        :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return flux * wave / HC

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,1,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput*wave)
        modtot = total / (H*C)
        return 1.0/modtot


class Photnu(FluxUnits):
    """Class to handle ``photnu`` unit.

    .. math::

        \\textnormal{photnu} = \\textnormal{photon} \\; \\textnormal{s}^{-1} \\; \\textnormal{cm}^{-2} \\; \\textnormal{Hz}^{-1}

    Attributes
    ----------
    name : str
        This is always 'photnu'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Hz` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'photnu'
        self.nativewave = Hz

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{c}{\\lambda^{2}} \\; \\textnormal{photnu}

        where :math:`c` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return C * flux / (wave * wave)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,-2,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput/(wave*wave))
        modtot = total/C
        return 1.0/modtot


class Fnu(FluxUnits):
    """Class to handle ``fnu`` unit.

    .. math::

        \\textnormal{fnu} = \\textnormal{erg} \\; \\textnormal{s}^{-1} \\textnormal{cm}^{-2} \\textnormal{Hz}^{-1}

    Attributes
    ----------
    name : str
        This is always 'fnu'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Hz` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'fnu'
        self.nativewave = Hz

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{1}{h \\lambda} \\; \\textnormal{fnu}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return flux /wave / H

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,-1,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput/wave)
        modtot = total/H
        return 1.0/modtot


class Jy(FluxUnits):
    """Class to handle Jy unit.

    .. math::

        \\textnormal{Jy} = 10^{-23} \\; \\textnormal{erg} \\; \\textnormal{s}^{-1} \\; \\textnormal{cm}^{-2} \\textnormal{Hz}^{-1}

    Attributes
    ----------
    name : str
        This is always 'jy'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Hz` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'jy'
        self.nativewave = Hz

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{10^{-23}}{h \\lambda} \\; \\textnormal{Jy}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return flux / wave * (1.0e-23 / H)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,-1,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput/wave)
        modtot = total * (1.0e-23/H)
        return 1.0/modtot


class mJy(FluxUnits):
    """Class to handle mJy unit.

    .. math::

        \\textnormal{mJy} = 10^{-26} \\; \\textnormal{erg} \\; \\textnormal{s}^{-1} \\; \\textnormal{cm}^{-2} \\textnormal{Hz}^{-1}

    Attributes
    ----------
    name : str
        This is always 'mjy'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Hz` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'mjy'
        self.nativewave = Hz

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{10^{-26}}{h \\lambda} \\; \\textnormal{mJy}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return flux / wave * (1.0e-26 / H)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,-1,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput/wave)
        modtot = total * (1.0e-26/H)
        return 1.0/modtot


class muJy(FluxUnits):	# New
    """Class to handle :math:`\\mu \\textnormal{Jy}` unit.

    .. math::

        \\mu \\textnormal{Jy} = 10^{-29} \\; \\textnormal{erg} \\; \\textnormal{s}^{-1} \\; \\textnormal{cm}^{-2} \\textnormal{Hz}^{-1}

    Attributes
    ----------
    name : str
        This is always 'mujy'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Hz` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'mujy'
        self.nativewave = Hz

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{10^{-29}}{h \\lambda} \\; \\mu \\textnormal{Jy}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return flux / wave * (1.0e-29 / H)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput/wave)
        modtot = total * (1.0e-29/H)
        return 1.0/modtot


class nJy(FluxUnits):  # New
    """Class to handle nJy unit.

    .. math::

        \\textnormal{nJy} = 10^{-32} \\; \\textnormal{erg} \\; \\textnormal{s}^{-1} \\; \\textnormal{cm}^{-2} \\textnormal{Hz}^{-1}

    Attributes
    ----------
    name : str
        This is always 'njy'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isDensity : bool
        This is always `True`.

    isMag : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Hz` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'njy'
        self.nativewave = Hz

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{10^{-32}}{h \\lambda} \\; \\textnormal{nJy}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return flux / wave * (1.0e-32 / H)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput/wave)
        modtot = total * (1.0e-32/H)
        return 1.0/modtot


class ABMag(LogFluxUnits):
    """Class to handle ``abmag`` unit.
    See :ref:`pysynphot-units-counts-mags` for more details.

    Attributes
    ----------
    name : str
        This is always 'abmag'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isMag, isDensity : bool
        This is always `True`.

    nativewave : `WaveUnits`
        This is `Angstrom` by default. (Not used.)

    linunit : `FluxUnits`
        Corresponding linear flux unit is `Fnu`.

    zeropoint : float
        Its zero point is as defined by ``pysynphot.units.ABZERO``.

    """
    def __init__(self):
        LogFluxUnits.__init__(self)
        self.name = 'abmag'
        self.linunit = Fnu()
        self.zeropoint = ABZERO

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            m = -0.4 \\; (\\textnormal{AB}_{\\nu} + 48.6)

            \\textnormal{photlam} = \\frac{10^{m}}{h \\lambda}

        where :math:`h` is as defined in :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return 1.0 / (H * wave) * 10.0**(-0.4 * (flux - ABZERO))

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,-1,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput/wave)
        modtot = total/H
        return 2.5*math.log10(modtot) + ABZERO


class STMag(LogFluxUnits):
    """Class to handle ``stmag`` unit.
    See :ref:`pysynphot-units-counts-mags` for more details.

    Attributes
    ----------
    name : str
        This is always 'stmag'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isMag, isDensity : bool
        This is always `True`.

    nativewave : `WaveUnits`
        This is `Angstrom` by default. (Not used.)

    linunit : `FluxUnits`
        Corresponding linear flux unit is `Flam`.

    zeropoint : float
        Its zero point is as defined by ``pysynphot.units.STZERO``.

    """
    def __init__(self):
        LogFluxUnits.__init__(self)
        self.name = 'stmag'
        self.linunit = Flam()
        self.zeropoint = STZERO

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            m = -0.4 \\; (\\textnormal{ST}_{\\lambda} + 21.1)

            \\textnormal{photlam} = \\frac{10^{m} \\lambda}{hc}

        where :math:`h` and :math:`c` are as defined in
        :ref:`pysynphot-constants`.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        return wave / H / C * 10.0**(-0.4 * (flux - STZERO))

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sumfilt(wave,1,band)
        # SUMFILT = Sum [ FILT(I) * WAVE(I) ** NPOW * DWAVE(I) ]
        wave=band.wave
        total = band.trapezoidIntegration(wave,band.throughput*wave)
        modtot = total/(H*C)
        return 2.5*math.log10(modtot) + STZERO


class OBMag(LogFluxUnits):
    """Class to handle ``obmag`` unit.
    See :ref:`pysynphot-units-counts-mags` for more details.

    Attributes
    ----------
    name : str
        This is always 'obmag'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isMag : bool
        This is always `True`.

    isDensity : bool
        This is always `False`.

    nativewave : `WaveUnits`
        This is `Angstrom` by default. (Not used.)

    linunit : `FluxUnits`
        Corresponding linear flux unit is `Counts`.

    zeropoint : float
        This is always 0.

    """
    def __init__(self):
        LogFluxUnits.__init__(self)
        self.name = 'obmag'
        self.linunit = Counts()
        self.zeropoint = 0.0
        self.isDensity = False

    def ToPhotlam(self, wave, flux, area=None):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{10^{-0.4 \\; \\textnormal{obmag}}}{\\delta \\lambda \\; \\times \\; \\textnormal{area}}

        where :math:`\\delta \\lambda` represent bin widths derived from
        :func:`~pysynphot.binning.calculate_bin_edges` and
        :func:`~pysynphot.binning.calculate_bin_widths`, using the input
        wavelength values as bin centers.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        area : number or `None`
            Telescope collecting area. If not given, default value from
            :ref:`pysynphot-refdata` is used.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        area = area if area else refs.PRIMARY_AREA
        bin_widths = \
            binning.calculate_bin_widths(binning.calculate_bin_edges(wave))

        return 10.0**(-0.4 * flux) / (bin_widths * area)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sum = asumr(band,nwave)
        total = band.throughput.sum()
        return 2.5*math.log10(total)


class VegaMag(LogFluxUnits):
    """Class to handle ``vegamag`` unit.
    See :ref:`pysynphot-units-counts-mags` for more details.

    Attributes
    ----------
    name : str
        This is always 'vegamag'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux, isMag, isDensity : bool
        This is always `True`.

    nativewave : `WaveUnits`
        This is `Angstrom` by default. (Not used.)

    linunit, zeropoint : `None`
        This is not used.

    vegaspec : `~pysynphot.spectrum.SourceSpectrum`
        This is set to :ref:`pysynphot-vega-spec`.

    """
    def __init__(self):
        from . import spectrum
        LogFluxUnits.__init__(self)
        self.name = 'vegamag'
        self.vegaspec = spectrum.Vega

    def ToPhotlam(self, wave, flux, **kwargs):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = 10^{-0.4 \\; \\textnormal{vegamag}} \\; f_{\\textnormal{Vega}}

        where :math:`f_{\\textnormal{Vega}}` is the flux of
        :ref:`pysynphot-vega-spec` resampled at given wavelength values
        and converted to ``photlam``.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        kwargs : dict
            Extra keywords (not used).

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        resampled = self.vegaspec.resample(wave)
        return resampled.flux * 10.0**(-0.4 * flux)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        sp=band*self.vegaspec
        total=sp.integrate()
        return 2.5*math.log10(total)


class Counts(FluxUnits):
    """Class to handle counts unit.
    See :ref:`pysynphot-units-counts-mags` for more details.

    Attributes
    ----------
    name : str
        This is always 'counts'.

    Dispatch : dict
        Defines conversion to ``photlam``.

    isFlux : bool
        This is always `True`.

    isMag, isDensity : bool
        This is always `False`.

    nativewave : `WaveUnits`
         This is `Angstrom` by default. (Not used.)

    """
    def __init__(self):
        FluxUnits.__init__(self)
        self.name = 'counts'
        self.isDensity = False

    def ToPhotlam(self, wave, flux, area=None):
        """Convert to ``photlam``.

        .. math::

            \\textnormal{photlam} = \\frac{\\textnormal{counts}}{\\delta \\lambda \\; \\times \\; \\textnormal{area}}

        where :math:`\\delta \\lambda` represent bin widths derived from
        :func:`~pysynphot.binning.calculate_bin_edges` and
        :func:`~pysynphot.binning.calculate_bin_widths`, using the input
        wavelength values as bin centers.

        Parameters
        ----------
        wave, flux : number or array_like
            Wavelength and flux values to be used for conversion.

        area : number or `None`
            Telescope collecting area. If not given, default value from
            :ref:`pysynphot-refdata` is used.

        Returns
        -------
        result : number or array_like
            Converted values.

        """
        area = area if area else refs.PRIMARY_AREA
        bin_widths = \
            binning.calculate_bin_widths(binning.calculate_bin_edges(wave))

        return flux / (bin_widths * area)

    def unitResponse(self,band):
        """This is used internally for :ref:`pysynphot-formula-effstim`
        calculations."""
        #sum = asumr(band,nwave)
        total = band.throughput.sum()
        return 1.0/total


################   Factory for Units subclasses.   #####################
def factory(uname, *args, **kwargs):
    unitsClasses = {'flam'      : Flam,
                    'fnu'       : Fnu,
                    'photlam'   : Photlam,
                    'photnu'    : Photnu,
                    'jy'        : Jy,
                    'mjy'       : mJy,
                    'mujy'      : muJy,
                    'microjy'   : muJy,
                    'ujy'       : muJy,
                    'njy'       : nJy,
                    'nanojy'    : nJy,
                    'abmag'     : ABMag,
                    'stmag'     : STMag,
                    'obmag'     : OBMag,
                    'vegamag'   : VegaMag,
                    'counts'    : Counts,
                    'count'     : Counts,
                    'angstrom'  : Angstrom,
                    'angstroms' : Angstrom,
                    'nm'        : Nm,
                    'micron'    : Micron,
                    'microns'   : Micron,
                    'um'        : Micron,
                    'inversemicron': InverseMicron,
                    'inversemicrons': InverseMicron,
                    '1/um'      : InverseMicron,
                    'mm'        : Mm,
                    'cm'        : Cm,
                    'm'         : Meter,
                    'meter'     : Meter,
                    'hz'        : Hz}

    key=uname.lower()
    ans= unitsClasses[key]()
    return ans
