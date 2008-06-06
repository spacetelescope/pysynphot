from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase

class calcspecCase1(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase3(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase4(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase5(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase6(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase7(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase8(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase9(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase10(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase11(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase12(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase13(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase14(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase15(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase16(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase17(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase18(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase19(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase20(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase21(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase23(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase24(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase25(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase26(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase28(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase29(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase30(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase33(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase34(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase35(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase36(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase38(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase39(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase40(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase41(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase42(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase43(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase44(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase45(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase46(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase47(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase48(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase49(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase50(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase51(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase52(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase53(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase54(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase55(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase56(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase57(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase58(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase59(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase60(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase61(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase62(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase63(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase64(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase65(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase66(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase67(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase68(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase69(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase70(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase71(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase72(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase73(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase74(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase75(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase76(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase77(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase78(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase79(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase80(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase81(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase82(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase83(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase84(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase85(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase86(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase87(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase88(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase89(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase90(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase91(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase92(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase93(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase94(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase95(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase96(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase97(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase98(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase99(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase100(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase101(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase102(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase103(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase104(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase105(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase106(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase107(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase108(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase109(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase110(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase111(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase112(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase113(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase114(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase115(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase116(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase117(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase118(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase119(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase120(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase121(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase122(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase123(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase124(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase125(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase126(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase127(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase128(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal2),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase129(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase130(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase131(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase132(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal2)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_7.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_8.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal2)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_13.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal2)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase133(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase134(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase135(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase136(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase137(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase138(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase139(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase140(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase141(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
# calcspec:141
# calcphot:10
# countrate:10
# SpecSourcerateSpec:36
