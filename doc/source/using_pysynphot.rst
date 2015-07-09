.. _pysynphot-using:

########
Overview
########

There are two basic objects in **pysynphot**:

* :ref:`pysynphot-spectrum`
* :ref:`pysynphot-bandpass`

A source spectrum can be created from:

* FITS or ASCII table file
* Wavelength and flux arrays
* Pre-defined analytic forms (:ref:`blackbody <pysynphot-planck-law>`,
  :ref:`flat <pysynphot-flat-spec>`,
  :ref:`Gaussian <pysynphot-gaussian>`, or
  :ref:`power-law <pysynphot-powerlaw>`)

A bandpass can be created from:

* FITS or ASCII table file
* Wavelength and transmission arrays
* Pre-defined analytic forms (:ref:`box <pysynphot-box-bandpass>`)
* :ref:`Observation mode <pysynphot-obsmode-bandpass>` string expression
  (e.g., ``"acs,wfc1,f555w"``)

A source spectrum can be:

* :ref:`Added to another source spectrum <pysynphot-composite-spectrum>`
* :ref:`Multiplied by a constant or a bandpass <pysynphot-composite-spectrum>`
* :ref:`Redshifted <pysynphot-redshift>`
* :ref:`Normalized <pysynphot-renorm>`
* Changed to different :ref:`units <pysynphot-units>` (both wavelength and flux)

A bandpass can be:

* :ref:`Multiplied by a constant, another bandpass, or a source spectrum <pysynphot-composite-spectrum>`
* Change :ref:`units <pysynphot-units>` (wavelength only)

Flux (for source spectrum) and throughput (for bandpass) values are not
actually calculated they are sampled. Evaluation on an as-needed basis
enables accurate sampling, especially for asymptotic curves (e.g., power-law)
and :ref:`composite spectra <pysynphot-composite-spectrum>`.

Both source spectrum and bandpass can be written out to FITS or ASCII tables
(see :ref:`pysynphot-io`).

An :ref:`observation <pysynphot-observation>` can be created using a
source spectrum and a bandpass.
An observation is a special kind of spectrum that enables effective stimulus
(including count rate) and wavelength calculations.
It has two different datasets:

* As defined by the native wavelength set, which is constructed when combining
  the source spectrum and the bandpass.
* As defined by the binned wavelength set, which uses the optimal binning for
  the detector (as used by its
  :meth:`~pysynphot.observation.Observation.countrate` method).

While units can be changed, unless explicitly stated otherwise, all calculations
are done in pre-defined internal units:

* Angstrom for wavelength
* ``photlam`` for flux

Below are some items that are commonly mentioned in **pysynphot**:

* ``obsmode`` - Passband created from a specific HST instrument configuration,
  a.k.a. observation mode.
* ``form`` - Flux unit of the output data. For example, ``flam``, counts,
  or ``obmag``.
* ``waveset`` - Wavelength array on which passband and spectrum will be
  calculated.
* ``ref`` - Reference data parameters, which include graph, component, and
  thermal tables, telecope collecting area, and default wavelength set.
  To access them, use :func:`~pysynphot.refs.setref` or
  :func:`~pysynphot.refs.showref`.
  They are analogous to ``refdata`` in IRAF STSDAS SYNPHOT.


.. _pysynphot-primary-passband:

Passband and Spectral Computations
==================================

The tables below summarize some main functionality of **pysynphot**.
These are only for quick reference. Detailed explanations are available
in their respective sections in other parts of this document.

**Create a passband:**

+-------------------------------------+----------------------------------------+
|Command                              |Description                             |
+=====================================+========================================+
|bp = S.FileBandpass(filename)        |Load from file.                         |
+-------------------------------------+----------------------------------------+
|bp = S.ObsBandpass(obsmode)          |HST observation mode.                   |
+-------------------------------------+----------------------------------------+
|bp = S.Box(mu, width)                |Box centered at ``mu`` with given width.|
+-------------------------------------+----------------------------------------+

.. _pysynphot-passband-parameters:

**Calculate bandpass parameters:**

