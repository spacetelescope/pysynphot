.. _pysynphot-properties:

**********************
Photometric Properties
**********************

In here, we describe bandpass and spectral photometric properties that can be
calculated using **pysynphot**, along with their respective formulae.
More information can also be found in
:ref:`Koornneef et al. (1986) <synphot-ref-koornneef1986>`,
:ref:`pysynphot-bandpass`, and :ref:`pysynphot-observation`.

The following table summarizes the available photometric properties, which are
further elaborated in the sub-sections below:

+------------------+----------------------------------------------------------+
|Command           |Description                                               |
+==================+==========================================================+
|bp.avgwave()      |:ref:`pysynphot-formula-avgwv` or reference wavelength    |
+------------------+----------------------------------------------------------+
|bp.rmswidth()     |:ref:`pysynphot-formula-rmswidth`                         |
+------------------+----------------------------------------------------------+
|bp.photbw()       |:ref:`pysynphot-formula-bandw`                            |
+------------------+----------------------------------------------------------+
|bp.rectwidth()    |:ref:`pysynphot-formula-rectw`                            |
+------------------+----------------------------------------------------------+
|bp.equivwidth()   |:ref:`pysynphot-formula-equvw`                            |
+------------------+----------------------------------------------------------+
|bp.efficiency()   |:ref:`pysynphot-formula-qtlam`                            |
+------------------+----------------------------------------------------------+
|bp.unit_response()|:ref:`pysynphot-formula-uresp`                            |
+------------------+----------------------------------------------------------+
|obs.effstim()     |:ref:`pysynphot-formula-effstim`                          |
+------------------+----------------------------------------------------------+
|obs.efflam()      |:ref:`pysynphot-formula-efflam`                           |
+------------------+----------------------------------------------------------+
|bp.pivot()        |:ref:`pysynphot-formula-pivwv`                            |
|obs.pivot()       |                                                          |
+------------------+----------------------------------------------------------+

These are not directly available but they are used to calculate other
properties:

* :ref:`pysynphot-formula-barlam`
* :ref:`pysynphot-formula-emflx`

These are some common variables mentioned in the formulae in this section:

=================== =================================
Variable            Description
=================== =================================
:math:`F_{\lambda}` Source flux distribution
:math:`P_{\lambda}` Dimensionless bandpass throughput
*area*              Telescope collecting area
*h*                 The Planck constant
*c*                 The speed of light
=================== =================================


.. _pysynphot-formula-avgwv:

Bandpass Average Wavelength
===========================

For a bandpass, :meth:`~pysynphot.spectrum.SpectralElement.avgwave` implements
the equation for :math:`\lambda_{0}` as defined in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836). It is
equivalent to IRAF STSDAS SYNPHOT ``bandpar`` results for ``avglam``, ``avgmw``,
or ``refwave``; The throughput at this wavelength is ``tlambda``.

.. math::

    \lambda_{0} = \frac{\int \; P_{\lambda} \; \lambda \; d\lambda }{\int \; P_{\lambda} \; d\lambda}

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.avgwave()
5373.2182275673349


.. _pysynphot-formula-rmswidth:

Bandpass RMS Band Width (Koornneef)
===================================

For a bandpass, :meth:`~pysynphot.spectrum.SpectralElement.rmswidth` implements
the bandpass RMS width as defined in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836), where
:math:`\lambda_{0}` is the :ref:`pysynphot-formula-avgwv`.

.. math::

    \lambda_{rms} = \sqrt{\frac{\int \; P_{\lambda} \; (\lambda - \lambda_{0})^{2} \; d\lambda}{\int \; P_{\lambda} \: d\lambda}}

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.rmswidth()
361.9997795461671


.. _pysynphot-formula-bandw:

Bandpass RMS Band Width (SYNPHOT)
=================================

For a bandpass, :meth:`~pysynphot.spectrum.SpectralElement.photbw` implements
the equivalent for ``bandw`` from IRAF STSDAS SYNPHOT ``bandpar`` task, where
:math:`\bar{\lambda}` is :ref:`pysynphot-formula-barlam`. This is not the same
as :ref:`pysynphot-formula-rmswidth`.

.. math::

    bandw = \bar{\lambda} \; \sqrt{\frac{\int \; (P_{\lambda} / \lambda) \; \ln(\lambda \; / \; \bar{\lambda})^{2} \; d\lambda}{\int \; (P_{\lambda} / \lambda) \; d\lambda}}

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.photbw()
360.11107577076439


.. _pysynphot-formula-barlam:

Bandpass Mean Log Wavelength
============================

For a bandpass, this is the mean wavelength as defined in
:ref:`Schneider, Gunn, and Hoessel (1983) <synphot-ref-schneider1983>`.
This rather unusual definition is such that the corresponding mean frequency is
:math:`c / \bar{\lambda}`. This cannot be directly calculated by
**pysynphot**, but is used for :ref:`pysynphot-formula-bandw`. It is equivalent
to ``barlam`` in IRAF STSDAS SYNPHOT.

.. math::

    \bar{\lambda} = \exp\Bigg[\frac{\int \; (P_{\lambda} / \lambda) \; \ln(\lambda) \; d\lambda}{\int (P_{\lambda} / \lambda) \; d\lambda}\Bigg]


.. _pysynphot-formula-rectw:

Bandpass Rectangular Width
==========================

