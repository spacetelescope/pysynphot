.. _pysynphot-doc-main:

**********************************
Astrolib PySynphot (**pysynphot**)
**********************************

Introduction
============

Astrolib PySynphot (hereafter referred to only as **pysynphot**) is an
object-oriented replacement for STSDAS SYNPHOT synthetic photometry package in
IRAF. It is distributed as part of
`AstroConda <http://astroconda.readthedocs.io/en/latest/>`_ (preferred)
and also as `standalone <https://pypi.python.org/pypi/pysynphot/>`_.
Although this package was developed for HST, it can be utilized with other
observatories.

**pysynphot** simulates photometric data and spectra as they are observed with
the Hubble Space Telescope (HST). Passbands for standard photometric systems are
available, and users can incorporate their own filters, spectra, and data.
**pysynphot** user interface allows you to:

* Construct complicated composite spectra from various grids of model atmosphere
  spectra, parameterized spectrum models, and atlases of stellar
  spectrophotometry.
* Simulate observations.
* Query the resulting structures for quantities of interest, such as countrate,
  effective wavelength, effective stimulus, as well as the wavelength and flux
  arrays.
* Plot HST sensitivity curves and calibration target spectra.
* Compute photometric calibration parameters for any HST instrument mode.

**pysynphot** can help HST observers to perform cross-instrument simulations, to
examine the transmission curve of the HST Optical Telescope Assembly (OTA), and
spectra of HST calibration targets. Expert users can take advantage of the
control and data structures available in Python to easily perform repetitive
operations such as simulate the observation of multiple type of sources through
multiple observing modes.

If you use **pysynphot** in your work, please cite it as,
"*Lim, P. L., Diaz, R. I., & Laidler, V. 2015, PySynphot User's Guide
(Baltimore, MD: STScI), https://pysynphot.readthedocs.io/en/latest/*".
Alternately, bibcode is available from
`Astrophysics Source Code Library <http://ascl.net/1303.023>`_.

If you have questions or concerns regarding the software, please contact
STScI Help Desk via ``help[at]stsci.edu``.


.. _pysynphot-installation-setup:

Installation and Setup
======================

If you have AstroConda, simply install with this command::

    conda install pysynphot

To install the PyPI release::

    pip install pysynphot

If missing, the following dependencies must also be installed:

* `astropy <https://pypi.python.org/pypi/astropy>`_ 1.1 or greater
* `numpy <https://pypi.python.org/pypi/numpy>`_ 1.9 or greater
* `matplotlib <http://matplotlib.org/>`_ (optional)

Data files for **pysynphot** are distributed separately by
`Calibration Reference Data System <http://www.stsci.edu/hst/observatory/crds/throughput.html>`_.
They are expected to follow a certain directory structure under the root
directory, identified by the ``PYSYN_CDBS`` environment variable that *must* be
set prior to using this package. In the example below, the root directory is
arbitrarily named ``/my/local/dir/cdbs/``.

In bash shell::

    export PYSYN_CDBS=/my/local/dir/cdbs/

In csh shell::

    setenv PYSYN_CDBS /my/local/dir/cdbs/

