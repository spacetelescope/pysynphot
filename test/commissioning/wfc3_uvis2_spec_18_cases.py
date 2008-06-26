from pytools import testutil
import sys
import basecase
class calcspecCase1(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase3(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase4(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase5(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase6(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase7(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase8(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase9(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase10(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase11(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase12(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase13(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase14(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase15(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase16(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase17(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase18(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase19(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase20(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase21(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase23(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase24(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase25(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase26(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase28(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase29(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase30(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase33(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase34(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase35(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase36(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase38(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase39(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase40(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase41(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase42(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase43(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase44(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase45(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase46(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase47(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase48(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase49(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase50(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase51(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase52(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase53(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase54(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase55(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase56(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase57(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase58(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase59(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase60(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase61(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase62(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase63(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase64(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase65(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase66(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase67(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase68(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase69(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase70(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase71(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase72(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase73(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase74(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase75(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase76(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase77(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase78(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase79(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase80(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase81(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase82(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase83(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase84(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase85(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase86(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase87(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase88(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase89(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase90(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase91(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase92(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase93(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase94(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase95(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase96(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase97(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase98(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase99(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase100(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase101(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase102(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase103(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase104(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase105(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase106(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase107(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase108(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase109(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase110(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase111(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase112(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase113(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase114(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase115(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase116(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase117(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase118(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase119(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase120(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase121(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase122(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase123(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase124(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase125(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase126(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase127(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase128(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase129(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase130(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase131(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase132(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_7.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_8.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_13.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase133(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase134(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase135(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase136(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase137(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase138(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase139(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase140(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(basecase.SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase141(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(basecase.SpecSourcerateSpecCase):
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
# thermback:0
# calcphot:10
# countrate:10
# SpecSourcerateSpec:36
