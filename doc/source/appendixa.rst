.. _pysynphot-appendixa:

*****************************************
Appendix A: Catalogs and Spectral Atlases
*****************************************

There are several spectral atlases consisting of both observed
and model data, which are available in FITS table format for use
with **pysynphot**. They are as tabulated below.

Current descriptions and access to all available
calibration spectra and astronomical catalogs be found at the
`CRDS website <http://www.stsci.edu/hst/observatory/crds/astronomical_catalogs.html>`_,
which supersedes this documentation in case of conflicting information.
The data files are available at STScI on all science computing clusters in the
``$PYSYN_CDBS`` directory. Off-site users can obtain these data via
anonymous FTP (see :ref:`pysynphot-installation-setup`).

Stellar models:

+-------------------------------------+-------------------------------+--------------+
|Atlas/Catalog                        |Installation Path              |Interpolatable|
+=====================================+===============================+==============+
|:ref:`pysynphot-appendixa-ck04`      |$PYSYN_CDBS/grid/ck04models    |Yes           |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-kurucz1993`|$PYSYN_CDBS/grid/k93models     |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-phoenix`   |$PYSYN_CDBS/grid/phoenix       |              |
+-------------------------------------+-------------------------------+--------------+
|:ref:`pysynphot-appendixa-calspec`   |$PYSYN_CDBS/calspec            |No            |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-pickles`   |$PYSYN_CDBS/grid/pickles       |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-bkmodels`  |$PYSYN_CDBS/grid/bkmodels      |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-bz77`      |$PYSYN_CDBS/grid/bz77          |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-gs`        |$PYSYN_CDBS/grid/gunnstryker   |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-bpgs`      |$PYSYN_CDBS/grid/bpgs          |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-jacobi`    |$PYSYN_CDBS/grid/jacobi        |              |
+-------------------------------------+-------------------------------+--------------+

Non-stellar models:

+-------------------------------------+-------------------------------+--------------+
|Atlas/Catalog                        |Installation Path              |Interpolatable|
+=====================================+===============================+==============+
|:ref:`pysynphot-appendixa-bc95`      |$PYSYN_CDBS/grid/bc95/templates|No            |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-kc96`      |$PYSYN_CDBS/grid/kc96          |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-agn`       |$PYSYN_CDBS/grid/agn           |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-galactic`  |$PYSYN_CDBS/grid/galactic      |              |
+-------------------------------------+-------------------------------+              |
|:ref:`pysynphot-appendixa-etcsource` |$PYSYN_CDBS/etc/source         |              |
+-------------------------------------+-------------------------------+--------------+


.. _pysynphot-appendixa-ck04:

Castelli-Kurucz Atlas
=====================

The ``$PYSYN_CDBS/grid/ck04models`` directory contains ATLAS9 stellar atmosphere
models by Castelli & Kurucz 2004. There are about 4300 models for a wide range
of metallicities, effective temperatures and gravities. The ones available
in CRDS are from "the Grids of ATLAS9-ODFNEW Models and Fluxes" from
`Dr. F. Castelli's webpage <http://wwwuser.oats.inaf.it/castelli/grids.html>`_
(created on January 2007) and also available from
`Dr. R. Kurucz's webpage <http://kurucz.harvard.edu>`_. See
`Castelli-Kurucz 2004 atlas README file <http://www.stsci.edu/hst/observatory/crds/castelli_kurucz_atlas.html>`_
for more details.
The atlas data files are organized in a similar naming convention as
:ref:`pysynphot-appendixa-kurucz1993`, and are easily accessible using
`~pysynphot.catalog.Icat` (also see :ref:`pysynphot-spec-atlas`).

The example below generates a spectrum with metallicity ``[M/H] = +0.1``,
temperature :math:`T_{\textnormal{eff}} = 10000 \textnormal{K}`, and gravity
:math:`\log g = 3.0`:

>>> sp = S.Icat('ck04models', 10000, 0.1, 3.0)


