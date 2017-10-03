.. _pysynphot-appendixb:

****************************
Appendix B: OBSMODE Keywords
****************************

In this section, we describe the keywords available for
:ref:`pysynphot-obsmode-bandpass`. **pysynphot** supports
:ref:`science instruments currently installed on HST <pysynphot-appendixb-inflight>`
as of Servicing Mission 4 (SM4) performed in May 2009,
:ref:`legacy HST instruments <pysynphot-appendixb-legacy>`, and
:ref:`non-HST filter systems <pysynphot-appendixb-nonhst>`.
:ref:`Cross-instrument keywords <pysynphot-appendixb-special-keywords>` are
also listed.

In all the following tables, the |mjd_par| keyword is used to account for
time-dependent sensitivity, while the ADC (Analog-to-Digital Converter) gain
keyword is used to convert flux unit from electrons to data number (DN).
The keywords are also further explained in the
following sections. More instrument-specific details
can be obtained from their respective Instrument Handbooks.

The complete list of allowed component names that represent the
telescope (:ref:`pysynphot-ota`), Corrective Optics Space Telescope Axial
Replacement (:ref:`pysynphot-costar`), and science instruments is as tabulated
below:

+-----------+-----------------------------------------------------------------+
|Description|Keywords                                                         |
+===========+=================================================================+
|Telescope  |ota noota                                                        |
+-----------+-----------------------------------------------------------------+
|COSTAR     |costar nocostar                                                  |
+-----------+-----------------------------------------------------------------+
|Instrument |acs cos fgs foc fos hrs hsp nicmos pc stis wf wfc wfc3 wfpc wfpc2|
+-----------+-----------------------------------------------------------------+

As of September 1993, the default modes for the telescope and COSTAR components
are ``ota`` and ``nocostar``, respectively. Soon after COSTAR was installed in
the telescope, the default mode was changed to ``costar`` for original
instruments. Once the second-generation instruments were installed, with their
built-in optical corrections, the default mode for ``costar`` or ``nocostar``
became instrument-specific. Note that for the :ref:`pysynphot-appendixb-wfpc1`
instrument, the names ``wf``, ``wfc``, and ``wfpc`` are all equivalent and
correspond to the Wide Field Camera.

.. |acs_ramp| replace:: :ref:`Ramp filter <pysynphot_acs_parameterized_ramp>`
.. |aper_par| replace:: :ref:`EE radius <pysynphot-parameterized-aper>`
.. |cont_par| replace:: :ref:`Decontamination <pysynphot-parameterized-contamination>`
.. |mjd_par| replace:: :ref:`pysynphot-parameterized-mjd`
.. |nic_therm| replace:: :ref:`Thermal component <pysynphot-parameterized-temperature>`
.. |wfc3_bkg| replace:: :ref:`Background calculation <pysynphot-parameterized-temperature>`
.. |wfc3_qyc| replace:: :ref:`Quantum yield correction <pysynphot-wfc3-qyc>`
.. |wfpc2_lrf| replace:: :ref:`lrf# <pysynphot-wfpc2-ramp>`
.. |wfpc2_quad| replace:: :ref:`fquvn fquvn33 fqch4n fqch4n33 fqch4n15 fqch4p15 polq polq_par polq_perp polqn33 polqn18 polqp15 <pysynphot-wfpc2-quad>`


.. _pysynphot-appendixb-inflight:

In-Flight Instruments
=====================

This section contains science instruments that are currently installed on HST.


.. _pysynphot-appendixb-acs:

ACS
---

.. note:: HRC is currently not operational.

The ACS keywords consist of a list of detectors, filters,
:ref:`extraction apertures <pysynphot-parameterized-aper>`, and
|mjd_par| specifications. For example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w')

+---------------+-----------------------------------------------------------------+
|Description    |Keywords                                                         |
+===============+=================================================================+
|Detector       |hrc sbc wfc1 wfc2                                                |
+-----------+---+-----------------------------------------------------------------+
|Filter     |HRC|f220w f250w f330w f344n f435w f475w f502n f550m f555w f606w f625w|
|           |   |f658n f660n f775w f814w f850lp f892n pol_uv pol_v                |
|           +---+-----------------------------------------------------------------+
|           |WFC|f435w f475w f502n f550m f555w f606w f625w f658n f660n f775w f814w|
|           |   |f850lp f892n pol_uv pol_v                                        |
|           +---+-----------------------------------------------------------------+
|           |SBC|f115lp f125lp f140lp f150lp f165lp f122m                         |
+-----------+---+-----------------------------------------------------------------+
||acs_ramp| |HRC|fr388n fr459m fr505n fr656n fr914m                               |
|           +---+-----------------------------------------------------------------+
|           |WFC|fr1016n fr388n fr423n fr459m fr462n fr505n fr551n fr601n fr647m  |
|           |   |fr656n fr716n fr782n fr853n fr914m fr931n                        |
+-----------+---+-----------------------------------------------------------------+
|Disperser  |HRC|g800l pr200l                                                     |
|           +---+-----------------------------------------------------------------+
|           |WFC|g800l                                                            |
|           +---+-----------------------------------------------------------------+
|           |SBC|pr110l pr130l                                                    |
+-----------+---+-----------------------------------------------------------------+
||aper_par|     |aper#0.0 aper#0.1 aper#0.2 aper#0.3 aper#0.4 aper#0.5 aper#0.6   |
|               |aper#0.8 aper#1.0 aper#1.5 aper#2.0 aper#4.0                     |
+---------------+-----------------------------------------------------------------+
||mjd_par|      |mjd#                                                             |
+---------------+-----------------------------------------------------------------+
|Coronographic  |coron                                                            |
|(HRC only)     |                                                                 |
+---------------+-----------------------------------------------------------------+


.. _pysynphot_acs_parameterized_ramp:

Ramp Filter
^^^^^^^^^^^

The WFC detector has 15 ramp filters available for use, while the HRC has 6.
To use a ramp filter in simulations, use the keyword syntax
``filtername#cenwave``, where ``filtername`` is the name of the ramp filter
and ``cenwave`` the desired central wavelength in Angstroms.
Also see :ref:`pysynphot-parameterized` for more information. For example:

>>> bp = S.ObsBandpass('acs,wfc1,fr388n#3880')


.. _pysynphot-appendixb-cos:

COS
---

The COS keywords consist of a list of detectors, apertures,
mirrors, gratings, central wavelengths, and |mjd_par| specifications.

FUV spectral simulations are performed by specifying one of the FUV gratings
along with a central wavelength. NUV spectral simulations are
performed by specifying one of the NUV gratings along with a
central wavelength. In both cases, only first-order light is
included in the calculation, and the resulting spectrum will
include all three stripes on the detector.

Imaging simulations are performed by specifying one of the mirrors
(``mirrorb`` for bright objects) with the NUV detector.

Either the Primary Science Aperture (``psa``) or the Bright Object
Aperture (``boa``) may be specified with any simulation; the Primary
Science Aperture will be included by default if neither is specified.

For example:

>>> bp = S.ObsBandpass('cos,nuv,g185m,c1786')

