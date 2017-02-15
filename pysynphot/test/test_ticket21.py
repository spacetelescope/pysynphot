from __future__ import absolute_import, division, print_function

import os

from .utils import use_cdbs
from .. import refs
from ..observationmode import ObservationMode
from ..spectrum import InterpolatedSpectralElement

old_comptable = None


def setup_module(module):
    """
    Freeze the version of the comptable so tests are not susceptible to
    updates to CDBS.
    """
    global old_comptable
    old_comptable = refs.COMPTABLE
    refs.COMPTABLE = os.path.join(
        os.environ['PYSYN_CDBS'], 'mtab', 'OLD_FILES', 'rcb1833hm_tmc.fits')


def teardown_module(module):
    refs.COMPTABLE = old_comptable


@use_cdbs
def test_one_param():
    parkey = 'mjd'
    parval = 54000
    om = ObservationMode('acs,hrc,f555w,mjd#54000')
    rnames = [x for x in om._throughput_filenames if (x != 'clear')]
    reffile = os.path.join(os.environ['PYSYN_CDBS'], 'comp', 'acs',
                           'acs_hrc_ccd_mjd_013_syn.fits[mjd#]')
    idx = rnames.index(reffile)

    # parm# in modes
    assert (parkey + '#') in om.modes

    # filename has a "#"
    assert reffile in om._throughput_filenames

    # dict entry
    assert om.pardict[parkey] == parval

    # interpolated type
    assert isinstance(om.components[idx].throughput,
                      InterpolatedSpectralElement), \
        '{}\n{}'.format(len(om.components), idx)


@use_cdbs
def test_two_params():
    pardict = {'fr459m': 4610, 'aper': 0.3}
    om = ObservationMode('acs,hrc,fr459m#4610,aper#0.3')

    # parm# in modes
    for k in pardict:
        assert (k + '#') in om.modes

    # dict vals
    for k in pardict:
        assert om.pardict[k] == pardict[k]
