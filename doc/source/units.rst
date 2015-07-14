.. _pysynphot-units:

*******************
Units and Constants
*******************

**pysynphot** understands some :ref:`pysynphot-flux-units` and
:ref:`pysynphot-wave-units` that are commonly used in astronomy.
Unit conversion can be easily done within spectral objects by using
:meth:`pysynphot.spectrum.SourceSpectrum.convert` (for flux and wavelength) and
:meth:`pysynphot.spectrum.SpectralElement.convert` (wavelength only, as
throughput is unitless) methods. As in IRAF STSDAS SYNPHOT, only lowercase
unit names are valid.

Unless explicitly stated otherwise in API documentations, all calculations are
done in the following internal units first, and then presented in
user-specified units:

* Angstrom for wavelength
* ``photlam`` for flux


.. _pysynphot-constants:

Constants
=========

These are the constants used in unit conversion:

========================== ====================== ===============
Constant                   Description            Value
========================== ====================== ===============
``pysynphot.units.C``      Speed of light, *c*    |speed_c_math|
``pysynphot.units.H``      Planck's constant, *h* |planck_h_math|
``pysynphot.units.ABZERO`` ``abmag`` zero point   -48.6 mag
``pysynphot.units.STZERO`` ``stmag`` zero point   -21.1 mag
========================== ====================== ===============

.. |speed_c_math| replace:: :math:`2.99792458 \times 10^{18} \; \AA \; \textnormal{s}^{-1}`
.. |planck_h_math| replace:: :math:`6.62620 \times 10^{-27} \; \textnormal{ergs} \; \textnormal{s}`


.. _pysynphot-flux-units:

Flux Units
==========

The recognized flux units for source spectrum and observation objects are as
tabulated below. For IRAF STSDAS SYNPHOT users, the unit name is equivalent to
``form``, which has become ``fluxunits`` in **pysynphot** (see
:ref:`pysynphot-units-examples`). Most calculation and sampling results are
presented in the given flux unit (e.g.,
:meth:`~pysynphot.spectrum.SourceSpectrum.sample` and
:meth:`~pysynphot.observation.Observation.effstim`).
Since all internal flux calculations are done using ``photlam``, no special
steps are necessary when an operation is done on source spectra with different
flux units.
:ref:`pysynphot-units-counts-mags` further explains the units of ``vegamag``,
``abmag``, ``stmag``, ``obmag``, and counts.  The rest of the supported
flux units should be self-evident.

+-------+--------------------------+--------------+
|Name   |Class Object              |Unit          |
+=======+==========================+==============+
|photlam|`~pysynphot.units.Photlam`||photlam_math||
+-------+--------------------------+--------------+
|photnu |`~pysynphot.units.Photnu` ||photnu_math| |
+-------+--------------------------+--------------+
|flam   |`~pysynphot.units.Flam`   ||flam_math|   |
+-------+--------------------------+--------------+
|fnu    |`~pysynphot.units.Fnu`    ||fnu_math|    |
+-------+--------------------------+--------------+
|stmag  |`~pysynphot.units.STMag`  ||stmag_math|  |
+-------+--------------------------+--------------+
|abmag  |`~pysynphot.units.ABMag`  ||abmag_math|  |
+-------+--------------------------+--------------+
|obmag  |`~pysynphot.units.OBMag`  ||obmag_math|  |
+-------+--------------------------+--------------+
|vegamag|`~pysynphot.units.VegaMag`||vegamag_math||
+-------+--------------------------+--------------+
|count  |`~pysynphot.units.Counts` ||counts_math| |
|       |                          |              |
|counts |                          |              |
+-------+--------------------------+--------------+
|jy     |`~pysynphot.units.Jy`     ||jy_math|     |
+-------+--------------------------+--------------+
|mjy    |`~pysynphot.units.mJy`    ||mjy_math|    |
+-------+--------------------------+--------------+
|ujy    |`~pysynphot.units.muJy`   ||mujy_math|   |
|       |                          |              |
|mujy   |                          |              |
|       |                          |              |
|microjy|                          |              |
+-------+--------------------------+--------------+
|njy    |`~pysynphot.units.nJy`    ||njy_math|    |
|       |                          |              |
|nanojy |                          |              |
+-------+--------------------------+--------------+

