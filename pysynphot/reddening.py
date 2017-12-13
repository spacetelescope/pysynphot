"""This module handles
:ref:`reddening laws and extinction <pysynphot-extinction>` calculations.

"""
from __future__ import absolute_import, division, print_function

from astropy.io import fits as pyfits
from .spectrum import ArraySpectralElement
from . import Cache
from . import extinction #temporary(?) backwards compatibility
from . import units


# https://github.com/spacetelescope/pysynphot/issues/44
class ExtinctionSpectralElement(ArraySpectralElement):
    """Like :class:`~pysynphot.spectrum.ArraySpectralElement` but
    with special ``waveset`` handling.
    """
    def GetWaveSet(self):
        """Extinction curve ``waveset`` should not be merged."""
        return None

    def _getWaveProp(self):
        """Return wavelength in user units."""
        wave = units.Angstrom().Convert(self._wavetable, self.waveunits.name)
        return wave

    wave = property(_getWaveProp, doc="Wavelength property.")

    def GetThroughput(self):
        return self.__call__(self._wavetable)

    throughput = property(GetThroughput, doc='Throughput property.')


class CustomRedLaw(object):
    """Class to handle reddening law.

    Parameters
    ----------
    wave : array_like
        Wavelength values.

    waveunits : str
        Wavelength unit, as accepted by `~pysynphot.units.Units`.
        By default, it is :math:`\\mu m^{-1}`.

    Avscaled : array_like
        Values of :math:`A(V)/E(B-V)`.

    name : str
        Short description of the reddening law.

    litref : str
        Literature reference of the reddening law.

    Attributes
    ----------
    wave, waveunits, name, litref
        Same as inputs.

    obscuration
        Same as input ``Avscaled``.

    """
    def __init__(self,
                 wave=None,
                 waveunits='InverseMicrons',
                 Avscaled=None,
                 name='Unknown Reddening Law',
                 litref=None):

        self.wave=wave
        self.waveunits=waveunits
        self.obscuration=Avscaled
        self.name=name
        self.litref=litref

    def reddening(self,extval):
        """Compute the reddening for the given extinction.

        .. math::

            A(V) = R(V) \\; \\times \\; E(B-V)

            \\textnormal{THRU} = 10^{-0.4 \\; A(V)}

        .. note::

            ``self.litref`` is passed into ``ans.citation``.

        Parameters
        ----------
        extval : float
            Value of :math:`E(B-V)` in magnitudes.

        Returns
        -------
        ans : `~pysynphot.spectrum.ArraySpectralElement`
            Extinction curve to apply to a source spectrum.

        """
        T = 10.0**(-0.4*extval*self.obscuration)
        ans = ExtinctionSpectralElement(wave=self.wave,
                                        waveunits=self.waveunits,
                                        throughput=T,
                                        name='%s(EBV=%g)'%(self.name, extval))
        ans.citation = self.litref
        return ans


class RedLaw(CustomRedLaw):
    """`CustomRedLaw` from a FITS file.

    Table must be in EXT 1 and contains the following columns:

    #. ``WAVELENGTH``
    #. ``Av/E(B-V)``

    Wavelength unit is extracted from ``TUNIT1`` keyword in EXT 1 header.
    The primary header (EXT 0) must have ``SHORTNM`` and ``LITREF`` keywords.

    Parameters
    ----------
    filename : str
        FITS table filename.

    Attributes
    ----------
    wave : array_like
        Wavelength values from the ``WAVELENGTH`` column in EXT 1.

    waveunits : str
        Value of ``TUNIT1`` in EXT 1 header.

    name : str
        Value of ``SHORTNM`` in EXT 0 header.

    litref : str
        Value of ``LITREF`` in EXT 0 header.

    obscuration
        Values from the ``Av/E(B-V)`` column in EXT 1.

    """
    def __init__(self,filename):
        f=pyfits.open(filename)
        d=f[1].data
        CustomRedLaw.__init__(self,
                              wave=d.field('wavelength'),
                              waveunits=f[1].header['tunit1'],
                              Avscaled=d.field('Av/E(B-V)'),
                              litref=f[0].header['litref'],
                              name=f[0].header['shortnm'])
        f.close()


def print_red_laws():
    """Print available extinction laws to screen.

    Available extinction laws are extracted from ``pysynphot.locations.EXTDIR``.
    The printed names may be used with :func:`Extinction`
    to retrieve available reddening laws.

    Examples
    --------
    >>> S.reddening.print_red_laws()
    name       reference
    --------   --------------------------------------------------------------
    None        Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 3.10.
    gal3        Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 3.10.
    lmc30dor    Gordon et al. (2003, ApJ, 594, 279) R_V = 2.76.
    lmcavg      Gordon et al. (2003, ApJ, 594, 279) R_V = 3.41.
    mwavg       Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 3.10.
    mwdense     Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 5.00.
    mwrv21      Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 2.1.
    mwrv4       Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 4.0.
    smcbar      Gordon et al. (2003, ApJ, 594, 279) R_V=2.74.
    xgalsb      Calzetti et al. (2000. ApJ, 533, 682)

    """
    laws = {}

    # start by converting the Cache.RedLaws file names to RedLaw objects
    # if they aren't already
    for k in Cache.RedLaws:
        if isinstance(Cache.RedLaws[k],str):
            Cache.RedLaws[k] = RedLaw(Cache.RedLaws[k])

        laws[str(k)] = Cache.RedLaws[k].litref

    # get the length of the longest name and litref
    maxname = max([len(name) for name in laws.keys()])
    maxref = max([len(ref) for ref in laws.values()])

    s = '%-' + str(maxname) + 's   %-' + str(maxref) + 's'

    print(s % ('name','reference'))
    print(s % ('-'*maxname,'-'*maxref))

    for k in sorted(laws.keys()):
        print(s % (k, laws[k]))


def Extinction(extval,name=None):
   """Generate extinction curve to be used with spectra.

    By default, :meth:`~CustomRedLaw.reddening` is used to
    generate the extinction curve. If a deprecated
    reddening law is given, then
    `~pysynphot.extinction.DeprecatedExtinction` is used
    instead.

   .. note::

       Reddening laws are cached in ``pysynphot.Cache.RedLaws``
       for better performance. Repeated calls to the same
       reddening law here returns the cached result.

   Parameters
   ----------
   extval : float
       Value of :math:`E(B-V)` in magnitudes.

   name : str or `None`
       Name of reddening law (see :func:`print_red_laws`).
       If `None` (default), the average Milky Way extinction
       (``'mwavg'``) will be used.

   Returns
   -------
   ext : `~pysynphot.spectrum.ArraySpectralElement` or `~pysynphot.extinction.DeprecatedExtinction`
       Extinction curve.

   Raises
   ------
   ValueError
       Invalid reddening law.

   Examples
   --------
   >>> ext = S.Extinction(0.3, 'mwavg')

   """
   try:
       ext=Cache.RedLaws[name].reddening(extval)
   except AttributeError:
       #The cache hasn't yet been filled.
       Cache.RedLaws[name]=RedLaw(Cache.RedLaws[name])
       ext=Cache.RedLaws[name].reddening(extval)
   except KeyError:
       #There's no reddening law by that name. See if we've been
       #given a filename from which we can read one.
       try:
           Cache.RedLaws[name]=RedLaw(name)
           ext=Cache.RedLaws[name].reddening(extval)
       except IOError:
           #If not, see if it's an old extinction law
           try:
               ext=extinction.DeprecatedExtinction(extval,name)
           except KeyError:
               raise ValueError('No extinction law has been defined for "%s", and no such file exists'%name)
   return ext