+----------------+------------------------------------+
|Description     |Keywords                            |
+================+====================================+
|Detector        |fuv nuv                             |
+----------------+------------------------------------+
|Aperture        |boa psa                             |
+----------------+------------------------------------+
|Mirror          |mirrora mirrorb                     |
+----------+-----+------------------------------------+
|Grating   |FUV  |g130m g140l g160m                   |
|          +-----+------------------------------------+
|          |NUV  |g185m g225m g230l g285m             |
+----------+-----+------------------------------------+
|Central   |g130m|c1291 c1300 c1309 c1318 c1327       |
|wavelength+-----+------------------------------------+
|          |g140l|c1105 c1230                         |
|          +-----+------------------------------------+
|          |g160m|c1577 c1589 c1600 c1611 c1623       |
|          +-----+------------------------------------+
|          |g185m|c1786 c1817 c1835 c1850 c1864 c1882 |
|          |     |c1890 c1900 c1913 c1921 c1941 c1953 |
|          |     |c1971 c1986 c2010                   |
|          +-----+------------------------------------+
|          |g225m|c2186 c2217 c2233 c2250 c2268 c2283 |
|          |     |c2306 c2325 c2339 c2357 c2373 c2390 |
|          |     |c2410                               |
|          +-----+------------------------------------+
|          |g230l|c2635 c2950 c3000 c3360             |
|          +-----+------------------------------------+
|          |g285m|c2617 c2637 c2657 c2676 c2695 c2709 |
|          |     |c2719 c2739 c2850 c2952 c2979 c2996 |
|          |     |c3018 c3035 c3057 c3074 c3094       |
+----------+-----+------------------------------------+
||mjd_par|       |mjd#                                |
+----------+-----+------------------------------------+


.. _pysynphot-appendixb-fgs:

FGS
---

The FGS instrument keywords consist of a list of filters plus a coordinate axis.
Some of the filter names are aliases for other filters. For instance,
``astroclear`` is an alias for F605W, ``clear`` for F583W, ``red`` for
F650W, and ``yellow`` for 550W. For example:

>>> bp = S.ObsBandpass('fgs,f583w,y')

+-----------+-----------------------------------------------------------+
|Description|Keywords                                                   |
+===========+===========================================================+
|Filter     |f550w (yellow) f583w (clear) f605w (astroclear) f650w (red)|
|           |nd5 pupil                                                  |
+-----------+-----------------------------------------------------------+
|Axis       |x y                                                        |
+-----------+-----------------------------------------------------------+


.. _pysynphot-appendixb-nicmos:

NICMOS
------

.. note:: NICMOS is currently not operational.

The NICMOS keywords consist of a list of filters, grisms, polarizers, and
detectors.

Both the filter name and camera number are required in the observation mode.
The detector keyword ``tacq`` is another way to specify Detector 2.
For thermal calculations, all component keywords, except the detector, may be
:ref:`parameterized for temperature <pysynphot-parameterized-temperature>`.

For example:

>>> bp = S.ObsBandpass('nicmos,1,f090m,dn,primary#270')

+-----------------+-----------------------------------------------------------------+
|Description      |Keywords                                                         |
+=================+=================================================================+
|Detector         |1 2 3 tacq                                                       |
+------+----------+-----------------------------------------------------------------+
|Filter|Detector 1|blank f090m f095n f097n f108n f110m f110w f113n f140w f145m f160w|
|      |          |f164n f165m f166n f170m f187n f190n pol0s pol120s pol240s        |
|      +----------+-----------------------------------------------------------------+
|      |Detector 2|blank f100w f160w f165m f171m f180m f187n f187w f190n f204m f205w|
|      +----------+f207m f212n f215n f216n f222m f237m pol0l pol120l pol240l        |
|      |tacq      |                                                                 |
|      +----------+-----------------------------------------------------------------+
|      |Detector 3|blank f108n f110w f113n f150w f160w f164n f166n f175w f187n f190n|
|      |          |f196n f200n f212n f215n f222m f240m g096 g141 g206               |
+------+----------+-----------------------------------------------------------------+
|ADC gain         |dn                                                               |
+-----------------+-----------------------------------------------------------------+
||nic_therm|      |spider primary pads hole sec edge bend1 reimag pupil image para1 |
|                 |para2 bend dewar cmask dqe                                       |
+-----------------+-----------------------------------------------------------------+


.. _pysynphot-appendixb-stis:

STIS
----

The STIS keywords consist of filters, apertures, gratings, central wavelengths,
and ADC gains.

In the STIS instrument, imaging mirrors and gratings are contained in the
Mode Select Mechanism (MSM) while filters and slits are in the aperture wheel.
Each grating or imaging mirror can be used with only one of the 3 STIS
detectors (CCD, NUVMAMA, or FUVMAMA); Therefore, specifying the grating
automatically determines the detector.

Each central wavelength is intended for use with a particular grating.
See the STIS Instrument Handbook for a listing of which central wavelengths are
allowed with each grating. The low order gratings (G140L, G230L, G230LB, G430L,
and G750L) have only one allowed setting; Thus, central wavelength should not be
specified for those. If no central wavelength is specified,
results will be calculated for the entire bandpass of the grating.

In principle, any filter or slit (aperture) could be used with any grating or
mirror, although in practice, certain combinations are restricted or forbidden.
Since the slits and filters are in the same wheel, it is not possible to use
both a slit and a filter at the same time. Some small slits also contain
built-in neutral density filters.
In addition to the aperture names listed, those used for HST Phase 2 proposals
are also acceptable. For example, the ``52X0.05`` is equivalent to ``s52x005``
listed in the table below.
If no aperture or filter is specified, the calculation is done for the "clear"
aperture.

The |mjd_par| keyword only applies to FUV and NUV MAMAs.
The ADC gain keyword only applies to CCD; It is used to convert results from
units of electrons to DN.

These ``obsmode`` strings are all equivalent, with 50CCD being the unobstructed
full-field aperture for the CCD detector:

>>> bp = S.ObsBandpass('stis,g430l')
>>> bp = S.ObsBandpass('stis,ccd,g430l')
>>> bp = S.ObsBandpass('stis,ccd,g430l,50ccd')

This assumes that an imaging mirror is being used because the detector name is
specified without a grating:

>>> bp = S.ObsBandpass('stis,ccd,f28x50lp')

This will calculate results for the entire bandpass of the instrument because
no central wavelength is specified:

>>> bp = S.ObsBandpass('stis,ccd,g430m,52X0.2')

This will only calculate results for the wavelength range covered by the
specified wavelength setting:

>>> bp = S.ObsBandpass('stis,ccd,g430m,52X0.2,c4451')

+-----------+---------------------------------------------------------------------+
|Description|Keywords                                                             |
+===========+=====================================================================+
|Filter     |25mama 50ccd 50coron f25ciii f25cn182 f25cn270 f25lya f25mgii f25nd3 |
|           |f25nd5 f25ndq1 f25ndq2 f25ndq3 f25ndq4 f25qtz f25srf2 f28x50lp       |
|           |f28x50oii f28x50oiii                                                 |
+-----------+---------------------------------------------------------------------+
|Aperture   |s005x29 s005x31nda s005x31ndb s009x29 s01x003 s01x006 s01x009 s01x02 |
|           |s02x005nd s02x006 s02x006fpa s02x006fpb s02x006fpc s02x006fpd        |
|           |s02x006fpe s02x009 s02x02 s02x02fpa s02x02fpb s02x02fpc s02x02fpd    |
|           |s02x02fpe s02x05 s02x29 s03x005nd s03x006 s03x009 s03x02 s05x05      |
|           |s10x006 s10x02 s2x2 s31x005nda s31x005ndb s31x005ndc s36x005n45      |
|           |s36x005p45 s36x06n45 s36x06p45 s52x005 s52x01 s52x02 s52x05 s52x2    |
|           |s6x006 s6x02 s6x05 s6x6                                              |
+-----------+---------------------------------------------------------------------+
|Grating    |e140h e140hb e140m e140mb e230h e230m g140l g140lb g140m g140mb g230l|
|           |g230lb g230m g230mb g430l g430m g750l g750m prism x140 x140m x230    |
|           |x230h                                                                |
+-----------+---------------------------------------------------------------------+
|Mirror     |acq ccd fuvmama nuvmama                                              |
+-----------+---------------------------------------------------------------------+
|Central    |all c1687 c1769 c1851 c1933 c2014 c2095 c2176 c2257 c2338 c2419 c2499|
|wavelength |c2579 c2659 c2739 c2818 c2898 c2977 c3055 c3134 i1884 i2600 i2800    |
|           |i2828 c1713 c1854 c1995 c2135 c2276 c2416 c2557 c2697 c2836 c2976    |
|           |c3115 i2794 c1978 c2707 i2124 i2269 i2415 i2561 c1763 c2013 c2263    |
|           |c2513 c2762 c3012 i1813 i1863 i1913 i1963 i2063 i2113 i2163 i2213    |
|           |i2313 i2363 i2413 i2463 i2563 i2613 i2663 i2713 i2812 i2862 i2912    |
|           |i2962 c3165 c3423 c3680 c3936 c4194 c4451 c4706 c4961 c5216 c5471    |
|           |i3305 i3843 i4781 i5093 c1173 c1222 c1272 c1321 c1371 c1420 c1470    |
|           |c1518 c1567 c1616 c1665 c1714 i1218 i1387 i1400 i1540 i1550 i1640    |
|           |c1425 c1234 c1416 c1598 i1271 i1307 i1343 i1380 i1453 i1489 i1526    |
|           |i1562 c7751 c8975 c10363 c10871 c5734 c6252 c6768 c7283 c7795        |
|           |c8311 c8825 c9336 c9851 i6094 i6581 i8561 i9286 i9806                |
+-----------+---------------------------------------------------------------------+
|ADC gain   |a2d1 a2d2 a2d3 a2d4                                                  |
+-----------+---------------------------------------------------------------------+
||mjd_par|  |mjd#                                                                 |
+-----------+---------------------------------------------------------------------+