.. _pysynphot-appendixa-kurucz1993:

Kurucz Atlas
============

The ``$PYSYN_CDBS/grid/k93models`` directory contains the Kurucz 1993 Atlas
of Model Atmospheres. The atlas contains about 7600 stellar
atmosphere models for a wide range of metallicities, effective temperatures,
and gravities. These LTE models have improved opacities
and are computed with a finer wavelength and temperature resolution
than the :ref:`pysynphot-appendixa-bkmodels`.
The micro-turbulent velocity is 2 km/s.
This atlas is installed in CRDS from the Kurucz database at
Goddard Space Flight Center. The original atlas (CD-ROM No. 13)
was created on August 22, 1993 and can be obtained from Dr. R. Kurucz.
Considering that the entire atlas occupies close to 70 MB of disk space,
many applications could be satisfied by a copy of the solar metallicity
spectra only (Table 2 of the README file).
See
`Kurucz 1993 atlas README file <ftp://ftp.stsci.edu/cdbs/grid/k93models/AA_README>`_
for more details.

The models are in ``flam`` *surface* flux units. If the number of counts or the
absolute flux is needed, the model spectrum must be
:ref:`renormalized <pysynphot-renorm>` appropriately.

The following example shows the header from one of the atlas data files.
This file contains all the models for a star of metallicity
``[M/H] = 0.0`` (``p00``) and effective temperature
:math:`T_{\textnormal{eff}} = 8000 \textnormal{K}` (``8000``), which cover a
range of gravities from :math:`\log g = +1.0` (``g10``) to
:math:`\log g = +5.0` (``g50``).
In this example, :math:`\log g = +0.0` and :math:`\log g = +0.5` are unavailable,
thus ``g00`` and ``g05`` are not listed in the header, and their corresponding
columns in the file are filled with zeroes.

>>> from astropy.io import fits
>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'k93models', 'kp00', 'kp00_8000.fits')
>>> hdr = fits.getheader(filename)
>>> hdr
SIMPLE  =                    T / file does conform to FITS standard
BITPIX  =                   16 / number of bits per data pixel
NAXIS   =                    0 / number of data axes
EXTEND  =                    T / FITS dataset may contain extensions
COMMENT   FITS (Flexible Image Transport System) format defined in Astronomy and
COMMENT   Astrophysics Supplement Series v44/p363, v44/p371, v73/p359, v73/p365.
COMMENT   Contact the NASA Science Office of Standards and Technology for the
COMMENT   FITS Definition document #100 and other FITS information.
ORIGIN  = 'STScI-STSDAS/TABLES' / Tables version 1999-03-22
FILENAME= 'kp00_8000.fits'     / name of file
TEFF    =                 8000
LOG_Z   = 0.00000000000000E+00
HISTORY   g10
HISTORY   g15
HISTORY   g20
HISTORY   g25
HISTORY   g30
HISTORY   g35
HISTORY   g40
HISTORY   g45
HISTORY   g50
HISTORY   Kurucz model atmospheres (1993)
HISTORY   Fluxes tabulated in units of erg/s/cm^2/A
HISTORY   are surface fluxes. To transform to observed
HISTORY   fluxes multiply by (R/D)^2 where R is the
HISTORY   radius of the star and D the distance.
HISTORY   Each column in the table represents the
HISTORY   spectrum of a star for the same metallicity
HISTORY   and effective temperature but different gravity.

The example below shows you how to manually select the flux for a specific
model characterized by a given metallicity, effective temperature, and gravity.
The filename ``kp01_10000`` means ``[M/H] = +0.1`` (``p01``) and
:math:`T_{\textnormal{eff}} = 10000 \textnormal{K}` (``10000``). The column
name ``g30`` means :math:`\log g = 3.0`:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'k93models', 'kp01', 'kp01_10000.fits')
>>> spec = fits.getdata(filename)
>>> wave = spec['WAVELENGTH']
>>> flux = spec['g30']

