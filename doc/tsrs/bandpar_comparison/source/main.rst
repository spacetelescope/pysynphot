Comparison of Synphot and Pysynphot Bandpar Functionality
=========================================================

.. abstract::
   :author: Matt Davis (SSB)
   :date: 15 November 2011
   
   Pysynphot attempts to replicate much of the functionality of the Synphot
   ``bandpar`` utility but sometimes uses different formulae and algorithms.
   This TSR collects the calculations used in Pysynphot, Synphot, and the
   formula described in the `Synphot Manual`_ on page 42.
   
.. _Synphot Manual: http://stsdas.stsci.edu/stsci_python_epydoc/SynphotManual.pdf
   
PHOTBW - BANDW - RMS Width
==========================

Synphot
-------

The `Synphot Manual`_ gives the equation for RMS bandwidth as

.. math::

  \lambda_{rms}^2 = \bar{\lambda}^2 \frac{\int P_{\lambda} \ln(\lambda/\bar{\lambda})^2
  \,d\lambda/\lambda}{\int P_{\lambda} \,d\lambda/\lambda}
  
where

.. math::

  \bar{\lambda} = \exp \left[ \frac{\int P_{\lambda} \ln(\lambda) \,d\lambda/\lambda}
  {\int P_{\lambda} \,d\lambda/\lambda} \right].

The Synphot function `rmslam`_ does appear to implement this procedure for
calculating the RMS width of the bandpass. The source code references the WF/PC-1
Instrument Handbook as the source of the equation for RMS width and references
Schneider, Gunn and Hoessel (1983 ApJ 264,337) as the source for the equation
for mean wavelength.

A copy of the WF/PC-1 Instrument Handbook could not be found so it has not been
verified that the Synphot code faithfully reproduces whatever may be documented
there.

.. _rmslam: https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/rmslam.x

Pysynphot
---------

The Pysynphot 
`source code <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
references Koornneef et al 1987, page 836 as the
source for its RMS width calculation, which appears to be

.. math::

  \lambda_{rms}^2 = \frac{\int P_{\lambda} (\lambda - \bar{\lambda})^2 \,d\lambda}
  {\int P_{\lambda} \,d\lambda}
  
where

.. math::

  \bar{\lambda} = \frac{\int \lambda P_{\lambda} \,d\lambda}
  {\int P_{\lambda} \,d\lambda}.