.. _pysynphot-appendixb-wfc3:

WFC3
----

The WFC3 keywords consist of a list of detectors, filters, |mjd_par|, and
:ref:`extraction apertures <pysynphot-parameterized-aper>`
for each of its 2 channels (UVIS and IR), in addition to other special keyword,
as tabulated below. For example:

>>> bp = S.ObsBandpass('wfc3,uvis1,f218w')

+------------------------+-------------------------------------------------+
|Description             |Keywords                                         |
+========================+=================================================+
|Detector                |uvis1 uvis2 ir                                   |
+--------+---------------+-------------------------------------------------+
|Filter  |UVIS           |f200lp f218w f225w f275w f280n f300x f336w f343n |
|        |               |f350lp f373n f390m f390w f395n f410m f438w f467m |
|        |               |f469n f475w f475x f487n f502n f547m f555w f600lp |
|        |               |f606w f621m f625w f631n f645n f656n f657n f658n  |
|        |               |f665n f673n f680n f689m f763m f775w f814w f845m  |
|        |               |f850lp f953n fq232n fq243n fq378n fq387n fq422m  |
|        |               |fq436n fq437n fq492n fq508n fq575n fq619n fq634n |
|        |               |fq672n fq674n fq727n fq750n fq889n fq906n fq924n |
|        |               |fq937n                                           |
|        +---------------+-------------------------------------------------+
|        |IR             |f098m f105w f110w f125w f126n f127m f128n f130n  |
|        |               |f132n f139m f140w f153m f160w f164n f167n        |
+--------+---------------+-------------------------------------------------+
|Grism   |UVIS           |g280                                             |
|        +---------------+-------------------------------------------------+
|        |IR             |g102 g141                                        |
+--------+---------------+-------------------------------------------------+
|ADC gain                |dn                                               |
+------------------------+-------------------------------------------------+
||wfc3_qyc|              |qyc                                              |
+------------------------+-------------------------------------------------+
||wfc3_bkg|              |bkg                                              |
+------------------------+-------------------------------------------------+
||aper_par|              |aper#0.00 aper#0.10 aper#0.15 aper#0.20          |
|                        |aper#0.25a aper#0.30 aper#0.40 aper#0.50         |
|                        |aper#0.60 aper#0.80 aper#1.00 aper#1.50 aper#2.00|
+------------------------+-------------------------------------------------+
||mjd_par|               |mjd#                                             |
+------------------------+-------------------------------------------------+


.. _pysynphot-wfc3-qyc:

Quantum Yield Correction
^^^^^^^^^^^^^^^^^^^^^^^^

The ``qyc`` keyword is used to apply a wavelength-dependent
quantum yield correction.
At short wavelengths, the UVIS detector has a finite chance of
producing two elections for one incoming photon. By default,
**pysynphot** reports the count rate in electrons if the
``dn`` keyword is not specified, or data numbers otherwise.

However, the appropriate count rate for SNR calculations should be in
electrons with a correction for this quantum yield effect; That is,
users should specify the ``qyc`` keyword but not ``dn``. For example:

>>> bp = S.ObsBandpass('wfc3,uvis1,f218w,qyc')


.. _pysynphot-appendixb-legacy:

Legacy Instruments
==================

The instruments which had previously flown on HST but had been
replaced by more modern detectors are included here for completeness.


.. _pysynphot-appendixb-foc:

FOC
---

The FOC keywords consist of a list of detectors, filters, and
miscellaneous keywords. The ``f/48`` detector has 2 filter wheels and the
``f/96`` detector has 4. Some of the filters have aliases. For instance,
``fuvop`` is an alias for ``prism1``, ``nuvop`` for ``prism2``,
``fopcd`` for ``prism3``, ``g450m`` for F305LP,
``g225m`` for F220W, and ``g150m`` for F140W.
The miscellaneous keywords include the :ref:`pysynphot-costar` and
the occulting fingers. For example:

>>> bp = S.ObsBandpass('foc,costar,f/96,f410m')

+--------------+--------------------------------------------------+
|Description   |Keywords                                          |
+==============+==================================================+
|Detector      |f/48 f/96 f/288 spec                              |
+------+-------+--------------------------------------------------+
|f/48  |Wheel 1|f140w (g130m) f150w (g150m) f175w f195w f220w     |
|      |       |(g225m) f305lp (g450m) prism3 (fopcd) (grat-prism)|
|      +-------+--------------------------------------------------+
|      |Wheel 2|f130lp f180lp f275w f342w f430w prism1 (fuvop)    |
|      |       |prism2 (nuvop)                                    |
+------+-------+--------------------------------------------------+
|f/96  |Wheel 1|f600m f630m f2nd f4nd f6nd f8nd pol0 pol0_par     |
|      |       |pol0_per pol0_unp pol60 pol60_par pol60_per       |
|      |       |pol60_unp pol120 pol120_par pol120_per pol120_unp |
|      |       |prism1 (fuvop) prism2 (nuvop)                     |
|      +-------+--------------------------------------------------+
|      |Wheel 2|f140w f175w f220w f275w f320w f342w f370lp f430w  |
|      |       |f480lp f486n f501n                                |
|      +-------+--------------------------------------------------+
|      |Wheel 3|f120m f130m f140m f152m f165w f170m f190m f195w   |
|      |       |f210m f231m f1nd                                  |
|      +-------+--------------------------------------------------+
|      |Wheel 4|f130lp f253m f278m f307m f346m f372m f410m f437m  |
|      |       |f470m f502m f550m                                 |
+------+-------+--------------------------------------------------+
|Image |f/48   |x48n256 x48n256d x48n512 x48nlrg x48zlrg x48zrec  |
|Format+-------+--------------------------------------------------+
|      |f/96   |x96n128 x96n256 x96n512 x96nlrg x96z512 x96zlrg   |
+------+-------+--------------------------------------------------+
|Spectral Order|order1 order2 order3 order4                       |
+--------------+--------------------------------------------------+
|Occulting     |occ0p23 occ0p4 occ0p8                             |
|FIngers       |                                                  |
+--------------+--------------------------------------------------+
|Detector      |x48n256 x48n256d x48n512 x48nlrg x48zlrg x48zrec  |
|Format        |x96n128 x96n256 x96n512 x96z512 x96nlrg x96zlrg   |
+--------------+--------------------------------------------------+

