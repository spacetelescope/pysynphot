from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase

class calcspecCase1(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase1(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase1(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase2(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase2(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase2(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase3(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase3(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase4(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase4(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase3(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase5(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase5(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase6(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase6(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase4(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase7(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase7(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase8(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase8(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase5(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase9(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase9(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase10(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase10(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase6(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase11(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase11(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase7(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase12(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase12(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase8(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase13(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase13(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase14(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase14(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase9(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase15(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase15(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase10(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase16(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase16(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase11(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase17(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase17(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase18(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase18(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase12(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase19(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase19(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase20(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase20(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase13(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase21(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase21(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase22(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase22(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase14(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase23(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase23(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase24(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase24(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase15(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase25(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase25(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase26(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase26(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase16(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase27(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase27(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase28(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase28(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase17(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase29(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase29(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase30(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase30(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase18(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase31(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase31(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase19(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase32(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase32(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase20(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase33(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase33(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase21(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase34(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase34(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase22(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase35(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase35(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase23(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase36(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase36(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase24(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase37(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase37(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase38(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase38(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase25(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/bz77/bz_23.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase39(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase39(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase26(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase40(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase40(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase27(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/bz77/bz_41.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase41(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase41(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase28(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/bz77/bz_71.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase42(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase42(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase29(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/bz77/bz_76.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase43(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase43(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase30(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,6250,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase44(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase44(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase31(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,15000,0.0,3.5)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase45(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase45(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase32(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,7750,0.0,2.0)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase46(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase46(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase33(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,4750,0.0,1.0)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase47(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase47(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase48(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase48(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase49(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase49(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase50(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase50(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase51(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase51(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase34(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6200,0.0,4.4)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase52(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase52(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase35(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7700,0.0,1.7)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase53(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase53(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase36(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase54(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase54(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase55(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase55(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_23.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase56(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase56(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_41.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase57(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase57(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_71.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase58(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase58(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_76.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase59(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase59(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase60(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase60(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase61(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase61(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase62(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase62(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase63(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase63(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase64(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(qso_template.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase64(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(qso_template.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase37(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase65(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase65(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase38(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(7700)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase66(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase66(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase39(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(6200)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase67(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase67(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase40(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase68(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase68(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase41(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-0.5,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase69(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase69(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase42(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase70(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase70(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase43(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.5,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase71(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase71(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase72(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,fnu),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase72(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,fnu),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase73(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)+em(10000.0,10.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase73(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)+em(10000.0,10.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase74(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase74(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase75(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase75(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase76(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal1)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase76(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase77(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal2),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase77(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal2),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase78(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal2)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase78(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal2)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase79(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase79(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase80(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,lmc)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase80(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,lmc)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase81(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase81(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase82(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,xgal)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase82(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,xgal)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase83(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.5),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase83(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.5),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase84(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase84(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase85(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase85(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase86(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase86(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase87(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase87(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase88(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase88(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase89(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase89(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase90(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase90(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase91(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase91(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase92(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(cousins,i),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase92(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(cousins,i),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase93(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase93(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase94(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase94(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase95(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f160w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase95(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f160w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase96(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase96(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase97(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase97(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase98(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-06,jy)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase98(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-06,jy)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase99(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-06,jy)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase99(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-06,jy)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase100(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-06,jy)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase100(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-06,jy)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase44(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase101(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase101(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase102(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase102(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase103(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase103(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase104(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.9514,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase104(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.9514,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase105(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.0086,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase105(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.0086,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase106(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.1514,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase106(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.1514,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase107(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.40573333333333,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase107(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.40573333333333,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase108(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.067600000000002,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase108(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.067600000000002,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase109(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.964448767123287,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase109(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.964448767123287,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase110(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.26738684931507,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase110(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.26738684931507,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase111(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.808112328767123,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase111(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.808112328767123,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase112(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.628378447488586,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase112(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.628378447488586,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase113(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase113(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase114(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase114(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),28.0,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase115(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase115(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.setglobal(__file__)
        self.runpy()
class countrateCase116(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.5"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase116(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.5"
        self.setglobal(__file__)
        self.runpy()
class countrateCase117(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase117(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase118(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase118(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase119(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase119(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase120(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase120(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase121(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase121(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase122(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*1.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase122(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*1.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase123(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase123(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase124(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase124(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase125(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase125(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase126(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase126(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase127(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase127(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase128(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase128(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase129(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase129(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase130(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase130(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase131(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase131(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase132(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase132(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase133(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase133(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase134(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase134(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase135(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase135(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase136(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase136(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase137(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase137(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase138(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase138(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase1(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase139(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase139(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase2(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase140(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase140(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase3(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase4(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase5(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase6(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase141(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase141(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase7(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase142(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase142(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase8(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase143(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase143(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase9(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase144(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase144(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase10(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase145(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase145(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase11(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase146(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase146(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase12(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase147(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase147(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase13(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase148(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase148(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase14(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase149(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase149(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase15(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase150(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase150(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase16(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase151(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase151(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase17(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase152(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase152(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase18(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase153(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase153(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase19(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase154(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase154(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase20(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase155(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase155(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase21(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase156(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase156(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase22(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase157(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase157(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase23(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase158(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase158(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase24(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase25(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase26(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase27(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase28(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase29(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase30(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase31(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase32(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase33(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase34(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase35(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase36(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase37(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase38(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase39(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase40(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase41(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase42(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase43(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase44(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase45(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase46(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase47(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase48(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase49(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase45(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase50(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase46(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase51(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase52(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase47(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase53(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase48(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase54(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase49(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase55(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase50(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase56(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase51(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase57(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase52(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase58(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase53(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase59(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase54(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase60(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase55(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,45000,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase61(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase56(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,45000,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase62(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase57(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,45000,0.0,4.5)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase63(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase64(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase58(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase65(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase66(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_13.fits),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase59(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000.0)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase67(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(bb(5000.0),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase60(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase68(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase69(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase61(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase70(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase62(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase71(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase63(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase72(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase64(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase73(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase65(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase74(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase75(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-13,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase76(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-12,flam)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase77(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-06,jy)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase78(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bz77/bz_24.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-05,jy)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase66(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase159(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase159(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase160(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase160(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase67(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase161(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase161(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase68(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase162(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase162(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase163(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase163(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase69(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase164(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase164(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase165(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase165(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase70(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase166(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase166(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase167(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase167(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase71(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase168(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase168(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase169(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase169(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase72(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase170(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase170(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase73(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase171(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase171(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase172(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase172(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase74(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase173(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase173(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase174(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase174(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase75(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase175(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase175(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase176(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase176(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase76(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase177(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase177(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase77(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase178(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase178(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase179(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase179(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase78(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase180(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase180(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase181(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase181(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase79(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase182(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase182(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase183(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase183(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase80(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase184(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase184(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase185(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase185(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase81(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase186(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase186(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase187(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase187(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase82(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase188(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase188(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase189(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase189(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase83(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase190(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase190(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase84(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase191(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase191(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase85(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase192(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase192(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase86(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase193(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase193(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase194(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase194(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase87(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase195(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase195(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase196(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase196(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase88(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase197(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase197(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase198(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase198(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase89(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase199(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase199(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase200(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase200(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase90(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase201(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase201(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase202(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase202(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase91(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase203(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase203(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase204(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase204(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase92(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase205(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase205(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase206(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase206(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase93(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase207(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase207(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase208(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase208(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase94(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase209(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase209(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase210(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase210(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase95(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase211(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase211(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase96(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase212(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase212(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase213(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase213(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase97(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase214(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase214(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase215(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase215(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase98(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase216(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase216(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase217(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase217(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase99(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase100(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase218(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase218(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase101(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase219(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase219(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase220(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase220(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase102(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase221(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase221(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase222(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase222(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase103(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase223(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase223(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase104(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase224(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase224(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase225(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase225(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase105(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase226(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase226(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase227(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase227(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase106(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase228(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase228(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase107(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase229(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase229(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase230(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase230(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase108(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase231(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase231(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase232(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase232(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase109(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase233(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase233(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase234(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase234(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase110(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase235(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase235(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase236(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase236(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase111(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase237(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase237(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase238(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase238(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase112(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase239(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase239(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase240(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase240(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase113(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase241(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase241(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase114(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase242(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase242(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase243(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase243(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase115(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase116(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase117(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase118(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase119(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase120(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase121(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase122(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase123(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase124(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase125(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase126(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase127(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase128(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase129(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase130(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase131(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase132(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase133(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase244(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase244(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase245(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),23.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase245(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),23.5,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase134(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase246(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase246(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase135(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase247(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase247(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase136(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase248(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase248(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase137(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase138(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase249(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase249(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase139(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase250(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase250(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase140(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase251(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase251(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase141(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase252(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase252(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase142(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase253(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase253(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase143(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase254(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase254(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase144(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase255(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase255(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase145(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase256(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase256(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase257(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase257(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase258(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase258(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase259(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase259(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase260(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(egal.dat),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase260(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(egal.dat),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase146(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase261(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(10000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase261(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(10000),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase147(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase262(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase262(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase263(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase263(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcspecCase148(calcspecCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase264(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500)*ebmvx(0.5,lmc),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase264(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500)*ebmvx(0.5,lmc),band(bessell,h),20,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase265(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase265(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase79(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase266(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase266(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase80(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class calcphotCase267(calcphotCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class countrateCase267(countrateCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.setglobal(__file__)
        self.runpy()
class SpecSourcerateSpecCase81(SpecSourcerateSpecCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.setglobal(__file__)
        self.runpy()



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
# calcspec:148
# calcphot:267
# countrate:267
# SpecSourcerateSpec:81
