from pytools import testutil
import pysynphot as S
import numpy as N
from pysynphot import newetc as etc
from pyraf import iraf
from iraf import stsdas,hst_calib,synphot
import os,time
from pysynphot.wavetable import wavetable as Wavecat


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

    def run_calcspec(self,obsmode,spstring,form,output=None,binset=False):
        if binset:
            wavetab=Wavecat[self.obsmode]
        else:
            wavetab=""

        if obsmode in (None,"None"):
            spec=spstring
        else:
            spec="band(%s)*(%s)"%(obsmode,spstring)

        iraf.calcspec(spectrum=spec,
                      output=output,
                      form=form,wavetab=wavetab)

    def run_countrate(self,form,output=None):
        if output is None:
            output=""
        iraf.countrate(spectrum=self.spectrum,magnitude="",
                       instrument=self.obsmode,
                       output=output,form=form)

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

    def arraytest(self,test,ref):
        self.adiscrep=self.arraydiff(test,ref)
        self.tra['Discrepmin']=self.adiscrep.min()
        self.tra['Discrepmax']=self.adiscrep.max()
        self.failUnless(N.alltrue(abs(self.adiscrep)<self.thresh),msg="Worst case %f"%abs(self.adiscrep).max())


    def testspecphotlam(self):
        self.run_calcspec(None,self.spectrum,'photlam',self.csname)
        spref=S.FileSpectrum(self.csname)
        self.sptest.convert('photlam')
        rflux=spref.flux
        tflux=self.sptest(spref.wave)
        
        self.arraytest(tflux,rflux)
        
class calcphotCase(calcspecCase):
        
    def runpy(self):
        self.sptest=etc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.cbname=self.name+'.fits'
        self.csname=self.name+'_cs.fits'
        for fname in (self.cbname, self.csname):
            try:
                os.remove(fname)
            except OSError:
                pass
        self.discrep=-99
        

     
                    
    def testthru(self):
        iraf.calcband(obsmode=self.obsmode,output=self.cbname)
        ref=S.FileBandpass(self.cbname)
        rthru=ref.throughput
        rwave=ref.wave
        tthru=self.bp(rwave)
        
        self.arraytest(tthru,rthru)

        
    def testefflam(self):
        iraf.calcphot(obsmode=self.obsmode,spectrum=self.spectrum,
                      form='photlam', func='efflerg')
        rlam=iraf.calcphot.getParam('calcphot.result',native=1)
        obs=S.Observation(self.sptest,self.bp)
        tlam=obs.efflam()
        self.discrep=(tlam-rlam)/rlam
        self.tra['Discrep']=self.discrep
        self.failUnless(abs(self.discrep) < self.thresh,msg="Discrep=%f"%self.discrep)

        

class countrateCase(calcphotCase):
    def runpy(self):
        self.sptest=etc.parse_spec(self.spectrum)
        self.bp=S.ObsBandpass(self.obsmode)
        self.csname=self.name+'_cs.fits'
        self.crname=self.name+'_cr.fits'
        self.cbname=self.name+'.fits'
        for fname in (self.cbname, self.csname, self.crname):
            try:
                os.remove(fname)
            except OSError:
                pass

    def testcsphotlam(self):
        obs=S.Observation(self.sptest,self.bp)
        obs.convert('photlam')
        self.run_calcspec(self.obsmode,self.spectrum,
                          'photlam',self.csname,binset=True)
        spref=S.FileSpectrum(self.csname)
        rflux=spref.flux
        tflux=obs.binflux
        self.arraytest(tflux,rflux)

    def testcscounts(self):
        obs=S.Observation(self.sptest,self.bp)
        obs.convert('counts')
        self.run_calcspec(self.obsmode,self.spectrum,
                          'counts',self.csname.replace('.fits','_counts.fits'),
                          binset=True)
        spref=S.FileSpectrum(self.csname.replace('.fits','_counts.fits'))
        rflux=spref.flux
        tflux=obs.binflux
        self.arraytest(tflux,rflux)
 
    def testcrphotlam(self):
        obs=S.Observation(self.sptest,self.bp)
        obs.convert('photlam')
        self.run_countrate('photlam',self.crname.replace('.fits','_cr.fits'))
        spref=S.FileSpectrum(self.crname.replace('.fits','_cr.fits'))
        rflux=spref.flux
        tflux=obs.binflux
        self.arraytest(tflux,rflux)

    def testcrcounts(self):
        obs=S.Observation(self.sptest,self.bp)
        obs.convert('counts')
        self.run_countrate('counts',self.crname.replace('.fits','_counts.fits'))
        spref=S.FileSpectrum(self.crname.replace('.fits','_counts.fits'))
        rflux=spref.flux
        tflux=obs.binflux
        self.arraytest(tflux,rflux)

    def testcountrate(self):
        obs=S.Observation(self.sptest,self.bp)
        self.run_countrate('counts')
        rval=iraf.countrate.getParam('flux_tot',native=1)
        tval=obs.countrate()
        self.discrep=(tval-rval)/rval
        self.tra['Discrep']=self.discrep
        self.failUnless(abs(self.discrep) < self.thresh,msg="Discrep=%f"%self.discrep)
      
class SpecSourcerateSpecCase:
    pass