Note that the spectroscopic capabilities, and hence the related
keywords ``spec``, ``order1``, ``order2``, ``order3``, and ``order4``,
are only available for the ``f/48`` camera. Furthermore, the ``occ0p23``
keyword is only available with the ``f/48`` camera, and the ``occ0p4`` and
``occ0p8`` keywords are only available with the ``f/96`` camera.

The ``x48*`` and ``x96*`` keywords are used to account for the known dependency
of DQE on the detector format (see the FOC Instrument Handbook for
more details). These keywords invoke throughput tables that contain
the (wavelength-independent) relative sensitivities for each format,
where the 512x512 format (``x48n512`` and ``x96n512``) is set to 1.0.
The associations between formats and keywords are listed below.

+------+-------+-------------+
|Camera|Keyword|Camera Format|
+======+=======+=============+
|f/96  |x96n128|128 x 128    |
|      +-------+-------------+
|      |x96n256|256 x 256    |
|      +-------+-------------+
|      |x96n512|512 x 512    |
|      +-------+-------------+
|      |x96z512|512z x 512   |
|      +-------+-------------+
|      |x96zlrg|512z x 1024  |
+------+-------+-------------+
|f/48  |x48n256|256 x 256    |
|      +-------+-------------+
|      |x48n512|512 x 512    |
|      +-------+-------------+
|      |x48zrec|256z x 1024  |
|      +-------+-------------+
|      |x48nlrg|512 x 1024   |
|      +-------+-------------+
|      |x48zlrg|512z x 1024  |
+------+-------+-------------+


.. _pysynphot-appendixb-fos:

FOS
---

The FOS keywords consist of a list of detectors, apertures, gratings, and
polarimeter waveplates and waveplate position angles.
:ref:`pysynphot-costar` keyword is also accepted. For example:

>>> bp = S.ObsBandpass('fos,costar,blue,g160l')

The waveplate keywords indicate whether Waveplate A or  B is being used and
the angle of the waveplate. The waveplate keyword syntax is ``POLpa-wp``,
where ``pa`` is the position angle in degrees, and ``wp`` is the A or B
waveplate:

>>> bp = S.ObsBandpass('fos,blue,g130h,pol135-a')

The ``upper`` and ``lower`` aperture keywords are only recognized when used
in conjunction with one of the paired apertures:

>>> bp = S.ObsBandpass('fos,blue,g130h,upper,1.0-pair')

The ``order0`` keyword is only available in conjunction with the ``g160l``
grating and the ``blue`` detector:

>>> bp = S.ObsBandpass('fos,blue,g160l,order0')

+-----------+--------------------------------------------------+
|Description|Keywords                                          |
+===========+==================================================+
|Detector   |blue red                                          |
+-----------+--------------------------------------------------+
|Aperture   |0.3 0.5 1.0 4.3 0.1-pair 0.25-pair 0.5-pair       |
|           |1.0-pair upper lower 0.25x2.0 0.7x2.0-bar 2.0-bar |
|           |blank failsafe                                    |
+-----------+--------------------------------------------------+
|Grating    |g130h g190h g270h g400h g570h g780h g160l g650l   |
|           |mirror prism order0                               |
+-----------+--------------------------------------------------+
|Waveplate  |pol0-a pol0-b pol22.5-a pol22.5-b pol45-a pol45-b |
|           |pol67.5-a pol67.5-b pol90-a pol90-b pol112.5-a    |
|           |pol112.5-b pol135-a pol135-b pol157.5-a pol157.5-b|
|           |pol180-a pol180-b pol202.5-a pol202.5-b pol235-a  |
|           |pol235-b pol257.5-a pol257.5-b pol270-a pol270-b  |
|           |pol292.5-a pol292.5-b pol315-a pol315-b pol337.5-a|
|           |pol337.5-b                                        |
+-----------+--------------------------------------------------+


.. _pysynphot-appendixb-ghrs:

GHRS
----

The GHRS keywords consist of a list of detectors, apertures, gratings
or mirrors, and Echelle mode orders. :ref:`pysynphot-costar` keyword
is also accepted. For example:

>>> bp = S.ObsBandpass('hrs,costar,lsa,g160m')

The Echelle mode orders are used with the keywords ``echa`` and ``echb``.
Orders 18 to 33 are valid with Echelle mode B, while orders 33 to 53 with
mode A. For example:

>>> bp = S.ObsBandpass('hrs,costar,lsa,echa,33')

+-----------+--------------------------------------------------+
|Description|Keywords                                          |
+===========+==================================================+
|Aperture   |lsa ssa                                           |
+-----------+--------------------------------------------------+
|Grating    |echa echb g140l g140m g160m g200m g270m           |
+-----------+--------------------------------------------------+
|Mirror     |a1 a2 n1 n2                                       |
+-----------+--------------------------------------------------+
|Echelle    |18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34|
|Order      |35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51|
|           |52 53 all                                         |
+-----------+--------------------------------------------------+


.. _pysynphot-appendixb-hsp:

HSP
---

The HSP keywords consist of a list of detectors, filters,
apertures, and beams. The beams refer to the two beams that
come out of the beam splitter. Not all apertures can be used
with all detectors; Refer to the HSP Instrument Handbook for
further information. The polarization detector also has angle
and type keywords. For example:

>>> bp = S.ObsBandpass('hsp,uv1,f220w,c')

+------------------+-------------------------------------------------+
|Description       |Keywords                                         |
+==================+=================================================+
|Detector          |pmt pol uv1 uv2 vis                              |
+------------------+-------------------------------------------------+
|Relay mirror      |norelay relay                                    |
+------------------+-------------------------------------------------+
|Aperture          |a b c d e f h j s t                              |
+------------------+-------------------------------------------------+
|Beam              |blue red                                         |
+------------+-----+-------------------------------------------------+
|Filter      |POL  |f160lp f216m f237m f277m f327m                   |
|            +-----+-------------------------------------------------+
|            |UV1  |f122m f135w f140lp f145m f152m f184w f218m f220w |
|            |     |f240w f248m f278n prism                          |
|            +-----+-------------------------------------------------+
|            |UV2  |f122m f140lp f145m f152m f160lp f179m f184w f218m|
|            |     |f248m f262m f278n f284m prism                    |
|            +-----+-------------------------------------------------+
|            |VIS  |f160lp f184w f240w f262m f355m f400lp f419n f450w|
|            |     |f551w f620w prism                                |
+------------+-----+-------------------------------------------------+
|Polarization|Angle|0 45 90 135                                      |
|            +-----+-------------------------------------------------+
|            |Type |ext ord par per                                  |
+------------+-----+-------------------------------------------------+


.. _pysynphot-appendixb-wfpc1:

WF/PC-1
-------

The WF/PC-1 keywords consist of a list of filters, detectors,
and miscellaneous keywords.
The ``cal`` keyword accounts for the flat-field correction.
The ``cont#`` keyword accounts for changes in sensitivity between
:ref:`decontamination <pysynphot-parameterized-contamination>` events.

WF/PC-1 has 12 independently positionable filter wheels,
each of which has 5 positions, including a "clear" position.
Detectors 1-4 correspond to the Wide Field Camera; They are only valid
when used in conjunction with the ``wf``, ``wfc``, or ``wfpc`` keywords.
Meanwhile, Detectors 5-8 correspond to the Planetary Camera;
They are only valid when used with the ``pc`` keyword.
If a detector number is not specified, the default detector for ``wf`` is 2,
and ``pc`` is 6.

For example:

>>> bp = S.ObsBandpass('wfpc,4,f194w,dn')

