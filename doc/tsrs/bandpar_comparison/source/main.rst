Comparison of Synphot and Pysynphot Bandpar Functionality
=========================================================

.. abstract::
   :author: Matt Davis (SSB)
   :date: 15 November 2011
   
   Pysynphot attempts to replicate much of the functionality of the Synphot
   `bandpar`_ utility but sometimes uses different formulae and algorithms.
   This TSR collects the calculations used in Pysynphot, Synphot, the
   formulae described in the `Synphot Manual`_ in Section 5.1 on page 42,
   and the formulae in the Synphot help files.
   
.. _Synphot Manual: http://stsdas.stsci.edu/stsci_python_epydoc/SynphotManual.pdf
   
RMS Width - BANDW - PHOTBW
==========================

Summary
-------

This value is added to image headers in the PHOTBW keyword.

**Pysynphot**

* *Function name*: `SpectralElement.rmswidth <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1106>`_
* *Source code*: `spectrum.py <https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py>`_
* *References*: :ref:`3 page 836 <ref3>`

**Synphot**

* *Bandpar name*: `BANDW <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
* *Function name*: `rmslam`_ called by `comppar`_ called by `bandpar`_.
* *Source code*: `rmslam.x <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/rmslam.x>`_
* *References*: :ref:`1 sections 5.1,7.1 <ref1>`, :ref:`2 <ref2>`

.. _comppar: https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/bandpar/comppar.x
.. _bandpar: https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/bandpar/bandpar.x


Synphot Equations
-----------------

The `Synphot Manual`_ section 5.1 gives the equation for RMS bandwidth as

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

The
`bandpar help file <https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/pkg/hst_calib/synphot/doc/bandpar.hlp>`_
gives the same equations as above for the RMS width but the `Synphot Manual`_
in section 7.1 gives different equations when describing bandpar. The equations
in section 7.1 are the same as used by Pysynphot, shown below.

.. _rmslam: https://svn.stsci.edu/trac/ssb/stsci_python/browser/stsdas/trunk/stsdas/lib/synphot/rmslam.x

Pysynphot Equations
-------------------

The Pysynphot `rmswidth`_ source code references Koornneef et al 1987, page 836
as the source for its RMS width calculation, which is

.. math::

   \lambda_{rms}^2 = \frac{\int P_{\lambda} (\lambda - \bar{\lambda})^2 \,d\lambda}
   {\int P_{\lambda} \,d\lambda}
  
where

.. math::

   \bar{\lambda} = \frac{\int \lambda P_{\lambda} \,d\lambda}
   {\int P_{\lambda} \,d\lambda}.
   
.. _rmswidth: https://trac.assembla.com/astrolib/browser/trunk/pysynphot/lib/pysynphot/spectrum.py#L1106
