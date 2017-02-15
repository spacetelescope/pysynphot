from __future__ import absolute_import, division, print_function

import pytest
from numpy.testing import assert_array_equal

from ..wavetable import wavetable


@pytest.mark.parametrize(
    ('obs', 'ans'),
    [('nicmos,3,f220m', '(7000.0,29996.0,1.0)'),
     ('acs,hrc,f550m', wavetable['acs,hrc']),
     ('stis,ccd,g750m', wavetable['stis,g750m']),
     ('stis,fuvmama,g140l,s52x2', wavetable['stis,g140l']),
     ('stis,nuvmama,e230h,c2263,s02x02', wavetable['stis,e230h,c2263'])])
def test_match(obs, ans):
    assert_array_equal(wavetable[obs], ans)


def test_missing():
    with pytest.raises(KeyError):
        wavetable.__getitem__('johnson,v')