+---------------+-------------------------------+
|Decription     |Keywords                       |
+===============+===============================+
|Instrument     |wfpc wfc wf (all equivalent) pc|
+---------------+-------------------------------+
|Detector       |1 2 3 4 5 6 7 8                |
+--------+------+-------------------------------+
|Filter  |  1   |f673n f8nd g450 g800           |
|Wheel   +------+-------------------------------+
|        |  2   |f122m f336w f439w g200 g200m2  |
|        +------+-------------------------------+
|        |  3   |pol0 pol60 pol120 f1083n       |
|        +------+-------------------------------+
|        |  4   |f157w f194w f230w f284w        |
|        +------+-------------------------------+
|        |  5   |f569w f658n f675w f791w        |
|        +------+-------------------------------+
|        |  6   |f631n f656n f664n f702w        |
|        +------+-------------------------------+
|        |  7   |f375n f437n f502n f588n        |
|        +------+-------------------------------+
|        |  8   |f368m f413m f492m f622w        |
|        +------+-------------------------------+
|        |  9   |f547m f555w f648m f718m        |
|        +------+-------------------------------+
|        | 10   |f785lp f814w f875m f1042m      |
|        +------+-------------------------------+
|        | 11   |f128lp f469n f487n f517n       |
|        +------+-------------------------------+
|        | 12   |f606w f725lp f850lp f889n      |
+--------+------+-------------------------------+
|ADC gain       |dn                             |
+---------------+-------------------------------+
|Baum spot      |baum                           |
+---------------+-------------------------------+
||cont_par|     |cont#                          |
+---------------+-------------------------------+
|Flat-field     |cal                            |
+---------------+-------------------------------+


.. _pysynphot-appendixb-wfpc2:

WFPC2
-----

The WFPC2 keywords consist of a list of detectors, filters, ADC gain, and
miscellaneous keywords. The ``cal`` keyword accounts for the flat-field
response. Meanwhile, the ``cont#`` keyword accounts for changes in throughput
between :ref:`decontamination <pysynphot-parameterized-contamination>` events;
Due to the removal of WFPC2 during SM4, this time-dependent effect is only
valid for dates prior to SM4.

WFPC2 has 12 filter wheels, each of which has 5 positions, including the "clear"
position. Wheel 11 contains :ref:`quad filters <pysynphot-wfpc2-quad>`, while
Wheel 12 contains :ref:`linear ramp filters <pysynphot-wfpc2-ramp>`.
Detector 1 is the Planetary Camera. Meanwhile, Detectors 2-4 correspond to the
Wide Field Camera. If a detector is not specified, the default is Detector 4.

For example:

>>> bp = S.ObsBandpass('wfpc2,2,f450w,a2d7,cont#50180')

+---------------+------------------------------------------------------+
|Description    |Keywords                                              |
+===============+======================================================+
|Detector       |1 2 3 4                                               |
+----------+----+------------------------------------------------------+
|Filter    |  1 |f122m f157w f160bw f953n                              |
|Wheel     +----+------------------------------------------------------+
|          |  2 |f130lp f165lp f785lp f850lp                           |
|          +----+------------------------------------------------------+
|          |  3 |f336w f410m f467m f547m                               |
|          +----+------------------------------------------------------+
|          |  4 |f439w f569w f675w f791w                               |
|          +----+------------------------------------------------------+
|          |  5 |f343n f375n f390n f437n                               |
|          +----+------------------------------------------------------+
|          |  6 |f469n f487n f502n f588n                               |
|          +----+------------------------------------------------------+
|          |  7 |f631n f656n f658n f673n                               |
|          +----+------------------------------------------------------+
|          |  8 |f170w f185w f218w f255w                               |
|          +----+------------------------------------------------------+
|          |  9 |f300w f380w f555w f622w                               |
|          +----+------------------------------------------------------+
|          | 10 |f450w f606w f702w f814w                               |
|          +----+------------------------------------------------------+
|          | 11 |f1042m |wfpc2_quad|                                   |
|          +----+------------------------------------------------------+
|          | 12 ||wfpc2_lrf|                                           |
+----------+----+------------------------------------------------------+
|ADC gain       |a2d7 a2d15                                            |
+---------------+------------------------------------------------------+
||cont_par|     |cont#                                                 |
+---------------+------------------------------------------------------+
|Flat-field     |cal                                                   |
+---------------+------------------------------------------------------+


.. _pysynphot-wfpc2-quad:

Quad Filter
^^^^^^^^^^^

Filter Wheel 11 contains 3 specialized quadrant (quad) filters.
Each quadrant corresponds to a facet of the pyramid, and therefore to a
distinct camera relay:

* FQUVN contains 4 narrow-band, redshifted [O II] filters
* FQCH4N contains 4 methane (CH4) band filters
* POLQ contains 4 polarizing elements

For FQUVN and FQCH4N filters, the :ref:`graph table <pysynphot-graph>` is
constructed such that distinct throughput values are automatically selected
for a given quadrant based on the selected detector. For POLQ filter, it can
also be specified by the direction its polarization; i.e., ``polq_perp`` for
perpendicular polarization, and ``polq_par`` for parallel.

The quad filters were designed to map onto a 4-faceted WFC configuration.
However, in the final design of the instrument, with WF Quadrant 1 replaced
by the PC, it is necessary to rotate the quad filters as follow
(see the WFPC2 Instrument Handbook for more details):

* ``fquvn33``, ``fqch4n33``, and ``polqn33`` represent the respective filters
  rotated by :math:`-33^{\circ}` in order to bring Filter Quadrant 1 into the
  WF2 and WF3 relays
* ``fqch4p15`` and ``fqch4n15`` represent FQCH4N partially rotated by
  :math:`\pm15^{\circ}` in order to bring 2 of its quadrants into the PC relay
* ``polqp15`` and ``polqn18`` represent POLQ partially rotated by
  :math:`+15^{\circ}` and :math:`-18^{\circ}`, respectively, in order to allow
  observations with different polarization angles

The nominal positions are represented as ``fquvn``, ``fqch4n``, and ``polq``
keywords. For example:

>>> bp = S.ObsBandpass('wfpc2,2,fqch4n')


.. _pysynphot-wfpc2-ramp:

Ramp Filter
^^^^^^^^^^^

.. warning::

    This is currently unsupported by **pysynphot** (see
    `Ticket 218 <https://aeon.stsci.edu/ssb/trac/astrolib/ticket/218>`_).
    However, flux calibration for these ramp filters can still be done using
    ``PHOT*`` keywords from image headers.

Filter Wheel 12 contains 4 linearly variable narrow-band ramp filters,
which together cover a total wavelength range of 3700 to 9800 Angstroms.
The FWHM of the throughput at a given wavelength is typically about 1% of
the central wavelength. To use a WFPC2 ramp filter in simulations, use the
keyword syntax ``lrf#cenwave``, where ``cenwave`` is the desired central
wavelength in Angstroms.

The example below is given in IRAF STSDAS SYNPHOT command::

  synphot> bandpar wfpc2,3,lrf#4861


.. _pysynphot-appendixb-special-keywords:

Special Keywords
================

This section contains special keywords that apply to multiple instruments.


.. _pysynphot-ota:

OTA
---

The HST OTA transmissivity is included by default in the calculation of
all HST-related observation modes. It can be included or excluded explicitly by
adding the keywords ``ota`` or ``noota``, respectively; For example:

>>> bp = S.ObsBandpass('stis,ccd,f25srf2,noota')


.. _pysynphot-costar:

COSTAR
------

An observation mode that involves a first-generation instrument
(:ref:`pysynphot-appendixb-foc`, :ref:`pysynphot-appendixb-fos`, or
:ref:`pysynphot-appendixb-ghrs`) also automatically accounts for the effects of
COSTAR on its wavelength-dependent sensitivity. This includes the product of the
reflectivity curves for each pair of the COSTAR mirrors for each of these
instruments, as well as the effects on instrument throughput and
sensitivity due to the improved point-spread function that is achieved
with COSTAR.

