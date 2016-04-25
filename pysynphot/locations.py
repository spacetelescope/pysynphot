"""This module handles locations of data files.

**Global Variables**

* ``pysynphot.locations.pysynphot._root()`` - Root directory for CDBS/CRDS
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
from __future__ import division
import glob
import os
import re
import warnings
import pysynphot

from astropy.io import fits as pyfits

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





def _refTable(template):
    try:
        names = glob.glob(os.path.join(pysynphot._root(), template))
        names.sort()
    except KeyError:
        warnings.warn("PYSYN_CDBS is undefined; cannot find %s file" % template)
        return None

    try:
        return names[-1]
    except IndexError:
        msg= "No files found for %s." % os.path.join(pysynphot._root(),
                                                     template)
        raise IOError(msg)

RedLaws = {}

def _get_RedLaws():
    global RedLaws

    extdir = os.path.join(pysynphot._root(), EXTDIR)

    # get all the fits files in EXTDIR
    globstr = os.path.join(extdir, '*.fits')
    files = glob.glob(globstr)

    if not files:
        warnings.warn('Extinction files not found in %s' % (extdir,))
        return

    # replace ###.fits at the end of file names with *.fits
    # and get a unique set
    files = set(f[:-8] + '*.fits' for f in files)

    # use _refTable to get the most recent version of each extinction file
    # and add that to the RedLaws dict
    for f in files:
        lawf = _refTable(f)

        key = pyfits.getval(lawf,'shortnm')

        RedLaws[key.lower()] = lawf

rootdir = pysynphot._root()

#Eliminate use of temporary directory; use python tmpfile utilities instead
CAT_TEMPLATE = os.path.join(pysynphot._root(), 'grid', '*', 'catalog.fits')
KUR_TEMPLATE = os.path.join(pysynphot._root(), 'grid', '*')

#Vega
VegaFile = get_data_filename('alpha_lyr_stis_008.fits')


# CDBS is moving extinction files to $PYSYN_CDBS/extinction so here we
# test whether that location exists and use it if it does.
# If it doesn't exist we use the old location $PYSYN_CDBS/grid/extinction
# and print a warning.
if (os.path.exists(os.path.join(pysynphot._root(), 'extinction')) and
    os.path.isdir(os.path.join(pysynphot._root(), 'extinction'))):
    EXTDIR = 'extinction'
else:
    EXTDIR = os.path.join('grid', 'extinction')

    warnings.warn('Extinction files should be moved to '
                  '$PYSYN_CDBS/extinction for compatibility with '
                  'future versions of pysynphot.')


#Define wavecat file explicitly
wavecat = get_data_filename('wavecat.dat')

# load the extintion law file names
_get_RedLaws()

## This dictionary maps IRAF-specific directory names for synphot
## directories into their Unix equivalents.
#BUG: supports only a single variable in a string
#............basically this is a weak routine that should be made
#............more robust
#BUG: this dictionary should be in a data file
CONVERTDICT = {'crrefer':pysynphot._root(),
              'crotacomp':os.path.join(pysynphot._root(),'comp','ota'),
              'cracscomp':os.path.join(pysynphot._root(),'comp','acs'),
              'crcalobs':os.path.join(pysynphot._root(),'calobs'),
              'crcalspec':os.path.join(pysynphot._root(),'calspec'),
              'croldcalspec':os.path.join(pysynphot._root(),'oldcalspec'),
              'crcomp':os.path.join(pysynphot._root(),'comp'),
              'crfgs':os.path.join(pysynphot._root(),'fgs'),
              'crfields':os.path.join(pysynphot._root(),'fields'),
              'crmodewave':os.path.join(pysynphot._root(),'modewave'),
              'crcostarcomp':os.path.join(pysynphot._root(),'comp','costar'),
              'cracscomp':os.path.join(pysynphot._root(),'comp','acs'),
              'crfoccomp':os.path.join(pysynphot._root(),'comp','foc'),
              'crfoscomp':os.path.join(pysynphot._root(),'comp','fos'),
              'crfgscomp':os.path.join(pysynphot._root(),'comp','fgs'),
              'crhrscomp':os.path.join(pysynphot._root(),'comp','hrs'),
              'crhspcomp':os.path.join(pysynphot._root(),'comp','hsp'),
              'crotacomp':os.path.join(pysynphot._root(),'comp','ota'),
              'crnicmoscomp':os.path.join(pysynphot._root(),'comp','nicmos'),
              'crnonhstcomp':os.path.join(pysynphot._root(),'comp','nonhst'),
              'crstiscomp':os.path.join(pysynphot._root(),'comp','stis'),
              'crstiscomp':os.path.join(pysynphot._root(),'comp','stis'),
              'crwfc3comp':os.path.join(pysynphot._root(),'comp','wfc3'),
              'crcoscomp':os.path.join(pysynphot._root(),'comp','cos'),
              'coscomp':os.path.join(pysynphot._root(),'comp','cos'),
              'crwave':os.path.join(pysynphot._root(),'crwave'),
              'crwfpccomp':os.path.join(pysynphot._root(),'comp','wfpc'),
              'crwfpc2comp':os.path.join(pysynphot._root(),'comp','wfpc2'),
              'crgrid':os.path.join(pysynphot._root(),'grid'),
              'crgridbz77':os.path.join(pysynphot._root(),'grid','bz77'),
              'crgridgs':os.path.join(pysynphot._root(),'grid','gunnstryker'),
              'crgridjac':os.path.join(pysynphot._root(),'grid','jacobi'),
              'crgridbpgs':os.path.join(pysynphot._root(),'grid','bpgs'),
              'crgridbk':os.path.join(pysynphot._root(),'grid','bkmodels'),
              'crgridk93':os.path.join(pysynphot._root(),'grid','k93models'),
              'crgridagn':os.path.join(pysynphot._root(),'grid','agn'),
              'crgridgalactic':os.path.join(pysynphot._root(),'grid','galactic'),
              'crgridkc96':os.path.join(pysynphot._root(),'grid','kc96'),
              'mtab':os.path.join(pysynphot._root(),'mtab'),
              'synphot': os.path.dirname(__file__) + os.path.sep,
              # PATH for JWST instrument files
              'crjwstotecomp':os.path.join(pysynphot._root(),'comp','jwstote'),
              # PATH for JWST MIRI instrument files
              'crmiricomp':os.path.join(pysynphot._root(),'comp','miri'),
              # PATH for JWST NIRCam instrument files
              'crnircamcomp':os.path.join(pysynphot._root(),'comp','nircam'),
              # PATH for JWST NIRSpec instrument files
              'crnirspeccomp':os.path.join(pysynphot._root(),'comp','nirspec'),
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
    iraffilename = os.path.normpath(iraffilename)

    #BUG: supports environment variables only as the leading element in the
    #     filename
    if iraffilename.startswith('$'):
        #Then this is an environment variable.
        #Use a regex to pull off the front piece.
        pat = re.compile('\$(\w*)')
        match = re.match(pat,iraffilename)
        dirname = match.group(1)
        unixdir = os.environ[dirname]
        basename = iraffilename[match.end()+1:] #1 to omit leading slash
        unixfilename = os.path.join(unixdir, basename)
        return unixfilename
    elif '$' in iraffilename:
        #Then it's an iraf-style variable
        irafdir, basename = iraffilename.split('$')
        if irafdir == 'synphot':
            return get_data_filename(os.path.basename(basename))
        unixdir = convertdict[irafdir]
        unixfilename = os.path.join(unixdir, basename)
        return unixfilename
    else:
        #If no $ sign found, just return the filename unchanged
        return iraffilename
