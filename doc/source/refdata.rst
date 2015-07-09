.. _pysynphot-refdata:

**************
Reference Data
**************

Reference data has its history in IRAF STSDAS SYNPHOT::

    synphot> lpar refdata
    (area = 45238.93416) Telescope area in cm^2
    (grtbl = "mtab$*_tmg.fits") Instrument graph table
    (cmptbl = "mtab$*_tmc.fits") Instrument component table
    (mode = "a")

In **pysynphot**, reference data is expanded to manage the following:

* Instrument graph table (``graphtable``)
* Instrument component table (``comptable``)
* Instrument thermal component table (``thermtable``)
* :ref:`Telescope collecting area <pysynphot-area>` (``area``)
* Default :ref:`wavelength set <pysynphot-wavelength-table>` (``waveset``)

The current settings can be displayed with :func:`~pysynphot.refs.showref`.
To use custom settings or reset any changes back to software default, you can
use :func:`~pysynphot.refs.setref`. Meanwhile, :func:`~pysynphot.refs.getref`
also returns the current settings, but as a Python :py:class:`dict` instead of
printing to screen. For example:

>>> S.showref()
thermtable: /my/local/dir/cdbs/mtab/tae17277m_tmt.fits
   waveset: Min: 500, Max: 26000, Num: 10000.0, Delta: None, Log: True
 comptable: /my/local/dir/cdbs/mtab/yah1742rm_tmc.fits
graphtable: /my/local/dir/cdbs/mtab/yah1742qm_tmg.fits
      area: 45238.93416
>>> S.setref(graphtable='new_tmg.fits', comptable='new_tmc.fits', area=1)
>>> S.showref()
thermtable: /my/local/dir/cdbs/mtab/tae17277m_tmt.fits
   waveset: Min: 500, Max: 26000, Num: 10000.0, Delta: None, Log: True
 comptable: new_tmc.fits
graphtable: new_tmg.fits
      area: 1
>>> S.setref()  # Reset to software default
>>> S.showref()
thermtable: /my/local/dir/cdbs/mtab/tae17277m_tmt.fits
   waveset: Min: 500, Max: 26000, Num: 10000.0, Delta: None, Log: True
 comptable: /my/local/dir/cdbs/mtab/yah1742rm_tmc.fits
graphtable: /my/local/dir/cdbs/mtab/yah1742qm_tmg.fits
      area: 45238.93416
>>> S.refs.getref()
{'area': 45238.93416,
 'comptable': '/my/local/dir/cdbs/mtab/yah1742rm_tmc.fits',
 'graphtable': '/my/local/dir/cdbs/mtab/yah1742qm_tmg.fits',
 'thermtable': '/my/local/dir/cdbs/mtab/tae17277m_tmt.fits',
 'waveset': 'Min: 500, Max: 26000, Num: 10000.0, Delta: None, Log: True'}

Changing the default tables is not recommended unless you know what you are
doing because **pysynphot** always uses the most up-to-date version in your
``$PYSYN_CDBS/mtab/`` directory.

The HST bandpass for available
:ref:`observation modes <pysynphot-obsmode-bandpass>`
are defined by ``graphtable`` and ``comptable``. In addition, for IR
instruments, thermal component is defined by ``thermtable``. These files are
described in detail in :ref:`Appendix C <pysynphot-appendixc>`. It is also
possible to
:ref:`provide your own tables and telescope area for other telescopes <pysynphot-other-telescopes>`.

The tables decide which throughput files will be used for a particular
observation mode. They can be displayed using
:meth:`~pysynphot.obsbandpass.ObsModeBandpass.showfiles`. A bandpass that does
not rely on the tables does not have this feature. For example:

>>> bp_hst = S.ObsBandpass('wfc3,ir,f105w')
>>> bp_hst.name
'wfc3,ir,f105w'
>>> bp_hst.showfiles()
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_primary_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_secondary_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_pom_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_csm_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_fold_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_mir1_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_mir2_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_mask_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_rcp_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_f105w_004_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_win_001_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_qe_003_syn.fits
/my/local/dir/cdbs/comp/wfc3/wfc3_ir_cor_004_syn.fits
>>> bp_nonhst = S.ObsBandpass('johnson,v')
>>> bp_nonhst.name
'/my/local/dir/cdbs/comp/nonhst/johnson_v_004_syn.fits'
>>> bp_nonhst.showfiles()
AttributeError: 'TabularSpectralElement' object has no attribute 'showfiles'

