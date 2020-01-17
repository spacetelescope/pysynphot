import os

from astropy.tests.helper import (enable_deprecations_as_exceptions,
                                  treat_deprecations_as_exceptions)
from pytest_astropy_header.display import PYTEST_HEADER_MODULES, TESTED_VERSIONS

enable_deprecations_as_exceptions()


def pytest_configure(config):
    treat_deprecations_as_exceptions()

    # Configure header here.
    PYTEST_HEADER_MODULES['astropy'] = 'astropy'
    PYTEST_HEADER_MODULES.pop('h5py', None)
    PYTEST_HEADER_MODULES.pop('Pandas', None)
    PYTEST_HEADER_MODULES.pop('astropy-helpers', None)

    from pysynphot import __version__ as version
    packagename = os.path.basename(os.path.dirname(__file__))
    TESTED_VERSIONS[packagename] = version
