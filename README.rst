PySynphot
=========

|ci| |docs| |codecov|

.. |docs| image:: https://readthedocs.org/projects/pysynphot/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://pysynphot.readthedocs.io/en/latest/?badge=latest

.. |ci| image:: https://github.com/spacetelescope/pysynphot/workflows/CI/badge.svg
    :alt: Github Actions CI Status

.. |codecov| image:: https://codecov.io/gh/spacetelescope/pysynphot/branch/master/graph/badge.svg
    :alt: Coverage results
    :target: https://codecov.io/gh/spacetelescope/pysynphot

Synthetic photometry package from Astrolib.

As stated in the project roadmap (https://github.com/spacetelescope/pysynphot/blob/master/ROADMAP.md), Pysynphot is now past its end of life and will no longer receive updates or support. Pysynphot support expired with Python=3.11.9 and numpy=1.24.4.  We recommend users transition to Astropy’s affiliated synphot package (https://synphot.readthedocs.io/) and STScI’s STsynphot (https://stsynphot.readthedocs.io/), an extension of synphot which provides enhanced functionality, improved performance, and better support for modern data analysis needs.

STsynphot is actively maintained and offers comprehensive tools for synthetic photometry, including capabilities to work with both legacy and current instruments. For more information, documentation, and installation instructions, please visit the STsynphot GitHub repository or the STScI documentation page.  For assistance in migrating away from Pysynphot, please see the astrolib switcher guide here: 
https://synphot.readthedocs.io/en/latest/synphot/from_pysyn_iraf.html#astrolib-switcher-guide

Thank you for your continued support, and we encourage you to upgrade to STsynphot for your photometric analysis needs. 
