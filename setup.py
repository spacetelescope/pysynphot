#!/usr/bin/env python
import os
import pkgutil
import sys
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, Extension
from subprocess import check_call, CalledProcessError


if not pkgutil.find_loader('relic'):
    relic_local = os.path.exists('relic')
    relic_submodule = (relic_local and
                       os.path.exists('.gitmodules') and
                       not os.listdir('relic'))
    try:
        if relic_submodule:
            check_call(['git', 'submodule', 'update', '--init', '--recursive'])
        elif not relic_local:
            check_call(['git', 'clone', 'https://github.com/jhunkeler/relic.git'])

        sys.path.insert(1, 'relic')
    except CalledProcessError as e:
        print(e)
        exit(1)

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
    tests_require=['pytest'],
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
    use_2to3=False,
    zip_safe=False
)