Like the :ref:`pysynphot-ota`, the COSTAR effects on passbands and
count rates are included by default for these instruments when using versions
of the HST graph table created on or after February 24, 1995. In earlier
versions of the graph table, ``nocostar`` is the default. To explicitly include
or exclude COSTAR, use the keywords ``costar`` and ``nocostar``, respectively,
anywhere within your observation mode string; For example:

>>> bp = S.ObsBandpass('fos,red,4.3,g270h,costar')

All current HST instruments (except :ref:`pysynphot-appendixb-fgs`) have
built-in corrective optics to compensate for the spherical aberration of the
primary mirror. It is not necessary to explicitly exclude COSTAR for the current
generation instruments, as it is excluded by default. Inclusion of COSTAR for
these instruments are not allowed.


.. _pysynphot-parameterized-mjd:

MJD
---

In the case of :ref:`pysynphot-appendixb-acs`, :ref:`pysynphot-appendixb-cos`,
:ref:`pysynphot-appendixb-stis`, and :ref:`pysynphot-appendixb-wfc3`,
the ``mjd`` keyword is used to handle time-dependent sensitivity of certain
detectors. To use this capability in simulations, include ``mjd#ddddd`` in the
``obsmode`` string, where ``ddddd`` is the desired Modified Julian Date (MJD)
value, which could be an integer or a floating point.

**pysynphot** interpolates between the dates for which data exist in the table
to arrive at an estimate of the throughput on the requested date
(see :ref:`pysynphot-parameterized`). For example:

>>> bp = S.ObsBandpass('acs,wfc1,f555w,mjd#49486')

If not specified, the default is to use
the latest set of throughput values in the ``THROUGHPUT`` column without any
interpolation or extrapolation.
This default column is expected to be updated by the relevant instrument team
whenever significant changes to the current trend are identified, such that the
throughput should not differ by more than 2% from the one obtained by using the
current date.


.. _pysynphot-parameterized-aper:

Encircled Energy
----------------

For :ref:`pysynphot-appendixb-acs` and :ref:`pysynphot-appendixb-wfc3`,
the ``aper`` keyword is used to specify a circular aperture, given by its
radius in arcseconds, to calculate the source counts within.
If no aperture is given, calculations are done for an infinite aperture, which
is also 5.5 arcsec or larger for ACS, and 2 arcsec or larger for WFC3.

This enables **pysynphot** to be more flexible and accurate, particularly for
cases where red targets are observed at long wavelengths.
At wavelengths greater than 7500 Angstroms (for ACS/HRC) and about
9000 Angstroms (for ACS/WFC), the observations are affected by a
red halo due to light scattered off the CCD substrate. An increasing
fraction of the light as a function of wavelength is scattered
from the center of the PSF into the wings. This problem affects
particularly the very broad *z*-band F850LP filter, for which the
encircled energy (EE) depends on the underlying spectral energy
distribution the most.

Supported apertures are instrument-dependent, as listed below.
Arbitrary aperture sizes are permitted, but not recommended.
This is because **pysynphot** only provides a linear interpolation between
supported apertures (see :ref:`pysynphot-parameterized`), which is a poor
approximation, especially at small apertures.

For ACS, the following apertures are supported:

* every 0.1 arcsec between 0 and 0.6 arcsec
* 0.8 arcsec
* 1.0 arcsec
* 1.5 arcsec
* 2.0 arcsec
* 4.0 arcsec

For WFC3, the following apertures are supported:

* every 0.05 arcsec between 0.1 and 0.3 arcsec
* every 0.1 arcsec between 0.3 and 0.6 arcsec
* 0.8 arcsec
* 1.0 arcsec
* 1.5 arcsec
* 2.0 arcsec

To use this capability in simulations, include ``aper#value`` in the ``obsmode``
string, where ``value`` is the radius in arcseconds. When "aper#0" is specified,
the user will obtain the number of counts in the brightest pixel (i.e., the
peak counts of the source centered at that pixel). For example:

>>> bp = S.ObsBandpass('acs,wfc1,f850lp,aper#0.2')


.. _pysynphot-parameterized-temperature:

Temperature
-----------

For :ref:`pysynphot-appendixb-nicmos` and :ref:`pysynphot-appendixb-wfc3`
IR detectors, :ref:`thermal background <pysynphot-command-therm>`
can be calculated by **pysynphot**. If no temperature is specified, the default
value for each component is used (see :ref:`pysynphot_thermal_em` and
:ref:`pysynphot-parameterized`).

For WFC3, the calculation can only be done at the default temperature
(not yet parameterized). For observation modes using a grism, the ``bkg``
keyword is used to perform throughput and emission calculations pertaining to
the associated background signal. This is because in grism observations,
a given detector pixel will receive source signal from only a small wavelength
interval of the dispersed source spectrum, but it will receive background
signal from the entire bandpass of the grism. Therefore, a special throughput
table is used to correctly compute the detected signal from a background
spectrum, which gives the transmission of the grism over its entire bandpass.
The ``bkg`` keyword cannot be used with non-grism observations. For example:

>>> bp = S.ObsBandpass('wfc3,ir,g102,bkg')

For NICMOS, all keywords except the detector are parameterized for
temperature. This includes OTA components that are opaque but thermally
emitting. Most of the its optical elements (``reimag``, ``pupil``, ``image``,
``para1``, ``para2``, ``bend``, ``dewar``, and ``cmask``) are contained in the
dewar, and are therefore at the same temperature. However, **pysynphot** does
not enforce this, so the user must specify any non-default temperature for each
component individually. For example, to specify a primary mirror temperature of
290 K and then calculate the thermal background:

>>> bp = S.ObsBandpass('nicmos,3,f222m,primary#290.0')
>>> bp.thermback()
82.206182481038724


.. _pysynphot-parameterized-contamination:

Contamination
-------------

The ``cont#`` keyword for :ref:`pysynphot-appendixb-wfpc1` and
:ref:`pysynphot-appendixb-wfpc2` references the Modified Julian Date,
which is used to account for the gradual decline in throughput between
decontamination events, as well as for the sudden increase in throughput
immediately after a decontamination.

For WF/PC-1, data exists for dates between May 8, 1991 (MJD 48384) and
December 8, 1993 (MJD 49329), non-inclusive, in the intervals of 20-30 days.
For WFPC2, data currently exists from December 26, 1993 (MJD 49347) until SM4,
in intervals of approximately 30 days.

**pysynphot** interpolates between the dates for which data exist in the table
to arrive at an estimate of the throughput on the requested date
(see :ref:`pysynphot-parameterized`). For example:

>>> bp = S.ObsBandpass('wfpc2,3,f555w,cont#49800')


.. _pysynphot-appendixb-nonhst:

Non-HST Filter Systems
======================

.. |nonhst_cousins| replace:: :ref:`cousins <pysynphot-nonhst-cousins>`
.. |nonhst_cousins2| replace:: :ref:`Cousins <pysynphot-nonhst-cousins>`
.. |nonhst_galex| replace:: :ref:`galex <pysynphot-nonhst-galex>`
.. |nonhst_johnson| replace:: :ref:`johnson <pysynphot-nonhst-johnson>`
.. |nonhst_johnson2| replace:: :ref:`Johnson <pysynphot-nonhst-johnson>`
.. |nonhst_landolt| replace:: :ref:`landolt <pysynphot-nonhst-landolt>`
.. |nonhst_landolt2| replace:: :ref:`Landolt <pysynphot-nonhst-landolt>`
.. |nonhst_sdss| replace:: :ref:`sdss <pysynphot-nonhst-sdss>`
.. |nonhst_stromgren| replace:: :ref:`stromgren <pysynphot-nonhst-stromgren>`
.. |nonhst_stromgren2| replace:: :ref:`Stromgren <pysynphot-nonhst-stromgren>`

