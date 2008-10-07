from pytools import testutil
import sys
import basecase
class thermbackCase1(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase3(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase4(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase5(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase6(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase7(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase8(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase9(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase10(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase11(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase12(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase13(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase14(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase15(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()
class thermbackCase16(basecase.thermbackCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="None"
        self.subset=True
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
#calcspec:0-0=0
#thermback:16-1=15
#calcphot:0-0=0
#countrate:0-0=0
#SpecSourcerateSpec:0-0=0
