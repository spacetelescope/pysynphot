from __future__ import division
from unittest import TestCase
try:
    from pysynphot.comptab import Comptab
except ImportError:
    print "not implemented yet"

class CompCase(TestCase):
    def setUp(self):
        self.fname='something'
        self.C=Comptab(self.fname)

    def test_nodups(self):
        #Test for duplicate filenames.
        #Duplicate compnames will be caught at construction
        self.assert_(self.C._dupcheck())
        
    def testvalid(self):
        #C is dictionary-like
        self.assert_(self.C.validate())

class BadComp(TestCase):
    def setUp(self):
        self.fname='somethingelse'

    def testdupcomp(self):
        self.assertRaises(Comptab,
                          self.fname,
                          KeyError)

        
