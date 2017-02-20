"""This module handles locations of data files.

**Global Variables**

* ``pysynphot.locations.rootdir`` - Root directory for CDBS/CRDS
  data files. By default, it is extracted from your ``PYSYN_CDBS``
  environment variable.

* ``pysynphot.locations.specdir`` - Data directory for
  data files distributed with this software.

* ``pysynphot.locations.CAT_TEMPLATE`` and
  ``pysynphot.locations.KUR_TEMPLATE`` - String templates used for
  `~pysynphot.catalog.Icat` to select spectra from catalogs.

* ``pysynphot.locations.VegaFile`` - Vega spectrum to use for
  ``vegamag`` calculations.

* ``pysynphot.locations.EXTDIR`` - Directory containing extinction
  curves.

* ``pysynphot.locations.RedLaws`` - Dictionary mapping reddening laws
  to data files or cached instances (see `~pysynphot.Cache`).

* ``pysynphot.locations.wavecat`` - Data file for `~pysynphot.wavetable`.

* ``pysynphot.locations.CONVERTDICT`` - Dictionary mapping IRAF-style
  directory shortcuts to actual paths.

"""
from __future__ import division, print_function

import fnmatch
import glob
import os
import re
import warnings

from astropy.io import fits as pyfits


# Replace cdbs_roots lookup with an environment variable
try:
    rootdir = os.environ['PYSYN_CDBS']
except KeyError:
    warnings.warn("PYSYN_CDBS is undefined; functionality will be SEVERELY "
                  "crippled.")
    rootdir = ''

ftp_rootdir = 'ftp://ftp.stsci.edu/cdbs'

# Data directory is now installed locally
specdir = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.isdir(specdir):
    # We might be running out of the source; try looking up a level
    pardir = os.path.join(os.path.dirname(__file__), os.pardir)
    specdir = os.path.join(pardir, 'data')
    setup_py = os.path.join(pardir, 'setup.py')
    # Ensure that we're actually in the source tree
    if not os.path.exists(specdir) or not os.path.exists(setup_py):
        # It's possible when running ./setup.py nosetests that we're running
        # out of the build/ directory so check for that case too (note we
        # can't guarnatee the directory is named 'build')
        pardir = os.path.join(pardir, os.pardir, os.pardir)
        specdir = os.path.join(pardir, 'data')
        setup_py = os.path.join(pardir, 'setup.py')
        if not os.path.exists(specdir) or not os.path.exists(setup_py):
            raise RuntimeError('pysynphot data directory missing!')
    del pardir
    del setup_py

specdir = os.path.abspath(specdir) + os.sep


# Map of filenames to their actual path
_data_map = None


# This dictionary maps IRAF-specific directory names for synphot
# directories into their Unix equivalents.
# BUG: supports only a single variable in a string
# ............basically this is a weak routine that should be made
# ............more robust
# BUG: this dictionary should be in a data file
CONVERTDICT = {'crrefer': rootdir,
               'crotacomp': os.path.join(rootdir, 'comp', 'ota'),
               'cracscomp': os.path.join(rootdir, 'comp', 'acs'),
               'crcalobs': os.path.join(rootdir, 'calobs'),
               'crcalspec': os.path.join(rootdir, 'calspec'),
               'croldcalspec': os.path.join(rootdir, 'oldcalspec'),
               'crcomp': os.path.join(rootdir, 'comp'),
               'crfgs': os.path.join(rootdir, 'fgs'),
               'crfields': os.path.join(rootdir, 'fields'),
               'crmodewave': os.path.join(rootdir, 'modewave'),
               'crcostarcomp': os.path.join(rootdir, 'comp', 'costar'),
               'cracscomp': os.path.join(rootdir, 'comp', 'acs'),
               'crfoccomp': os.path.join(rootdir, 'comp', 'foc'),
               'crfoscomp': os.path.join(rootdir, 'comp', 'fos'),
               'crfgscomp': os.path.join(rootdir, 'comp', 'fgs'),
               'crhrscomp': os.path.join(rootdir, 'comp', 'hrs'),
               'crhspcomp': os.path.join(rootdir, 'comp', 'hsp'),
               'crotacomp': os.path.join(rootdir, 'comp', 'ota'),
               'crnicmoscomp': os.path.join(rootdir, 'comp', 'nicmos'),
               'crnonhstcomp': os.path.join(rootdir, 'comp', 'nonhst'),
               'crstiscomp': os.path.join(rootdir, 'comp', 'stis'),
               'crstiscomp': os.path.join(rootdir, 'comp', 'stis'),
               'crwfc3comp': os.path.join(rootdir, 'comp', 'wfc3'),
               'crcoscomp': os.path.join(rootdir, 'comp', 'cos'),
               'coscomp': os.path.join(rootdir, 'comp', 'cos'),
               'crwave': os.path.join(rootdir, 'crwave'),
               'crwfpccomp': os.path.join(rootdir, 'comp', 'wfpc'),
               'crwfpc2comp': os.path.join(rootdir, 'comp', 'wfpc2'),
               'crgrid': os.path.join(rootdir, 'grid'),
               'crgridbz77': os.path.join(rootdir, 'grid', 'bz77'),
               'crgridgs': os.path.join(rootdir, 'grid', 'gunnstryker'),
               'crgridjac': os.path.join(rootdir, 'grid', 'jacobi'),
               'crgridbpgs': os.path.join(rootdir, 'grid', 'bpgs'),
               'crgridbk': os.path.join(rootdir, 'grid', 'bkmodels'),
               'crgridk93': os.path.join(rootdir, 'grid', 'k93models'),
               'crgridagn': os.path.join(rootdir, 'grid', 'agn'),
               'crgridgalactic': os.path.join(rootdir, 'grid', 'galactic'),
               'crgridkc96': os.path.join(rootdir, 'grid', 'kc96'),
               'mtab': os.path.join(rootdir, 'mtab'),
               'synphot': os.path.dirname(__file__) + os.path.sep,
               # PATH for JWST instrument files
               'crjwstotecomp': os.path.join(rootdir, 'comp', 'jwstote'),
               # PATH for JWST MIRI instrument files
               'crmiricomp': os.path.join(rootdir, 'comp', 'miri'),
               # PATH for JWST NIRCam instrument files
               'crnircamcomp': os.path.join(rootdir, 'comp', 'nircam'),
               # PATH for JWST NIRSpec instrument files
               'crnirspeccomp': os.path.join(rootdir, 'comp', 'nirspec'),
               }


def irafconvert(iraffilename):
    """Convert the IRAF file name to its Unix equivalent.

    Input can be in ``directory$file`` or ``$directory/file`` format.
    If ``'$'`` is not found in the input string, it is returned as-is.

    Parameters
    ----------
    iraffilename : str
        Filename in IRAF format.

    Returns
    -------
    unixfilename : str
        Filename in Unix format.

    Raises
    ------
    AttributeError
        Input is not a string.

    """
    convertdict = CONVERTDICT

    # remove duplicate separators and extraneous relative paths
    if not iraffilename.lower().startswith('ftp'):
        iraffilename = os.path.normpath(iraffilename)

    # BUG: supports environment variables only as the leading element in the
    #      filename
    if iraffilename.startswith('$'):
        # Then this is an environment variable.
        # Use a regex to pull off the front piece.
        pat = re.compile('\$(\w*)')
        match = re.match(pat, iraffilename)
        dirname = match.group(1)
        unixdir = os.environ[dirname]
        basename = iraffilename[match.end()+1:]  # 1 to omit leading slash
        unixfilename = os.path.join(unixdir, basename)
        return unixfilename
    elif '$' in iraffilename:
        # Then it's an iraf-style variable
        irafdir, basename = iraffilename.split('$')
        if irafdir == 'synphot':
            return get_data_filename(os.path.basename(basename))
        unixdir = convertdict[irafdir]
        unixfilename = os.path.join(unixdir, basename)
        return unixfilename
    else:
        # If no $ sign found, just return the filename unchanged
        return iraffilename