.. |photlam_math| replace:: :math:`\textnormal{photon} \; \textnormal{s}^{-1} \; \textnormal{cm}^{-2} \; \AA^{-1}`
.. |photnu_math| replace:: :math:`\textnormal{photon} \; \textnormal{s}^{-1} \; \textnormal{cm}^{-2} \; \textnormal{Hz}^{-1}`
.. |flam_math| replace:: :math:`\textnormal{erg} \; \textnormal{s}^{-1} \; \textnormal{cm}^{-2} \; \AA^{-1}`
.. |fnu_math| replace:: :math:`\textnormal{erg} \; \textnormal{s}^{-1} \textnormal{cm}^{-2} \textnormal{Hz}^{-1}`
.. |stmag_math| replace:: :math:`-2.5 \times \log(\textnormal{flam}) - 21.1`
.. |abmag_math| replace:: :math:`-2.5 \times \log(\textnormal{fnu})  - 48.6`
.. |obmag_math| replace:: :math:`-2.5 \times \log(\textnormal{count})`
.. |vegamag_math| replace:: :math:`-2.5 \times \log(\textnormal{flux} \; / \; \textnormal{flux}_{\textnormal{Vega}})`
.. |counts_math| replace:: :math:`\textnormal{photon} \; \textnormal{s}^{-1}`
.. |jy_math| replace:: :math:`10^{-23} \; \textnormal{erg} \; \textnormal{s}^{-1} \; \textnormal{cm}^{-2} \textnormal{Hz}^{-1}`
.. |mjy_math| replace:: :math:`10^{-26} \; \textnormal{erg} \; \textnormal{s}^{-1} \; \textnormal{cm}^{-2} \textnormal{Hz}^{-1}`
.. |mujy_math| replace:: :math:`10^{-29} \; \textnormal{erg} \; \textnormal{s}^{-1} \; \textnormal{cm}^{-2} \textnormal{Hz}^{-1}`
.. |njy_math| replace:: :math:`10^{-32} \; \textnormal{erg} \; \textnormal{s}^{-1} \; \textnormal{cm}^{-2} \textnormal{Hz}^{-1}`


.. _pysynphot-units-counts-mags:

Counts and Magnitudes
---------------------

.. |ab_nu| replace:: :math:`\textnormal{AB}_{\nu}`
.. |st_lam| replace:: :math:`\textnormal{ST}_{\lambda}`

**pysynphot** supports counts and the following magnitude systems:

* ``obmag``, the instrumental magnitude that is the logarithmic form of counts.
  Conversion involving counts and ``obmag`` assumes a
  :ref:`pre-defined telescope collecting area <pysynphot-area>`.
* ``abmag``, the |ab_nu| magnitude from :ref:`Oke (1974) <synphot-ref-oke1974>`,
  which is based on a constant flux density per unit frequency.
* ``stmag``, the |st_lam| or Space Telescope magnitude, which is based on a
  constant flux density per unit wavelength.
* ``vegamag``, which is defined by setting the magnitude of Vega to
  zero in all bands. The :ref:`adopted Vega spectrum <pysynphot-vega-spec>`
  is defined over a wavelength range of 900 Angstroms to 300 microns.

``vegamag`` offers a reasonable approximation to many of the conventional
photometric systems that use the spectrum of Vega to define
magnitude zero in one or more passbands. In broadband photometry, the relevant
passband integral is calculated first for the source spectrum and then again
for the spectrum of Vega, and the ratio of the two results is converted to a
magnitude. This would not be a scientifically meaningful option for
spectrophotometry.

Meanwhile, ``abmag`` and ``stmag`` are appropriate for either spectrophotometry
or photometry. Their zero point values of 48.60 and 21.10 mag, respectively, are
chosen for convenience so that Vega has |ab_nu| and |st_lam| magnitudes close
to 0 in the Johnson *V* passband, as shown in the following figure:

.. figure:: _static/VegaPhotomSys.png
    :width: 600px
    :alt: Standard photometric system

    Standard photometric systems generally use the spectrum of Vega to
    define magnitude zero. The spectrophotometric magnitudes
    |ab_nu| and |st_lam| refer instead to spectra of constant :math:`f_{\nu}`
    and :math:`f_{\lambda}`, respectively. Magnitude zero in both systems is
    defined to be the mean flux density of Vega in the Johnson *V* passband.
    Thus all three of the spectra shown here produce the same count rate in
    the Johnson *V* passband. The pivot wavelength of Johnson *V* is defined to
    be the crossing point of the |ab_nu|:math:`= 0` and |st_lam|:math:`= 0`
    spectra.

Because the ``abmag`` and ``stmag`` systems are defined such that they result in
constant magnitudes for spectra having constant flux per unit frequency and
wavelength, respectively, they will not provide magnitudes on a conventional
system, such as *UBVRI*, without first deriving an appropriate transformation
onto the desired standard system.