In addition to the HST instruments, filters, and gratings, the
:ref:`graph table <pysynphot-graph>` also contains entries for various
standard passbands from photometric systems that are not specific to HST.
Actively supported systems (i.e., their data files are updated on CRDS as
needed) are as tabulated below.
Non-HST filters are specified using the name of the filter system,
followed by the desired band name. For example:

>>> bp = S.ObsBandpass('cousins,i')
>>> bp = S.ObsBandpass('stromgren,u')

If the name of the filter system is omitted for any of the common *UBVRIJHK*
filters, the defaults are Johnson *UBV*, Cousins *RI*, and Bessell *JHK*.
For example, the following are equivalent:

>>> bp = S.ObsBandpass('v')
>>> bp = S.ObsBandpass('johnson,v')

+------------------+-------------+
|System Name       |Band Name    |
+==================+=============+
||nonhst_cousins|  |r i          |
+------------------+-------------+
||nonhst_galex|    |nuv fuv      |
+------------------+-------------+
||nonhst_johnson|  |u v b r i j k|
+------------------+-------------+
||nonhst_landolt|  |u v b r i    |
+------------------+-------------+
||nonhst_sdss|     |u g r i z    |
+------------------+-------------+
||nonhst_stromgren||u v b y      |
+------------------+-------------+


Comparing pysynphot Results with Observed Non-HST Photometry
------------------------------------------------------------

There are two issues that are sometimes overlooked when comparing
synthetic photometry from **pysynphot** with observed photometry using a
non-HST system.

Firstly, one should be careful whether the throughput data have been
defined for a photon-counting or an energy-integrating detector.
**pysynphot** always assumes that a throughput are of the former.
In particular, some authors in the past have defined throughput curves
for photomultipliers as if these detectors were energy integrators,
which they are not. Such curves have to be converted into photon-counting
form before they can be correctly used by **pysynphot**
(:ref:`Maiz Apellaniz 2006 <synphot-ref-maiz2006>`).
Using the wrong definition can lead to errors of a few percent for
broad-band filters.

Secondly, many systems (e.g., Johnson *UBV*) use Vega
as a reference spectrum, but have been calibrated using secondary standards,
leading to the existence of finite zero points. In some systems
(e.g. Stromgren), those zero points are not even
close to 0.0 for some filters. The table below defines the zero point
corrections for ground-based filter systems from measurements of zero points
collected from the respective literature; These values should be added to the
``vegamag`` magnitude in **pysynphot** before they are compared with the
observed data:

+-------------------+-------------+----------+-------------+
|System             |Color/Index  |Zero point|References   |
|                   |             |(mag)     |             |
+===================+=============+==========+=============+
||nonhst_johnson2|  |:math:`V`    |0.026     ||bohlin2004| |
|and                +-------------+----------+-------------+
||nonhst_landolt2|  |:math:`B-V`  |0.010     ||maiz2006|   |
|                   +-------------+----------+-------------+
|                   |:math:`U-B`  |0.020     ||maiz2006|   |
+-------------------+-------------+----------+-------------+
||nonhst_cousins2|  |:math:`V-R`  |-0.012    ||holberg2006||
|and                +-------------+----------+-------------+
||nonhst_landolt2|  |:math:`V-I`  |-0.002    ||holberg2006||
+-------------------+-------------+----------+-------------+
||nonhst_stromgren2||:math:`y`    |0.038     ||holberg2006||
|                   +-------------+----------+-------------+
|                   |:math:`b-y`  |0.007     ||maiz2006|   |
|                   +-------------+----------+-------------+
|                   |:math:`m_{1}`|0.154     ||maiz2006|   |
|                   +-------------+----------+-------------+
|                   |:math:`c_{1}`|1.092     ||maiz2006|   |
+-------------------+-------------+----------+-------------+

.. |bohlin2004| replace:: :ref:`Bohlin & Gilliland (2004) <synphot-ref-bohlin2004>`
.. |holberg2006| replace:: :ref:`Holberg & Bergeron (2006) <synphot-ref-holberg2006>`
.. |maiz2006| replace:: :ref:`Maiz Apellaniz (2006) <synphot-ref-maiz2006>`

The existence of these issues has led CRDS to divide the non-HST photometric
systems into supported (as mentioned above) and
:ref:`not supported <pysynphot-nonhst-deprecated>`.

Systems for which there are analyses in the literature that deal with
the issues mentioned above are as follow. CRDS Team is reasonably confident
that the possible systematic errors in the **pysynphot** results for these
systems are small:

* |nonhst_cousins2| *RI*
* |nonhst_johnson2| *UBV* (but not *RIJK*)
* |nonhst_landolt2| *UBVRI*
* :ref:`pysynphot-nonhst-sdss` *ugriz*
* |nonhst_stromgren2| *uvby*


.. _pysynphot-nonhst-cousins:

Cousins
-------

The Cousins *RI* throughputs are taken from
:ref:`Bessell (1983) <synphot-ref-bessell1983>`. They have been transformed
into photon-counting form. For example:

>>> bp = S.ObsBandpass('cousins,i')


.. _pysynphot-nonhst-galex:

GALEX
-----

The GALEX FUV and NUV throughputs were provided by Tom Barlow on
behalf of the `GALEX <http://www.galex.caltech.edu/>`_ project, as described in
:ref:`Morrissey et al. (2007) <synphot-ref-morrissey2007>`.
They were measured on the ground in units of effective area,
and were divided by the full area of the GALEX primary mirror
(:math:`1963.495 \; \textnormal{cm}^{2}`) to convert them to the dimensionless
transmission values required by **pysynphot**. Therefore, these curves represent
the true total throughput, including obscuration by the secondary mirror,
reflectivity of the mirrors, sensitivity of the detector, and so forth.
For example:

>>> bp = S.ObsBandpass('galex,fuv')


.. _pysynphot-nonhst-johnson:

Johnson
-------

The throughput data for the Johnson *UBV* bands were obtained from
:ref:`Maiz Apellaniz (2006) <synphot-ref-maiz2006>`, while the *RIJK* bands
from :ref:`Johnson (1965) <synphot-ref-johnson1965>`. For example:

>>> bp = S.ObsBandpass('johnson,v')


.. _pysynphot-nonhst-landolt:

Landolt
-------

The :ref:`Landolt (1983) <synphot-ref-landolt1983>` *UBVRI* system is made up of
the :ref:`pysynphot-nonhst-johnson` *UBV* and the
:ref:`pysynphot-nonhst-cousins` *RI* passbands. For example:

>>> bp = S.ObsBandpass('landolt,v')


.. _pysynphot-nonhst-sdss:

SDSS
----

The `Sloan Digital Sky Survey (SDSS) <http://www.sdss.org/>`_ *ugriz* filter
throughputs were provided by Sebastian Jester on behalf of the SDSS team,
as described in :ref:`Gunn et al. (2001) <synphot-ref-gunn2001>`.
The filter curves are shown in the
`SDSS filter response plot <http://www.sdss.org/dr1/instruments/imager/index.html#filters>`_. For example:

>>> bp = S.ObsBandpass('sdss,g')

