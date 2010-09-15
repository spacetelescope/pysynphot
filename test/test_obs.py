from __future__ import division
import sys
import os
import math
import pysynphot as S
import numpy as N
from pysynphot import spectrum,observationmode
from pysynphot import observation
from pysynphot import ObsBandpass
from pysynphot import BlackBody

import testutil
import unittest

#QUERY: It is important to note that obs = Obs(sp1 + sp2, bp) 
#       = Obs(sp1,bp1) + Obs(sp2,bp2) if bp1 = bp2, otherwise
#       it would be necessary to incorporate further testing.

class ObservationTestCase(unittest.TestCase):

    """The following set of tests verify that certain operations
       for observations, which were previously not allowed, now
       function as a result of lines being commented in observation.py
       
       testobs4 is the only test that deviates from this description
       in that it verifies that a particular operation that was not
       previously allowed, is still not allowed.
    """

    def setUp(self):
        self.sp=S.BlackBody(4400)
        self.bp=S.ObsBandpass('acs,hrc,f555w')
        self.obs=S.Observation(self.sp,self.bp)
        self.jv=S.ObsBandpass('johnson,v')
        print ' '
        print 'OBSERVATION: ',self.obs
        print ' '
        
    def testobs1(self):
        tst1 = self.obs * 2
        if isinstance(tst1, observation.Observation):
            raise TypeError("tst1 is not a valid observation")
      
    def testobs2(self):
        tst2 = self.obs * self.jv
        if isinstance(tst2, observation.Observation):
            raise TypeError("tst2 is not a valid observation")

    def testobs3(self):
        tst3 = self.obs + self.obs
        if isinstance(tst3, observation.Observation):
            raise TypeError("tst3 is not a valid observation")

    def testobs4(self):
         self.assertRaises(TypeError, self.obs.__mul__, self.obs)
