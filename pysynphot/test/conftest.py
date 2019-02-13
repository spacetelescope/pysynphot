from astropy.tests.helper import (enable_deprecations_as_exceptions,
                                  treat_deprecations_as_exceptions)

enable_deprecations_as_exceptions()


def pytest_configure(config):
    treat_deprecations_as_exceptions()
