"""Contains ParentCase used by commissioning_cases.CommCase*.
Defines all the common setup and testing.
"""
from pytools import testutil
import numpy as N
import pysynphot as S
from pysynphot import etc

class ParentCase(object):
    #@classmethod
    def setUp(self):
        """Always overridden by the child cases, but let's put some
        real values in here to test with"""
        self.obsmode=None
        self.spectrum=None
        self.bp=None
        self.sp=None
        self.obs=None
        self.setup2()
        
    def setup2(self):
        #Do the common setup here.
        print "hi, setup2"
        self.sigthresh = 0.01
        self.thresh = 0.01
        self.tda=dict(obsmode=self.obsmode,
                      spectrum=self.spectrum,
                      thresh=self.thresh,
                      sigthresh=self.sigthresh)
        self.tra=dict()
        
        if self.obsmode != "None":
            self.bp=S.ObsBandpass(self.obsmode)
            self.bp.writefits(self.fname%'bp', clobber=True,
                              trimzero=False)
            self.tra['bp']=self.bp.name
        else:
            self.bp = None

            
        if self.spectrum != "None":
            self.sp=etc.parse_spec(self.spectrum)
            self.sp.writefits(self.fname%'sp', clobber=True,
                              trimzero=False)
            self.tra['sp']=self.sp.name
        else:
            self.sp = None

            
        if "None" not in (self.obsmode, self.spectrum):
            self.obs = S.Observation(self.sp, self.bp)
            self.obs.convert('counts')
            x = dict(PSCNTRAT = (self.obs.countrate(),'countrate'),
                     PSEFFLAM = (self.obs.efflam(),'efflam'))
            self.obs.writefits(self.fname%'obs', hkeys=x, clobber=True,
                               trimzero=False)
            self.tra['obs']=self.obs.name
            self.tra.update(x)
        else:
            self.obs = None

    def testthru(self):
        if self.bp:
            self.bpref = S.FileBandpass((self.fname%'bp').replace('.fits','_ref.fits'))
            self.arraytest(self.bpref.throughput, self.bp.throughput)

    def testflux(self):
        if self.sp:
            self.spref = S.FileSpectrum((self.fname%'sp').replace('.fits','_ref.fits'))
            self.arraytest(self.spref.flux, self.sp.flux)

    def testcounts(self):
        if self.obs:
            self.obsref = S.FileSpectrum((self.fname%'obs').replace('.fits','_ref.fits'))
            self.arraytest(self.obsref.flux, self.obs.binflux)

    def testcntrate(self):
        if self.obs:
            self.obsref = S.FileSpectrum((self.fname%'obs').replace('.fits','_ref.fits'))
            self.tcompare(self.obsref.fheader['PSCNTRAT'],
                          self.obs.countrate())

    def testefflam(self):
        if self.obs:
            self.obsref = S.FileSpectrum((self.fname%'obs').replace('.fits','_ref.fits'))
            self.tcompare(self.obsref.fheader['PSEFFLAM'],
                          self.obs.efflam())

    #TODO: add thermal stuff

#Helper methods for arrays
    def count_outliers(self,Nsigma=3):
        mean=self.adiscrep.mean()
        std=self.adiscrep.std()
        outliers=N.where(abs(self.adiscrep) > mean + Nsigma*std)
        return len(outliers[0])

    def arraysigtest(self,ref,test):
        #Raise an error if the arrays are not the same size
        if test.shape != ref.shape:
            raise ValueError("Array size mismatch")
        tt=test[2:-2]
        rr=ref[2:-2]
        #Identify the significant elements
        tidx=N.where(tt>(self.sigthresh*tt.max()))[0]
        ridx=N.where(rr>(self.sigthresh*rr.max()))[0]
        #Set a flag if they're not the same set
        if not (N.alltrue(tidx == ridx)):
            self.tra['SigElemDiscrep']=True
            tidx=ridx

        #Now compare only the significant elements.
        #We no longer need to exclude points with zero value, because
        #those points were already excluded as insignificant.
        self.arraytest(tt[ridx],rr[ridx])

    def arraydiff(self,test,ref):
        idx=N.nonzero(ref)
        ans=(test[idx]-ref[idx])/ref[idx]
        return ans

    def arraytest(self,ref,test):
        #Exclude the endpoints where the gradient is very steep
        self.adiscrep=self.arraydiff(test,ref)#[2:-2]
        count=N.where(abs(self.adiscrep)>self.thresh)[0].size
        try:
            self.tra['Discrepfrac']=float(count)/self.adiscrep.size
            self.tra['Discrepmin']=self.adiscrep.min()
            self.tra['Discrepmax']=self.adiscrep.max()
            self.tra['Discrepmean']=self.adiscrep.mean()
            self.tra['Discrepstd']=self.adiscrep.std()
            self.tra['Outliers']=self.count_outliers(5)
            self.failUnless(N.alltrue(abs(self.adiscrep)<self.thresh),
                            msg="Worst case %f"%abs(self.adiscrep).max())
        except ZeroDivisionError:
            self.tra['Discrepfrac']=0.0
            self.tra['Discrepmin']=0.0
            self.tra['Discrepmax']=0.0

#Helper method for scalar comparison
    def tcompare(self,rval,tval):
        if rval != 0:
            self.discrep=(tval-rval)/rval
        else:
            self.discrep=tval-rval
        self.tra['Discrep']=self.discrep
        self.tra['ref']=rval
        self.tra['tst']=tval
        self.failUnless(abs(self.discrep) < self.thresh,
                        msg="Discrep=%f"%self.discrep)

    def failUnless(self, expr, msg=None):
        #Copied from unittest.TestCase
        """Fail the test unless the expression is true."""
        if not expr: raise self.failureException, msg


class Testing(ParentCase):
    #@classmethod
    def setUp(self):
        self.obsmode="stis,e230h,i1913"
        self.spectrum="bb(30000)"
        self.fname="T1_%s.fits"
        self.setup2()
