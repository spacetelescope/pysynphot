"""
Package:  Astrolib Specman

Purpose:
========

Object-oriented replacement for STSDAS synphot package.

This __init__ file is used to expose the desired elements of the user
interface for interactive use.


Dependencies:
=============
numpy 1.0 or greater
pyfits 1.1 or greater
spark (syntax parser) (included in package tho; really dependency?)

Example
=======

>>> import specman as S
Astrolib Specman version 0.3d1

>>> #Read a spectrum from a file
>>> vega=S.FileSpectrum('alpha_lyr_stis_003.fits')
>>> print vega
alpha_lyr_stis_003.fits

"""


__version__ = '0.3d1'

#UI:
from spectrum import BlackBody, GaussianSource, UnitSpectrum
from spectrum import Powerlaw as PowerLaw
from spectrum import TabularSourceSpectrum as FileSpectrum

from spectrum import TabularSpectralElement as FileBandpass
from observationmode import ObservationMode as Obsmode
#.........this is incomplete; eventually I want an ObsBandpass

print "Astrolib Specman version %s"%__version__



def _test():
    import doctest
    doctest.testfile('__init__.py')

if __name__ == '__main__':
    _test()
