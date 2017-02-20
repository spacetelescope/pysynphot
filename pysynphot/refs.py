"""This module handles constants and look-up tables used in calculations.

**Global Variables**

* ``pysynphot.refs._default_waveset`` - Default wavelength set to use if no
  instrument-specific values found.
* ``pysynphot.refs._default_waveset_str`` - Description of the default
  wavelength set above.
* ``pysynphot.refs.PRIMARY_AREA`` - Telescope collecting area, i.e., the primary
  mirror, in :math:`\\textnormal{cm}^{2}`. The value for HST is 45238.93416.

These are used in `~pysynphot.observationmode` to look up throughput files for
a given bandpass:

* ``pysynphot.refs.GRAPHTABLE``
* ``pysynphot.refs.GRAPHDICT``
* ``pysynphot.refs.COMPTABLE``
* ``pysynphot.refs.COMPDICT``
* ``pysynphot.refs.THERMTABLE``
* ``pysynphot.refs.THERMDICT``

"""
from __future__ import print_function

import os.path
import warnings

import numpy as np

from .locations import irafconvert, _refTable

_default_waveset = None
_default_waveset_str = None

# Constants to hold tables.
GRAPHTABLE = ''
GRAPHDICT = {}
COMPTABLE = ''
COMPDICT = {}
THERMTABLE = ''
THERMDICT = {}

PRIMARY_AREA = 45238.93416  # cm^2 - default to HST mirror


def set_default_waveset(minwave=500, maxwave=26000, num=10000,
                        delta=None, log=True):
    """Set the default wavelength set, ``pysynphot.refs._default_waveset``.

    Parameters
    ----------
    minwave, maxwave : float, optional
        The start (inclusive) and end (exclusive) points of the wavelength set.
        Values should be given in linear space regardless of ``log``.

    num : int, optional
        The number of elements in the wavelength set.
        Only used if ``delta=None``.

    delta : float, optional
        Delta between values in the wavelength set.
        If ``log=True``, this defines wavelegth spacing in log space.

    log : bool, optional
        Determines whether the wavelength set is evenly spaced in log or linear
        space.

    """
    global _default_waveset
    global _default_waveset_str

    # Must be int for numpy>=1.12
    num = int(num)

    s = 'Min: %s, Max: %s, Num: %s, Delta: %s, Log: %s'

    if log and not delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, num, None, log)])

        logmin = np.log10(minwave)
        logmax = np.log10(maxwave)

        _default_waveset = np.logspace(logmin, logmax, num, endpoint=False)

    elif log and delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, None, delta, log)])

        logmin = np.log10(minwave)
        logmax = np.log10(maxwave)

        _default_waveset = 10 ** np.arange(logmin, logmax, delta)

    elif not log and not delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, num, None, log)])

        _default_waveset = np.linspace(minwave, maxwave, num, endpoint=False)

    elif not log and delta:
        s = s % tuple([str(x) for x in (minwave, maxwave, None, delta, log)])

        _default_waveset = np.arange(minwave, maxwave, delta)

    _default_waveset_str = s


def _set_default_refdata():
    """Default refdata set on import."""
    global GRAPHTABLE, COMPTABLE, THERMTABLE, PRIMARY_AREA
    # Component tables are defined here.

    try:
        GRAPHTABLE = _refTable(os.path.join('mtab','*_tmg.fits'))
        COMPTABLE  = _refTable(os.path.join('mtab','*_tmc.fits'))
    except IOError as e:
        GRAPHTABLE = None
        COMPTABLE = None
        warnings.warn('No graph or component tables found; '
                      'functionality will be SEVERELY crippled. ' + str(e))

    try:
        THERMTABLE = _refTable(os.path.join('mtab','*_tmt.fits'))
    except IOError as e:
        THERMTABLE = None
        warnings.warn('No thermal tables found, '
                      'no thermal calculations can be performed. ' + str(e))

    PRIMARY_AREA = 45238.93416  # cm^2 - default to HST mirror

    set_default_waveset()

#Do this on import
_set_default_refdata()


def setref(graphtable=None, comptable=None, thermtable=None,
           area=None, waveset=None):
    """Set default graph and component tables, primary area, and
    wavelength set.

    This is similar to setting ``refdata`` in IRAF STSDAS SYNPHOT.
    If all parameters set to `None`, they are reverted to software default.
    If any of the parameters are not `None`, they are set to desired
    values while the rest (if any) remain at current setting.

    Parameters
    ----------
    graphtable, comptable, thermtable : str or `None`
        Graph, component, and thermal table names, respectively,
        for `~pysynphot.observationmode` throughput look-up.
        Do not use "*" wildcard.

    area : float or `None`
        Telescope collecting area, i.e., the primary
        mirror, in :math:`\\textnormal{cm}^{2}`.

    waveset : tuple or `None`
        Parameters for :func:`set_default_waveset` as follow:
            * ``(minwave, maxwave, num)`` - This assumes log scale.
            * ``(minwave, maxwave, num, 'log')``
            * ``(minwave, maxwave, num, 'linear')``

    Raises
    ------
    ValueError
        Invalid ``waveset`` parameters.

    """
    global GRAPHTABLE, COMPTABLE, THERMTABLE, PRIMARY_AREA, GRAPHDICT, COMPDICT, THERMDICT

    GRAPHDICT = {}
    COMPDICT = {}
    THERMDICT = {}

    #Check for all None, which means reset
    kwds=set([graphtable,comptable,thermtable,area,waveset])
    if kwds == set([None]):
        #then we should reset everything.
        _set_default_refdata()
        return

    #Otherwise, check them all separately
    if graphtable is not None:
        GRAPHTABLE = irafconvert(graphtable)

    if comptable is not None:
        COMPTABLE = irafconvert(comptable)

    if thermtable is not None:
        THERMTABLE = irafconvert(thermtable)

    #Area is a bit different:
    if area is not None:
        PRIMARY_AREA = area

    if waveset is not None:
        if len(waveset) not in (3, 4):
            raise ValueError('waveset tuple must contain 3 or 4 values')

        minwave = waveset[0]
        maxwave = waveset[1]
        num = waveset[2]

        if len(waveset) == 3:
            log = True
        elif len(waveset) == 4:
            if waveset[3].lower() == 'log':
                log = True
            elif waveset[3].lower() == 'linear':
                log = False
            else:
                raise ValueError('fourth waveset option must be "log" or "linear"')

        set_default_waveset(minwave,maxwave,num,log=log)

    #That's it.
    return


def getref():
    """Current default values for graph and component tables, primary area,
    and wavelength set.

    .. note::

        Also see  :func:`setref`.

    Returns
    -------
    ans : dict
        Mapping of parameter names to their current values.

    """
    ans=dict(graphtable=GRAPHTABLE,
             comptable=COMPTABLE,
             thermtable=THERMTABLE,
             area=PRIMARY_AREA,
             waveset=_default_waveset_str)
    return ans


def showref():
    """Like :func:`getref` but print results to screen instead of returning
    a dictionary.

    """
    refdata = getref()
    for k, v in refdata.items():
        print("%10s: %s" % (k,v))