The throughput data give the system photon response to point sources of the
2.5-m SDSS survey telescope, including extinction through an airmass of 1.3 at
`Apache Point Observatory <http://www.apo.nmsu.edu/>`_ (to which all SDSS
photometry is referenced).
Originally, the *ugriz* system was intended to be identical to the
:math:`u^{\prime} g^{\prime} r^{\prime} i^{\prime} z^{\prime}`
system described in :ref:`Fukugita et al. (1996) <synphot-ref-fukugita1996>`
and defined by the standard star system in
:ref:`Smith et al. (2002) <synphot-ref-smith2002>`. However, in the course
of processing the SDSS data, an unpleasant discovery was made that
the filters in the 2.5-m telescope have significantly different
effective wavelengths from the filters in the
`USNO <http://www.usno.navy.mil/USNO/>`_ telescope, which was used to observe
the :math:`u^{\prime} g^{\prime} r^{\prime} i^{\prime} z^{\prime}`
standards; The difference originates from the USNO filters being exposed to
ambient air, while the survey-telescope filters live in the vacuum of the
survey camera. Therefore, it became necessary to distinguish between the primed
and unprimed SDSS filter sets.

The response curves in *r* and *i* are slightly different for
large extended sources (larger than about 80 pixels in size)
because the extended IR scattering wings in these bands,
which do not affect the photometry of point sources, begin to be
included. The modified curves are shown in an
`updated SDSS system response plot <http://www.sdss.org/dr3/instruments/imager/#filters>`_.

The SDSS photometry is intended to be on the AB system
(:ref:`Oke & Gunn 1983 <synphot-ref-oke1983>`), by which a 0-magnitude object
should have the same counts as a source of
:math:`F_{\nu} = 3631 \; \textnormal{Jy}` (except that it used the so-called
"asinh" magnitudes defined by
:ref:`Lupton et al. 1999 <synphot-ref-lupton1999>` instead of conventional
Pogson magnitudes). However, this is known not to be exactly true, such that
the photometric zero points are slightly off the AB standard. The SDSS team
continues to work to pin down these shifts. Their estimate, based on comparison
to the STIS standards of :ref:`Bohlin et al. (2001) <synphot-ref-bohlin2001>`
and confirmed by SDSS photometry and spectroscopy of fainter hot white dwarfs,
is that the *u* band zero point is in error by 0.04 mag,
:math:`u_{\textnormal{AB}} = u_{\textnormal{SDSS}} - 0.04 \; \textnormal{mag}`,
and that *g*, *r*, and *i* are close to AB; These statements are certainly not
precise to better than 0.01 mag. The *z* band zero point is not as certain
(as of January 2005), but there is mild evidence that it may be shifted by about
0.02 mag in the sense that
:math:`z_{\textnormal{AB}} = z_{\textnormal{SDSS}} + 0.02 \; \textnormal{mag}`.

See :ref:`Holberg & Bergeron (2006) <synphot-ref-holberg2006>` for a
calibration of SDSS magnitudes using Vega as a reference spectrum.
Further information about SDSS photometric calibration and the "asinh"
magnitude system can be found at
`SDSS Photometric Flux Calibration webpage <http://www.sdss.org/dr3/algorithms/fluxcal.html>`_.


.. _pysynphot-nonhst-stromgren:

Stromgren
---------

The Stromgren *uvby* throughputs are taken from
:ref:`Maiz Apellaniz (2006) <synphot-ref-maiz2006>`. For example:

>>> bp = S.ObsBandpass('stromgren,y')


.. _pysynphot-nonhst-deprecated:

Deprecated Systems
------------------

.. |nonhst_ans| replace:: :ref:`ans <pysynphot-nonhst-ans>`
.. |nonhst_baum| replace:: :ref:`baum <pysynphot-nonhst-baum>`
.. |nonhst_bessell| replace:: :ref:`bessell <pysynphot-nonhst-bessell>`
.. |nonhst_eso| replace:: :ref:`eso <pysynphot-nonhst-eso>`
.. |nonhst_kpno| replace:: :ref:`kpno <pysynphot-nonhst-kpno>`
.. |nonhst_steward| replace:: :ref:`steward <pysynphot-nonhst-steward>`
.. |nonhst_walraven| replace:: :ref:`walraven <pysynphot-nonhst-walraven>`

As of March 2006, some non-HST bandpass systems were deprecated, as tabulated
below. They remain accessible by **pysynphot**, but mostly for backward
compatibility. There will be no updates from CRDS, so use these at your own
risk.

+-----------------+-----------------------------------------------+
|System Name      |Band Name                                      |
+=================+===============================================+
||nonhst_ans|     |1550 1550n 1800 2200 2500 3300                 |
+-----------------+-----------------------------------------------+
||nonhst_baum|    |f336w f439w f547m f555w f569w f606w f622w f675w|
|                 |f702w f725lp f785lp f791w f814w f850lp f1042m  |
+-----------------+-----------------------------------------------+
||nonhst_bessell| |j h k                                          |
+-----------------+-----------------------------------------------+
||nonhst_eso|     |88 97 100-102 104-106 109-119 121 122 125      |
|                 |127-130 132 136 140 141 145 149 152 154-157    |
|                 |159-161 163-166 168-170 172-179 181-183 185 186|
|                 |189 192-194 196-199 201-207 209-234 236-242 244|
|                 |247 248 253 254 260 264 265 537 538            |
+-----------------+-----------------------------------------------+
||nonhst_kpno|    |j h k                                          |
+-----------------+-----------------------------------------------+
||nonhst_steward| |j h k                                          |
+-----------------+-----------------------------------------------+
||nonhst_walraven||v b l u w                                      |
+-----------------+-----------------------------------------------+


.. _pysynphot-nonhst-ans:

ANS
^^^

The Astronomical Netherlands Satellite (ANS) system is a set of UV filters used
by the satellite, as described in
:ref:`van Duinen et al. (1975) <synphot-ref-vanduinen1975>`. For example:

>>> bp = S.ObsBandpass('ans,1550')


.. _pysynphot-nonhst-baum:

Baum
^^^^

The Baum filter set is a set of 15 broadband and intermediate-band
filters that are copies the ones onboard :ref:`pysynphot-appendixb-wfpc1` that
were used as part of a ground-based calibration campaign for the instrument.
In order to match the response of the in-flight passbands as closely as
possible, the throughputs for the Baum filters have been multiplied
by the spectral response curve of the ground-based CCD (measured
in the laboratory) and twice by the spectral reflectance of aluminum
(:ref:`Harris et al. 1991 <synphot-ref-harris1991>`). For example:

>>> bp = S.ObsBandpass('baum,f336w')


.. _pysynphot-nonhst-bessell:

Bessell
^^^^^^^

The Bessell *JHK* filter curves are taken from
:ref:`Bessell & Brett (1988) <synphot-ref-bessell1988>`, Table IV.
These curves include the mean atmospheric transmission equivalent to 1.2
air masses of a standard `KPNO <http://www.noao.edu/kpno/>`_  atmosphere.
For example:

>>> bp = S.ObsBandpass('bessell,k')


.. _pysynphot-nonhst-eso:

ESO
^^^

The 530 ESO band throughput tables were received from Jan Koornneef in 1990.
For example:

>>> bp = S.ObsBandpass('eso,198')


.. _pysynphot-nonhst-kpno:

KPNO
^^^^

The `Kitt Peak National Observatory (KPNO) <http://www.noao.edu/kpno/>`_ *JHK*
filter curves are taken from the tracings of the Simultaneous Quad Infrared
Image Device (SQIID) filter set, which were provided by Richard Joyce from the
observatory. For example:

>>> bp = S.ObsBandpass('kpno,k')


.. _pysynphot-nonhst-steward:

Steward
^^^^^^^

The `Steward Observatory <https://www.as.arizona.edu/observing>`_ *JHK* filter
curves are from data provided by Marcia Rieke from the observatory. For example:

>>> bp = S.ObsBandpass('steward,k')


.. _pysynphot-nonhst-walraven:

Walraven
^^^^^^^^

The throughput data for the Walraven *VBLUW* bands are from
:ref:`Lub & Pel (1977) <synphot-ref-lub1977>`, Table 6. For example:

>>> bp = S.ObsBandpass('walraven,v')
