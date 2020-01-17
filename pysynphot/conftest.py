import os

from astropy.tests.helper import (enable_deprecations_as_exceptions,
                                  treat_deprecations_as_exceptions)
# from pytest_astropy_header.display import PYTEST_HEADER_MODULES
from pytest_astropy_header.display import TESTED_VERSIONS

enable_deprecations_as_exceptions()


def pytest_configure(config):
    treat_deprecations_as_exceptions()

    # Configure header here. Examples:
    # PYTEST_HEADER_MODULES.pop('Pandas', None)
    # PYTEST_HEADER_MODULES['scikit-image'] = 'skimage'

    from pysynphot import __version__ as version
    packagename = os.path.basename(os.path.dirname(__file__))
    TESTED_VERSIONS[packagename] = version