Every HST observation mode has an optimal binned wavelength set (``binset``) for
constructing an :ref:`pysynphot-observation`. The ``binset`` is set according to
a pre-defined wavelength catalog in ``pysynphot.locations.wavecat`` and can be
accessed via :meth:`~pysynphot.observationmode.BaseObservationMode.bandWave`.
The default ``waveset`` shown above is used for when such a ``binset`` is not
available. The example below illustrate both situations:

>>> S.locations.wavecat
'/my/installation/path/pysynphot/data/wavecat.dat'
>>> bp_hst.obsmode.bandWave()
array([  7000.,   7001.,   7002., ...,  17998.,  17999.,  18000.])
>>> bp_nonhst.obsmode.bandWave()
AttributeError: 'TabularSpectralElement' object has no attribute 'obsmode'


.. _pysynphot-area:

Area
====

Some calculations require the telescope collecting area in
:math:`\textnormal{cm}^{2}`. For example, flux conversion involving counts or
``obmag``, and  :ref:`bandpass unit response <pysynphot-formula-uresp>`
calculation.

When an area is required, a spectrum object first looks in its ``primary_area``
class attribute. If it is undefined, the object then takes the value from
``pysynphot.refs.PRIMARY_AREA``, which defaults to the area of the HST primary
mirror but can be changed with :func:`~pysynphot.refs.setref` (see
:ref:`pysynphot-refdata`).

For non-HST calculations, you can set the primary area to the value of your
telescope right after you import **pysynphot** and just leave it at that for the
rest of the session. For HST calculations, you do not have to do anything
because it is the default value. When in doubt, check the ``primary_area`` class
attributes of your spectrum objects.

Composite spectra (`~pysynphot.spectrum.CompositeSourceSpectrum` and
`~pysynphot.spectrum.CompositeSpectralElement`) inherit their
``primary_area`` values from either of the input spectra, if defined. If both
input spectra have defined but different values, then an error is raised.

Bandpass object constructed from observation mode string
(`~pysynphot.obsbandpass.ObsModeBandpass`) inherits its ``primary_area`` value
from `~pysynphot.tables.GraphTable`, which in turn read its value from
``PRIMAREA`` keyword in the table primary header of the given ``*_tmg.fits``
file.

`~pysynphot.observation.Observation` inherits its ``primary_area`` from the
input bandpass.


.. _pysynphot-wavelength-table:

Wavelength Table
================

The wavelength table is a feature inherited from IRAF STSDAS SYNPHOT, in which
it is known as ``wavetab``. It is used to specify the name of a file containing
a list of wavelength values that determine the wavelength grid to be used in the
calculations and plotting. In **pysynphot**, this is equivalent to ``waveset``,
``binwave``, or ``binset``, depending on the type of spectral objects that
you are working with.

The default ``waveset`` can be changed using :func:`~pysynphot.refs.setref`.
This is used when a spectral object has no instrument-specific (see below)
or custom wavelength set (e.g., a Gaussian source has its own values that
tightly sample the peak). The default grid consists of 10000 points covering
500 to 26000 Angstroms (sufficient for most HST calculations), spaced
logarithmically with :func:`numpy.logspace` such that:

.. math::

       \log \lambda = \log \lambda_{min} + (\log \lambda_{max} - \log \lambda_{min}) \frac{i}{N}

where

* :math:`N` is the number of data points
* :math:`i` is the index value, starting from 0
* :math:`\lambda_{min}` and :math:`\lambda_{max}` are the wavelength limits

Instrument-specific wavelength sets (``binwave``) are stored in a data file
defined by ``pysynphot.locations.wavecat``, which is "wavecat.dat" that comes
with the software by default; The wavelength grid contains optimal coverage
and resolution that is appropriate for each HST instrument.

Instead of modifying ``wavecat``, which requires the knowledge of how
`~pysynphot.wavetable` works, it is easier to just provide your own
``binset``. You can generate wavelength values using :func:`numpy.arange` (also
accessible as ``pysynphot.Waveset()``). If you wish to save the values in a
file, follow the instructions in :ref:`pysynphot-io` but ignore the second
column (for flux or throughput). The wavelength values must be monotonically
increasing or decreasing. See :ref:`pysynphot_tutorial_6` for a working example.
