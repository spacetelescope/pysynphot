#!/usr/bin/env python
import sys
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, Extension

# Use submodule
sys.path.insert(1, 'relic')
import relic.release  # noqa

version = relic.release.get_info()
relic.release.write_template(version, 'pysynphot')

setup(
    name='pysynphot',
    version=version.pep386,
    author=('Vicki Laidler, Pey Lian Lim, Matt Davis, Robert Jedrzejewski, '
            'Ivo Busko'),
    author_email='help@stsci.edu',
    description='Python Synthetic Photometry Utilities',
    url='https://github.com/spacetelescope/pysynphot',
    license='BSD',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'astropy',
        'numpy'
    ],
    tests_require=['nose'],
    packages=['pysynphot',
              'pysynphot.test',
              'pysynphot.test.from_commissioning',
              'pysynphot.test.from_commissioning.acs',
              'pysynphot.test.from_commissioning.nicmos',
              'pysynphot.test.from_commissioning.stis',
              'pysynphot.test.from_commissioning.wfc3_ir',
              'pysynphot.test.from_commissioning.wfc3_uvis1',
              'pysynphot.test.from_commissioning.wfc3_uvis2'],
    package_dir={'pysynphot': 'pysynphot'},
    package_data={'pysynphot': ['data/generic/*', 'data/wavecat/*'],
                  'pysynphot.test': ['data/*.*', 'data/cdbs/extinction/*',
                                     'data/cdbs/jref/*', 'data/cdbs/mtab/*'],
                  'pysynphot.test.from_commissioning': ['data/*'],
                  'pysynphot.test.from_commissioning.stis': ['*ref.fits']},
    ext_modules=[
        Extension('pysynphot.pysynphot_utils',
                  glob('pysynphot/src/*.c'),
                  include_dirs=[np_include()],
                  optional=True)
    ],
    use_2to3=False,
    zip_safe=False
)
