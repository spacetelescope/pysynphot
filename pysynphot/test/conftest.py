import pytest  # noqa

from astropy.tests.helper import (enable_deprecations_as_exceptions,
                                  treat_deprecations_as_exceptions)

enable_deprecations_as_exceptions()


def pytest_configure(config):
    treat_deprecations_as_exceptions()


def pytest_addoption(parser):
    parser.addoption("--cdbs", action="store_true",
                     help="run tests requiring CDBS")
