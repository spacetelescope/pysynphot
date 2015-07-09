.. _pysynphot-api:

*************
Reference/API
*************


``pysynphot.binning``
=====================

.. currentmodule:: pysynphot.binning

.. automodule:: pysynphot.binning
   :members:


``pysynphot.Cache``
===================

.. currentmodule:: pysynphot.Cache

.. automodule:: pysynphot.Cache
   :members:


``pysynphot.catalog``
=====================

.. currentmodule:: pysynphot.catalog

.. automodule:: pysynphot.catalog

.. inheritance-diagram:: pysynphot.catalog.Icat
   :parts: 1

.. autoclass:: pysynphot.catalog.Icat
   :show-inheritance:
   :members:


``pysynphot.exceptions``
========================

.. currentmodule:: pysynphot.exceptions

.. automodule:: pysynphot.exceptions

.. inheritance-diagram:: pysynphot.exceptions
   :parts: 1

.. autoclass:: pysynphot.exceptions.PysynphotError
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.TableFormatError
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.DuplicateWavelength
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.ZeroWavelength
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.UnsortedWavelength
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.BadRow
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.OverlapError
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.PartialOverlap
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.DisjointError
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.GraphtabError
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.UnusedKeyword
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.IncompleteObsmode
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.AmbiguousObsmode
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.UndefinedBinset
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.ExtrapolationNotAllowed
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.ParameterOutOfBounds
   :show-inheritance:

.. autoclass:: pysynphot.exceptions.IncompatibleSources
   :show-inheritance:


``pysynphot.extinction``
========================

.. currentmodule:: pysynphot.extinction

.. automodule:: pysynphot.extinction

.. inheritance-diagram:: pysynphot.extinction.DeprecatedExtinction
   :parts: 1

.. autoclass:: pysynphot.extinction.DeprecatedExtinction
   :show-inheritance:

.. autoclass:: pysynphot.extinction.Gal1
.. autoclass:: pysynphot.extinction.Smc
.. autoclass:: pysynphot.extinction.Lmc
.. autoclass:: pysynphot.extinction.Xgal


``pysynphot.locations``
=======================

.. currentmodule:: pysynphot.locations

.. automodule:: pysynphot.locations
   :members:


``pysynphot.obsbandpass``
=========================

.. currentmodule:: pysynphot.obsbandpass

.. automodule:: pysynphot.obsbandpass
   :members: ObsBandpass

.. inheritance-diagram:: pysynphot.obsbandpass.ObsModeBandpass
   :parts: 1

.. autoclass:: pysynphot.obsbandpass.ObsModeBandpass
   :show-inheritance:
   :members:
   :exclude-members: fwhm

.. autofunction:: pysynphot.obsbandpass.pixel_range
.. autofunction:: pysynphot.obsbandpass.wave_range


``pysynphot.observationmode``
=============================

.. currentmodule:: pysynphot.observationmode

.. automodule:: pysynphot.observationmode

.. inheritance-diagram:: pysynphot.observationmode.ObservationMode
   :parts: 1

.. autoclass:: pysynphot.observationmode.BaseObservationMode
   :members:

.. autoclass:: pysynphot.observationmode.ObservationMode
   :show-inheritance:
   :members:
   :exclude-members: Sensitivity


``pysynphot.observation``
=========================

.. currentmodule:: pysynphot.observation

.. automodule:: pysynphot.observation

.. inheritance-diagram:: pysynphot.observation.Observation
   :parts: 1

.. autoclass:: pysynphot.observation.Observation
   :show-inheritance:
   :members:
   :exclude-members: redshift, binflux

.. autofunction:: pysynphot.observation.check_overlap
.. autofunction:: pysynphot.observation.validate_overlap


``pysynphot.planck``
====================

.. currentmodule:: pysynphot.planck

.. automodule:: pysynphot.planck
   :members:


``pysynphot.reddening``
=======================

.. currentmodule:: pysynphot.reddening

.. automodule:: pysynphot.reddening
   :members: print_red_laws, Extinction

.. inheritance-diagram:: pysynphot.reddening.RedLaw
   :parts: 1

.. autoclass:: pysynphot.reddening.CustomRedLaw
   :members:

.. autoclass:: pysynphot.reddening.RedLaw
   :show-inheritance:
   :members:


``pysynphot.refs``
==================