def get_data_filename(filename):
    """Map filename to its actual path.

    Parameters
    ----------
    filename : str
        Filename to search.

    Returns
    -------
    path : str
        Full path to the file in data directory.

    """
    global _data_map

    if _data_map is None:
        _data_map = {}
        for root, dirs, files in os.walk(specdir):
            for fname in files:
                _data_map[fname] = os.path.join(root, fname)

    if filename not in _data_map:
        raise KeyError(filename + ' not found in ' + specdir)
    return _data_map[filename]


# Eliminate use of temporary directory; use python tmpfile utilities instead
CAT_TEMPLATE = os.path.join(rootdir, 'grid', '*', 'catalog.fits')
KUR_TEMPLATE = os.path.join(rootdir, 'grid', '*')

# Vega
VegaFile = get_data_filename('alpha_lyr_stis_008.fits')


# CDBS moved extinction files to $PYSYN_CDBS/extinction .
# The old location $PYSYN_CDBS/grid/extinction is no longer used.
EXTDIR = 'extinction'

# Define wavecat file explicitly
wavecat = get_data_filename('wavecat.dat')


# Copied over from stsynphot
def get_latest_file(template, raise_error=False, err_msg=''):
    """Find the filename that appears last in sorted order
    based on given template.

    Parameters
    ----------
    template : str
        Search template in the form of ``path/pattern``
        where pattern is acceptable by :py:mod:`fnmatch`.

    raise_error : bool, optional
        Raise an error when no files found.
        Otherwise, will issue warning only.

    err_msg : str
        Alternate message for when no files found.
        If not given, generic message is used.

    Returns
    -------
    filename : str
        Latest filename.

    Raises
    ------
    IOError
        No files found.

    """
    path, pattern = os.path.split(irafconvert(template))

    # Remote FTP directory
    if path.lower().startswith('ftp:'):
        from astropy.extern.six.moves.urllib import request

        try:
            response = request.urlopen(path).read().decode('utf-8').splitlines()  # noqa
        except Exception:
            allfiles = []
        else:
            # Rid symlink
            allfiles = list(set([x.split()[-1] for x in response]))

    # Local directory
    elif os.path.isdir(path):
        allfiles = os.listdir(path)

    # Bogus directory
    else:
        allfiles = []

    matched_files = sorted(fnmatch.filter(allfiles, pattern))

    # Last file in sorted listing
    if matched_files:
        filename = os.path.join(path, matched_files[-1])

    # No files found
    else:
        if not err_msg:
            err_msg = 'No files found for {0}'.format(template)

        if raise_error:
            raise IOError(err_msg)
        else:
            warnings.warn(err_msg)
            filename = ''

    return filename


def _refTable(template):
    return get_latest_file(
        os.path.join(os.environ.get('PYSYN_CDBS', ftp_rootdir), template),
        raise_error=True)

RedLaws = {}


def _get_RedLaws():
    global RedLaws

    extdir = os.path.join(rootdir, EXTDIR)

    # get all the fits files in EXTDIR
    globstr = os.path.join(extdir, '*.fits')

    if extdir.lower().startswith('ftp:'):
        from astropy.extern.six.moves.urllib import request
        response = request.urlopen(extdir).read().decode('utf-8').splitlines()
        files = list(set([x.split()[-1] for x in response if x.endswith('.fits')]))  # Rid symlink # noqa
        files = [os.path.join(extdir, f) for f in files]
    else:
        files = glob.glob(globstr)

    if not files:
        warnings.warn('Extinction files not found in %s' % (extdir, ))
        return

    # replace ###.fits at the end of file names with *.fits
    # and get a unique set
    patterns = set(f[:-8] + '*.fits' for f in files)

    # use _refTable to get the most recent version of each extinction file
    # and add that to the RedLaws dict
    for pattern in patterns:
        lawf = sorted(fnmatch.filter(files, pattern))[-1]

        key = pyfits.getval(lawf, 'shortnm')

        RedLaws[key.lower()] = lawf

# load the extintion law file names
_get_RedLaws()
