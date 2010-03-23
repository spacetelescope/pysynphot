from __future__ import division
from unittest import TestCase
import os

try:
    from pysynphot.graphtab import GraphTable
except ImportError:
    print "Warning, the tests won't run; GraphTabl not yet implemented"

def make_tmg(strdata,tmgname):
    """Helper function"""
    import pyfits
    out=open(tmgname,'w')
    out.write(strdata)
    out.flush()
    out.close()
##     tbhdu=pyfits.tcreate('data.txt',cdfile='cdfile.txt',hfile='h1.txt')
##     tbhdu.writeto(tmgname, clobber=True)
      
    
class GraphCase(TestCase):
    #Drat, put compname first like in real table
    old_simple1="""acs 1 20 clear clear
cos 1 20 clear clear
default 1 100 clear clear
noota 20 30 clear clear
default 20 30 hst_ota clear
ota 20 30 hst_ota clear
acs 30 10000 clear clear
cos 30 11000 clear clear
sbc 10000 10199 clear clear
hrc 10000 10150 clear clear
wfc1 10000 10100 clear clear
default 10100 10101 clear clear
default 10101 10130 acs_wfc_im123 clear
f606w 10130 10140 acs_f606w clear
f550m 10130 10140 acs_f550m clear
f555w 10130 10140 acs_f555w clear
default 10140 10300 clear clear
wfc1 10300 10310 acs_wfc_ebe_win12f clear
default 10310 10320 acs_wfc_ccd1 clear
mjd# 10310 10320 acs_wfc_ccd1_mjd clear
"""
    simple1="""clear  acs  1  20  clear
clear  cos  1  20  clear
clear  default  1  100  clear
clear  noota  20  30  clear
hst_ota  default  20  30  clear
hst_ota  ota  20  30  clear
clear  acs  30  10000  clear
clear  cos  30  11000  clear
clear  sbc  10000  10199  clear
clear  hrc  10000  10150  clear
clear  wfc1  10000  10100  clear
clear  default  10100  10101  clear
acs_wfc_im123  default  10101  10130  clear
acs_f606w  f606w  10130  10140  clear
acs_f550m  f550m  10130  10140  clear
acs_f555w  f555w  10130  10140  clear
clear  default  10140  10300  clear
acs_wfc_ebe_win12f  wfc1  10300  10310  clear
acs_wfc_ccd1  default  10310  10320  clear
acs_wfc_ccd1_mjd  mjd#  10310  10320  clear"""

    def setUp(self):
        self.fname='/tmp/simple1.tmg'
        make_tmg(self.simple1, self.fname)
        self.G=GraphTable(self.fname)

    def tearDown(self):
        os.unlink(self.fname)
        #os.unlink('data.txt')
        
    def test1(self):
        self.instring='acs,wfc1,f555w'
        self.ref=['hst_ota',
                  'acs_wfc_im123',
                  'acs_f555w',
                  'acs_wfc_ebe_win12f',
                  'acs_wfc_ccd1']
        tst, ignoretherm =self.G.traverse(self.instring)
        self.assertEqual(self.ref,tst)

    def testparam(self):
        self.instring='acs,wfc1,f606w,mjd#70123'
        self.ref=['hst_ota',
                  'acs_wfc_im123',
                  'acs_f606w',
                  'acs_wfc_ebe_win12f',
                  'acs_wfc_ccd1_mjd']
        test, ignoretherm =self.G.traverse(self.instring)
        self.assertEqual(self.ref,test)

    def testnext(self):
        self.instring="acs"
        self.ref=set(['hrc','wfc1'])
        tst=self.G.getnext(self.instring)

    def testunused(self):
        self.instring="cos,foo"
        self.assertRaises(ValueError,
                          self.G.traverse,
                          self.instring)


    def testincomplete(self):
        self.instring="acs"
        self.assertRaises(ValueError,
                          self.G.traverse,
                          self.instring)
                          

    def testambiguous(self):
        self.instring="acs,wfc1,f550m,f555w"
        self.assertRaises(ValueError,
                          self.G.traverse,
                          self.instring)
                          

    def testloopcheck(self):
        self.assert_(self.G._loopcheck())

    def testascending(self):
        self.assert_(self.G._ordercheck())

    def testreachable(self):
        self.assert_(self.G._orphancheck())

    def testvalidate(self):
        #Performs all the earlier checks
        self.assert_(self.G.validate())

    def testallmodes(self):
        self.ref=set(['cos',
                      'acs, hrc',
                      'acs, wfc1, f606w',
                      'acs, wfc1, f550m',
                      'acs, wfc1, f555w'])
        tst=self.G.allmodes()
        self.assertEqual(self.ref,tst)
                        

class ThermalCase(GraphCase):
    simpletherm="""something with thermal modes"""

    def setUp(self):
        self.fname='simpletherm_tmg.fits'
        self.G=GraphTable(self.fname)

    def test_consistent(self):
        self.assert_(self.G._thermback())

    def test_opt_therm(self):
        self.instring='nicmos,3,f222m'
        #Is this the right UI? Or should traverse always return
        #an (opt,thm) tuple?
        opt=self.G.traverse(self.instring)
        thm=self.G.traverse(self.instring,thermal=True)
        #The thermal path must be a superset of the optical path,
        #though it need not be a strict superset.
        self.assert_(set(thm)>=set(opt))

    def test_therm(self):
        self.instring='nicmos,2,f187n'
        self.ref='tbd'
        tst=self.G.traverse(self.instring,thermal=True)
        self.assertEqual(self.ref,tst)

    def test_temp(self):
        #Do we really want to keep this interface?
        self.instring='nicmos,3,f222m,primary#320'
        self.ref='tbd'
        tst=self.G.traverse(self.instring,thermal=True)
        #A better interface might be to specify temperature overrides
        #when calling the method
        #bp.thermback(primary=320)

class BadGraph(TestCase):
    badgraph="""something with loops and orphans and so on"""
    def setUp(self):
        self.fname='badgraph_tmg.fits'
        self.G=GraphTable(self.fname)

class MissingGraph(BadGraph):
    missinggraph="""something with some missing columns"""
    def setUp(self):
        self.fname='missinggraph_tmg.fits'

    def testconstructor(self):
        self.assertRaises(GraphTable,
                          self.fname,
                          ValueError) #or some other error?)