The easier way to to use `~pysynphot.catalog.Icat` (also see
:ref:`pysynphot-spec-atlas`). Equivalent to the example above:

>>> sp = S.Icat('k93models', 10000, 0.1, 3.0)


.. _pysynphot-appendixa-phoenix:

Phoenix Models
==============

The ``$PYSYN_CDBS/grid/phoenix`` directory contains models provided by
`F. Allard et al. <http://perso.ens-lyon.fr/france.allard/>`_
and can be found in the
`Star, Brown Dwarf, and Planet Simulator <http://phoenix.ens-lyon.fr/simulator/index.faces>`_. They use static, spherical symmetric, 1D simulations to completely
describe the atmospheric emission spectrum. The models account for the
formation of molecular bands, such as those of water vapor, methane, or
titanium dioxide, solving for the transfer equation over more than 20,000
wavelength points on average, producing synthetic spectra with 2 Angstroms
resolution. The line selection is repeated at each iteration of the model
until it has converged and the thermal structure obtained. The models here
are calculated with a cloud model, valid across the entire parameter range.
See
`Phoenix models README file <http://www.stsci.edu/hst/observatory/crds/SIfileInfo/pysynphottables/index_phoenix_models_html>`_
for more details.
The atlas data files are organized in a similar naming convention as
:ref:`pysynphot-appendixa-kurucz1993`, and are easily accessible using
`~pysynphot.catalog.Icat` (also see :ref:`pysynphot-spec-atlas`).

The example below generates a spectrum with metallicity ``[M/H] = +0.1``,
temperature :math:`T_{\textnormal{eff}} = 10000 \textnormal{K}`, and gravity
:math:`\log g = 3.0`:

>>> sp = S.Icat('phoenix', 10000, 0.1, 3.0)


.. _pysynphot-appendixa-calspec:

HST Calibration Spectra
=======================

The ``$PYSYN_CDBS/calspec`` directory contains the composite stellar spectra
that are the fundamental flux standards for HST calibrations. All
files are in machine-independent binary FITS table format. Information
about the pedigree of a given spectrum is in the header of the FITS
table file, which can be read using `astropy.io.fits`. The example below reads
the header from G191B2B spectrum and then loads it into **pysynphot**:

>>> from astropy.io import fits
>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'calspec', 'g191b2b_mod_010.fits')
>>> hdr = fits.getheader(filename)
>>> hdr
SIMPLE  =                    T / Fits standard
BITPIX  =                   16 / Bits per pixel
NAXIS   =                    0 / Number of axes
EXTEND  =                    T / File may contain extensions
ORIGIN  = 'NOAO-IRAF FITS Image Kernel July 2003' / FITS file originator
DATE    = '2015-01-06T17:00:20' / Date FITS file was generated
IRAF-TLM= '2015-01-06T17:00:24' / Time of last modification
SOURCE  = 'Bohlin, Gordon, Tremblay 2014, PASP, 126, 711' /
COMMENT = 'Rauch: METAL LINE BLANKETED NLTE MODEL' /
TEFFGRAV= '59000/7.60'         /Teff/log g for model
DESCRIP = 'MODEL Fluxes ------------------------------------------------------'
DBTABLE = 'CRSPECTRUM'         /
TARGETID= 'G191B2B_MOD'        /
AIRMASS =              0.00000 /mean airmass of the observation
USEAFTER= 'Jan 01 2000 00:00:00' /
PEDIGREE= 'MODEL   '           /
WMIN    =        100.000000000 /Minimum Wavelength
WMAX    =        400104.068000 /Maximum Wavelength
FILENAME= 'g191b2b_mod_010.fits' /
HISTORY Model directory: /internal/1/models/rauch/
HISTORY Model 0059000_7.60_ABUND_015_LF_000100-400000
HISTORY Vega Flux at 5557.5A (5556 air) = 3.44e-9 erg s-1 cm-2 A-1
HISTORY Vega & Star elect/s= 12326689.78     237.70
HISTORY Model Reddened by E(B-V)=0.0005
HISTORY Model Normalization factor=   2.1760340e-30
HISTORY Written by newmakstd.pro 23-Dec-2014 10:15:43.00
HISTORY Vacuum Wavelengths
HISTORY UNITS: Wavelength(Angstroms), Flux(erg s-1 cm-2 Ang-1)
HISTORY Vega Flux(5556A)=3.44e-9 (Bohlin 2014, AJ, 147, 127)
HISTORY INPUT FILE: /internal/1/wd/dat/g191.rauch59000-nlte
HISTORY Written by MAKE_MOD_CALSPEC.pro  23-Dec-2014 10:20:09.00
>>> sp = S.FileSpectrum(filename)

