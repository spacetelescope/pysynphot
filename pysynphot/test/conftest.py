import pytest


def pytest_addoption(parser):
    parser.addoption("--cdbs", action="store_true",
                     help="run tests requiring CDBS")
