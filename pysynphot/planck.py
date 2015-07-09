"""This module handles Planck's law of blackbody radiation.

**Global Variables**

* ``pysynphot.planck.H`` - Planck's constant in CGS units.
* ``pysynphot.planck.HS`` - Planck's constant in SI units.
* ``pysynphot.planck.C`` - Speed of light in SI units.
* ``pysynphot.planck.K`` - Boltzmann constant in SI units.

These are used in calculations to prevent floating point overflow, as defined
in IRAF STSDAS SYNPHOT ``bbfunc`` task:

* ``pysynphot.planck.LOWER``
* ``pysynphot.planck.UPPER``

These are constants used in :func:`llam_SI`:

* ``pysynphot.planck.C1`` - Power :math:`\\times` unit area per steradian.
* ``pysynphot.planck.C2``

This is used in :func:`bb_photlam_arcsec`:

* ``pysynphot.planck.F`` - Factor for conversion from
  :math:`\\textnormal{m}^{2} \\; \\textnormal{sr}^{-1} \\; \\textnormal{m}^{-1}` to
  :math:`\\textnormal{cm}^{2} \\; \\textnormal{arcsec}^{-2} \\; \\AA^{-1}`.

"""
from __future__ import division

import math
import numpy as N


H  = 6.6262E-27                # Planck's constant in cgs units
HS = 6.6262E-34                # Planck's constant in standard units
C  = 2.997925E+8               # speed of light in standard units
K  = 1.38062E-23               # Boltzmann constant in standard units

C1 = 2.0 * HS * C * C          # Power * unit area / steradian
C2 = HS * C / K

#  Anand's original comments for the F factor:
#
#       >>> af = 0.01 * 0.01    # per m^2  -->  per cm^2
#       >>> af
#       0.0001
#       >>> sf = 206265.0 * 206265.0
#       >>> sf = 1/sf
#       >>> sf                  # per sr  -->  per sqarcsec
#       2.3504386381829067e-11
#       >>> af * sf
#       2.3504386381829069e-15
#       >>> af * sf * 1.0e-10   # per m  -->  per Angstrom
#       2.3504386381829069e-25
#
F = 2.3504386381829069E-25     # convert from m^2/steradian/m to
                               # cm^2/sq.arcsec/A (see below)

LOWER = 1.0E-4                 # taken from synphot's bbfunc.
UPPER = 85.


def bbfunc(wave, temperature):
    """Evaluate Planck's law in ``photlam`` (per steradian).

    .. note::

        Adapted from IRAF STSDAS SYNPHOT ``bbfunc`` task.

    Parameters
    ----------
    wave : array_like
        Wavelength values in Angstrom.

    temperature : float
        Blackbody temperature in Kelvin.

    Returns
    -------
    result : array_like
        Blackbody radiation in ``photlam`` per steradian.

    """
    x = wave * temperature

    mask = N.where(x > 0.0, 1, 0)
    x = N.where(mask==1, 1.43883E8 / x, 0.0)

    factor = N.zeros(wave.shape, dtype=N.float64)

    mask1 = N.where(x < LOWER, 0, 1)
    factor = N.where(mask1 == 0, 2.0 / (x * (x + 2.0)), factor)

    mask2 = N.where(x < UPPER, 1, 0)
    mask = mask1 * mask2
    factor = N.where(mask == 1, 1.0 / (N.exp(x) - 1.0), factor)

    x = x * temperature / 1.95722E5
    x = factor * x * x * x

    return x / (H * wave)     # cgs -> photlam conversion


def llam_SI(wave, temperature):
    """Like :func:`bbfunc` but in SI units.

    .. note::

        Adapted from SSP code by Dr. Anand Sivaramakrishnan in
        IRAF STSDAS SYNPHOT.

    Parameters
    ----------
    wave : array_like
        Wavelength values in meters.

    temperature : float
        Blackbody temperature in Kelvin.

    Returns
    -------
    result : array_like
        Blackbody radiation in SI units.

    """
    exponent = C2 / (wave * temperature)

    result = N.zeros(wave.shape, dtype=N.float64)

    mask1 = N.where(exponent <= LOWER, 0, 1)
    result = N.where(mask1==0, (2.0 * C1 * (wave**-5.0)) / (exponent * (exponent + 2.0)), result)

    mask2 = N.where(exponent <= UPPER, 1, 0)
    mask = mask1 * mask2
    exponent = N.where(mask2==1, exponent, UPPER)
    expfactor = N.exp(exponent)
    result = N.where(mask==1, (C1 * (wave**-5.0) / (expfactor - 1.0)), result)

    return result


def bb_photlam_arcsec(wave, temperature):
    """Evaluate Planck's law in ``photlam`` per square arcsec.

    .. note::

        Uses :func:`llam_SI` for calculation, and then converts
        SI units back to CGS.

    Parameters
    ----------
    wave : array_like
        Wavelength values in Angstrom.

    temperature : float
        Blackbody temperature in Kelvin.

    Returns
    -------
    result : array_like
        Blackbody radiation in ``photlam`` per square arcsec.

    """
    lam = wave * 1.0E-10    # Angstrom -> meter

    return F * llam_SI(lam, temperature) / (HS * C / lam)
