from pytools import testutil
import pysynphot as S
import numpy as N
from pysynphot import newetc as etc
from pyraf import iraf
from iraf import stsdas,hst_calib,synphot
import os,time


class calcspecCase(testutil.LogTestCase):
    def setUp(self):
        self.obsmode=None
        self.spectrum=None
        self.runpy()

    def setglobal(self,fname=None):
        if fname is None:
            fname=__file__
        self.propername=self.id() 
        self.name=self.propername.replace('__main__',os.path.basename(fname))
                                          
        self.file=os.path.basename(__file__)
        self.thresh=0.01
        self.discrep=-99
        self.tda={'Obsmode':self.obsmode,
                 'Spectrum':self.spectrum,
                 'Thresh':self.thresh}
        self.tra={}

    def runpy(self):
        self.sptest=etc.parse_spec(self.spectrum)
        self.csname=self.name+'.fits'

        try:
            os.remove(self.csname)
        except OSError:
            pass

    def arraydiff(self,test,ref):
        idx=N.nonzero(ref)
        ans=(test[idx]-ref[idx])/ref[idx]
        return ans


    def testphotlam(self):
        iraf.calcspec(spectrum=self.spectrum,form='photlam',
                      output=self.csname)
        spref=S.FileSpectrum(self.csname)
        rflux=spref.flux
        tflux=self.sptest(spref.wave)
        
        self.adiscrep=self.arraydiff(tflux,rflux)
        self.tra['Discrepmin']=self.adiscrep.min()
        self.tra['Discrepmax']=self.adiscrep.max()
        self.failUnless(N.alltrue(abs(self.adiscrep)<self.thresh),msg="Worst case %f"%abs(self.adiscrep).max())


##     def log(self,status):
##         f=open(self.name+'.log','w')
##         f.write("%s:: Status=%s\n"%(self.name,status))
##         f.write("%s:: Time=%s\n"%(self.name,time.asctime()))
##         f.write("%s:: ta_Obsmode=%s\n"%(self.name,self.obsmode))
##         f.write("%s:: ta_Spectrum=%s\n"%(self.name,self.spectrum))
##         try:
##             f.write("%s:: ra_Discrepmax=%g\n"%(self.name,self.discrep[1]))
##             f.write("%s:: ra_Discrepmin=%g\n"%(self.name,self.discrep[0]))
##         except TypeError:
##             f.write("%s:: ra_Discrep=%g\n"%(self.name,self.discrep))
##         if status != 'P':
##             f.write("%s:: ra_Trace=%s\n"%(self.name,str(self._exc_info())))
##         f.close()
        
class calcphotCase(calcspecCase):
        
    def runpy(self):
        self.sptest=etc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.cbname=self.name+'.fits'
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
        
        self.adiscrep=self.arraydiff(tthru,rthru)
        self.tra['Discrepmin']=self.adiscrep.min()
        self.tra['Discrepmax']=self.adiscrep.max()
        self.failUnless(N.alltrue(abs(self.adiscrep)<self.thresh),msg="Worst case %f"%abs(self.adiscrep).max())

        
    def testefflam(self):
        iraf.calcphot(obsmode=self.obsmode,spectrum=self.spectrum,
                      form='photlam', func='efflerg')
        rlam=iraf.calcphot.getParam('calcphot.result',native=1)
        obs=S.Observation(self.sptest,self.bp)
        tlam=obs.efflam()
        self.discrep=(tlam-rlam)/rlam
        self.tra['Discrep']=self.discrep
        self.failUnless(abs(self.discrep) < self.thresh,msg="Discrep=%f"%self.discrep)

        

class countrateCase(calcspecCase):
    def tearDown(self):
        pass




class SpecSourcerateSpecCase:
    pass
