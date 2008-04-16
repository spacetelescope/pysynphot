import newobs_test 
import sys
import testutil

class C2(newobs_test.NativeCase):
    """C2:Ticket #21, parameterized keywords"""
    def setparms(self):

        self.spectrum = "em(3880.0,10.0,1.0000000168623835E-16,flam)"
        self.obsmode = "acs,wfc1,FR388N#3880"

class C6(newobs_test.NativeCase):
    """C6:Ticket #21, parameterized keywords"""
    def setparms(self):

        self.spectrum = "rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15.0,vegamag)"
        self.obsmode = "acs,hrc,FR388N#3880"

class C7(newobs_test.NativeCase):
    """C7:Ticket #33, no binset associated with observation"""
    def setparms(self):

        self.spectrum = " rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        self.obsmode = "stis,ccd"

class C19(newobs_test.BinnedCase):
    """C19: Unused STIS keyword; graph table will be changed"""
    def setparms(self):

        self.spectrum = "(spec(crcalspec$agk_81d266_stis_001.fits))"
        self.obsmode = "stis,ccd,g230lb,c2375,s52x2"


if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__)
        
