#!/usr/bin/env python

# We use the local copy of stsci_distutils_hack, unless
# the user asks for the stpytools version

import os
try:
    import stsci.tools.stsci_distutils_hack as H
except ImportError, e:
    import stsci_distutils_hack as H
H.run()


