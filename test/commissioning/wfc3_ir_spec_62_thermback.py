from pytools import testutil
import sys
import basecase 

class thermbackCase1(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="None"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase2(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="None"
        self.setglobal(__file__)
        self.runpy()
class thermbackCase3(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="None"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
# calcspec:0
# thermback:3
# calcphot:0
# countrate:0
# SpecSourcerateSpec:0