These data files [#f1]_ are needed for calculations involving HST bandpasses:

+----------------------------+------------------------------+-------------------------------------------------+
| Description                | Directory name               | Download                                        |
+============================+==============================+=================================================+
|Master tables               | $PYSYN_CDBS/mtab/            |ftp://ftp.stsci.edu/cdbs/tarfiles/synphot1.tar.gz|
+----------------------------+------------------------------+                                                 |
|HST/ACS throughput tables   | $PYSYN_CDBS/comp/acs/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/COS throughput tables   | $PYSYN_CDBS/comp/cos/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/FGS throughput tables   | $PYSYN_CDBS/comp/fgs/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/FOC throughput tables   | $PYSYN_CDBS/comp/foc/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/FOS throughput tables   | $PYSYN_CDBS/comp/fos/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/HRS throughput tables   | $PYSYN_CDBS/comp/hrs/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/HSP throughput tables   | $PYSYN_CDBS/comp/hsp/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/NICMOS throughput tables| $PYSYN_CDBS/comp/nicmos/     |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/OTA throughput tables   | $PYSYN_CDBS/comp/ota/        |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/STIS throughput tables  | $PYSYN_CDBS/comp/stis/       |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/WFC3 throughput tables  | $PYSYN_CDBS/comp/wfc3/       |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/WFPC1 throughput tables | $PYSYN_CDBS/comp/wfpc/       |                                                 |
+----------------------------+------------------------------+                                                 |
|HST/WFPC2 throughput tables | $PYSYN_CDBS/comp/wfpc2/      |                                                 |
+----------------------------+------------------------------+                                                 |
|Non-HST throughput tables   | $PYSYN_CDBS/comp/nonhst/     |                                                 |
+----------------------------+------------------------------+-------------------------------------------------+

These data files [#f1]_ are needed for calculations involving source spectra:

+------------------------------------------+----------------------------+-------------------------------------------------+
| Description                              | Directory name             | Download                                        |
+==========================================+============================+=================================================+
|Interstellar extinction curves            |$PYSYN_CDBS/extinction/     |ftp://ftp.stsci.edu/cdbs/tarfiles/synphot2.tar.gz|
+------------------------------------------+----------------------------+                                                 |
|AGN templates                             |$PYSYN_CDBS/grid/agn/       |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Bruzual-Charlot galaxy spectra            |$PYSYN_CDBS/grid/bc95/      |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Buser-Kurucz stellar atlas                |$PYSYN_CDBS/grid/bkmodels/  |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Bruzual-Persson-Gunn-Stryker stellar atlas|$PYSYN_CDBS/grid/bpgs/      |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Bruzual stellar atlas                     |$PYSYN_CDBS/grid/bz77/      |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Galactic emission line objects            |$PYSYN_CDBS/grid/galactic/  |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Gunn-Stryker atlas                        |$PYSYN_CDBS/grid/gunnstryker|                                                 |
+------------------------------------------+----------------------------+                                                 |
|Jacobi-Hunter-Christian stellar atlas     |$PYSYN_CDBS/grid/jacobi/    |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Kinney-Calzetti galaxy spectra            |$PYSYN_CDBS/grid/kc96/      |                                                 |
+------------------------------------------+----------------------------+                                                 |
|Pickles stellar atlas                     |$PYSYN_CDBS/grid/pickles/   |                                                 |
+------------------------------------------+----------------------------+-------------------------------------------------+
|Castelli & Kurucz (2004) stellar atlas    |$PYSYN_CDBS/grid/ck04models/|ftp://ftp.stsci.edu/cdbs/tarfiles/synphot3.tar.gz|
+------------------------------------------+----------------------------+-------------------------------------------------+
|Kurucz (1993) stellar atlas               |$PYSYN_CDBS/grid/k93models/ |ftp://ftp.stsci.edu/cdbs/tarfiles/synphot4.tar.gz|
+------------------------------------------+----------------------------+-------------------------------------------------+
|Phoenix stellar atlas                     |$PYSYN_CDBS/grid/phoenix/   |ftp://ftp.stsci.edu/cdbs/tarfiles/synphot5.tar.gz|
+------------------------------------------+----------------------------+-------------------------------------------------+
|HST calibration spectra                   |$PYSYN_CDBS/calspec/        |ftp://ftp.stsci.edu/cdbs/tarfiles/synphot6.tar.gz|
+------------------------------------------+----------------------------+-------------------------------------------------+

Throughout this document, unless explicitly stated otherwise, the examples
assume that ``PYSYN_CDBS`` points to the correct location, and that the relevant
packages are already imported:

>>> import os
>>> os.environ['PYSYN_CDBS']
'/my/local/dir/cdbs/'
>>> import numpy as np
>>> import pysynphot as S

For plotting, make sure you have the optional
`matplotlib <http://matplotlib.org/>`_ package and turn on its interactive mode:

>>> import matplotlib.pyplot as plt
>>> plt.ion()

Before drawing a new plot, you must clear the existing plot:

>>> plt.clf()


.. rubric:: Footnotes

.. [#f1] There is a known bug with the FTP service from Safari, so we recommend
   to use Firefox to download these files via FTP. If this does not work, use a
   standalone application or anonymous FTP; which is more likely to allow you
   access to these FTP areas.


.. _pysynphot-tree:

Using **pysynphot**
===================

.. toctree::
   :maxdepth: 1

   how_works
   using_pysynphot
   iraf_synphot
   bandpass
   spectrum
   observation
   properties
   refdata
   units
   tutorials
   appendixa
   appendixb
   appendixc
   ref_api


References
==========

.. _synphot-ref-bessell1983:

* Bessell, M. S. 1983, PASP, 95, 480

.. _synphot-ref-bessell1988:

* Bessell, M. S. & Brett, J. M. 1988, PASP, 100, 1134

.. _synphot-ref-bohlin2001:

* Bohlin, R. C., Dickinson, M. E., & Calzetti, D. 2001, AJ, 122, 2118

.. _synphot-ref-bohlin2004:

* Bohlin, R. C. & Gilliland, R. L. 2004, AJ, 127, 3508

.. _synphot-ref-calzetti2000:

* Calzetti, D., Armus, L., Bohlin, R. C., Kinney, A. L., Koornneef, J., & Storchi-Bergmann, T. 2000, ApJ, 533, 682

.. _synphot-ref-calzetti1994:

* Calzetti, D., Kinney, A. L., & Storchi-Bergmann, T. 1994, ApJ, 429, 582

.. _synphot-ref-cardelli1989:

* Cardelli, J. A., Clayton, G. C., & Mathis, J. S. 1989, ApJ, 345, 245

.. _synphot-ref-demarchi2004:

* `De Marchi, G. et al. 2004, ISR ACS 2004-08: Detector Quantum Efficiency and Photometric Zero Points of the ACS (Baltimore, MD: STScI) <http://www.stsci.edu/hst/acs/documents/isrs/isr0408.pdf>`_

.. _synphot-ref-diaz2012:

* `Diaz, R.I. 2012, ISR CDBS 2012-01: pysynphot/Synphot Throughput Files: Mapping to instrument components for ACS, COS, and WFC3 (Baltimore, MD: STScI) <http://www.stsci.edu/hst/observatory/crds/documents/TIR-CDBS-2012-01.pdf>`_

.. _synphot-ref-francis1991:

* Francis, P. J., Hewett, P. C., Foltz, C. B., Chaffee, F. H., Weymann, R. J., & Morris, S. L. 1991, ApJ, 373, 465

.. _synphot-ref-fukugita1996:

* Fukugita, M., Ichikawa, T., Gunn, J. E., Doi, M., Shimasaku, K., & Schneider, D. P. 1996, AJ, 111, 1748

.. _synphot-ref-gordon2003:

* Gordon, K. D., Clayton, G. C., Misselt, K. A., Landolt, A. U., & Wolff, M. J. 2003, ApJ, 594, 279

.. _synphot-ref-greenfield2007:

* `Greenfield, P. & Jedrzejewski, R. 2007, Using Python for Interactive Data Analysis (Baltimore, MD: STScI) <http://ssb.stsci.edu/perry/pydatatut.pdf>`_

.. _synphot-ref-gunn2001:

* `Gunn, J. E., Hogg, D., Finkbeiner, D., & Schlegel, D. 2001, Photometry White Paper <http://www.sdss.org/dr3/algorithms/sdssphot.ps>`_

.. _synphot-ref-gunn1983:

* Gunn, J. E. & Stryker, L. L. 1983, ApJS, 52, 121

.. _synphot-ref-harris1991:

* Harris, H., Baum, W., Hunter, D., & Kreidl, T. 1991, AJ, 101, 677

.. _synphot-ref-holberg2006:

* Holberg, J. B. & Bergeron, P. 2006, AJ, 132, 1221

.. _synphot-ref-howarth1983:

* Howarth, I. D. 1983, MNRAS, 203, 301

.. _synphot-ref-jacoby1984:

* Jacoby, G. H., Hunter, D. A., & Christian, C. A. 1984, ApJS, 56, 257

.. _synphot-ref-johnson1965:

* Johnson, H. L. 1965, ApJ, 141, 923

.. _synphot-ref-kinney1996:

* Kinney, A. L., Calzetti, D., Bohlin, R. C., McQuade, K., Storchi-Bergmann, T., & Schmitt, H. R. 1996, ApJ, 467, 38

.. _synphot-ref-koornneef1986:

* Koornneef, J., Bohlin, R., Buser, R., Horne, K., & Turnshek, D. 1986, Highlights Astron., 7, 833

.. _synphot-ref-laidler2009:

* `Laidler, V. 2009, TSR 2009-01: Pysynphot Commissioning Report (Baltimore, MD: STScI) <http://ssb.stsci.edu/tsr/2009_01/>`_

.. _synphot-ref-laidler2008:

* `Laidler, V., et al. 2008, Synphot Data User's Guide, Version 1.2 (Baltimore, MD: STScI) <http://www.stsci.edu/hst/HST_overview/documents/synphot/hst_synphotTOC.html>`_

.. _synphot-ref-landolt1983:

* Landolt, A. U. 1983, AJ, 88, 439

.. _synphot-ref-lub1977:

* Lub, J. & Pel, J. W. 1977, A&A, 54, 137

.. _synphot-ref-lupton1999:

* Lupton, R. H., Gunn, J. E., & Szalay A. S. 1999, AJ, 118, 1406

.. _synphot-ref-maiz2006:

* Maiz Apellaniz, J. 2006, AJ, 131, 1184

* `matplotlib Tutorial <http://matplotlib.org/users/pyplot_tutorial.html>`_

.. _synphot-ref-morrissey2007:

* Morrissey, P. et al. 2007, ApJS, 173, 682

.. _synphot-ref-oke1974:

* Oke, J. B., 1974, ApJS, 27, 21

.. _synphot-ref-oke1983:

* Oke, J. B. & Gunn, J. E. 1983, ApJ, 266, 713

.. _synphot-ref-pickles1998:

* Pickles, A. J. 1998, PASP, 110, 863

.. _synphot-ref-prevot1984:

* Prevot, M. L., Lequeux, J., Prevot, L., Maurice, E., & Rocca-Volmerange, B. 1984, A&A, 132, 389

* `pysynphot Code Repository <https://aeon.stsci.edu/ssb/trac/astrolib/browser/trunk/pysynphot>`_

* `pysynphot Open Issues <https://aeon.stsci.edu/ssb/trac/astrolib/query?status=assigned&status=new&status=reopened&component=pysynphot&col=id&col=summary&col=owner&col=type&col=status&col=priority&col=milestone&order=priority>`_

.. _synphot-ref-rybicki1979:

* Rybicki, G. B., & Lightman, A. P. 1979, Radiative Processes in Astrophysics (New York, NY: Wiley)

.. _synphot-ref-savage1979:

* Savage, B. D. & Mathis, J. S. 1979, ARA&A, 17, 73

.. _synphot-ref-schneider1983:

* Schneider, D. P., Gunn, J. E., & Hoessel J. G. 1983, ApJ, 264, 337

.. _synphot-ref-seaton1979:

* Seaton, M. J. 1979, MNRAS, 187, 785

.. _synphot-ref-smith2002:

* Smith, J. A. et al. 2002, AJ, 123, 2121

.. _synphot-ref-strecker1979:

* Strecker, D. W. et al. 1979, ApJS, 41, 501

.. _synphot-ref-vanduinen1975:

* van Duinen, R. J., Aalders, J. W. G., Wesselius, P. R., Wildeman, K. J., Wu, C. C., Luinge, W., & Snel, D. 1975, A&A, 39, 159
