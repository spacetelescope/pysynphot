from pytools import testutil
import pysynphot as S
import numpy as N
from pysynphot import newetc as etc
from pyraf import iraf
from iraf import stsdas,hst_calib,synphot
import os,time

print os.path.basename(__file__)

class calcspecCase(testutil.FPTestCase):
    def setUp(self):
        self.obsmode=None
        self.spectrum=None
        
    def runpy(self):
        self.name=self.id().replace('__main__',os.path.basename(__file__))
        self.sptest=etc.parse_spec(self.spectrum)
        self.csname=self.name+'.fits'
        self.thresh=0.01
        try:
            os.remove(self.csname)
        except OSError:
            pass

    def testphotlam(self):
        iraf.calcspec(spectrum=self.spectrum,form='photlam',
                      output=self.csname)
        spref=S.FileSpectrum(self.csname)
        rflux=spref.flux
        tflux=self.sptest(spref.wave)
        
        self.adiscrep=abs(1.0-tflux/rflux)
        self.discrep=self.adiscrep.min(),self.adiscrep.max()
        self.failUnless(N.alltrue(self.adiscrep<self.thresh),msg="Worst case %f"%abs(self.adiscrep).max())


    def tearDown(self):
        if self._exc_info() == (None,None,None):
            status='P'
        else:
            status='S'


                              
        f=open(self.name+'.log','w')
        f.write("%s:: Status=%s\n"%(self.name,status))
        f.write("%s:: Time=%s\n"%(self.name,time.asctime()))
        f.write("%s:: Obsmode=%s\n"%(self.name,self.obsmode))
        f.write("%s:: Spectrum=%s\n"%(self.name,self.spectrum))
        try:
            f.write("%s:: Discrepmax=%f\n"%(self.name,self.discrep[1]))
            f.write("%s:: Discrepmin=%f\n"%(self.name,self.discrep[0]))
        except TypeError:
            f.write("%s:: Discrep=%f\n"%(self.name,self.discrep))
        if status != 'P':
            f.write("%s:: Trace=%s\n"%(self.name,str(self._exc_info())))
        f.close()
        
class calcphotCase(calcspecCase):
    def runpy(self):
        self.name=self.id().replace('__main__',__file__)
        self.sptest=etc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.cbname=self.name+'.fits'
        self.thresh=0.01
        try:
            os.remove(self.cbname)
        except OSError:
            pass
        self.discrep=-99
        
    def testphotlam(self):
        pass
                    
    def testthru(self):
        iraf.calcband(obsmode=self.obsmode,output=self.cbname)
        ref=S.FileBandpass(self.cbname)
        rthru=ref.throughput
        rwave=ref.wave
        tthru=self.bp(rwave)
        
        self.adiscrep=abs(1.0-tthru/rthru)
        self.discrep=self.adiscrep.min(),self.adiscrep.max()
        self.failUnless(N.alltrue(self.adiscrep<self.thresh),msg="Worst case %f"%abs(self.adiscrep).max())

        
    def testefflam(self):
        iraf.calcphot(obsmode=self.obsmode,spectrum=self.spectrum,
                      form='photlam', func='efflerg')
        rlam=iraf.calcphot.getParam('calcphot.result',native=1)
        obs=S.Observation(self.sptest,self.bp)
        tlam=obs.efflam()
        self.discrep=abs(1.0-tlam/rlam)
        self.failUnless(self.discrep < self.thresh,msg="Discrep=%f"%self.discrep)

        

class countrateCase(calcspecCase):
    def tearDown(self):
        pass




class SpecSourcerateSpecCase:
    pass
