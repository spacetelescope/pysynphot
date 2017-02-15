from __future__ import absolute_import, division, print_function

import numpy as np
import pytest
from numpy.testing import assert_array_equal

from .. import binning


@pytest.mark.parametrize(
    ('centers', 'ref'),
    [(np.arange(10, 20, dtype=np.float), np.arange(9.5, 20)),
     (2.0 ** np.arange(1, 10), [1, 3, 6, 12, 24, 48, 96, 192, 384, 640])])
def test_calculate_bin_edges(centers, ref):
    """Test bin edges calculated for an evenly and an unevenly spaced
    set of centers.
    """
    assert_array_equal(binning.calculate_bin_edges(centers), ref)


@pytest.mark.parametrize(
    ('edges', 'widths', 'centers'),
    [([1, 2, 4, 10, 20], [1, 2, 6, 10], [1.5, 2.5, 5.5, 14.5]),
     ([1, 2], [1], [1.5])])
def test_calculate_bins(edges, widths, centers):
    """Test a normal case and an edge case with only one bin."""
    assert_array_equal(binning.calculate_bin_widths(edges), widths)
    assert_array_equal(binning.calculate_bin_centers(edges), centers)


def test_center_edge_center_roundtrip():
    """
    Test that we can start with centers and roundtrip to the same centers.
    """
    centers = [1, 2, 4, 10, 20]
    calc_edges = binning.calculate_bin_edges(centers)
    calc_centers = binning.calculate_bin_centers(calc_edges)
    assert_array_equal(calc_centers, centers)


@pytest.mark.parametrize('a', [np.arange(20).reshape((4, 5)), np.array([5])])
def test_calculate_bin_raises(a):
    """Test we get a ValueError with a non-1D or scalar array."""
    with pytest.raises(ValueError):
        binning.calculate_bin_edges(a)

    with pytest.raises(ValueError):
        binning.calculate_bin_widths(a)

    with pytest.raises(ValueError):
        binning.calculate_bin_centers(a)
