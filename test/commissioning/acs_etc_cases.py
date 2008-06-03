from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase

class calcphotCase1(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(calcphotCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(calcphotCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase177(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase178(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase179(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase180(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase181(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase182(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase183(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase184(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase185(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase186(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase187(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase188(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase189(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase190(calcphotCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase3(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase4(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase5(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase6(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase7(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase8(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase9(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase10(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase11(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase12(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase13(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase14(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase15(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase16(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase17(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase18(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase19(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase20(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase21(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase23(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase24(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase25(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase26(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase28(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase29(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase30(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase33(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase34(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase35(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase36(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase38(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase39(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase40(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(countrateCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase176(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase177(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase178(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase179(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase180(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase181(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase182(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase183(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase184(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase185(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase186(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase187(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase188(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        self.setglobal(__file__)
        self.runpy()
class countrateCase189(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase190(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="em(4000.0,10.0,1.0E-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
# calcspec:40
# calcphot:190
# countrate:190
# SpecSourcerateSpec:35
