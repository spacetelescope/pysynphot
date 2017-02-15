import pytest

# This is to mark tests that require access to CDBS
try:
    use_cdbs = pytest.mark.skipif(not pytest.config.getoption('--cdbs'),
                                  reason='need --cdbs option to run')
except AttributeError:  # Not using pytest
    use_cdbs = pytest.mark.skipif(True, reason='need --cdbs option to run')
