"""
This __init__ file is used to expose the desired elements of the user
interface for interactive use.

"""
from __future__ import absolute_import

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = 'unknown'

# For backwards compatibility
__svn_version__ = 'none'
__full_svn_info__ = 'none'
__svn_revision__ = __svn_version__
__svn_full_info__ = __full_svn_info__

# UI:
# AnalyticSpectra:
from .spectrum import BlackBody, GaussianSource, FlatSpectrum  # noqa
from .spectrum import Powerlaw as PowerLaw  # noqa
# Tabular Spectra
from .spectrum import FileSourceSpectrum as FileSpectrum  # noqa
from .spectrum import ArraySourceSpectrum as ArraySpectrum  # noqa
from .catalog import Icat  # noqa
# Analytic Spectral Elements
from .spectrum import Box, UniformTransmission  # noqa
# Tabular Spectral Elements
from .spectrum import FileSpectralElement as FileBandpass  # noqa
from .spectrum import ArraySpectralElement as ArrayBandpass  # noqa
# Complicated spectral elements
from .obsbandpass import ObsBandpass  # noqa
from .reddening import Extinction  # noqa
# Observations
from .observation import Observation  # noqa
# Other constructs
from .observationmode import ObservationMode as Obsmode  # noqa
from numpy import arange as Waveset  # noqa
# Get Vega
from .spectrum import Vega  # noqa
# Get cache
from . import Cache  # noqa
# Permit resetting refdata
from .refs import setref, showref, getref  # noqa
# Others
from .locations import get_data_filename  # noqa
from .spparser import parse_spec  # noqa
from . import tables  # noqa
