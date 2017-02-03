"""Very preliminary tests of some bandpar functionality.
These answers were computed with pysynphot and eyeballed against
synphot answers. These tests are only to establish that the
functionality doesn't *break*. More rigorous tests should be added."""
from __future__ import division

import os
import pysynphot as S
import testutil

orig_graphtable = S.refs.getref()['graphtable']
orig_comptable = S.refs.getref()['comptable']


def setUpModule():
    #Answers computed using specified tables
    S.setref(graphtable='/grp/hst/cdbs/mtab/OLD_FILES/0661437lm_tmg.fits',
             comptable='/grp/hst/cdbs/mtab/OLD_FILES/0661429jm_tmc.fits')


def tearDownModule():
    S.setref(graphtable=orig_graphtable, comptable=orig_comptable)


class JohnsonV(testutil.FPTestCase):
    def setUp(self):
        self.bp = S.FileBandpass('crnonhstcomp$johnson_v_004_syn.fits')
        self.r_avgwave=5490.5552003639823
        self.r_efficiency=0.15678915809503616
        self.r_equivwidth=857.34999515116215
        self.r_rectwidth=857.34999515116215
        self.r_rmswidth=357.13065617707804

    def testavg(self):
        tst=self.bp.avgwave()
        self.assertApproxFP(self.r_avgwave, tst)

    def testeff(self):
        tst=self.bp.efficiency()
        self.assertApproxFP(self.r_efficiency, tst)

    def testequiv(self):
        tst=self.bp.equivwidth()
        self.assertApproxFP(self.r_equivwidth, tst)

    def testrect(self):
        tst=self.bp.rectwidth()
        self.assertApproxFP(self.r_rectwidth, tst)

    def testrms(self):
        tst=self.bp.rmswidth()
        self.assertApproxFP(self.r_rmswidth, tst)


class NarrowWfc3(JohnsonV):
    def setUp(self):
        self.tda=dict(obsmode='wfc3,uvis1,fq672n')
        self.bp=S.ObsBandpass(self.tda['obsmode'])
        self.r_avgwave=6716.6253925114133
        self.r_efficiency=0.00071479633888800855
        self.r_equivwidth=4.8006812790841318
        self.r_rectwidth=19.373016584072371
        self.r_rmswidth=46.46729888277223