Note that in some cases, the calibration spectrum is truncated in the blue or
the red at wavelength longer or shorter, respectively, than the sensitivity
limit of the instrument. As a result, **pysynphot** may underestimate the total
counts. Users should check that the wavelength range of the spectrum they are
using is compatible with the wavelength range of the calculation they require.

See `CALSPEC Calibration Database <http://www.stsci.edu/hst/observatory/crds/calspec.html>`_
for available spectra and their descriptions.


.. _pysynphot-appendixa-pickles:

Pickles Library
===============

The ``$PYSYN_CDBS/grid/pickles`` directory contains the stellar spectral flux
library by :ref:`Pickles (1998) <synphot-ref-pickles1998>`.
This library of wide spectral coverage, consists of 131 flux calibrated
stellar spectra, encompassing all normal spectral types and luminosity
classes at solar abundance, and metal-weak and metal-rich F-K dwarf
and G-K giant components. Each spectrum in the library is a combination of
several sources overlapping in wavelength coverage. See
`Pickles library README file <http://www.stsci.edu/hst/observatory/crds/pickles_atlas.html>`_
for more details.

The library data were obtained from
`its webpage <http://cdsarc.u-strasbg.fr/viz-bin/ftp-index?J/PASP/110/863>`_ and
divided into two sub-directories below:

* ``dat_uvi`` (a.k.a. UVILIB) groups all spectra derived from all UV, optical,
  and near-IR sources, in the wavelength range 1150-10620 Angstroms.
  It has complete spectral coverage for all components over this wavelength
  range. Its data files are named "pickles_ttt.fits", where ``ttt`` is a number
  ranging from 1 to 131.
* ``dat_uvk`` (a.k.a. UVKLIB) groups all spectra that were derived by combining
  the UVILIB spectra with additional IR data to a long wavelength limit of
  25000 Angstroms. Its data files are named "pickles_uk_ttt.fits", where ``ttt``
  is a number ranging from 1 to 131.

The example below loads a source spectrum of spectral type G5V from the UVKLIB
subset of the library:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'pickles', 'dat_uvk', 'pickles_uk_27.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-bkmodels:

Buser-Kurucz Atlas
==================

The ``$PYSYN_CDBS/grid/bkmodels`` directory contains an extensive collection
of Kurucz model atmosphere spectra provided by R. Buser, covering a wide range
in metallicity, effective temperature, and gravity. For all the spectra, fluxes
are given mostly with a resolution of 25 Angstroms on a uniform grid of
wavelengths from the UV to the IR. Thus, the atlas is especially suited for
synthetic photometry applications, including the calibration and the
interpretation of HST observations
(:ref:`Koornneef et al. 1986 <synphot-ref-koornneef1986>`).
The atlas is grouped into different "blocks" (A, B, C, D, M, and S),
corresponding to the physical distinctions of their underlying model
atmospheres. It consists of 1434 files, each of which represents a metal-line
blanketed flux spectrum for a theoretical stellar model atmosphere.
Data files are named "bk_mnnnn.fits", where ``m`` is the block code and
``nnnn`` the sequence number. See
`Buser-Kurucz atlas README file <http://www.stsci.edu/hst/observatory/crds/bkmodels.html>`_
for more details, in including the mapping of filenames to their respective
parameter specifications.

