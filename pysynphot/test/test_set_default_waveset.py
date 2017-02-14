from __future__ import absolute_import, division, print_function

import numpy as np
from numpy.testing import assert_allclose, assert_array_equal

from .. import refs


def setup_module(module):
    pass


def teardown_module(module):
    """Reset refs; specifically the default waveset."""
    refs.setref()


def test_log_num():
    testref = [10, 10.71773463, 11.48698355, 12.31144413, 13.19507911,
               14.14213562, 15.15716567, 16.24504793, 17.41101127, 18.66065983]

    refs.set_default_waveset(10, 20, 10)
    assert_allclose(testref, refs._default_waveset)

    refs.setref(waveset=(10, 20, 10))
    assert_allclose(testref, refs._default_waveset)

    refs.setref(waveset=(10, 20, 10, 'log'))
    assert_allclose(testref, refs._default_waveset)


def test_log_delta():
    testref = [10, 11.22018454, 12.58925412, 14.12537545, 15.84893192,
               17.7827941, 19.95262315]
    refs.set_default_waveset(10, 20, delta=0.05)
    assert_allclose(testref, refs._default_waveset)


def test_linear():
    testref = np.arange(10, 20)

    refs.set_default_waveset(10, 20, 10, log=False)
    assert_array_equal(refs._default_waveset, testref)

    refs.setref(waveset=(10, 20, 10, 'linear'))
    assert_allclose(testref, refs._default_waveset)

    refs.set_default_waveset(10, 20, delta=1, log=False)
    assert_array_equal(refs._default_waveset, testref)
