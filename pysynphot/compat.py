"""Module to handle compatibility with dependencies like Astropy."""
from __future__ import absolute_import, division, print_function

import astropy
from astropy.utils.introspection import minversion

__all__ = ['ASTROPY_LT_1_3']

ASTROPY_LT_1_3 = not minversion(astropy, '1.3')