The example below loads Block S (models for the Sun and Vega) with
:math:`T_{\textnormal{eff}} = 5770 \textnormal{K}` and gravity
:math:`\log g = 4.44`:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'bkmodels', 'bk_s0001.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-bz77:

Bruzual Atlas
=============

The ``$PYSYN_CDBS/grid/bz77`` directory contains 77 stellar spectra that are
frequently used in the synthesis of galaxy spectra. They were provided by
Gustavo Bruzual. Each spectrum is stored in a table named "bz_nn.fits",
where ``nn`` runs from 1 to 77. See
`Bruzual atlas README file <http://www.stsci.edu/hst/observatory/crds/bz77.html>`_
for a mapping of filenames to their respective spectral types.

The example below loads a source spectrum of spectral type G5V from the atlas:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'bz77', 'bz_27.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-gs:

Gunn-Stryker Atlas
==================

The ``$PYSYN_CDBS/grid/gunnstryker`` contains the optical spectrophotometric
catalog of 175 stars, covering a complete range of spectral types and luminosity
classes from the observations of
:ref:`Gunn & Stryker (1983) <synphot-ref-gunn1983>`.
The spectra cover the wavelength range 3130 to 10800 Angstroms.
Each spectrum is stored in a table named "gs_nnn.fits",
where ``nnn`` runs from 1 to 175. See
`Gunn-Stryker atlas README file <http://www.stsci.edu/hst/observatory/crds/gs.html>`_
for a mapping of filenames to their respective spectral types.

The example below loads a source spectrum of spectral type G5V from the atlas:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'gunnstryker', 'gs_44.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-bpgs:

Bruzual-Persson-Gunn-Stryker Atlas
==================================

The ``$PYSYN_CDBS/grid/bpgs`` directory contains the extension of
:ref:`pysynphot-appendixa-gs`, where the spectral data have been extended into
both the UV and the IR. The IR data are from
:ref:`Strecker et al. (1979) <synphot-ref-strecker1979>` and other unpublished
sources. The IR and the optical data are tied together by the :math:`V – K`
colors.
Each spectrum is stored in a table named "bpgs_nnn.fits",
where ``nnn`` runs from 1 to 175. See
`Bruzual-Persson-Gunn-Stryker atlas README file <http://www.stsci.edu/hst/observatory/crds/bpgs.html>`_
for a mapping of filenames to their respective spectral types.

Note that the spectral data for all of the stars in this atlas have been
arbitrarily renormalized to a *V* magnitude of zero. Therefore, in order to
use these data for calculations of absolute photometry, they must be
:ref:`renormalized <pysynphot-renorm>` to their appropriate absolute levels.
In addition, the magnitudes and colors stored in their header keywords
are not on the standard *UBVRI* system, but rather "scanner" magnitudes and
colors that were synthesized by the authors from the observed spectra (see
:ref:`Gunn & Stryker 1983 <synphot-ref-gunn1983>`).

The example below loads a source spectrum of spectral type G5V from the atlas:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'bpgs', 'bpgs_44.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-jacobi:

Jacoby-Hunter-Christian Atlas
=============================

The ``$PYSYN_CDBS/grid/jacobi`` directory contains the optical
spectrophotometric atlas of 161 stars having spectral classes O through M,
and luminosity classes V, III, and I. The data are from the observations of
:ref:`Jacoby, Hunter, & Christian (1984) <synphot-ref-jacoby1984>`.
They cover the wavelength range 3510 to 7427 Angstroms at a resolution of
approximately 4.5 Angstroms.
Each spectrum is stored in a table named "jc_nnn.fits",
where ``nnn`` runs from 1 to 161. See
`Jacoby-Hunter-Christian atlas README file <http://www.stsci.edu/hst/observatory/crds/JHC.html>`_
for a mapping of filenames to their respective spectral types.

The example below loads a source spectrum of spectral type G0V from the atlas:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'jacobi', 'jc_43.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-bc95:

Bruzual-Charlot Atlas
=====================

The ``$PYSYN_CDBS/grid/bc95/templates`` directory contains a library of galaxy
spectra computed using the Isochrone Synthesis Spectral Evolutionary Code from
Bruzual & Charlot (December 1995 version). The spectra represent bursts
characterized by a Salpeter IMF with different ranges in lower and upper
mass limits, and at several ages after the burst.
Spectra for instantaneous and composite bursts are both available.
Each spectrum has 1187 wavelength points covering the 0.01 to 100 microns range.
The flux unit is solar luminosity per Angstrom.
The nebular contribution to the SED (i.e., emission lines and nebular continuum)
is not included in the spectra. See
`Bruzual-Charlot atlas README file <http://www.stsci.edu/hst/observatory/crds/cdbs_bc95.html>`_
for available spectra and their descriptions.

The example below loads a galaxy spectrum with Salpeter IMF containing mass
limits from 0.1-30 :math:`M_{\odot}` and :math:`50 \times 10^{5}` year-old instantaneous burst:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'bc95', 'templates', 'bc95_c_50E5.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-kc96:

Kinney-Calzetti Atlas
=====================

The ``$PYSYN_CDBS/grid/kc96`` directory contains an homogeneous set of
12 spectral templates of galaxies covering the UV, optical, and near-IR
wavelength range up to about 1 micron. Templates include various morphological
types (:ref:`Kinney et al. 1996 <synphot-ref-kinney1996>`) and starburst
galaxies (:ref:`Calzetti et al. 1994 <synphot-ref-calzetti1994>`).
The flux of the spectral templates has been normalized to a visual magnitude
of 12.5 ``stmag``. See
`Kinney-Calzetti atlas README file <http://www.stsci.edu/hst/observatory/crds/cdbs_kc96.html>`_
for more details.

The example below loads a galaxy spectrum from the elliptical template:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'kc96', 'elliptical_template.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-agn:

AGN Atlas
=========

The ``$PYSYN_CDBS/grid/agn`` directory contains a few spectral templates of AGNs
ranging from LINER to Seyfert and bright QSO (Calzetti 1995, private
communication; :ref:`Francis et al. 1991 <synphot-ref-francis1991>`;
J. R. Walsh, private communication).
The flux of the LINER and Seyfert 2 templates is normalized to a Johnson *V*
magnitude of 12.5 ``stmag``, while the Seyfert 1 and QSO templates are
normalized to a Johnson *B* magnitude of 12.5 ``stmag``. See
`AGN atlas README file <http://www.stsci.edu/hst/observatory/crds/cdbs_agn.html>`_
for more details.

The example below loads a Seyfert 2 spectrum:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'agn', 'seyfert2_template.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-galactic:

Galactic Atlas
==============

The ``$PYSYN_CDBS/grid/galactic`` directory contains the model spectra of
Orion nebula and NGC 7009 planetary nebula (J. R. Walsh, private communication).
See
`Galactic atlas README file <http://www.stsci.edu/hst/observatory/crds/cdbs_galactic.html>`_
for more details.

The example below loads the spectrum for Orion nebula:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'grid', 'galactic', 'orion_template.fits')
>>> sp = S.FileSpectrum(filename)


.. _pysynphot-appendixa-etcsource:

Other Non-Stellar Objects
=========================

The ``$PYSYN_CDBS/etc/source`` directory contains spectra for
`various non-stellar objects used in ETC <http://etc.stsci.edu/etcstatic/users_guide/1_ref_2_spectral_distribution.html#non-stellar-spectra>`_. See `Non-stellar objects README file <http://www.stsci.edu/hst/observatory/crds/non-stellar.html>`_
for more details.

The example below loads a spectrum for Gliese 229B brown dwarf:

>>> filename = os.path.join(
...     os.environ['PYSYN_CDBS'], 'etc', 'source', 'gl229b_001.dat')
>>> sp = S.FileSpectrum(filename)