For a bandpass, :meth:`~pysynphot.spectrum.SpectralElement.rectwidth` implements
the rectangular width, where ``equvw`` is :ref:`pysynphot-formula-equvw`.
It is equivalent to IRAF STSDAS SYNPHOT ``bandpar`` result for ``rectw``.

.. math::

    rectw = \frac{equvw}{\textnormal{MAX}(P_{\lambda})}

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.rectwidth()
1124.6106504868569


.. _pysynphot-formula-equvw:

Bandpass Equivalent Width
=========================

For a bandpass, :meth:`~pysynphot.spectrum.SpectralElement.equivwidth`
implements the equivalent width. It is equivalent to
:meth:`~pysynphot.spectrum.SpectralElement.integrate` and IRAF STSDAS SYNPHOT
``bandpar`` result for ``equvw``.

.. math::

    equvw = \int P_{\lambda} d\lambda

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.equivwidth()
412.91237693252498


.. _pysynphot-formula-qtlam:

Bandpass Dimensionless Efficiency
=================================

For a bandpass, :meth:`~pysynphot.spectrum.SpectralElement.efficiency`
implements the dimensionless efficiency. It is equivalent to IRAF STSDAS SYNPHOT
``bandpar`` result for ``qtlam``.

.. math::

    qtlam = \int \frac{P_{\lambda}}{\lambda} d\lambda

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.efficiency()
0.077196835355538812


.. _pysynphot-formula-uresp:

Bandpass Unit Response
======================

For a bandpass, :meth:`~pysynphot.spectrum.SpectralElement.unit_response`
implements the computation of the flux (in ``flam``) of a star that produces a
response of one count per second in that bandpass, where *h* and *c* are
:ref:`astronomical constants <pysynphot-constants>`, and *area* is the
:ref:`telescope collecting area <pysynphot-area>`.
It is equivalent to IRAF STSDAS SYNPHOT ``bandpar`` result for ``uresp``.

.. math::

    uresp = \frac{hc}{area} \int P_{\lambda}\; \lambda\; d\lambda

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.unit_response()
1.9791581474812573e-19


.. _pysynphot-formula-emflx:

Bandpass Equivalent Monochromatic Flux
======================================

For a bandpass, its equivalent monochromatic flux is as defined below, where
:math:`\lambda_{0}` is :ref:`pysynphot-formula-avgwv`.
It is equivalent to IRAF STSDAS SYNPHOT ``bandpar`` result for ``emflx``.

.. math::

    emflx = \frac{uresp \times equvw}{P(\lambda_{0})}

This can be calculated indirectly in **pysynphot**, as given in the example
below:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.unit_response() * bp.equivwidth() / bp(bp.avgwave())
2.3693354953649259e-16


.. _pysynphot-formula-effstim:

Effective Stimulus
==================

For an observation, :meth:`~pysynphot.observation.Observation.effstim`
calculates the predicted effective stimulus in given flux unit.
:meth:`~pysynphot.observation.Observation.countrate` is a
special form of effective stimulus in the unit of counts/s given a
:ref:`pre-defined telescope collecting area <pysynphot-area>`. It is equivalent
to IRAF STSDAS SYNPHOT ``calcphot`` result for ``effstim``.

.. math::

    effstim = \frac{\int\; F_{\lambda}\; P_{\lambda}\; \lambda\; d\lambda}{\int\; P_{\lambda}\; \lambda\; d\lambda}

Example:

>>> obs = S.Observation(S.BlackBody(5000), S.ObsBandpass('acs,wfc1,f555w'))
>>> obs.effstim()  # photlam
0.00053965665649945897
>>> obs.effstim('flam')
1.9951166916464645e-15
>>> obs.effstim('counts')
10080.63299128226
>>> obs.countrate()
10080.633086603204


.. _pysynphot-formula-efflam:

Effective Wavelength
====================

For an observation, :meth:`~pysynphot.observation.Observation.efflam` implements
the effective wavelength, as defined in
:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836), where flux
unit is converted to ``flam`` prior to calculations. It is equivalent to
IRAF STSDAS SYNPHOT ``calcphot`` result for ``efflerg``.

.. math::

    \lambda_{eff} = \frac{\int \; F_{\lambda} \; P_{\lambda} \; \lambda^2 \; d\lambda}{\int \; F_{\lambda} \; P_{\lambda} \; \lambda \; d\lambda}

Example:

>>> obs = S.Observation(S.BlackBody(5000), S.ObsBandpass('acs,wfc1,f555w'))
>>> obs.efflam()
5406.9723492971125


.. _pysynphot-formula-pivwv:

Pivot Wavelength
================

For an observation, :meth:`pysynphot.observation.Observation.pivot` calculates
the pivot wavelength. For a bandpass, it is
:meth:`pysynphot.spectrum.SpectralElement.pivot`.
The formula below applies to an observation.
For a bandpass, replace
:math:`F_{\lambda}` with :math:`P_{\lambda}` in the formula.
It is equivalent to IRAF STSDAS SYNPHOT result for ``pivwv`` and ``pivot``.

.. math::

    \lambda_{pivot} = \sqrt{\frac{\int \: F_{\lambda} \; \lambda \; d\lambda}{\int(F_{\lambda} \; / \; \lambda) \; d\lambda}}

Example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')
>>> bp.pivot()
5361.007831073981
>>> obs = S.Observation(S.BlackBody(5000), bp)
>>> obs.pivot()
5394.930514954142
