"""Holds cases suggested by science oversight (Ralph Bohlin)."""

from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase

class S1(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class S2(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class S3(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class S4(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

 
class stisS0(countrateCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS1(countrateCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS2(countrateCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS3(countrateCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS4(countrateCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS5(countrateCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS6(countrateCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS7(countrateCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS8(countrateCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS9(countrateCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS10(countrateCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS11(countrateCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS12(countrateCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS13(countrateCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS14(countrateCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class acsS0(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS1(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS2(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS3(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS4(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS5(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS6(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS7(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS8(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS9(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS10(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS11(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS12(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS13(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS14(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS15(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS16(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS17(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS18(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS19(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS20(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS21(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS22(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS23(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS24(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS25(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS26(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS27(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS28(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS29(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS30(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS31(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS32(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS33(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS34(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS35(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS36(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS37(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS38(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS39(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS40(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS41(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS42(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS43(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS44(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS45(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS46(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS47(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS48(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS49(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS50(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS51(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS52(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS53(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS54(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS55(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS56(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS57(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS58(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS59(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS60(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS61(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS62(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS63(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS64(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS65(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS66(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS67(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS68(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS69(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS70(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS71(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS72(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS73(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS74(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS75(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS76(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS77(countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS78(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS79(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS80(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS81(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS82(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS83(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS84(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS85(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS86(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS87(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS88(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS89(countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class e1(countrateCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el1215a.fits"
        self.setglobal(__file__)
        self.runpy()


class e2(countrateCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el1302a.fits"
        self.setglobal(__file__)
        self.runpy()

class e3(countrateCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el1356a.fits"
        self.setglobal(__file__)
        self.runpy()

class e4(countrateCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el2471a.fits"
        self.setglobal(__file__)
        self.runpy()


if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
