import os
import sys
sys.path.append('../')
import conv_base

conv_base.HERE = os.path.abspath(os.path.dirname(__file__))

class Test791(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C791_%s.fits"
        cls.setup2()

class Test792(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C792_%s.fits"
        cls.setup2()

class Test793(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C793_%s.fits"
        cls.setup2()

class Test794(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C794_%s.fits"
        cls.setup2()

class Test795(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f095n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C795_%s.fits"
        cls.setup2()

class Test796(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f095n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C796_%s.fits"
        cls.setup2()

class Test797(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f097n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C797_%s.fits"
        cls.setup2()

class Test798(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f097n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C798_%s.fits"
        cls.setup2()

class Test799(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f108n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C799_%s.fits"
        cls.setup2()

class Test800(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f108n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C800_%s.fits"
        cls.setup2()

class Test801(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C801_%s.fits"
        cls.setup2()

class Test802(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C802_%s.fits"
        cls.setup2()

class Test803(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        cls.fname="C803_%s.fits"
        cls.setup2()

class Test804(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C804_%s.fits"
        cls.setup2()

class Test805(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C805_%s.fits"
        cls.setup2()

class Test806(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C806_%s.fits"
        cls.setup2()

class Test807(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C807_%s.fits"
        cls.setup2()

class Test808(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C808_%s.fits"
        cls.setup2()

class Test809(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C809_%s.fits"
        cls.setup2()

class Test810(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C810_%s.fits"
        cls.setup2()

class Test811(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C811_%s.fits"
        cls.setup2()

class Test812(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C812_%s.fits"
        cls.setup2()

class Test813(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C813_%s.fits"
        cls.setup2()

class Test814(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C814_%s.fits"
        cls.setup2()

class Test815(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C815_%s.fits"
        cls.setup2()

class Test816(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C816_%s.fits"
        cls.setup2()

class Test817(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C817_%s.fits"
        cls.setup2()

class Test818(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C818_%s.fits"
        cls.setup2()

class Test819(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C819_%s.fits"
        cls.setup2()

class Test820(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C820_%s.fits"
        cls.setup2()

class Test821(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C821_%s.fits"
        cls.setup2()

class Test822(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C822_%s.fits"
        cls.setup2()

class Test823(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C823_%s.fits"
        cls.setup2()

class Test824(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C824_%s.fits"
        cls.setup2()

class Test825(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C825_%s.fits"
        cls.setup2()

class Test826(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C826_%s.fits"
        cls.setup2()

class Test827(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C827_%s.fits"
        cls.setup2()

class Test828(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C828_%s.fits"
        cls.setup2()

class Test829(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C829_%s.fits"
        cls.setup2()

class Test830(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C830_%s.fits"
        cls.setup2()

class Test831(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C831_%s.fits"
        cls.setup2()

class Test832(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C832_%s.fits"
        cls.setup2()

class Test833(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C833_%s.fits"
        cls.setup2()

class Test834(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C834_%s.fits"
        cls.setup2()

class Test835(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C835_%s.fits"
        cls.setup2()

class Test836(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal3),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C836_%s.fits"
        cls.setup2()

class Test837(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C837_%s.fits"
        cls.setup2()

class Test838(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C838_%s.fits"
        cls.setup2()

class Test839(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        cls.fname="C839_%s.fits"
        cls.setup2()

class Test840(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        cls.fname="C840_%s.fits"
        cls.setup2()

class Test841(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(cousins,i),15,vegamag)"
        cls.fname="C841_%s.fits"
        cls.setup2()

class Test842(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,k),15,vegamag)"
        cls.fname="C842_%s.fits"
        cls.setup2()

class Test843(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,k),20,vegamag)"
        cls.fname="C843_%s.fits"
        cls.setup2()

class Test844(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C844_%s.fits"
        cls.setup2()

class Test845(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C845_%s.fits"
        cls.setup2()

class Test846(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C846_%s.fits"
        cls.setup2()

class Test847(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(nicmos,2,f160w),15,vegamag)"
        cls.fname="C847_%s.fits"
        cls.setup2()

class Test848(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),15,vegamag)"
        cls.fname="C848_%s.fits"
        cls.setup2()

class Test849(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-06,jy)"
        cls.fname="C849_%s.fits"
        cls.setup2()

class Test850(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C850_%s.fits"
        cls.setup2()

class Test851(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal1)"
        cls.fname="C851_%s.fits"
        cls.setup2()

class Test852(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal3)"
        cls.fname="C852_%s.fits"
        cls.setup2()

class Test853(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,lmc)"
        cls.fname="C853_%s.fits"
        cls.setup2()

class Test854(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,xgal)"
        cls.fname="C854_%s.fits"
        cls.setup2()

class Test855(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)+em(10000.0,10.0,1.0E-13,flam)"
        cls.fname="C855_%s.fits"
        cls.setup2()

class Test856(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-06,jy)"
        cls.fname="C856_%s.fits"
        cls.setup2()

class Test857(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-13,flam)"
        cls.fname="C857_%s.fits"
        cls.setup2()

class Test858(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-06,jy)"
        cls.fname="C858_%s.fits"
        cls.setup2()

class Test859(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-13,flam)"
        cls.fname="C859_%s.fits"
        cls.setup2()

class Test860(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,fnu),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C860_%s.fits"
        cls.setup2()

class Test861(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C861_%s.fits"
        cls.setup2()

class Test862(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),1.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C862_%s.fits"
        cls.setup2()

class Test863(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C863_%s.fits"
        cls.setup2()

class Test864(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(qso_template.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C864_%s.fits"
        cls.setup2()

class Test865(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        cls.fname="C865_%s.fits"
        cls.setup2()

class Test866(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C866_%s.fits"
        cls.setup2()

class Test867(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C867_%s.fits"
        cls.setup2()

class Test868(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C868_%s.fits"
        cls.setup2()

class Test869(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.628378447488586,vegamag)"
        cls.fname="C869_%s.fits"
        cls.setup2()

class Test870(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.0086,vegamag)"
        cls.fname="C870_%s.fits"
        cls.setup2()

class Test871(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C871_%s.fits"
        cls.setup2()

class Test872(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.26738684931507,vegamag)"
        cls.fname="C872_%s.fits"
        cls.setup2()

class Test873(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.40573333333333,vegamag)"
        cls.fname="C873_%s.fits"
        cls.setup2()

class Test874(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C874_%s.fits"
        cls.setup2()

class Test875(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.808112328767123,vegamag)"
        cls.fname="C875_%s.fits"
        cls.setup2()

class Test876(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.9514,vegamag)"
        cls.fname="C876_%s.fits"
        cls.setup2()

class Test877(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.964448767123287,vegamag)"
        cls.fname="C877_%s.fits"
        cls.setup2()

class Test878(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.067600000000002,vegamag)"
        cls.fname="C878_%s.fits"
        cls.setup2()

class Test879(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.1514,vegamag)"
        cls.fname="C879_%s.fits"
        cls.setup2()

class Test880(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C880_%s.fits"
        cls.setup2()

class Test881(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),28.0,vegamag)"
        cls.fname="C881_%s.fits"
        cls.setup2()

class Test882(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        cls.fname="C882_%s.fits"
        cls.setup2()

class Test883(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        cls.fname="C883_%s.fits"
        cls.setup2()

class Test884(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.5"
        cls.fname="C884_%s.fits"
        cls.setup2()

class Test885(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*1.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C885_%s.fits"
        cls.setup2()

class Test886(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C886_%s.fits"
        cls.setup2()

class Test887(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C887_%s.fits"
        cls.setup2()

class Test888(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f113n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C888_%s.fits"
        cls.setup2()

class Test889(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f113n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C889_%s.fits"
        cls.setup2()

class Test890(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f140w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C890_%s.fits"
        cls.setup2()

class Test891(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f140w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C891_%s.fits"
        cls.setup2()

class Test892(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f145m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C892_%s.fits"
        cls.setup2()

class Test893(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f145m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C893_%s.fits"
        cls.setup2()

class Test894(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C894_%s.fits"
        cls.setup2()

class Test895(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C895_%s.fits"
        cls.setup2()

class Test896(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C896_%s.fits"
        cls.setup2()

class Test897(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C897_%s.fits"
        cls.setup2()

class Test898(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C898_%s.fits"
        cls.setup2()

class Test899(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C899_%s.fits"
        cls.setup2()

class Test900(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C900_%s.fits"
        cls.setup2()

class Test901(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f164n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C901_%s.fits"
        cls.setup2()

class Test902(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C902_%s.fits"
        cls.setup2()

class Test903(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C903_%s.fits"
        cls.setup2()

class Test904(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C904_%s.fits"
        cls.setup2()

class Test905(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C905_%s.fits"
        cls.setup2()

class Test906(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f166n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C906_%s.fits"
        cls.setup2()

class Test907(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f166n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C907_%s.fits"
        cls.setup2()

class Test908(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f170m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C908_%s.fits"
        cls.setup2()

class Test909(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f170m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C909_%s.fits"
        cls.setup2()

class Test910(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C910_%s.fits"
        cls.setup2()

class Test911(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C911_%s.fits"
        cls.setup2()

class Test912(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C912_%s.fits"
        cls.setup2()

class Test913(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C913_%s.fits"
        cls.setup2()

class Test914(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,pol0s"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C914_%s.fits"
        cls.setup2()

class Test915(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,pol0s"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C915_%s.fits"
        cls.setup2()

class Test916(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C916_%s.fits"
        cls.setup2()

class Test917(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C917_%s.fits"
        cls.setup2()

class Test918(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C918_%s.fits"
        cls.setup2()

class Test919(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C919_%s.fits"
        cls.setup2()

class Test920(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C920_%s.fits"
        cls.setup2()

class Test921(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C921_%s.fits"
        cls.setup2()

class Test922(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C922_%s.fits"
        cls.setup2()

class Test923(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C923_%s.fits"
        cls.setup2()

class Test924(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C924_%s.fits"
        cls.setup2()

class Test925(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C925_%s.fits"
        cls.setup2()

class Test926(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C926_%s.fits"
        cls.setup2()

class Test927(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C927_%s.fits"
        cls.setup2()

class Test928(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C928_%s.fits"
        cls.setup2()

class Test929(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C929_%s.fits"
        cls.setup2()

class Test930(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C930_%s.fits"
        cls.setup2()

class Test931(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C931_%s.fits"
        cls.setup2()

class Test932(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C932_%s.fits"
        cls.setup2()

class Test933(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C933_%s.fits"
        cls.setup2()

class Test934(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f171m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C934_%s.fits"
        cls.setup2()

class Test935(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f171m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C935_%s.fits"
        cls.setup2()

class Test936(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f180m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C936_%s.fits"
        cls.setup2()

class Test937(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f180m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C937_%s.fits"
        cls.setup2()

class Test938(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C938_%s.fits"
        cls.setup2()

class Test939(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C939_%s.fits"
        cls.setup2()

class Test940(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C940_%s.fits"
        cls.setup2()

class Test941(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C941_%s.fits"
        cls.setup2()

class Test942(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C942_%s.fits"
        cls.setup2()

class Test943(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C943_%s.fits"
        cls.setup2()

class Test944(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f204m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C944_%s.fits"
        cls.setup2()

class Test945(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f204m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C945_%s.fits"
        cls.setup2()

class Test946(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f205w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C946_%s.fits"
        cls.setup2()

class Test947(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f205w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C947_%s.fits"
        cls.setup2()

class Test948(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f207m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C948_%s.fits"
        cls.setup2()

class Test949(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f207m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C949_%s.fits"
        cls.setup2()

class Test950(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f212n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C950_%s.fits"
        cls.setup2()

class Test951(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f212n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C951_%s.fits"
        cls.setup2()

class Test952(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f216n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C952_%s.fits"
        cls.setup2()

class Test953(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f216n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C953_%s.fits"
        cls.setup2()

class Test954(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C954_%s.fits"
        cls.setup2()

class Test955(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C955_%s.fits"
        cls.setup2()

class Test956(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C956_%s.fits"
        cls.setup2()

class Test957(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C957_%s.fits"
        cls.setup2()

class Test958(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f237m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C958_%s.fits"
        cls.setup2()

class Test959(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f237m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C959_%s.fits"
        cls.setup2()

class Test960(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,pol0l"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C960_%s.fits"
        cls.setup2()

class Test961(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,pol0l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C961_%s.fits"
        cls.setup2()

class Test962(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f108n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C962_%s.fits"
        cls.setup2()

class Test963(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f108n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C963_%s.fits"
        cls.setup2()

class Test964(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(10000),band(bessell,h),20,vegamag)"
        cls.fname="C964_%s.fits"
        cls.setup2()

class Test965(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C965_%s.fits"
        cls.setup2()

class Test966(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5500)*ebmvx(0.5,lmc),band(bessell,h),20,vegamag)"
        cls.fname="C966_%s.fits"
        cls.setup2()

class Test967(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C967_%s.fits"
        cls.setup2()

class Test968(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C968_%s.fits"
        cls.setup2()

class Test969(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(bessell,h),20,vegamag)"
        cls.fname="C969_%s.fits"
        cls.setup2()

class Test970(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(bessell,h),20,vegamag)"
        cls.fname="C970_%s.fits"
        cls.setup2()

class Test971(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(bessell,h),20,vegamag)"
        cls.fname="C971_%s.fits"
        cls.setup2()

class Test972(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(bessell,h),20,vegamag)"
        cls.fname="C972_%s.fits"
        cls.setup2()

class Test973(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(bessell,h),20,vegamag)"
        cls.fname="C973_%s.fits"
        cls.setup2()

class Test974(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(egal.dat),band(bessell,h),20,vegamag)"
        cls.fname="C974_%s.fits"
        cls.setup2()

class Test975(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,h),20,vegamag)"
        cls.fname="C975_%s.fits"
        cls.setup2()

class Test976(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C976_%s.fits"
        cls.setup2()

class Test977(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f113n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C977_%s.fits"
        cls.setup2()

class Test978(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f113n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C978_%s.fits"
        cls.setup2()

class Test979(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C979_%s.fits"
        cls.setup2()

class Test980(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(bb(5500),band(bessell,h),23.5,vegamag)"
        cls.fname="C980_%s.fits"
        cls.setup2()

class Test981(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C981_%s.fits"
        cls.setup2()

class Test982(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C982_%s.fits"
        cls.setup2()

class Test983(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C983_%s.fits"
        cls.setup2()

class Test984(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C984_%s.fits"
        cls.setup2()

class Test985(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C985_%s.fits"
        cls.setup2()

class Test986(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C986_%s.fits"
        cls.setup2()

class Test987(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C987_%s.fits"
        cls.setup2()

class Test988(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C988_%s.fits"
        cls.setup2()

class Test989(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C989_%s.fits"
        cls.setup2()

class Test990(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C990_%s.fits"
        cls.setup2()

class Test991(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C991_%s.fits"
        cls.setup2()

class Test992(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C992_%s.fits"
        cls.setup2()

class Test993(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C993_%s.fits"
        cls.setup2()

class Test994(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C994_%s.fits"
        cls.setup2()

class Test995(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C995_%s.fits"
        cls.setup2()

class Test996(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C996_%s.fits"
        cls.setup2()

class Test997(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C997_%s.fits"
        cls.setup2()

class Test998(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C998_%s.fits"
        cls.setup2()

class Test999(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C999_%s.fits"
        cls.setup2()

class Test1000(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f164n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1000_%s.fits"
        cls.setup2()

class Test1001(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1001_%s.fits"
        cls.setup2()

class Test1002(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f166n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1002_%s.fits"
        cls.setup2()

class Test1003(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f166n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1003_%s.fits"
        cls.setup2()

class Test1004(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1004_%s.fits"
        cls.setup2()

class Test1005(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1005_%s.fits"
        cls.setup2()

class Test1006(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1006_%s.fits"
        cls.setup2()

class Test1007(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1007_%s.fits"
        cls.setup2()

class Test1008(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1008_%s.fits"
        cls.setup2()

class Test1009(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1009_%s.fits"
        cls.setup2()

class Test1010(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1010_%s.fits"
        cls.setup2()

class Test1011(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1011_%s.fits"
        cls.setup2()

class Test1012(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f196n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1012_%s.fits"
        cls.setup2()

class Test1013(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f196n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1013_%s.fits"
        cls.setup2()

class Test1014(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f200n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1014_%s.fits"
        cls.setup2()

class Test1015(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f200n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1015_%s.fits"
        cls.setup2()

class Test1016(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f212n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1016_%s.fits"
        cls.setup2()

class Test1017(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f212n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1017_%s.fits"
        cls.setup2()

class Test1018(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f215n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1018_%s.fits"
        cls.setup2()

class Test1019(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f215n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1019_%s.fits"
        cls.setup2()

class Test1020(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1020_%s.fits"
        cls.setup2()

class Test1021(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1021_%s.fits"
        cls.setup2()

class Test1022(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1022_%s.fits"
        cls.setup2()

class Test1023(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1023_%s.fits"
        cls.setup2()

class Test1024(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f240m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1024_%s.fits"
        cls.setup2()

class Test1025(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f240m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1025_%s.fits"
        cls.setup2()

class Test1026(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(bb(5000.0),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1026_%s.fits"
        cls.setup2()

class Test1027(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1027_%s.fits"
        cls.setup2()

class Test1028(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1028_%s.fits"
        cls.setup2()

class Test1029(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1029_%s.fits"
        cls.setup2()

class Test1030(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1030_%s.fits"
        cls.setup2()

class Test1031(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1031_%s.fits"
        cls.setup2()

class Test1032(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1032_%s.fits"
        cls.setup2()

class Test1033(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1033_%s.fits"
        cls.setup2()

class Test1034(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1034_%s.fits"
        cls.setup2()

class Test1035(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1035_%s.fits"
        cls.setup2()

class Test1036(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1036_%s.fits"
        cls.setup2()

class Test1037(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1037_%s.fits"
        cls.setup2()

class Test1038(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1038_%s.fits"
        cls.setup2()

class Test1039(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1039_%s.fits"
        cls.setup2()

class Test1040(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1040_%s.fits"
        cls.setup2()

class Test1041(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1041_%s.fits"
        cls.setup2()

class Test1042(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1042_%s.fits"
        cls.setup2()

class Test1043(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1043_%s.fits"
        cls.setup2()

class Test1044(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1044_%s.fits"
        cls.setup2()

class Test1045(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1045_%s.fits"
        cls.setup2()

class Test1046(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1046_%s.fits"
        cls.setup2()

class Test1047(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1047_%s.fits"
        cls.setup2()

class Test1048(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1048_%s.fits"
        cls.setup2()

class Test1049(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1049_%s.fits"
        cls.setup2()

class Test1050(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1050_%s.fits"
        cls.setup2()

class Test1051(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1051_%s.fits"
        cls.setup2()

class Test1052(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1052_%s.fits"
        cls.setup2()

class Test1053(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1053_%s.fits"
        cls.setup2()

class Test1054(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1054_%s.fits"
        cls.setup2()

class Test1055(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1055_%s.fits"
        cls.setup2()

class Test1056(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1056_%s.fits"
        cls.setup2()

class Test1057(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1057_%s.fits"
        cls.setup2()

class Test1058(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1058_%s.fits"
        cls.setup2()

class Test1059(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1059_%s.fits"
        cls.setup2()

class Test1060(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1060_%s.fits"
        cls.setup2()

class Test1061(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1061_%s.fits"
        cls.setup2()

class Test1062(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1062_%s.fits"
        cls.setup2()

class Test1063(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1063_%s.fits"
        cls.setup2()

class Test1064(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-05,jy)"
        cls.fname="C1064_%s.fits"
        cls.setup2()

class Test1065(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-06,jy)"
        cls.fname="C1065_%s.fits"
        cls.setup2()

class Test1066(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-12,flam)"
        cls.fname="C1066_%s.fits"
        cls.setup2()

class Test1067(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-13,flam)"
        cls.fname="C1067_%s.fits"
        cls.setup2()

class Test1068(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1068_%s.fits"
        cls.setup2()

class Test1069(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1069_%s.fits"
        cls.setup2()

class Test1070(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1070_%s.fits"
        cls.setup2()

class Test1071(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1071_%s.fits"
        cls.setup2()

class Test1072(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1072_%s.fits"
        cls.setup2()

class Test1073(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1073_%s.fits"
        cls.setup2()

class Test1074(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1074_%s.fits"
        cls.setup2()

class Test1075(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1075_%s.fits"
        cls.setup2()

class Test1076(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1076_%s.fits"
        cls.setup2()

class Test1077(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1077_%s.fits"
        cls.setup2()

class Test1078(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1078_%s.fits"
        cls.setup2()

class Test1079(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1079_%s.fits"
        cls.setup2()

class Test1080(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1080_%s.fits"
        cls.setup2()

class Test1081(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1081_%s.fits"
        cls.setup2()

class Test1082(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1082_%s.fits"
        cls.setup2()

class Test1083(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1083_%s.fits"
        cls.setup2()

class Test1084(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1084_%s.fits"
        cls.setup2()

class Test1085(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1085_%s.fits"
        cls.setup2()

class Test1086(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1086_%s.fits"
        cls.setup2()

class Test1087(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1087_%s.fits"
        cls.setup2()

class Test1088(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1088_%s.fits"
        cls.setup2()

class Test1089(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1089_%s.fits"
        cls.setup2()

class Test1090(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1090_%s.fits"
        cls.setup2()

class Test1091(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1091_%s.fits"
        cls.setup2()

class Test1092(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1092_%s.fits"
        cls.setup2()

class Test1093(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1093_%s.fits"
        cls.setup2()

class Test1094(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1094_%s.fits"
        cls.setup2()

class Test1095(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1095_%s.fits"
        cls.setup2()

class Test1096(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1096_%s.fits"
        cls.setup2()

class Test1097(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1097_%s.fits"
        cls.setup2()

class Test1098(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1098_%s.fits"
        cls.setup2()

class Test1099(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1099_%s.fits"
        cls.setup2()

class Test1100(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1100_%s.fits"
        cls.setup2()

