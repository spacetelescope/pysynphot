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
    'version'       :      	"0.9a",
    'description'   :       'Python Synthetic Photometry Utilities',
    'fullname'      :       'AstroLib Pysynphot',
    'license'       :       'BSD',
    'author'        :     	"Robert Jedrzejewski, Ivo Busko, Vicki Laidler, Matt Davis",
    'author_email'  :      	"help@stsci.edu",
    'url'           :       "http://projects.scipy.org/astropy/astrolib",
    'platforms'     :      	["Linux","Solaris","Mac OS X", "Win"],
    'requires'      :       ['pyfits','numpy'],
    'data_files'    :     	[ ( pkg+'/data', [ 'data/generic/*', 'data/wavecat/*' ] ) ],
    'ext_modules'   :       ext,
    'cmdclass'      :       {'build_ext':build_ext},
    'package_dir'   :       { 'pysynphot' : 'lib/pysynphot' },

}

