import newobs_test 
import sys
from pytools import testutil


class C1(newobs_test.NativeCase):
    def setparms(self):
        self.spectrum = "(earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1\
302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5)"
        self.obsmode = "acs,hrc,f220w"

class C3(newobs_test.NativeCase):
    def setparms(self):

        self.spectrum = "rn(pl(4000,1.0,jy),box(5500.0,1),1e-18,flam)"
        self.obsmode = "acs,sbc,F150LP"

class C4(newobs_test.NativeCase):
    def setparms(self):

        self.spectrum = "rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20.0,vegamag)"
        self.obsmode = "acs,sbc,F125LP"

class C5(newobs_test.NativeCase):
    def setparms(self):

        self.spectrum = "((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        self.obsmode = "acs,sbc,F140LP"




class C8(newobs_test.NativeCase):
    def setparms(self):

        self.spectrum = "rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        self.obsmode = "wfc3,ir,F110W"

class C9(newobs_test.NativeCase):
    def setparms(self):

        self.spectrum = "rn(bb(5000.0),band(johnson,v),28.0,vegamag)"
        self.obsmode = "wfc3,uvis1,F606W"

class C10(newobs_test.NativeCase):
    def setparms(self):

        self.spectrum = "((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        self.obsmode = "wfc3,uvis1,F606W"

################################################################
#         SpecSourcerateSpec cases follow
################################################################        
class C11(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "(earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)"
        self.obsmode = "acs,hrc,PR200L"

class C12(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "rn((unit(1,flam)),band(johnson,v),15.0,vegamag)"
        self.obsmode = "acs,wfc1,G800L"

class C13(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "em(4000.0,10.0,1.0000000168623835E-16,flam)"
        self.obsmode = "acs,hrc,PR200L"

class C14(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "rn((unit(1,flam)),band(johnson,v),15.0,vegamag)"
        self.obsmode = "acs,hrc,PR200L"

class C15(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "rn((spec(crcalspec$gd71_mod_005.fits))*ebmvx(0.1,gal1),box(5500.0,1),1.0E-16,flam)"
        self.obsmode = "acs,hrc,PR200L"

class C16(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "(spec(crcalspec$grw_70d5824_stis_001.fits))"
        self.obsmode = "stis,fuvmama,g140l,s52x2"

class C17(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "rn((icat(k93models,44500,0.0,5.0)),band(johnson,v),10.516,vegamag)"
        self.obsmode = "stis,nuvmama,e230h,c2263,s02x02"


class C18(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "rn((spec(crcalspec$bd_28d4211_stis_001.fits)),box(2000.0,1),1.0E-12,flam)"
        self.obsmode = "stis,nuvmama,e230h,c2263,s02x02"


class C20(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "em(4300.0,1.0,9.999999960041972E-13,flam)"
        self.obsmode = "stis,ccd,g430l"

class C21(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "rn((icat(k93models,5770,0.0,4.5)),band(johnson,v),20.0,vegamag)"
        self.obsmode = "acs,hrc,PR200L"

class C22(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        self.obsmode = "stis,fuvmama,g140l"

class C23(newobs_test.BinnedCase):
    def setparms(self):

        self.spectrum = "((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"
        self.obsmode = "cos,fuv,g130m,c1309"

if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
        
