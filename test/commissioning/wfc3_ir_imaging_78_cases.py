from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase

class calcspecCase1(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase3(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
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
class calcphotCase6(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase7(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase9(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase12(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase12(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase17(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase15(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase18(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase21(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase24(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase27(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase42(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase30(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase47(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase33(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase52(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase36(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase57(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase39(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase62(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase42(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase67(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
class calcphotCase45(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase72(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
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
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase128(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase129(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase130(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase131(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase132(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase133(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase134(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase135(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase136(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase137(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase138(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase139(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase140(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase141(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase142(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase143(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase144(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase145(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase146(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase147(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase148(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase149(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase150(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase151(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase152(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase153(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase154(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase155(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase156(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase157(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase158(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase159(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase160(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase161(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase162(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase163(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase164(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase165(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase166(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase167(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase168(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase169(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase170(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase171(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase172(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase173(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase174(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase175(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase176(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase177(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase178(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase179(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase180(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase181(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase182(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase183(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase184(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase185(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase186(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase187(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase188(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase189(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase190(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase191(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase192(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase193(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase194(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase195(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase196(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase197(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase198(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase199(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase200(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase201(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase202(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase203(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase204(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase205(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase206(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase207(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase208(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase209(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase210(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase211(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase212(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase213(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase214(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase215(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase216(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase217(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase218(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase219(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase220(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase221(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase222(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase223(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase224(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase225(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase226(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase227(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase228(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase229(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase230(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase231(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase232(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase233(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase234(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase235(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase236(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase237(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase238(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase239(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase240(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase241(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase242(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase243(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase244(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase245(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase246(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase247(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase248(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase249(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase250(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase251(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase252(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase253(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase254(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase255(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase256(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase257(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase258(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase259(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase260(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase261(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase262(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase263(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase264(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase265(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase266(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase267(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase268(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase269(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase270(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase271(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase272(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase273(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase274(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase275(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase276(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase277(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase278(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase279(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase280(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase281(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase282(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase283(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase284(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase285(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase286(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase287(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase288(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase289(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase290(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase291(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase292(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase293(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase294(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase295(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase296(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase297(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase298(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase299(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase300(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase301(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase302(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase303(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase304(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase305(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase306(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase307(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase308(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase309(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase310(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase311(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase312(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase313(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase314(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase315(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase316(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase317(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase318(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase319(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase320(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase321(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase322(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase323(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase324(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase325(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase326(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase327(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase328(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase329(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase330(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase331(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase332(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase333(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase334(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase335(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase336(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase337(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase338(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase339(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase340(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase341(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase342(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase343(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase344(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase345(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase346(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase347(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase348(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase349(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase350(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase351(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase352(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase353(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase354(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase355(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase356(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase357(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase358(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase359(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase360(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase361(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase362(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase363(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase364(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase365(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase366(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase367(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase368(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase369(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase370(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase371(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase372(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase373(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase374(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase375(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase376(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase377(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase378(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase379(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase380(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase381(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase382(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase383(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase384(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase385(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase386(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase387(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase388(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase389(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase390(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase391(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase392(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase393(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase394(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase395(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase396(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase397(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase398(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase399(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase400(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase401(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase402(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase403(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase404(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase405(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase406(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase407(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase408(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase409(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase410(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase411(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase412(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase413(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase414(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase415(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase416(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase417(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase418(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase419(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase420(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase421(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase422(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase423(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase424(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase425(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase426(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase427(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase428(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase429(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase430(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase431(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase432(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase433(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase434(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase435(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase436(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase437(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase438(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase439(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase440(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase441(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase442(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase443(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase444(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase445(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase446(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase447(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase448(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase449(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase450(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase451(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase452(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase453(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase454(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase455(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase456(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase457(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase458(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase459(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase460(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase461(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase462(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase463(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase464(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase465(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase466(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase467(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase468(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase469(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase470(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase471(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase472(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase473(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase474(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase475(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase476(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase477(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase478(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase479(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase480(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase481(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase482(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase483(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase484(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase485(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase486(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase487(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase488(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase489(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase490(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase491(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase492(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase493(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase494(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase495(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase496(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase497(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase498(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase499(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase500(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase501(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase502(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase503(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase504(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase505(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase506(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase507(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase508(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase509(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase510(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase511(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase512(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase513(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase514(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase515(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase516(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase517(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase518(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase519(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase520(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase521(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase522(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase523(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase524(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase525(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase526(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase527(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase528(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase529(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase530(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase531(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase532(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase533(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase534(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase535(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase536(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase537(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase538(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase539(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase540(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase541(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase542(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase543(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase544(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase545(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase546(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase547(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8720,0.0,4.2)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase548(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase549(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7700,0.0,1.7)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase550(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase551(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6890,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase552(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6440,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase553(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6200,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase554(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase555(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase556(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase557(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5570,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase558(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5250,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase559(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4560,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase560(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4060,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase561(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase562(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase563(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,38000.,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase564(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,33000.,0.0,4.0)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_7.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_7.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_8.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_8.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_21.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_21.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_28.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_28.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_30.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_30.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_32.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_32.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_35.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_35.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_39.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_39.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_42.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_42.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_43.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_43.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_45.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_45.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_46.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_46.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_47.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_47.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_48.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_48.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_49.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_49.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_57.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_57.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_58.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_58.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_59.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_59.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_61.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_61.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_62.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_62.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_64.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_64.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_66.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_66.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_68.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_68.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_70.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_70.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_72.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_72.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_73.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_73.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_74.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_74.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_75.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_75.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),1.0),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),1.0),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),2.0),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),2.0),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),0.1),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase565(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase566(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase567(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase568(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase569(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase570(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase571(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase572(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase573(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(13200.0,5.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(13200.0,5.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(countrateCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(calcphotCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
# calcspec:573
# calcphot:176
# countrate:175
# SpecSourcerateSpec:0
