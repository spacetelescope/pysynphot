"""This module handles selection of the appropriate
:ref:`wavelength table <pysynphot-wavelength-table>` for a given
:ref:`observation mode <pysynphot-obsmode-bandpass>`.
This is the same selection as used by ETC.

Its ``wavecat_file`` (see below) can contain a mix of the following:

* Name of the ASCII file containing the wavelength values. The filename
  can contain IRAF-style path shortcut. The file must only contain one
  column, with a single wavelength value in Angstrom in each row. The file
  can also contain comment lines that begin with "#", which will be skipped.
* A string of comma-separated coefficients that describe how to construct
  the wavelength table in Angstrom, in the format of ``(c0,c1[,c2[,c3]])``,
  where ``c2`` and ``c3`` are optional. They are used for the following
  computation. Basically, the wavelength table runs from ``c0`` to ``c1``,
  with constant :math:`\\delta \\lambda` if ``c2`` is undefined, or if ``c2``
  is given but not ``c3``, or variable :math:`\\delta \\lambda` if both ``c2``
  and ``c3`` are given:

  .. math::

    c_{2} = \\left \\{
              \\begin{array}{ll}
                c_{2} & : \\textnormal{if given} \\\\
                (c_{1} - c_{0})/1999 & : \\textnormal{else, where 1999 was taken from IRAF STSDAS SYNPHOT}
              \\end{array}
            \\right.

    c_{3} = \\left \\{
              \\begin{array}{ll}
                c_{3} & : \\textnormal{if given} \\\\
                c_{2} & : \\textnormal{else}
              \\end{array}
            \\right.

    n = \\textnormal{int}(\\frac{2 \\; (c_{1} - c_{0})}{c_{3} + c_{2}}) + 1

    a = \\frac{0.25 \\; (c_{3}^{2} - c_{2}^{2})}{c_{1} - c_{0}}

    \\lambda_{i=0,n-1} = (a i + c_{2}) i + c_{0}

Example contents of a ``wavecat_file``::

    # OBSMODE           FILENAME_OR_COEFFS
    stis,e140h,c1598    (1497.0,1699.0,0.0066,0.0075)
    stis,g230l          (1568.0,3184.0,1.6)
    stis,prism          synphot$data/prism.dat
    stis,prism,c1200    synphot$data/prism.dat

**Global Variables**

* ``pysynphot.wavetable.wavecat_file`` - This is the same as
  ``pysynphot.locations.wavecat``. It is the data file used in this module.

* ``pysynphot.wavetable.wavetable`` - This is a `Wavetable` object created
  using ``pysynphot.wavetable.wavecat_file``.

"""
from __future__ import absolute_import, division

import re
import numpy as N
from . import locations


# Class to handle wavecat.dat initialization and access. (This class
# may need a better name; wavetable and waveset are awfully close.)
# Also, put the default waveset into this object with a key of NONE.
class Wavetable(object):
    """Class to handle :ref:`wavelength table <pysynphot-wavelength-table>`.

    :py:meth:`~object.__getitem__` is used to look up the wavelength table.
    It raises ``KeyError`` or ``ValueError`` if look-up fails.
    The look-up result is resolved into actual wavelength values by
    :meth:`~pysynphot.observationmode.BaseObservationMode.bandWave`.

    Parameters
    ----------
    fname : str
        Data file.

    Attributes
    ----------
    file
        Same as input ``fname``.

    lookup : dict
        Look-up table using ``obsmode`` string as key. This is used by default for direct match.

    setlookup : dict
        Same as ``lookup`` but the ``obsmode`` string is converted into a frozen set consisting of its components. This is used for partial look-up if there is no direct match.

    Raises
    ------
    ValueError
        Failed to parse input file.

    Examples
    --------
    >>> wavetab = S.wavetable.Wavetable(S.wavetable.wavecat_file)
    >>> wavetab['stis,g230l']
    '(1568.0,3184.0,1.6)'
    >>> wavetab['stis,prism']
    'synphot$data/prism.dat'

    """
    def __init__(self, fname):
        self.file=fname
        self.lookup={}
        self.setlookup={}
        fs = open(wavecat_file, mode='r')
        lines = fs.readlines()
        fs.close()

        regx = re.compile(r'\S+', re.IGNORECASE)
        for line in lines:
            if not line.startswith("#"):
                try:
                    [obm,coeff] = regx.findall(line)
                    self.lookup[obm] = coeff
                    self.setlookup[frozenset(obm.split(','))] = coeff
                except ValueError:
                    raise ValueError("Error processing line: %s"%line)

    def __getitem__(self, key):
        """Fairly smart lookup: if no exact match, find the most complete
        match."""
        ans=None
        try:
            #Try an exact match
            ans = self.lookup[key]
        except KeyError:
            ans=None
            #Try a setwise match.
            #The correct key will be a subset of the input key.
            setkey=set(key.split(','))
            candidates=[]
            for k in self.setlookup:
                if k.issubset(setkey):
                    candidates.append(k)
            #We may have 1, 0, or >1 candidates.
            if len(candidates) == 1:
                ans = self.setlookup[candidates[0]]

            elif len(candidates) == 0:
                raise KeyError("%s not found in %s; candidates:%s"%(setkey,self.file,str(candidates)))

            elif len(candidates) > 1:
                setlens=N.array([len(k) for k in candidates])
                srtlen=setlens.argsort()
                k,j=srtlen[-2:]
                if setlens[k] == setlens[j]:
                    #It's really ambiguous
                    raise ValueError("Ambiguous key %s; candidates %s"%(setkey, candidates))
                else:
                    #We have a winner
                    k=candidates[srtlen[-1]]
                    ans=self.setlookup[k]
        return ans


wavecat_file=locations.wavecat
wavetable=Wavetable(wavecat_file)
