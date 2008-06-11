"""Holds cases suggested by science oversight (Ralph Bohlin)."""

from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase

class S1(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="crcalspec$g191b2b_stisnic_001.fits"
        self.setglobal(__file__)
        self.runpy()

class S2(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="crcalspec$g191b2b_stisnic_001.fits"
        self.setglobal(__file__)
        self.runpy()

class S3(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="crcalspec$g191b2b_stisnic_001.fits"
        self.setglobal(__file__)
        self.runpy()

class S4(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="crcalspec$g191b2b_stisnic_001.fits"
        self.setglobal(__file__)
        self.runpy()

        
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)

