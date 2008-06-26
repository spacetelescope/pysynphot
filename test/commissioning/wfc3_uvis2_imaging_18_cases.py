from pytools import testutil
import sys
import basecase
class calcspecCase1(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase3(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
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
class calcphotCase6(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase7(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase9(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase12(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase12(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase17(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase15(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase18(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase21(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase24(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase27(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase42(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase30(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase47(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase33(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase52(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase36(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase57(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase39(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase62(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase42(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase67(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase45(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase72(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase48(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase77(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase51(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase82(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase54(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase87(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase57(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase92(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase60(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase97(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase63(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase102(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase103(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
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
class calcphotCase66(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase107(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase69(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase112(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase72(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase117(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase75(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase122(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase78(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase127(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase128(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase129(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase130(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase131(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase132(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase133(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase134(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase135(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase136(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase137(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase138(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase139(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase140(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase141(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase142(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase143(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase144(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase145(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase146(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase147(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase148(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase149(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase150(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase151(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase152(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase153(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase154(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase155(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase156(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase157(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase158(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase159(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase160(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase161(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase162(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase163(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase164(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase165(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase166(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase167(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase168(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase169(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase170(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase171(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase172(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase173(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase174(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase175(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase176(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase177(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase178(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase179(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase180(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase181(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase182(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase183(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase184(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase185(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase186(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase187(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase188(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase189(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase190(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase191(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase192(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase193(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase194(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase195(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase196(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase197(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase198(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase199(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase200(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase201(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase202(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase203(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase204(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase205(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase206(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase207(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase208(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase209(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase210(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase211(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase212(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase213(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase214(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase215(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase216(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase217(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase218(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase219(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase220(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase221(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase222(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase223(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase224(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase225(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase226(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase227(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase228(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase229(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase230(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase231(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase232(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase233(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase234(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase235(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase236(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase237(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase238(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase239(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase240(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase241(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase242(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase243(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase244(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase245(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase246(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase247(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase248(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase249(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase250(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase251(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase252(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase253(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase254(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase255(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase256(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase257(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase258(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase259(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase260(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase261(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase262(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase263(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase264(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase265(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase266(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase267(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase268(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase269(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase270(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase271(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase272(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase273(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase274(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase275(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase276(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase277(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase278(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase279(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase280(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase281(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase282(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase283(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase284(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase285(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase286(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase287(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase288(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase289(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase290(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase291(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase177(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase176(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase177(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase178(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase292(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase178(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase179(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase293(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase294(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase295(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase296(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase180(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase179(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase180(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase181(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase297(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase181(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase182(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase298(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase299(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase300(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase301(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase183(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase182(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase183(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase184(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase302(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase184(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase185(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase303(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase304(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase305(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase306(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase186(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase185(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase186(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase187(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase307(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase187(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase188(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase308(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase309(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase310(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase311(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase312(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase313(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase314(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase315(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase316(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase317(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase318(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase319(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase320(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase321(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase322(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase323(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase324(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase325(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase326(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase327(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase328(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase329(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase330(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase331(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase332(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase333(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase334(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase335(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase336(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase337(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase338(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase339(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase340(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase341(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase342(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase343(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase344(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase345(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase346(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase347(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase348(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase349(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase350(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase351(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase352(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase353(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase354(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase355(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase356(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase357(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase358(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase359(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase360(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase361(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase362(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase363(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase364(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase365(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase366(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase367(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase368(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase369(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase370(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase371(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase372(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase373(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase374(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase375(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase376(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase377(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase378(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase379(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase380(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase381(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase382(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase383(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase384(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase385(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase386(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase387(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase388(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase389(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase390(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase391(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase392(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase393(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase394(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase395(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase396(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase397(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase398(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase399(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase400(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase401(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase402(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase403(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase404(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase405(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase406(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase407(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase408(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase409(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase410(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase411(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase412(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase413(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase414(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase415(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase416(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase417(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase418(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase419(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase420(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase421(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase422(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase423(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase424(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase425(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase426(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase427(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase428(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase429(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase430(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase431(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase432(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase433(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase434(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase435(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase436(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase437(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase438(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase439(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase440(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase441(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase442(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase443(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase444(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase445(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase446(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase447(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase448(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase449(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase450(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase451(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase452(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase453(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase454(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase455(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase456(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase457(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase458(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase459(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase460(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase461(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase462(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase463(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase464(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase465(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase466(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase467(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase468(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase469(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase470(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase471(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase472(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase473(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase474(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase475(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase476(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase477(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase478(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase479(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase480(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase481(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase482(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase483(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase484(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase485(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase486(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase487(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase488(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase489(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase490(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase491(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase492(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase493(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase494(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase495(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase496(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase497(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase498(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase499(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase500(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase501(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase502(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase503(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase504(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase505(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase506(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase507(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase508(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase509(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase510(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase511(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase512(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase513(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase514(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase515(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase516(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase517(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase518(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase519(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase520(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase521(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase522(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase523(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase524(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase525(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase526(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase527(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase528(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase529(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase530(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase531(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase532(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase533(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase534(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase535(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase536(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase537(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase538(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase539(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase540(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase541(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase542(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase543(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase544(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase545(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase546(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase547(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase548(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase549(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase550(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase551(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase552(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase553(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase554(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase555(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase556(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase557(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase558(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase559(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase560(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase561(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase562(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase563(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase564(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase565(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase566(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase567(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase568(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase569(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase570(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase571(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase572(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase573(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase574(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase575(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase576(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase577(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase578(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase579(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase580(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase581(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase582(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase583(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase584(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase585(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase586(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase587(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase588(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase589(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase590(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase591(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase592(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase593(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase594(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase595(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase596(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase597(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase598(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase599(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase600(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase601(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase602(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase603(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase604(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase605(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase606(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase607(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase608(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase609(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase610(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase611(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase612(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase613(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase614(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase615(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase616(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase617(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase618(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase619(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase620(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase621(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase622(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase623(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase624(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase625(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase626(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase627(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase628(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase629(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase630(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase631(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase632(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase633(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase634(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase635(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase636(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase637(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase638(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase639(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase640(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase641(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase642(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase643(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase644(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase645(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase646(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase647(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase648(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase649(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase650(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase651(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase652(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase653(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase654(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase655(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase656(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase657(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase658(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase659(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase660(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase661(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase662(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase663(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase664(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase665(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase666(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase667(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase668(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase669(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase670(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase671(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase672(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase673(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase674(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase675(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase676(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase677(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase678(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase679(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase680(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase681(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase682(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase683(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase684(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase685(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase686(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase687(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase688(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase689(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase690(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase691(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase692(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase693(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase694(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase695(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase696(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase697(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase698(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase699(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase700(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase701(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase702(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase703(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase704(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase705(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase706(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase707(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase708(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase709(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase710(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase711(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase712(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase713(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase714(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase715(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase716(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase717(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase718(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase719(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase720(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase721(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase722(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase723(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase724(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase725(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase726(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase727(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase728(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase729(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase730(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase731(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase732(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase733(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase734(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase735(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase736(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase737(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase738(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase739(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase740(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase741(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase742(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase743(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase744(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase745(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase746(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase747(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase748(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase749(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase750(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase751(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase752(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase753(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase754(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase755(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase756(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase757(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase758(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase759(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase760(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase761(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase762(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase763(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase764(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase765(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase766(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase767(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase768(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase769(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase770(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase771(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase772(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase773(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase774(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase775(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase776(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase777(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase778(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase779(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase780(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase781(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase782(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase783(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase784(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase785(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase786(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase787(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase788(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase789(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase790(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase791(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase792(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase793(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase794(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase795(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase796(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase797(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase798(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase799(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase800(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase801(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase802(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase803(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase804(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase805(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase806(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase807(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase808(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase809(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase810(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase811(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase812(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase813(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase814(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase815(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase816(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase817(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase818(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase819(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase820(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase821(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase822(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase823(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase824(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase825(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase826(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase827(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase828(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase829(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase830(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase831(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase832(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase833(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase834(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase835(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase836(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase837(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase838(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase839(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase840(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase841(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase842(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase843(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase844(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase845(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase846(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase847(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase848(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase849(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase850(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase851(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase852(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase853(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase854(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase855(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase856(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase857(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase858(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase859(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase860(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase861(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase862(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase863(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase864(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase865(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase866(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase867(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase868(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase869(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase870(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase871(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase872(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase873(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase874(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase875(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase876(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase877(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase878(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase879(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase880(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase881(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase882(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase883(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase884(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase885(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase886(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase887(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase888(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase889(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase890(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase891(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase892(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase893(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase894(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase895(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase896(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase897(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase898(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase899(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase900(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase901(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase902(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase903(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase904(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase905(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase906(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase907(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase908(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase909(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase910(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase911(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase912(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase913(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase914(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase915(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase916(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase917(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase918(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase919(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase920(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase921(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase922(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase923(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase924(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase925(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase926(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase927(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase928(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase929(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase930(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase931(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase932(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase933(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase934(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase935(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase936(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase937(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase938(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase939(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase940(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase941(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase942(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase943(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase944(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase945(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase946(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase947(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase948(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase949(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase950(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase951(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase952(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase953(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase954(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase955(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase956(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase957(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase958(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase959(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase960(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase961(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase962(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase963(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase964(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase965(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase966(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase967(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase968(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase969(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase970(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase971(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase972(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase973(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase974(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase975(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase976(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase977(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase978(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase979(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase980(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase981(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase982(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase983(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase984(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase985(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase986(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase987(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase988(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase989(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase990(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase991(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase992(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase993(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase994(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase995(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase996(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase997(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase998(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase999(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1000(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1001(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1002(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1003(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1004(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1005(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1006(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1007(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1008(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1009(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1010(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1011(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1012(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1013(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1014(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1015(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1016(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1017(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1018(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1019(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1020(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1021(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1022(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1023(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1024(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1025(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1026(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1027(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1028(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1029(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1030(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1031(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1032(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1033(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1034(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1035(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1036(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1037(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1038(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1039(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1040(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1041(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1042(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1043(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1044(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1045(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1046(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1047(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1048(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1049(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1050(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1051(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1052(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1053(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1054(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1055(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1056(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1057(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1058(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1059(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1060(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1061(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1062(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1063(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1064(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1065(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1066(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1067(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1068(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1069(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1070(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1071(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1072(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1073(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1074(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1075(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1076(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1077(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1078(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1079(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1080(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1081(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1082(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1083(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1084(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1085(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1086(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1087(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1088(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1089(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1090(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1091(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1092(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1093(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1094(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1095(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1096(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1097(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1098(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1099(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1100(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1101(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1102(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1103(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1104(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1105(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1106(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1107(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1108(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1109(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1110(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1111(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1112(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1113(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1114(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1115(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1116(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1117(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1118(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1119(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1120(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1121(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1122(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1123(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1124(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1125(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1126(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1127(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1128(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1129(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1130(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1131(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1132(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1133(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1134(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1135(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1136(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1137(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1138(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1139(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1140(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1141(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1142(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1143(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1144(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1145(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1146(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1147(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1148(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1149(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1150(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1151(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1152(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1153(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1154(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1155(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1156(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1157(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1158(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1159(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1160(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1161(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1162(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1163(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1164(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1165(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1166(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1167(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1168(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1169(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1170(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1171(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1172(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1173(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1174(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1175(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1176(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1177(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1178(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1179(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1180(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1181(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1182(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1183(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1184(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1185(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1186(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1187(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1188(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1189(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1190(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1191(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1192(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1193(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1194(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1195(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1196(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1197(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1198(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1199(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1200(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1201(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1202(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1203(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1204(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1205(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1206(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1207(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1208(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1209(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1210(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1211(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1212(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1213(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1214(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1215(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1216(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1217(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1218(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1219(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1220(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1221(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1222(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1223(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1224(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1225(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1226(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1227(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1228(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1229(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1230(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1231(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1232(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1233(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1234(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1235(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1236(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1237(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1238(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1239(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1240(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1241(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1242(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1243(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1244(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1245(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1246(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1247(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1248(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1249(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1250(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1251(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1252(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1253(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1254(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1255(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1256(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1257(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1258(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1259(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1260(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1261(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1262(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1263(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1264(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1265(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1266(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1267(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1268(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1269(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1270(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1271(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1272(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1273(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1274(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1275(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1276(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1277(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1278(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1279(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1280(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1281(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1282(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1283(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1284(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1285(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1286(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1287(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1288(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1289(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1290(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1291(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1292(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1293(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1294(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1295(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1296(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1297(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1298(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1299(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1300(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1301(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1302(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1303(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1304(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1305(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1306(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1307(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1308(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1309(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1310(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1311(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1312(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1313(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1314(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1315(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1316(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1317(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1318(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1319(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1320(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1321(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1322(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1323(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1324(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1325(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1326(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1327(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1328(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1329(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1330(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1331(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1332(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1333(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1334(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1335(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1336(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1337(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1338(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1339(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1340(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1341(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1342(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1343(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1344(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1345(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1346(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1347(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1348(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1349(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1350(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1351(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1352(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1353(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1354(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1355(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1356(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1357(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1358(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1359(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1360(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1361(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1362(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1363(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1364(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1365(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1366(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1367(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1368(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1369(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1370(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1371(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1372(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1373(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1374(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1375(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1376(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1377(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1378(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1379(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1380(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1381(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1382(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1383(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1384(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1385(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1386(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1387(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1388(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1389(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1390(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1391(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1392(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1393(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1394(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1395(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1396(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1397(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1398(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1399(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1400(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1401(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1402(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1403(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1404(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1405(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1406(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1407(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1408(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1409(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1410(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1411(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1412(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1413(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1414(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1415(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1416(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1417(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1418(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1419(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1420(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1421(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1422(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1423(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1424(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1425(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1426(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1427(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1428(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1429(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1430(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1431(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1432(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1433(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1434(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1435(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1436(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1437(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1438(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1439(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1440(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1441(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1442(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1443(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1444(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1445(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1446(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1447(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1448(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1449(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1450(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1451(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1452(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1453(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1454(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1455(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1456(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1457(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1458(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1459(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1460(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1461(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1462(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1463(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1464(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1465(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1466(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1467(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1468(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1469(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1470(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1471(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1472(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1473(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1474(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1475(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1476(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1477(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1478(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1479(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1480(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1481(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1482(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1483(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1484(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1485(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1486(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1487(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1488(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1489(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1490(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1491(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1492(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1493(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1494(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1495(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1496(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1497(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1498(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1499(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1500(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1501(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1502(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1503(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1504(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1505(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1506(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1507(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1508(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1509(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1510(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1511(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1512(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1513(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1514(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1515(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1516(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1517(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1518(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1519(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1520(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1521(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1522(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1523(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1524(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1525(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1526(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1527(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1528(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1529(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1530(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1531(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1532(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1533(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1534(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1535(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1536(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1537(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1538(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1539(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1540(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1541(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1542(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1543(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1544(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1545(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1546(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1547(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1548(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1549(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1550(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1551(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1552(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1553(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1554(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1555(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1556(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1557(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1558(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1559(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1560(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1561(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1562(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1563(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1564(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1565(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1566(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1567(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1568(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1569(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1570(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1571(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1572(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1573(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1574(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1575(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1576(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1577(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1578(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1579(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1580(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1581(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1582(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1583(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1584(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1585(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1586(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1587(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1588(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1589(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1590(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1591(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1592(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1593(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1594(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1595(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1596(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1597(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1598(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1599(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1600(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1601(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1602(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1603(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1604(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1605(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1606(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1607(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1608(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1609(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1610(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1611(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1612(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1613(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1614(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1615(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1616(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1617(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1618(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1619(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1620(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1621(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1622(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1623(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1624(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1625(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1626(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1627(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1628(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1629(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1630(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1631(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1632(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1633(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1634(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1635(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1636(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1637(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1638(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1639(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1640(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1641(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1642(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1643(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1644(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1645(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1646(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1647(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1648(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1649(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1650(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1651(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1652(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1653(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1654(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1655(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1656(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1657(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1658(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1659(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1660(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1661(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1662(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1663(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1664(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1665(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1666(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1667(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1668(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1669(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1670(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1671(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1672(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1673(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1674(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1675(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1676(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1677(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1678(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1679(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1680(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1681(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1682(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1683(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1684(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1685(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1686(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1687(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1688(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1689(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1690(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1691(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1692(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1693(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1694(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1695(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1696(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1697(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1698(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1699(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1700(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1701(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1702(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1703(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1704(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1705(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1706(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1707(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1708(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1709(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1710(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1711(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1712(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1713(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1714(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1715(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1716(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1717(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1718(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1719(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1720(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1721(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1722(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1723(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1724(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1725(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1726(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1727(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1728(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1729(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1730(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1731(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1732(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1733(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1734(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1735(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1736(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1737(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1738(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1739(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1740(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1741(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1742(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1743(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1744(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1745(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1746(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1747(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1748(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1749(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1750(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1751(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1752(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1753(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1754(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1755(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1756(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1757(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1758(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1759(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1760(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1761(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1762(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1763(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1764(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1765(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1766(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1767(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1768(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1769(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1770(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1771(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1772(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1773(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1774(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1775(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1776(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1777(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1778(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1779(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1780(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1781(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1782(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1783(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1784(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1785(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1786(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1787(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1788(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1789(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1790(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1791(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1792(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1793(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1794(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1795(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1796(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1797(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1798(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1799(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1800(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1801(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1802(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1803(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1804(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1805(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1806(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1807(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1808(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1809(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1810(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1811(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1812(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1813(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1814(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1815(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1816(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1817(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1818(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1819(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1820(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1821(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1822(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1823(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1824(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1825(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1826(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1827(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1828(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1829(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1830(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1831(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1832(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1833(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1834(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1835(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1836(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1837(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1838(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1839(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1840(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1841(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1842(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1843(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1844(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1845(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1846(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1847(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1848(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1849(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1850(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1851(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1852(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1853(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1854(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1855(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1856(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1857(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1858(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1859(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1860(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1861(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1862(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1863(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1864(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1865(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1866(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1867(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1868(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1869(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1870(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1871(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1872(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1873(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1874(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1875(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1876(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1877(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1878(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1879(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1880(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1881(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1882(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1883(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1884(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1885(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1886(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1887(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1888(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1889(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1890(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1891(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1892(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1893(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1894(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1895(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1896(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1897(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1898(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1899(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1900(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1901(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1902(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1903(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1904(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1905(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1906(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1907(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1908(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1909(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1910(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1911(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1912(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1913(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1914(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1915(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1916(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1917(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1918(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1919(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1920(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1921(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1922(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1923(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1924(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1925(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1926(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1927(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1928(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1929(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1930(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1931(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1932(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1933(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1934(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1935(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1936(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1937(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1938(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1939(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1940(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1941(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1942(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1943(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1944(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1945(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1946(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1947(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1948(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1949(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1950(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1951(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1952(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1953(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1954(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1955(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1956(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1957(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1958(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1959(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1960(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1961(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1962(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1963(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1964(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1965(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1966(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1967(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1968(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1969(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1970(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1971(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1972(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1973(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1974(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1975(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1976(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1977(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1978(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1979(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1980(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1981(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1982(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1983(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1984(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1985(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1986(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1987(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1988(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1989(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1990(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1991(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1992(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1993(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1994(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1995(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1996(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1997(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1998(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase1999(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2000(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2001(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2002(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2003(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2004(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2005(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2006(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2007(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2008(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2009(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2010(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2011(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2012(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2013(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2014(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2015(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2016(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2017(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2018(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2019(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2020(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2021(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2022(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2023(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2024(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2025(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2026(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2027(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2028(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2029(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2030(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2031(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2032(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2033(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2034(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2035(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2036(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2037(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2038(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2039(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2040(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2041(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2042(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2043(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2044(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2045(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2046(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2047(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2048(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2049(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2050(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2051(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2052(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2053(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2054(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2055(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2056(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2057(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2058(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2059(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2060(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2061(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2062(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2063(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2064(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2065(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2066(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2067(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2068(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2069(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2070(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2071(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2072(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2073(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2074(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2075(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2076(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2077(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2078(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2079(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2080(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2081(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2082(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2083(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2084(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2085(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2086(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2087(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2088(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2089(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2090(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2091(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2092(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2093(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2094(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2095(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2096(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2097(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2098(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2099(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2100(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2101(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2102(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2103(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2104(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2105(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2106(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2107(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2108(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2109(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2110(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2111(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2112(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2113(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2114(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2115(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2116(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2117(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2118(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2119(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2120(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2121(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2122(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2123(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2124(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2125(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2126(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2127(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2128(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2129(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2130(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2131(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2132(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2133(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2134(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2135(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2136(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2137(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2138(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2139(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2140(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2141(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2142(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2143(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2144(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2145(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2146(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2147(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2148(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2149(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2150(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2151(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2152(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2153(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2154(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2155(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2156(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2157(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2158(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2159(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2160(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2161(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2162(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2163(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2164(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2165(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2166(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2167(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2168(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2169(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2170(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2171(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2172(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2173(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2174(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2175(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2176(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2177(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2178(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2179(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2180(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2181(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2182(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2183(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2184(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2185(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2186(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2187(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2188(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2189(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2190(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2191(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2192(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2193(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2194(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2195(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2196(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2197(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2198(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2199(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2200(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2201(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2202(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2203(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2204(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2205(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2206(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2207(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2208(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2209(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2210(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2211(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2212(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2213(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2214(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2215(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2216(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2217(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2218(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2219(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2220(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2221(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2222(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2223(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2224(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2225(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2226(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2227(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2228(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2229(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2230(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2231(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2232(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2233(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase188(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase189(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2234(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase189(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase190(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2235(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase190(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase191(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2236(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase191(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase192(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2237(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase192(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase193(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2238(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase193(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase194(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2239(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8720,0.0,4.2)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase194(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase195(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2240(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase195(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase196(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2241(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7700,0.0,1.7)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase196(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase197(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2242(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase197(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase198(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2243(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6890,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase198(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase199(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2244(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6440,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase199(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase200(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2245(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6200,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase200(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase201(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2246(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase201(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase202(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2247(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase202(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase203(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2248(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase203(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase204(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2249(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5570,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase204(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase205(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2250(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5250,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase205(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase206(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2251(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4560,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase206(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase207(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2252(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4060,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase207(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase208(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2253(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase208(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase209(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2254(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase209(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase210(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2255(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,38000.,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase210(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase211(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2256(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,33000.,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase211(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase212(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase212(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase213(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase213(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase214(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase214(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase215(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase215(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase216(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase216(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase217(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase217(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase218(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase218(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_7.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase219(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_7.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase219(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_8.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase220(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_8.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase220(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase221(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase221(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase222(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase222(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase223(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase223(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase224(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase224(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase225(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase225(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase226(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase226(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase227(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase227(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase228(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase228(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase229(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase229(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase230(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase230(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase231(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase231(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase232(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase232(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_21.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase233(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_21.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase233(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase234(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase234(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase235(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase235(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase236(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase236(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase237(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase237(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase238(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase238(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase239(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase239(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_28.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase240(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_28.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase240(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase241(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase241(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_30.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase242(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_30.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase242(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase243(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase243(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_32.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase244(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_32.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase244(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase245(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase245(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase246(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase246(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_35.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase247(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_35.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase247(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase248(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase248(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase249(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase249(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_39.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase250(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_39.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase250(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase251(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase251(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase252(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase252(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_42.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase253(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_42.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase253(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_43.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase254(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_43.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase254(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_45.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase255(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_45.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase255(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_46.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase256(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_46.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase256(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_47.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase257(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_47.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase257(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_48.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase258(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_48.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase258(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_49.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase259(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_49.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase259(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase260(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase260(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase261(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase261(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase262(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase262(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase263(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase263(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase264(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase264(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase265(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase265(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase266(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase266(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_57.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase267(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_57.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase267(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_58.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase268(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_58.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase268(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_59.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase269(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_59.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase269(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase270(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase270(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_61.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase271(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_61.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase271(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_62.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase272(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_62.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase272(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase273(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase273(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_64.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase274(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_64.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase274(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_66.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase275(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_66.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase275(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_68.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase276(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_68.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase276(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase277(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase277(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_70.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase278(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_70.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase278(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase279(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase279(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_72.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase280(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_72.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase280(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_73.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase281(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_73.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase281(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_74.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase282(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_74.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase282(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_75.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase283(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_75.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase283(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase284(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase284(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase285(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase285(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase286(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase286(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase287(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase287(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase288(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase288(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase289(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase289(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase290(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase290(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase291(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase291(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase292(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase292(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase293(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase293(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase294(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase294(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase295(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase295(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase296(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase296(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase297(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase297(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase298(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase298(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase299(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase299(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase300(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase300(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase301(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase301(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase302(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase302(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase303(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase303(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase304(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase304(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase305(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase305(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase306(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase306(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase307(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase307(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase308(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase308(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase309(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase309(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase310(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase310(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase311(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase311(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase312(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2257(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase312(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase313(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2258(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase314(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase313(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase314(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase315(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2259(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase316(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase315(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase316(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase317(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2260(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase318(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase317(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase318(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase319(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2261(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase320(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase319(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase320(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase321(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2262(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase322(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase321(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase322(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase323(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2263(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase324(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase323(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase324(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase325(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2264(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase326(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase325(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase326(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase327(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2265(basecase.calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase328(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase327(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase328(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase329(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase330(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase329(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase330(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase331(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase331(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase332(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase333(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase332(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase333(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase334(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase335(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase334(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase335(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase336(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase336(basecase.countrateCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase337(basecase.calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
# calcspec:2265
# thermback:0
# calcphot:337
# countrate:336
# SpecSourcerateSpec:0
