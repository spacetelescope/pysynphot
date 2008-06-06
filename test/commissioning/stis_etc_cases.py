from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase

class countrateCase1(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase3(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase4(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase5(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase6(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase7(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase8(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase9(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase10(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase11(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase12(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase13(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase14(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase15(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase16(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase17(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase18(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase19(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase20(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase21(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase23(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(calcphotCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(countrateCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase24(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase25(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase26(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(calcphotCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(countrateCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(calcphotCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(countrateCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mama"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230m,c2818"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230m,c2818,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140m,c1567"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140m,c1567,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism,s52x2"
        self.spectrum="spec(/usr/stsci/APT/userFiles/HS20270651.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140h,c1416"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140h,c1416,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism,s52x01"
        self.spectrum="spec(/usr/stsci/APT/userFiles/HS20270651.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750m,c7283"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750m,c7283,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230mb,c1995"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230mb,c1995,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),12.77,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),0.03),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase37(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),1.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase38(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,v),18,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase39(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),band(johnson,v),10.516,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase28(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase40(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10.516,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase29(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(50000)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase41(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(bb(50000),band(johnson,v),10.516,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase42(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10.516,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase30(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,0.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase43(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(pl(4000.0,0.0,flam),band(johnson,v),10.516,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase44(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),10.516,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase45(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),box(2000.0,1.0),1.0e-12,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase46(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase47(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,gal1),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase33(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase48(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,smc),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase34(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase49(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,lmc),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase35(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase50(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,xgal),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase36(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase51(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),6,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase52(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase38(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase53(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase39(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase54(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase40(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase55(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase56(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase57(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x01"
        self.spectrum="rn(spec(ngc1068_template.fits),band(johnson,v),9,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase58(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase59(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase41(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase60(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase42(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase61(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase43(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase62(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),27.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase44(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase63(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase45(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase64(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase65(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase46(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase66(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase47(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase67(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase68(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase48(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase69(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase49(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase50(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase51(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase70(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase52(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase71(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase53(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase72(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase54(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase73(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase55(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase74(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase56(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase75(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase57(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase76(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase77(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase58(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase59(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase78(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase60(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase79(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase61(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase80(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase81(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase82(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase83(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194,s52x2"
        self.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase84(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase85(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        self.spectrum="em(1425.0,1.0,1.0E-10,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase86(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        self.spectrum="em(1425.0,0.043487548828125,1.0E-10,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase87(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),band(johnson,v),10.516,vegamag)"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
# calcspec:61
# calcphot:63
# countrate:62
# SpecSourcerateSpec:87
