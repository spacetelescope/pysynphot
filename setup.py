#!/usr/bin/env python
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension('pysynphot.pysynphot_utils',
                  glob('pysynphot/src/*.c'),
                  include_dirs=[np_include()],
                  optional=True)
    ],
    zip_safe=False
)
