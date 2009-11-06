import unittest
import os
import copy

from pysynphot import observationmode, units
from pysynphot.obsbandpass import ObsBandpass
from pysynphot.locations import irafconvert

#Code under test
from pysynphot.observationmode import setref, showref, getref

startup = getref()


class TestSet(unittest.TestCase):

    def setUp(self):
        setref()
        self.ref='mtab$foobar.fits'
        self.ttype='graphtable'
        setref(graphtable=self.ref)
        
    def testset(self):
        tst=getref()[self.ttype]
        self.assertEquals(irafconvert(self.ref),
                          irafconvert(tst),
                          "(ref,tst)=(%s,%s)"%(self.ref,tst)
                          )
        
    def testget(self):
        tst = getref()
        ref = copy.deepcopy(startup)
        ref[self.ttype]=irafconvert(self.ref)
        self.assertEqual(ref,tst,"(ref,test):\n (%s\n%s)"%(ref,tst))
        
    def testreset(self):
        setref()
        tst=getref()
        self.assertEqual(startup,tst,
                         "(ref,tst)=(%s,%s)"%(startup,tst)
                         )

class TestComp(TestSet):
    def setUp(self):
        setref()
        self.ref='mtab$foobar.fits'
        self.ttype='comptable'
        setref(comptable=self.ref)

class TestArea(TestSet):
    def setUp(self):
        setref()
        self.ttype='area'
        self.ref=12345.6
        setref(area=self.ref)

    def testset(self):
        tst=getref()['area']
        self.assertEquals(self.ref, tst,
                          "(ref,tst)=(%s,%s)"%(self.ref,tst)
                          )
    def testget(self):
        tst = getref()
        ref = dict()
        ref.update(startup)
        ref[self.ttype]=self.ref
        self.assertEqual(ref,tst,"(ref,test):\n (%s\n%s)"%(ref,tst))



class TestMulti(unittest.TestCase):
    def setUp(self):
        setref()
        self.gref=irafconvert('mtab$t2605492m_tmg.fits')
        self.cref=irafconvert('mtab$t260548pm_tmc.fits')
        setref(graphtable=self.gref,
               comptable =self.cref)
        self.pick=getref()
        
    def testgraph(self):

        self.assertEqual(self.pick['graphtable'],
                         self.gref)

    def testcomp(self):
        self.assertEqual(self.cref,
                         self.pick['comptable'])

    def testbp(self):
        bp=ObsBandpass('acs,hrc,f555w')
        self.assertEqual(self.gref,bp.obsmode.gtname)
        self.assertEqual(self.cref,bp.obsmode.ctname)

    def testreset(self):
        setref()
        tst=getref()
        self.assertEqual(startup, tst)
        
                                          

    
    
