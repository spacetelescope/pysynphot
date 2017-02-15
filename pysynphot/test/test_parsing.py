from __future__ import absolute_import, division, print_function

import os

import pytest

from .utils import use_cdbs
from ..exceptions import DisjointError
from ..spectrum import SourceSpectrum
from ..spparser import parse_spec

is_ftp = os.environ['PYSYN_CDBS'].lower().startswith('ftp')


@use_cdbs
@pytest.mark.parametrize(
    'sp_str',
    ['spec($PYSYN_CDBS//calspec/gd71_mod_005.fits)',
     'rn(unit(1.,flam),band(acs,wfc1,fr388n#3881.0),10.000000,abmag)'])
def test_parse_source(sp_str):
    sp = parse_spec(sp_str)
    assert isinstance(sp, SourceSpectrum)


@use_cdbs
@pytest.mark.xfail(reason='Does not work')
@pytest.mark.parametrize(
    'sp_str',
    ['rn(unit(1.,flam),band(stis,ccd,g430m,c4451,52X0.2),10.000000,abmag)',
     'rn(unit(1.,flam),band(stis,ccd,mirror,50CCD),10.000000,abmag)'])
def test_x_decimal(sp_str):
    sp = parse_spec(sp_str)
    assert isinstance(sp, SourceSpectrum)


@use_cdbs
@pytest.mark.xfail(is_ftp, reason='rn does not work with FTP files')
def test_disjoint():
    with pytest.raises(DisjointError):
        parse_spec('rn($PYSYN_CDBS/etc/source/qso_fos_001.dat,'
                   'band(johnson,v),15,abmag)')


@use_cdbs
@pytest.mark.xfail(is_ftp, reason='rn does not work with FTP files')
def test_partial():
    sp = parse_spec('rn($PYSYN_CDBS/etc/source/qso_fos_001.dat,'
                    'band(johnson,u),15,abmag)')
    assert 'force_renorm' in sp.warnings
