"""
Test table format errors. Usually in real life these occur
in file access, but many of them apply to ArraySpectrum objects
as well & can be tested that way.
"""
from __future__ import absolute_import, division, print_function

import numpy as np
import pytest

from ..exceptions import (BadRow, DuplicateWavelength, UnsortedWavelength,
                          ZeroWavelength)
from ..spectrum import ArraySourceSpectrum, FileSourceSpectrum


def test_wave_exceptions():
    fx = np.array([10, 20, 20, 30, 50, 100])

    # No error
    sp = ArraySourceSpectrum(np.array([10, 20, 30, 40, 50, 100]), fx)
    assert sp(30) == 20

    with pytest.raises(DuplicateWavelength) as e:
        ArraySourceSpectrum(np.array([10, 20, 20, 30, 50, 100]), fx)
        assert e.rows == 1

    with pytest.raises(ZeroWavelength):
        ArraySourceSpectrum(np.array([0, 20, 30, 40, 50, 100]), fx)

    with pytest.raises(UnsortedWavelength):
        ArraySourceSpectrum(np.array([10, 20, 40, 30, 50, 100]), fx)


def test_file_badrow(tmpdir):
    wv = np.array([10, 20, 'grackle', 30, 50, 100])
    content = ''

    for w in wv:
        content += "{0}  {0}\n".format(w)

    # pytest will only keep the last few runs and auto delete the rest
    fname = tmpdir.join('grackle.dat')
    fname.write(content)

    with pytest.raises(BadRow) as e:
        FileSourceSpectrum(str(fname))
        assert e.rows == 3
