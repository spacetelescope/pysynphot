"""
This __init__ file is used to expose the desired elements of the user
interface for interactive use.

"""
from __future__ import absolute_import
from .version import *

# For backwards compatibility
__svn_version__ = __version_commit__
__full_svn_info__ = '-'.join([__version__,
    __version_post__,
    __version_commit__,]) + ' ({0})'.format(__version_date__)
__svn_revision__ = __svn_version__
__svn_full_info__ = __full_svn_info__

def _init():
    #UI:
    #AnalyticSpectra:
    from .spectrum import BlackBody, GaussianSource, FlatSpectrum
    from .spectrum import Powerlaw as PowerLaw
    #Tabular Spectra
    from .spectrum import FileSourceSpectrum as FileSpectrum
    from .spectrum import ArraySourceSpectrum as ArraySpectrum
    from .catalog import Icat
    #Analytic Spectral Elements
    from .spectrum import Box, UniformTransmission
    #Tabular Spectral Elements
    from .spectrum import FileSpectralElement as FileBandpass
    from .spectrum import ArraySpectralElement as ArrayBandpass
    #Complicated spectral elements
    from .obsbandpass import ObsBandpass
    from .reddening import Extinction
    #Observations
    from .observation import Observation
    #Other constructs
    from .observationmode import ObservationMode as Obsmode
    from numpy import arange as Waveset
    #Get Vega
    from .spectrum import Vega
    #Get cache
    from . import Cache
    #Permit resetting refdata
    from .refs import setref, showref
    #
    from .locations import get_data_filename
    from . import tables
    globals().update(locals())

user_path = None
def use(path):
    import pysynphot
    pysynphot.user_path = path
    pysynphot._init()
    return None

def _root():
    import pysynphot
    import os
    import warnings
    if pysynphot.user_path == None:
        try: pysynphot.user_path = os.environ['PYSYN_CDBS']
        except KeyError:
            warnings.warn("PYSYN_CDBS is undefined; functionality will be SEVERELY "
                          "crippled.")
    return pysynphot.user_path

def _test():
    "Runs doctest on the examples in this file"
    import doctest
    nfail,ntest=doctest.testfile('__init__.py')
    return nfail,ntest

if _root() is not None: _init()

if __name__ == '__main__':
    _init()
    nfail,ntest=_test()