+--------------------+----------------------------------------------------------------------------+
|Command             |Description                                                                 |
+====================+============================================================================+
|bp.avgwave()        |Average wavelength of bandpass.                                             |
+--------------------+----------------------------------------------------------------------------+
|bp.efficiency()     |Dimensionless efficiency.                                                   |
+--------------------+----------------------------------------------------------------------------+
|bp.equivwidth()     |Equivalent width of passband.                                               |
+--------------------+----------------------------------------------------------------------------+
|bp.rectwidth()      |Rectangular width of passband.                                              |
+--------------------+----------------------------------------------------------------------------+
|bp.rmswidth()       |RMS band width as in                                                        |
|                    |:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>` (page 836).        |
+--------------------+----------------------------------------------------------------------------+
|bp.throughput.max() |Peak throughput of passband.                                                |
+--------------------+----------------------------------------------------------------------------+
|bp.pivot()          |Pivot wavelength of passband.                                               |
+--------------------+----------------------------------------------------------------------------+
|bp.unit_response()  |Unit response; flux (in ``flam``) that produces 1 count/second in the       |
|                    |passband.                                                                   |
+--------------------+----------------------------------------------------------------------------+
|bp.thermback()      |Expose the thermal background calculation presently hidden in               |
|                    |`~pysynphot.observationmode`. Only bandpasses for which thermal             |
|                    |information has been supplied in the graph table supports this method.      |
+--------------------+----------------------------------------------------------------------------+
|bp.photbw()         |RMS band width compatible with SYNPHOT calculation.                         |
+--------------------+----------------------------------------------------------------------------+

.. _pysynphot-spectra-creation:

**Create a spectrum:**

+------------------------------------------------+--------------------------------------------+
|Command                                         |Description                                 |
+================================================+============================================+
|sp = S.FileSpectrum(filename)                   |Load from file.                             |
+------------------------------------------------+--------------------------------------------+
|sp = S.BlackBody(Teff)                          |Blackbody spectrum with specified           |
|                                                |temperature, ``Teff``, in Kelvin. The flux  |
|                                                |of the spectrum is normalized to a star of  |
|                                                |solar radius at a distance of 1 kpc.        |
+------------------------------------------------+--------------------------------------------+
|sp = S.FlatSpectrum(value[, fluxunits])         |Flat spectrum with constant flux of given   |
|                                                |value and optionally flux unit.             |
+------------------------------------------------+--------------------------------------------+
|sp = S.PowerLaw(refval, expon[, fluxunits])     |Power-law spectrum of the form              |
|                                                |:math:`f = (\lambda / refval)^{expon}`.     |
|                                                |The spectrum is normalized to a flux of 1   |
|                                                |(in given unit) at ``refval`` (in Angstrom).|
+------------------------------------------------+--------------------------------------------+
|sp = S.GaussianSource(totflux, mu, fwhm[,       |Emission line centered on wavelength, ``mu``|
|fluxunits])                                     |, with a Gaussian profile that has given    |
|                                                |FWHM and total flux in given unit.          |
+------------------------------------------------+--------------------------------------------+
|sp = S.Icat(catalog, key1, ...)                 |Interpolate a spectrum from given catalog,  |
|                                                |selected by given search criteria           |
|                                                |(``key1, ...``) that could be temperature,  |
|                                                |surface gravity, or metallicity.            |
+------------------------------------------------+--------------------------------------------+
|sp = S.ArraySpectrum(wave, flux [, waveunits,   |Create from given wavelength and flux       |
|fluxunits, name])                               |arrays, in given units and name.            |
+------------------------------------------------+--------------------------------------------+

.. _pysynphot-observation-creation:

**Create an observation:**

+---------------------------+---------------------------------------------------+
|Command                    |Description                                        |
+===========================+===================================================+
|obs = S.Observation(sp, bp)|Given spectrum as observed through given bandpasss.|
+---------------------------+---------------------------------------------------+

.. _pysynphot-observation-parameters:

**Calculate observational parameters:**

+------------------------+-----------------------------------------------------------------------+
|Command                 |Description                                                            |
+========================+=======================================================================+
|obs.countrate()         |Calculate the response of a HST instrument for the given model spectrum|
|                        |and passband.                                                          |
+------------------------+-----------------------------------------------------------------------+
|obs.effstim(fluxunit)   |Calculate the effective stimulus in given unit.                        |
+------------------------+-----------------------------------------------------------------------+
|obs.efflam()            |Calculate the effective wavelength. This is performed on the binned    |
|                        |wavelength set by default.                                             |
+------------------------+-----------------------------------------------------------------------+
|obs.efflam(binned=False)|Calculate the effective wavelength. This is performed on the native    |
|                        |wavelength set.                                                        |
+------------------------+-----------------------------------------------------------------------+

.. _pysynphot-spectra-modify:

**Modify a spectrum:**

+------------------------------------+--------------------------------------------+
|Command                             |Description                                 |
+====================================+============================================+
|sp2 = sp.renorm(value, fluxunit, bp)|Renormalize the spectrum to given flux value|
|                                    |in given unit over the given passband. The  |
|                                    |evaluator computes the integral of the      |
|                                    |spectrum over the specified passband and    |
|                                    |rescales it by appropriate factor, forcing  |
|                                    |the integral to have the requested          |
|                                    |value.                                      |
+------------------------------------+--------------------------------------------+
|sp2 = sp.redshift(z)                |Redshift a spectrum by the amount, ``z``.   |
+------------------------------------+--------------------------------------------+
|sp2 = sp * S.Extinction(ebv, law)   |Apply an extinction of given :math:`E(B-V)` |
|                                    |using the selected extinction law.          |
+------------------------------------+--------------------------------------------+

.. _pysynphot-utility-task:

**Utility tasks:**

+---------------------------------------+-------------------------------------------------------+
|Command                                |Description                                            |
+=======================================+=======================================================+
|wv = S.Waveset(minwave, maxwave, dwave)|Generate a wavelength set with given min, max, and     |
|                                       |delta. Alternatively, this can also be done using      |
|                                       |`numpy`.                                               |
+---------------------------------------+-------------------------------------------------------+
|S.showref()                            |Show the current settings for graph, component, and    |
|                                       |thermal component tables, in addition to wavelength set|
|                                       |and telescope collecting area.                         |
+---------------------------------------+-------------------------------------------------------+
|S.setref(...)                          |Override the default values by setting any or all of   |
|                                       |the supported keywords, or reset to software default if|
|                                       |no parameters are given.                               |
+---------------------------------------+-------------------------------------------------------+
|bp.showfiles()                         |Print all the files that went into generating the      |
|                                       |passband.                                              |
+---------------------------------------+-------------------------------------------------------+
|bp.check_overlap(sp)                   |Check whether the wavelength range of ``sp`` is defined|
|                                       |everywhere of that in ``bp``. The result can be        |
|                                       |``"full"``, ``"partial"``, or ``"none"``.              |
+---------------------------------------+-------------------------------------------------------+


.. _pysynphot-io:

File I/O
========

Source spectrum and bandpass can be read from FITS or ASCII table via
`~pysynphot.spectrum.FileSourceSpectrum` (also callable as
``pysynphot.FileSpectrum``) and `~pysynphot.spectrum.FileSpectralElement`
(also callable as ``pysynphot.FileBandpass``), respectively.

For FITS table, data is extracted from extension 1, where the first column
contains wavelength values, and the second flux (for source spectrum) or
throughput (for bandpass). The extension header must contain the following
keywords:

* ``TUNIT1`` set to
  :ref:`wavelength unit name recognized by pysynphot <pysynphot-wave-units>`.
* ``TUNIT2`` set to
  :ref:`flux unit name recognized by pysynphot <pysynphot-flux-units>`
  (source spectrum only).
* ``TTYPE1`` set to "WAVELENGTH".
* ``TTYPE2`` set to "FLUX" (for source spectrum; could be modified with
  ``fluxname`` keyword during object initialization) or "THROUGHPUT" (for
  bandpass; could be modified with ``thrucol`` keyword during object
  initialization).

In an ASCII table, wavelength and flux/throughput values must be in the first
and the second columns, respectively. Wavelength must be in Angstrom. For source
spectrum, flux must be in ``flam``. All values will be read in as
double-precision floating point. The ASCII file may contain blank or
comment lines (defined as any lines starting with ``"#"``).

For source spectrum, regardless of file format, flux with negative values will
be automatically set to zero, unless ``keepneg=True`` is set during
initialization.

Both source spectrum and bandpass can be written out to a FITS table with their
respective ``writefits()`` attribute, which provide options to overwrite existing
file with the same name, remove redundant zero flux/throughput rows from both
ends, set floating point precision, and add extra information to the primary
header in extension 0.


Examples
========

Read a source spectrum from FITS table:

>>> sp = S.FileSpectrum('/some/place/spectrum.fits')

Read a source spectrum from ASCII table.
Wavelength and flux values must already be in the units of Angstrom and
``flam``, respectively:

>>> sp = S.FileSpectrum('/some/place/spectrum.dat')

Write a source spectrum to FITS table. Options are set to overwrite any existing
file, trim redundant rows with zero flux at both ends, force double precision,
and add a new keyword ``MYKEY1`` to primary header:

>>> sp.writefits('/some/place/spectrum.fits', clobber=True, trimzero=True,
...              precision='double', hkeys={'MYKEY1':42})

Read a bandpass from FITS table:

>>> bp = S.FileBandpass('/some/place/bandpass.fits')

Read a bandpass from ASCII table. Wavelength values must already be in the unit
of Angstrom:

>>> bp = S.FileBandpass('/some/place/bandpass.dat')

Write a bandpass to FITS table with default options:

>>> bp.writefits('/some/place/bandpass.fits')

Plot a bandpass:

>>> plt.plot(bp.wave, bp.throughput)

Plot a source spectrum:

>>> plt.plot(sp.wave, sp.flux)
