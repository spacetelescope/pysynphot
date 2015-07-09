.. _pysynphot-how-it-works:

*******************
How pysynphot works
*******************

The throughput calibration of the HST observatory is represented in a framework
consisting of:

* Component throughput files for every optical component (e.g., mirror, filter,
  polarizer, disperser, and detector).
* A configuration table describing the allowed combinations of the components.

In **pysynphot**, a particular observing mode is specified by a list of
keywords, which might be familiar names of filters, detectors, and gratings.
The keywords are used to trace the light path through the observatory via the
configuration graph file (a.k.a. the TMG file) which helps translating the
keyword list into a list of pointers to data files that contain the individual
component throughput functions.
The grand throughput function of the requested observing mode is then formed
by multiplying together the individual component throughput at each wavelength.
(See :ref:`pysynphot-appendixb`, :ref:`pysynphot-appendixc`, and
:ref:`Diaz 2012 <synphot-ref-diaz2012>` for more details on the internal
structure and functioning of the configuration graph and component throughput
tables.)

To retrieve a particular HST passband, you furnish the passband
generator with a couple of keywords, for example, ``"wfc3,uvis2,f555w"``.
The passband generator uses the keywords to trace a path through the graph
file, multiplies together the component passbands it encounters along the way,
and returns the passband evaluated on a particular wavelength grid. You can
also generate passband in functional form (see :ref:`pysynphot-bandpass`).

Passbands can then be convolved with spectral data to simulate HST
observations of particular targets. Spectra may come from existing
files containing lists of fluxes as a function of wavelength, or may be
dynamically generated (individually or in combination) as simple blackbody,
power-law, or continuum emission spectra of chosen temperatures and slopes
(see :ref:`pysynphot-spectrum` and :ref:`pysynphot-appendixa`).

Most **pysynphot** data I/O is done via FITS files with binary table
extensions, but ASCII tables can also be used. The HST instrument graph (TMG),
component lookup (a.k.a. TMC and TMT tables), and component throughput tables
are all in FITS format. Input data files, such as passband throughput
and spectral data files, may be in either FITS or ASCII format.


.. _pysynphot-database:

The pysynphot database
======================

The **pysynphot** package is entirely data driven. That is, no information
pertaining to the physical description of instruments or their
throughput characteristics is contained within the software, but is
instead contained within an external "database." These data must be
available in order to run any **pysynphot** tasks. The data set contains
the HST instrument graph, component lookup, and component throughput
tables, which are maintained and stored within the HST Calibration
Reference Data System (CRDS) at STScI. New versions of these tables
are created whenever new or updated calibration information become
available for the HST instruments.  Users at STScI have automatic access
to the **pysynphot** data set on all science computing clusters.
Because the data set is not currently distributed along with this
software, off-site users must retrieve and install it separately before
they will be able to use **pysynphot**. This can be done in one of two ways:

* TAR files: Every time a new **pysynphot** file is delivered to CRDS,
  a "snapshot" of the current **pysynphot** data set is copied into a
  few TAR files, which can then be retrieved, unpacked, and installed
  on your system. Instructions on how to do this can be found in
  :ref:`pysynphot-installation-setup`. This method offers the convenience of
  automatically creating the necessary directory tree for the data.
* Individual CRDS files: An alternate method is to transfer the
  individual tables using anonymous FTP (``ftp.stsci.edu``) to STScI
  from the directories given also in :ref:`pysynphot-installation-setup`.

The best method is perhaps a combination of the two: First-time
installers may wish to use the "snapshot" TAR files to initially
create and populate the directory structure, and then periodically
check the CRDS area at STScI for updates to individual tables.

The instrument graph and component lookup tables are contained in
the ``mtab/`` subdirectory and are named ``*_tmg.fits``, ``*_tmc.fits``,
and ``*_tmt.fits``.
The component throughput tables are logically grouped into
subdirectories of ``comp/`` corresponding to each of the HST
instruments (``acs``, ``cos``, ``fgs``, ``foc``, ``fos``, ``hrs``, ``hsp``,
``nicmos``, ``nonhst``, ``ota``, ``stis``, ``wfc3``, ``wfpc``, and ``wfpc2``).
Component throughput table
names contain a three digit suffix indicating their version number.
You can determine which tables are new by comparing either their
names or creation dates with the corresponding set of tables
installed on your machine.


.. _pysynphot-accuracy:

How Accurate are the Synthetic Photometry Results from pysynphot?
=================================================================

Because the **pysynphot** package is entirely data driven, the accuracy
of its results depends entirely on the accuracy of the bandpass
sensitivity curves, and zero points in the **pysynphot** database. The
accuracy of these values is dependent on the instrument and photometric
system under consideration.

As a general rule of thumb, synthetic photometry involving photometric
systems that have been defined from the ground, or photometry that is
given in ``vegamag``, should only be considered accurate to about 5%. The
accuracy is a strong function of wavelength and in particular for the
available HST Calibration spectra, the accuracy
might be about 5% shortward of :math:`1700 \AA`, where IUE is used,
and around 2% over the
STIS range. The accuracy is > 5% at the longer IR wavelengths where
the dust ring emission dominates (around 2 microns).

Synthetic photometry with the stable HST instrumentation, flying above
the atmosphere, when used in HST instrument natural systems, without
reference to ``vegamag``, can achieve accuracy much better than 5%; for
example, for ACS broad band filters it can be less or about 1%
(:ref:`De Marchi et al. 2004 <synphot-ref-demarchi2004>`).
For more details, see the Data Analysis section in the Data Handbooks
for the respective HST instruments.


.. _pysynphot-other-telescopes:

Can pysynphot be Used for Other Telescopes?
===========================================

Because the tasks in the **pysynphot** package are data driven,
instrument observing modes can be changed and new instruments added
without changing the software. To use **pysynphot** with non-HST
instruments or components you would need to modify (or rebuild)
only the instrument graph and component lookup tables. In addition,
you also need to set the appropriate
:ref:`telescope collecting area <pysynphot-area>`.

For the tables, **pysynphot** requires:

* One instrument graph table.
* One component lookup table.
* One thermal component lookup table (only needed for thermal
  background calculations for NICMOS and WFC3)
* One throughput table for each telescope and instrument component
  that appears in the graph and component lookup tables.

The names of the instrument graph and component lookup tables to
be used by **pysynphot** are set by :func:`~pysynphot.refs.setref`.
The names of the
individual component throughput tables are contained in the component
lookup table and are located automatically when needed. See
:ref:`pysynphot-appendixc` for details on the structure of these tables.
To build your own
instrument graph and component lookup tables, it is perhaps the easiest to
either start with a copy of the existing HST tables and modify or add
to them, or at least use the HST tables as a model for your own tables.

To make use of your own custom graph and component lookup tables, and telescope
area in **pysynphot**, just change the relevant values in
:func:`~pysynphot.refs.setref`.
