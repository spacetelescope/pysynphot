from __future__ import division # confidence high

import sys
import distutils
import distutils.core
import distutils.sysconfig

from distutils.command.build_ext import build_ext as _build_ext

try:
    import numpy
except:
    raise ImportError('NUMPY was not found. It may not be installed or it may not be on your PYTHONPATH')

pythoninc = distutils.sysconfig.get_python_inc()
numpyinc = numpy.get_include()

pkg = 'pysynphot'

ext = [ distutils.core.Extension(pkg + '.pysynphot_utils',
                                  ['src/pysynphot_utils.c'],
                                  include_dirs = [pythoninc,numpyinc]) ]

class build_ext(_build_ext):
  def run(self):
    try:
        _build_ext.run(self)
    except:
        print '\n*************************'
        print 'Build failed, trying without C extension.'
        print 'This removes no functionality but may affect performance.'
        print '*************************\n'
  def build_extension(self, ext):
    try:
        _build_ext.build_extension(self, ext)
    except:
        print '\n*************************'
        print 'Build failed, trying without C extension.'
        print 'This removes no functionality but may affect performance.'
        print '*************************\n'

setupargs = {
    'version'       :       "0.9.2dev",
    'description'   :       'Python Synthetic Photometry Utilities',
    'fullname'      :       'AstroLib Pysynphot',
    'license'       :       'BSD',
    'author'        :       "Vicki Laidler, Matt Davis, Robert Jedrzejewski, Ivo Busko",
    'author_email'  :       "help@stsci.edu",
    'url'           :       "http://trac6.assembla.com/astrolib",
    'platforms'     :       ["Linux","Solaris","Mac OS X", "Win"],
    'requires'      :       ['pyfits','numpy'],
    'data_files'    :       [ ( pkg+'/data', [ 'data/generic/*', 'data/wavecat/*' ] ) ],
    'ext_modules'   :       ext,
    'cmdclass'      :       {'build_ext':build_ext},
    'package_dir'   :       { 'pysynphot' : 'lib/pysynphot' },

}

# We want to do this specially for pyetc.  In pyetc, the support libraries
# are a different version than in the latest stsci_python, so svn_version.py
# is created in the wrong place.  This code makes the old library use the
# new location, so that the svn info is actually installed.
try :
    import pyetc
except ImportError, e :
    # not in a pyetc system
    pass
else :
    # The svn_version file defaults to lib/svn_version.py but we are
    # installing it from lib/pysynphot/svn_version.py - so, here in defsetup
    # we create the file in the correct place.  The new library will want
    # to create it again when we install.  The old library will create it
    # again in the wrong place, but we don't care.
    import stsci.tools.stsci_distutils_hack
    stsci.tools.stsci_distutils_hack.__set_svn_version__( fname="pysynphot/svn_version.py" )