``obmag`` and counts are used to predict detected count rates. For instance,
:meth:`~pysynphot.observation.Observation.countrate` calculates the
predicted number of detected counts per second integrated over the passband.
There are two important things to remember concerning this unit:

#. The number of counts per channel depends on the width (in wavelength space)
   of the channel in the wavelength grid that is used.
   As stated above, all flux calculations are done internally in
   the unit of ``photlam``, so when the output unit of counts or ``obmag`` is
   requested, the ``photlam`` values are multiplied by the collecting area of
   the telescope and by the width (in Angstroms) of each channel in the
   wavelength grid. Therefore, in order to accurately predict the number of
   counts per channel for a spectroscopic instrument, it is necessary to use
   a wavelength grid that provides a good match to the dispersion properties
   of the selected instrument mode (see :ref:`pysynphot-wavelength-table`).
   For supported HST instruments, the appropriate wavelength grid will be
   automatically selected.
#. The unit "counts" refers to the actual detector counts for the FOC, FOS, HRS,
   and HSP instruments. While for the WF/PC-1, WFPC2, NICMOS, WFC3, COS, ACS,
   and STIS instruments, it refers to electrons. In order to obtain counts in
   the unit of data number (DN) for some of the latter instruments, include the
   appropriate keyword for ADC gain, if supported (see
   :ref:`pysynphot-appendixb`).


.. _pysynphot-wave-units:

Wavelength Units
================

These are the recognized wavelength units for all spectrum objects:

+--------------+--------------------------------+----------------+
|Name          |Class Object                    |Unit            |
+==============+================================+================+
|m             |`~pysynphot.units.Meter`        |SI base unit for|
|              |                                |length          |
|meter         |                                |                |
+--------------+--------------------------------+----------------+
|cm            |`~pysynphot.units.Cm`           ||cm_math|       |
+--------------+--------------------------------+----------------+
|mm            |`~pysynphot.units.Mm`           ||mm_math|       |
+--------------+--------------------------------+----------------+
|um            |`~pysynphot.units.Micron`       ||micron_math|   |
|              |                                |                |
|micron        |                                |                |
|              |                                |                |
|microns       |                                |                |
+--------------+--------------------------------+----------------+
|nm            |`~pysynphot.units.Nm`           ||nm_math|       |
+--------------+--------------------------------+----------------+
|angstrom      |`~pysynphot.units.Angstrom`     ||angstrom_math| |
|              |                                |                |
|angstroms     |                                |                |
+--------------+--------------------------------+----------------+
|1/um          |`~pysynphot.units.InverseMicron`||invmicron_math||
|              |                                |                |
|inversemicron |                                |                |
|              |                                |                |
|inversemicrons|                                |                |
+--------------+--------------------------------+----------------+
|hertz         |`~pysynphot.units.Hz`           ||hz_math|       |
+--------------+--------------------------------+----------------+

.. |cm_math| replace:: :math:`10^{-2} \; \textnormal{m}`
.. |mm_math| replace:: :math:`10^{-3} \; \textnormal{m}`
.. |micron_math| replace:: :math:`10^{-6} \; \textnormal{m}`
.. |nm_math| replace:: :math:`10^{-9} \; \textnormal{m}`
.. |angstrom_math| replace:: :math:`10^{-10} \; \textnormal{m}`
.. |invmicron_math| replace:: :math:`10^{6} \; \textnormal{m}^{-1}`
.. |hz_math| replace:: :math:`\textnormal{s}^{-1}`


.. _pysynphot-units-examples:

Examples
========

Create a source spectrum from arrays with default units:

>>> sp = S.ArraySpectrum(
...     np.array([1000, 2000, 3000]), np.array([0.1, 0.2, 0.3]))
>>> print('{0}, {1}'.format(sp.waveunits.name, sp.fluxunits.name))
angstrom, photlam

Convert both wavelength and flux units:

>>> sp.convert('nm')
>>> sp.convert('flam')
>>> print('{0}, {1}'.format(sp.waveunits.name, sp.fluxunits.name))
nm, flam
>>> sp.wave
array([ 100.,  200.,  300.])
>>> sp.flux
array([  1.98648479e-12,   1.98648479e-12,   1.98648479e-12])

To sample the spectrum in user units (i.e., nm and ``flam``), use its
:meth:`~pysynphot.spectrum.SourceSpectrum.sample` method:

>>> sp.sample(200)
1.9864847851996004e-12

To sample the spectrum in internal units (i.e., Angstrom and ``photlam``),
use its :py:meth:`~object.__call__` method:

>>> sp(2000)
0.20000000000000001
