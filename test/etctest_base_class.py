import os
import testutil
from pysynphot import locations
from pysynphot.observation import Observation 
from pysynphot import observationmode #to freeze comptable

#Freeze the version of the comptable so tests are not susceptible to
# updates to CDBS
cmptb_name = os.path.join('mtab','r1j2146sm_tmc.fits')
observationmode.COMPTABLE = observationmode._refTable(cmptb_name)

class ETCTestCase(testutil.FPTestCase):
    """Base class for cases generated from the ETC test listings"""
    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        os.chdir(locations.specdir)
        self.accuracy = 0.00109 
        self.setparms()
        if self.sp is not None:#Skip the base class!!
            self.obs=Observation(self.sp,self.bp)
        
    def setparms(self):
        self.sp=None
        self.bp=None
        self.ref_rate=None
        self.file=None
        self.cmd=None

        
    def tearDown(self):
        os.chdir(self.oldpath)
                                     
    def testrate(self):
        if self.sp is not None:
            self.assertApproxFP(self.obs.countrate(),self.ref_rate,
                                accuracy=self.accuracy)
                
#    def testfile(self):
#        """Need to figure out where to keep reference files"""
#        pass


