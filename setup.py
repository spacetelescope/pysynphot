#!/usr/bin/env python
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, Extension

setup(
    name='pysynphot',
    use_scm_version={'write_to': 'pysynphot/version.py'},
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
    setup_requires=['setuptools_scm'],
    python_requires='>=3.6',
    install_requires=[
        'astropy',
        'numpy',
        'beautifulsoup4',
        'six'
    ],
    tests_require=['pytest', 'pytest-remotedata'],
    packages=['pysynphot',
              'pysynphot.test'],
    package_dir={'pysynphot': 'pysynphot'},
    package_data={'pysynphot': ['data/generic/*', 'data/wavecat/*'],
                  'pysynphot.test': ['data/*.*', 'data/cdbs/extinction/*',
                                     'data/cdbs/jref/*', 'data/cdbs/mtab/*']},
    ext_modules=[
        Extension('pysynphot.pysynphot_utils',
                  glob('pysynphot/src/*.c'),
                  include_dirs=[np_include()],
                  optional=True)
    ],
    zip_safe=False
)
