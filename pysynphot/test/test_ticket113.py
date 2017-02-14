from __future__ import absolute_import, division, print_function

import pytest

from ..spparser import scan


@pytest.mark.parametrize('pstr', ['/a/b/c/foo.fits', 'C:/a/b/c/foo.fits'])
def test_path(pstr):
    tokens = [pstr]
    x = scan(pstr)
    assert x[0].attr == tokens[0]
    assert len(x) == len(tokens)