.. currentmodule:: pysynphot.refs

.. automodule:: pysynphot.refs
   :members: getref, showref, setref, set_default_waveset


``pysynphot.renorm``
====================

.. currentmodule:: pysynphot.renorm

.. automodule:: pysynphot.renorm
   :members:


.. _pysynphot-api-spark:

``pysynphot.spark``
===================

SPARK 0.6.1 is obtained from John Aycock (1998-2000).
It is the underlying engine used by :ref:`pysynphot-api-spparser`.


``pysynphot.spectrum``
======================

.. currentmodule:: pysynphot.spectrum

.. automodule:: pysynphot.spectrum

.. inheritance-diagram:: pysynphot.spectrum
   :parts: 1

.. autoclass:: pysynphot.spectrum.Integrator
   :members:

.. autoclass:: pysynphot.spectrum.SourceSpectrum
   :show-inheritance:
   :members:
   :exclude-members: setMagnitude, effstim

.. autoclass:: pysynphot.spectrum.TabularSourceSpectrum
   :show-inheritance:
   :members:
   :exclude-members: ToInternal

.. autoclass:: pysynphot.spectrum.ArraySourceSpectrum
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.FileSourceSpectrum
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.AnalyticSpectrum
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.GaussianSource
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.FlatSpectrum
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.Powerlaw
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.BlackBody
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.CompositeSourceSpectrum
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.SpectralElement
   :show-inheritance:
   :members:
   :exclude-members: fwhm, ToInternal

.. autoclass:: pysynphot.spectrum.TabularSpectralElement
   :show-inheritance:
   :members:
   :exclude-members: ToInternal, getHeaderKeywords

.. autoclass:: pysynphot.spectrum.ArraySpectralElement
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.FileSpectralElement
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.InterpolatedSpectralElement
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.UniformTransmission
   :show-inheritance:
   :members:
   :exclude-members: check_overlap

.. autoclass:: pysynphot.spectrum.Box
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.spectrum.ThermalSpectralElement
   :show-inheritance:
   :members:
   :exclude-members: getHeaderKeywords

.. autoclass:: pysynphot.spectrum.CompositeSpectralElement
   :show-inheritance:
   :members:
   :exclude-members: wave

.. autofunction:: pysynphot.spectrum.MergeWaveSets
.. autofunction:: pysynphot.spectrum.trimSpectrum


.. _pysynphot-api-spparser:

``pysynphot.spparser``
======================

This module implements the :ref:`pysynphot-language-parser`.
It uses :ref:`pysynphot-api-spark`.


``pysynphot.tables``
====================

.. currentmodule:: pysynphot.tables

.. automodule:: pysynphot.tables

.. autoclass:: pysynphot.tables.GraphTable
   :members:
   :exclude-members: GetNextNode

.. autoclass:: pysynphot.tables.CompTable
   :members:


``pysynphot.units``
===================

.. currentmodule:: pysynphot.units

.. automodule:: pysynphot.units
   :members: Units

.. inheritance-diagram:: pysynphot.units
   :parts: 1
   :private-bases:

.. autoclass:: pysynphot.units.BaseUnit
   :members:

.. autoclass:: pysynphot.units.WaveUnits
   :show-inheritance:
   :members:
   :exclude-members: ToAngstrom

.. autoclass:: pysynphot.units.Angstrom
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.Hz
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.InverseMicron
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units._MetricWavelength
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.Nm
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.Micron
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.Mm
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.Cm
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.Meter
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.FluxUnits
   :show-inheritance:
   :members:
   :exclude-members: ToPhotlam

.. autoclass:: pysynphot.units.Photlam
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.Flam
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.Photnu
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.Fnu
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.Jy
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.mJy
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.muJy
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.nJy
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.Counts
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.LogFluxUnits
   :show-inheritance:
   :members:

.. autoclass:: pysynphot.units.ABMag
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.STMag
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.OBMag
   :show-inheritance:
   :members:
   :exclude-members: unitResponse

.. autoclass:: pysynphot.units.VegaMag
   :show-inheritance:
   :members:
   :exclude-members: unitResponse


``pysynphot.wavetable``
=======================

.. currentmodule:: pysynphot.wavetable

.. automodule:: pysynphot.wavetable

.. autoclass:: pysynphot.wavetable.Wavetable
   :members:
