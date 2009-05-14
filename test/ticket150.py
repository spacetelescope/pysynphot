import pysynphot as S
from pysynphot.observation import Observation
from pysynphot import etc
import os, sys
import testutil
import numpy as N

from pysynphot import locations, observationmode


#Freeze the version of the comptable so tests are not susceptible to
# updates to CDBS
cmptb_name = os.path.join('mtab','t260548pm_tmc.fits')
observationmode.COMPTABLE = observationmode._refTable(cmptb_name)
print "%s:"%os.path.basename(__file__)
print "  Tests are being run with %s"%observationmode.COMPTABLE

#Also set the version of Vega for similar reasons
locations.VegaFile=os.path.join('crcalspec',
                                'alpha_lyr_stis_003.fits')
print "Using Vega spectrum: %s"%locations.VegaFile

class RenormOverlap(testutil.FPTestCase):
    """Tests for strict rejection."""
    def setUp(self):
        #(re)discovery case: stis_rn_cases/stisC94
        self.sp=S.FileSpectrum('$PYSYN_CDBS/grid/kc96/starb2_template.fits')
        self.bp=S.ObsBandpass('cos,fuv,g130m,c1300')
        self.cmd='rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)'
        self.ref=0.00718543 #expected renorm factor
        
    def testraise(self):
        self.assertRaises(ValueError,
                          self.sp.renorm,
                          16.0,'stmag',self.bp)

    def testforce(self):
        sp2=self.sp.renorm(16.0,'stmag',self.bp,force=True)
        ratio=sp2.flux/self.sp.flux
        self.failUnless(N.all(1-abs(ratio/self.ref)<0.0001))

    def testparse(self):
        sp2=S.etc.parse_spec(self.cmd)
        ratio=sp2.flux/self.sp.flux
        self.failUnless(N.all(1-abs(ratio/self.ref)<0.0001))

    def testfull(self):
        jv=S.ObsBandpass('johnson,v')
        try:
            sp2=self.sp.renorm(17.0,'abmag',jv)
        except ValueError,e:
            self.fail(e.message)
      

                       
class SmarterOverlap(RenormOverlap):
    #If 99% of throughput on spectrum, go ahead but print warning
    def testsmart(self):
        #does not yet test warning
        acs=S.ObsBandpass('acs,hrc,f555w')
        try:
            sp2=self.sp.renorm(17.0,'abmag',acs)
        except ValueError,e:
            self.fail(e.message)
