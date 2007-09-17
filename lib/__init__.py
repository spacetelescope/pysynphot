"""
Package:  Astrolib Pysynphot

Purpose:
========

Object-oriented replacement for STSDAS synphot package.

This __init__ file is used to expose the desired elements of the user
interface for interactive use.


Dependencies:
=============
- numpy 1.0 or greater
- pyfits 1.1 or greater
- spark (syntax parser) (included in package tho; really dependency?)

Environment:
===========
The environment variable PYSYN_CDBS must be set.

Example
=======

>>> import pysynphot as S
>>> print S.__version__
0.3d3
>>> #Read a spectrum from a file
>>> vega=S.FileSpectrum('alpha_lyr_stis_003.fits')
>>> print vega
alpha_lyr_stis_003.fits
>>> vega.wave
array([  9.00452026e+02,   9.01354004e+02,   9.02257996e+02, ...,
         2.99353200e+06,   2.99653275e+06,   2.99953700e+06], dtype=float32)
>>> vega.flux
array([  1.23810534e-17,   1.67559564e-17,   1.78002369e-17, ...,
         1.40140738e-19,   1.38734357e-19,   1.26490663e-19])
>>> bb=S.BlackBody(40000)
>>> print bb.wave
[   500.            500.19760122    500.39528054 ...,  25969.1985582
  25979.46164894  25989.72879567]
>>> print bb.flux
[ 1.15230179  1.15375888  1.15521646 ...,  0.00141824  0.0014166
  0.00141496]
>>> print bb
BlackBody(T=40000)

>>> pl=S.PowerLaw(10000,-2)
>>> print pl
Power law: refwave 10000.000000, index -2.000000
>>> print pl.wave
[   500.            500.19760122    500.39528054 ...,  25969.1985582
  25979.46164894  25989.72879567]
>>> print pl.flux
[  4.00000000e+02   3.99684021e+02   3.99368286e+02 ...,   1.48280114e-01
   1.48162976e-01   1.48045942e-01]

>>> g1=S.GaussianSource(18.3,18000,2000,fluxunits='abmag')
>>> print g1
Gaussian: mu=18000.000000,fwhm=2000.000000,flux=18.300000 abmag

>>> unitflux=S.UnitSpectrum(18,fluxunits='abmag')
>>> print unitflux
Unit spectrum of 18.000000 abmag

>>> bp1=S.ObsBandpass('acs,hrc,f555w')
>>> print bp1
acs,hrc,f555w
>>> print bp1.wave
[   500.   1000.   1001. ...,  11999.  30000.  30010.]
>>> print bp1.throughput
[ 0.  0.  0. ...,  0.  0.  0.]
>>> bp1.showfiles()
/data/cdbs1/comp/ota/hst_ota_007_syn.fits
/data/cdbs1/comp/acs/acs_hrc_m12_005_syn.fits
/data/cdbs1/comp/acs/acs_hrc_m3_005_syn.fits
/data/cdbs1/comp/acs/acs_f555w_003_syn.fits
/data/cdbs1/comp/acs/acs_hrc_win_005_syn.fits
/data/cdbs1/comp/acs/acs_hrc_ccd_011_syn.fits
>>> len(bp1)
6

>>> sp1=S.FileSpectrum('/data/cdbs1/calspec/feige66_002.fits')
>>> print bp1.waveunits
probably angstroms
>>> print sp1.waveunits
angstrom
>>> obs1=sp1*bp1
>>> print obs1
/data/cdbs1/calspec/feige66_002.fits * acs,hrc,f555w
>>> print obs1.wave
[   500.   1000.   1001. ...,  11999.  30000.  30010.]
>>> print obs1.flux.max()
7.47814099194e-14
>>> print obs1.flux.argmax()
6924

>>> sp2=S.FileSpectrum('/data/cdbs1/calspec/feige66_002.fits')*S.ObsBandpass('acs,hrc,f555w')
>>> print sp2
/data/cdbs1/calspec/feige66_002.fits * acs,hrc,f555w
>>> print sp2.waveunits
angstrom
>>> print sp2.fluxunits
flam

"""


__version__ = '0.3d3'

#UI:
from spectrum import BlackBody, GaussianSource, UnitSpectrum
from spectrum import Powerlaw as PowerLaw
from spectrum import TabularSourceSpectrum as FileSpectrum

from spectrum import TabularSpectralElement as FileBandpass
from observationmode import ObservationMode as Obsmode
from obsbandpass import ObsBandpass

from numpy import arange as Waveset


def _test():
    import doctest
    doctest.testfile('__init__.py')

if __name__ == '__main__':
    #WARNING: doctest won't presently work except in the correct directory.
    _test()
