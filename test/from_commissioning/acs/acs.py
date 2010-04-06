import os
import sys
sys.path.append('..')
import conv_base

conv_base.HERE = os.path.abspath(os.path.dirname(__file__))

class Test472(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C472_%s.fits"
        cls.setup2()

class Test473(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        cls.fname="C473_%s.fits"
        cls.setup2()

class Test474(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C474_%s.fits"
        cls.setup2()

class Test475(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        cls.fname="C475_%s.fits"
        cls.setup2()

class Test476(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        cls.fname="C476_%s.fits"
        cls.setup2()

class Test477(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        cls.fname="C477_%s.fits"
        cls.setup2()

class Test478(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        cls.fname="C478_%s.fits"
        cls.setup2()

class Test479(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        cls.fname="C479_%s.fits"
        cls.setup2()

class Test480(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C480_%s.fits"
        cls.setup2()

class Test481(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C481_%s.fits"
        cls.setup2()

class Test482(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C482_%s.fits"
        cls.setup2()

class Test483(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C483_%s.fits"
        cls.setup2()

class Test484(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C484_%s.fits"
        cls.setup2()

class Test485(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C485_%s.fits"
        cls.setup2()

class Test486(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C486_%s.fits"
        cls.setup2()

class Test487(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C487_%s.fits"
        cls.setup2()

class Test488(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C488_%s.fits"
        cls.setup2()

class Test489(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C489_%s.fits"
        cls.setup2()

class Test490(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C490_%s.fits"
        cls.setup2()

class Test491(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C491_%s.fits"
        cls.setup2()

class Test492(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C492_%s.fits"
        cls.setup2()

class Test493(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C493_%s.fits"
        cls.setup2()

class Test494(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C494_%s.fits"
        cls.setup2()

class Test495(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        cls.fname="C495_%s.fits"
        cls.setup2()

class Test496(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C496_%s.fits"
        cls.setup2()

class Test497(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C497_%s.fits"
        cls.setup2()

class Test498(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C498_%s.fits"
        cls.setup2()

class Test499(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C499_%s.fits"
        cls.setup2()

class Test500(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C500_%s.fits"
        cls.setup2()

class Test501(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C501_%s.fits"
        cls.setup2()

class Test502(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C502_%s.fits"
        cls.setup2()

class Test503(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C503_%s.fits"
        cls.setup2()

class Test504(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C504_%s.fits"
        cls.setup2()

class Test505(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C505_%s.fits"
        cls.setup2()

class Test506(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C506_%s.fits"
        cls.setup2()

class Test507(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C507_%s.fits"
        cls.setup2()

class Test508(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C508_%s.fits"
        cls.setup2()

class Test509(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C509_%s.fits"
        cls.setup2()

class Test510(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C510_%s.fits"
        cls.setup2()

class Test511(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C511_%s.fits"
        cls.setup2()

class Test512(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C512_%s.fits"
        cls.setup2()

class Test513(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C513_%s.fits"
        cls.setup2()

class Test514(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C514_%s.fits"
        cls.setup2()

class Test515(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C515_%s.fits"
        cls.setup2()

class Test516(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C516_%s.fits"
        cls.setup2()

class Test517(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C517_%s.fits"
        cls.setup2()

class Test518(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C518_%s.fits"
        cls.setup2()

class Test519(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C519_%s.fits"
        cls.setup2()

class Test520(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C520_%s.fits"
        cls.setup2()

class Test521(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C521_%s.fits"
        cls.setup2()

class Test522(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C522_%s.fits"
        cls.setup2()

class Test523(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C523_%s.fits"
        cls.setup2()

class Test524(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C524_%s.fits"
        cls.setup2()

class Test525(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C525_%s.fits"
        cls.setup2()

class Test526(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C526_%s.fits"
        cls.setup2()

class Test527(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C527_%s.fits"
        cls.setup2()

class Test528(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C528_%s.fits"
        cls.setup2()

class Test529(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C529_%s.fits"
        cls.setup2()

class Test530(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C530_%s.fits"
        cls.setup2()

class Test531(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C531_%s.fits"
        cls.setup2()

class Test532(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C532_%s.fits"
        cls.setup2()

class Test533(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C533_%s.fits"
        cls.setup2()

class Test534(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C534_%s.fits"
        cls.setup2()

class Test535(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        cls.fname="C535_%s.fits"
        cls.setup2()

class Test536(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        cls.fname="C536_%s.fits"
        cls.setup2()

class Test537(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C537_%s.fits"
        cls.setup2()

class Test538(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        cls.fname="C538_%s.fits"
        cls.setup2()

class Test539(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C539_%s.fits"
        cls.setup2()

class Test540(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C540_%s.fits"
        cls.setup2()

class Test541(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C541_%s.fits"
        cls.setup2()

class Test542(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C542_%s.fits"
        cls.setup2()

class Test543(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C543_%s.fits"
        cls.setup2()

class Test544(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C544_%s.fits"
        cls.setup2()

class Test545(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C545_%s.fits"
        cls.setup2()

class Test546(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C546_%s.fits"
        cls.setup2()

class Test547(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C547_%s.fits"
        cls.setup2()

class Test548(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C548_%s.fits"
        cls.setup2()

class Test549(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C549_%s.fits"
        cls.setup2()

class Test550(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C550_%s.fits"
        cls.setup2()

class Test551(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C551_%s.fits"
        cls.setup2()

class Test552(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C552_%s.fits"
        cls.setup2()

class Test553(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C553_%s.fits"
        cls.setup2()

class Test554(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C554_%s.fits"
        cls.setup2()

class Test555(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C555_%s.fits"
        cls.setup2()

class Test556(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C556_%s.fits"
        cls.setup2()

class Test557(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C557_%s.fits"
        cls.setup2()

class Test558(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C558_%s.fits"
        cls.setup2()

class Test559(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C559_%s.fits"
        cls.setup2()

class Test560(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C560_%s.fits"
        cls.setup2()

class Test561(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C561_%s.fits"
        cls.setup2()

class Test562(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C562_%s.fits"
        cls.setup2()

class Test563(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C563_%s.fits"
        cls.setup2()

class Test564(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C564_%s.fits"
        cls.setup2()

class Test565(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C565_%s.fits"
        cls.setup2()

class Test566(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C566_%s.fits"
        cls.setup2()

class Test567(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C567_%s.fits"
        cls.setup2()

class Test568(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C568_%s.fits"
        cls.setup2()

class Test569(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C569_%s.fits"
        cls.setup2()

class Test570(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C570_%s.fits"
        cls.setup2()

class Test571(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C571_%s.fits"
        cls.setup2()

class Test572(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C572_%s.fits"
        cls.setup2()

class Test573(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C573_%s.fits"
        cls.setup2()

class Test574(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C574_%s.fits"
        cls.setup2()

class Test575(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C575_%s.fits"
        cls.setup2()

class Test576(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C576_%s.fits"
        cls.setup2()

class Test577(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C577_%s.fits"
        cls.setup2()

class Test578(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C578_%s.fits"
        cls.setup2()

class Test579(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        cls.fname="C579_%s.fits"
        cls.setup2()

class Test580(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        cls.fname="C580_%s.fits"
        cls.setup2()

class Test581(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        cls.fname="C581_%s.fits"
        cls.setup2()

class Test582(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        cls.fname="C582_%s.fits"
        cls.setup2()

class Test583(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        cls.fname="C583_%s.fits"
        cls.setup2()

class Test584(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C584_%s.fits"
        cls.setup2()

class Test585(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C585_%s.fits"
        cls.setup2()

class Test586(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C586_%s.fits"
        cls.setup2()

class Test587(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        cls.fname="C587_%s.fits"
        cls.setup2()

class Test588(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C588_%s.fits"
        cls.setup2()

class Test589(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C589_%s.fits"
        cls.setup2()

class Test590(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C590_%s.fits"
        cls.setup2()

class Test591(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C591_%s.fits"
        cls.setup2()

class Test592(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C592_%s.fits"
        cls.setup2()

class Test593(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C593_%s.fits"
        cls.setup2()

class Test594(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C594_%s.fits"
        cls.setup2()

class Test595(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4592"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C595_%s.fits"
        cls.setup2()

class Test596(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4592"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C596_%s.fits"
        cls.setup2()

class Test597(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr505n#5050"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C597_%s.fits"
        cls.setup2()

class Test598(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr505n#5050"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C598_%s.fits"
        cls.setup2()

class Test599(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr656n#6560"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C599_%s.fits"
        cls.setup2()

class Test600(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr656n#6560"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C600_%s.fits"
        cls.setup2()

class Test601(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        cls.fname="C601_%s.fits"
        cls.setup2()

class Test602(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C602_%s.fits"
        cls.setup2()

class Test603(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C603_%s.fits"
        cls.setup2()

class Test604(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C604_%s.fits"
        cls.setup2()

class Test605(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C605_%s.fits"
        cls.setup2()

class Test606(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C606_%s.fits"
        cls.setup2()

class Test607(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C607_%s.fits"
        cls.setup2()

class Test608(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C608_%s.fits"
        cls.setup2()

class Test609(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C609_%s.fits"
        cls.setup2()

class Test610(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="em(4000.0,10.0,1.0E-16,flam)"
        cls.fname="C610_%s.fits"
        cls.setup2()

class Test611(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C611_%s.fits"
        cls.setup2()

class Test612(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C612_%s.fits"
        cls.setup2()

class Test613(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C613_%s.fits"
        cls.setup2()

class Test614(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C614_%s.fits"
        cls.setup2()

class Test615(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C615_%s.fits"
        cls.setup2()

class Test616(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C616_%s.fits"
        cls.setup2()

class Test617(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C617_%s.fits"
        cls.setup2()

class Test618(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C618_%s.fits"
        cls.setup2()

class Test619(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C619_%s.fits"
        cls.setup2()

class Test620(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C620_%s.fits"
        cls.setup2()

class Test621(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C621_%s.fits"
        cls.setup2()

class Test622(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C622_%s.fits"
        cls.setup2()

class Test623(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C623_%s.fits"
        cls.setup2()

class Test624(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f122m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C624_%s.fits"
        cls.setup2()

class Test625(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f122m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C625_%s.fits"
        cls.setup2()

class Test626(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C626_%s.fits"
        cls.setup2()

class Test627(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        cls.fname="C627_%s.fits"
        cls.setup2()

class Test628(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C628_%s.fits"
        cls.setup2()

class Test629(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f140lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C629_%s.fits"
        cls.setup2()

class Test630(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f140lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C630_%s.fits"
        cls.setup2()

class Test631(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C631_%s.fits"
        cls.setup2()

class Test632(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C632_%s.fits"
        cls.setup2()

class Test633(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C633_%s.fits"
        cls.setup2()

class Test634(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C634_%s.fits"
        cls.setup2()

class Test635(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C635_%s.fits"
        cls.setup2()

class Test636(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C636_%s.fits"
        cls.setup2()

class Test637(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f165lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C637_%s.fits"
        cls.setup2()

class Test638(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f165lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C638_%s.fits"
        cls.setup2()

class Test639(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        cls.fname="C639_%s.fits"
        cls.setup2()

class Test640(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C640_%s.fits"
        cls.setup2()

class Test641(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C641_%s.fits"
        cls.setup2()

class Test642(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C642_%s.fits"
        cls.setup2()

class Test643(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C643_%s.fits"
        cls.setup2()

class Test644(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C644_%s.fits"
        cls.setup2()

class Test645(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C645_%s.fits"
        cls.setup2()

class Test646(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C646_%s.fits"
        cls.setup2()

class Test647(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C647_%s.fits"
        cls.setup2()

class Test648(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C648_%s.fits"
        cls.setup2()

class Test649(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        cls.fname="C649_%s.fits"
        cls.setup2()

class Test650(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C650_%s.fits"
        cls.setup2()

class Test651(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C651_%s.fits"
        cls.setup2()

class Test652(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C652_%s.fits"
        cls.setup2()

class Test653(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C653_%s.fits"
        cls.setup2()

class Test654(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C654_%s.fits"
        cls.setup2()

class Test655(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C655_%s.fits"
        cls.setup2()

class Test656(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C656_%s.fits"
        cls.setup2()

class Test657(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C657_%s.fits"
        cls.setup2()

class Test658(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C658_%s.fits"
        cls.setup2()

class Test659(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C659_%s.fits"
        cls.setup2()

class Test660(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C660_%s.fits"
        cls.setup2()

class Test661(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C661_%s.fits"
        cls.setup2()

class Test662(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C662_%s.fits"
        cls.setup2()

class Test663(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C663_%s.fits"
        cls.setup2()

class Test664(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C664_%s.fits"
        cls.setup2()

class Test665(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C665_%s.fits"
        cls.setup2()

class Test666(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C666_%s.fits"
        cls.setup2()

class Test667(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C667_%s.fits"
        cls.setup2()

class Test668(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C668_%s.fits"
        cls.setup2()

class Test669(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C669_%s.fits"
        cls.setup2()

class Test670(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C670_%s.fits"
        cls.setup2()

class Test671(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C671_%s.fits"
        cls.setup2()

class Test672(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C672_%s.fits"
        cls.setup2()

class Test673(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C673_%s.fits"
        cls.setup2()

class Test674(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C674_%s.fits"
        cls.setup2()

class Test675(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C675_%s.fits"
        cls.setup2()

class Test676(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C676_%s.fits"
        cls.setup2()

class Test677(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C677_%s.fits"
        cls.setup2()

class Test678(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C678_%s.fits"
        cls.setup2()

class Test679(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C679_%s.fits"
        cls.setup2()

class Test680(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C680_%s.fits"
        cls.setup2()

class Test681(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C681_%s.fits"
        cls.setup2()

class Test682(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C682_%s.fits"
        cls.setup2()

class Test683(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C683_%s.fits"
        cls.setup2()

class Test684(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C684_%s.fits"
        cls.setup2()

class Test685(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C685_%s.fits"
        cls.setup2()

class Test686(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C686_%s.fits"
        cls.setup2()

class Test687(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C687_%s.fits"
        cls.setup2()

class Test688(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C688_%s.fits"
        cls.setup2()

class Test689(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C689_%s.fits"
        cls.setup2()

class Test690(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w,pol_v"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C690_%s.fits"
        cls.setup2()

class Test691(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w,pol_v"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C691_%s.fits"
        cls.setup2()

class Test692(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C692_%s.fits"
        cls.setup2()

class Test693(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C693_%s.fits"
        cls.setup2()

class Test694(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C694_%s.fits"
        cls.setup2()

class Test695(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C695_%s.fits"
        cls.setup2()

class Test696(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C696_%s.fits"
        cls.setup2()

class Test697(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C697_%s.fits"
        cls.setup2()

class Test698(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C698_%s.fits"
        cls.setup2()

class Test699(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C699_%s.fits"
        cls.setup2()

class Test700(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C700_%s.fits"
        cls.setup2()

class Test701(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C701_%s.fits"
        cls.setup2()

class Test702(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C702_%s.fits"
        cls.setup2()

class Test703(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C703_%s.fits"
        cls.setup2()

class Test704(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C704_%s.fits"
        cls.setup2()

class Test705(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C705_%s.fits"
        cls.setup2()

class Test706(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C706_%s.fits"
        cls.setup2()

class Test707(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C707_%s.fits"
        cls.setup2()

class Test708(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C708_%s.fits"
        cls.setup2()

class Test709(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C709_%s.fits"
        cls.setup2()

class Test710(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C710_%s.fits"
        cls.setup2()

class Test711(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C711_%s.fits"
        cls.setup2()

class Test712(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C712_%s.fits"
        cls.setup2()

class Test713(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C713_%s.fits"
        cls.setup2()

class Test714(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C714_%s.fits"
        cls.setup2()

class Test715(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C715_%s.fits"
        cls.setup2()

class Test716(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C716_%s.fits"
        cls.setup2()

class Test717(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C717_%s.fits"
        cls.setup2()

class Test718(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C718_%s.fits"
        cls.setup2()

class Test719(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C719_%s.fits"
        cls.setup2()

class Test720(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C720_%s.fits"
        cls.setup2()

class Test721(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C721_%s.fits"
        cls.setup2()

class Test722(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C722_%s.fits"
        cls.setup2()

class Test723(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C723_%s.fits"
        cls.setup2()

class Test724(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C724_%s.fits"
        cls.setup2()

class Test725(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C725_%s.fits"
        cls.setup2()

class Test726(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C726_%s.fits"
        cls.setup2()

class Test727(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C727_%s.fits"
        cls.setup2()

class Test728(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C728_%s.fits"
        cls.setup2()

class Test729(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/g191b2b_mod_004.fits"
        cls.fname="C729_%s.fits"
        cls.setup2()

class Test730(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd153_mod_004.fits"
        cls.fname="C730_%s.fits"
        cls.setup2()

class Test731(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="$PYSYN_CDBS/calspec/gd71_mod_005.fits"
        cls.fname="C731_%s.fits"
        cls.setup2()

class Test732(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C732_%s.fits"
        cls.setup2()

class Test733(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C733_%s.fits"
        cls.setup2()

class Test734(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr1016n#10000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C734_%s.fits"
        cls.setup2()

class Test735(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr1016n#10000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C735_%s.fits"
        cls.setup2()

class Test736(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        cls.fname="C736_%s.fits"
        cls.setup2()

class Test737(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C737_%s.fits"
        cls.setup2()

class Test738(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        cls.fname="C738_%s.fits"
        cls.setup2()

class Test739(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        cls.fname="C739_%s.fits"
        cls.setup2()

class Test740(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        cls.fname="C740_%s.fits"
        cls.setup2()

class Test741(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        cls.fname="C741_%s.fits"
        cls.setup2()

class Test742(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        cls.fname="C742_%s.fits"
        cls.setup2()

class Test743(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C743_%s.fits"
        cls.setup2()

class Test744(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C744_%s.fits"
        cls.setup2()

class Test745(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C745_%s.fits"
        cls.setup2()

class Test746(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C746_%s.fits"
        cls.setup2()

class Test747(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        cls.fname="C747_%s.fits"
        cls.setup2()

class Test748(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C748_%s.fits"
        cls.setup2()

class Test749(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits)"
        cls.fname="C749_%s.fits"
        cls.setup2()

class Test750(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C750_%s.fits"
        cls.setup2()

class Test751(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C751_%s.fits"
        cls.setup2()

class Test752(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3881"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C752_%s.fits"
        cls.setup2()

class Test753(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3881"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C753_%s.fits"
        cls.setup2()

class Test754(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr423n#4230"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C754_%s.fits"
        cls.setup2()

class Test755(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr423n#4230"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C755_%s.fits"
        cls.setup2()

class Test756(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C756_%s.fits"
        cls.setup2()

class Test757(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4590"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C757_%s.fits"
        cls.setup2()

class Test758(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4620"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C758_%s.fits"
        cls.setup2()

class Test759(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4620"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C759_%s.fits"
        cls.setup2()

class Test760(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr462n#4620"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C760_%s.fits"
        cls.setup2()

class Test761(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr462n#4620"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C761_%s.fits"
        cls.setup2()

class Test762(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr505n#5000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C762_%s.fits"
        cls.setup2()

class Test763(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr505n#5000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C763_%s.fits"
        cls.setup2()

class Test764(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr551n#5500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C764_%s.fits"
        cls.setup2()

class Test765(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr551n#5500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C765_%s.fits"
        cls.setup2()

class Test766(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr601n#6000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C766_%s.fits"
        cls.setup2()

class Test767(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr601n#6000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C767_%s.fits"
        cls.setup2()

class Test768(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr647m#6470"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C768_%s.fits"
        cls.setup2()

class Test769(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr647m#6470"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C769_%s.fits"
        cls.setup2()

class Test770(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr656n#6500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C770_%s.fits"
        cls.setup2()

class Test771(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr656n#6500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C771_%s.fits"
        cls.setup2()

class Test772(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr716n#7100"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C772_%s.fits"
        cls.setup2()

class Test773(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr716n#7100"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C773_%s.fits"
        cls.setup2()

class Test774(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr782n#7900"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C774_%s.fits"
        cls.setup2()

class Test775(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr782n#7900"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C775_%s.fits"
        cls.setup2()

class Test776(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr853n#8500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C776_%s.fits"
        cls.setup2()

class Test777(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr853n#8500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C777_%s.fits"
        cls.setup2()

class Test778(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr914m#9000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C778_%s.fits"
        cls.setup2()

class Test779(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr914m#9000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C779_%s.fits"
        cls.setup2()

class Test780(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr931n#9300"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C780_%s.fits"
        cls.setup2()

class Test781(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr931n#9300"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C781_%s.fits"
        cls.setup2()

class Test782(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        cls.fname="C782_%s.fits"
        cls.setup2()

class Test783(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C783_%s.fits"
        cls.setup2()

class Test784(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C784_%s.fits"
        cls.setup2()

class Test785(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C785_%s.fits"
        cls.setup2()

class Test786(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C786_%s.fits"
        cls.setup2()

class Test787(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C787_%s.fits"
        cls.setup2()

class Test788(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec($PYSYN_CDBS/calspec/gd71_mod_005.fits)"
        cls.fname="C788_%s.fits"
        cls.setup2()

class Test789(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C789_%s.fits"
        cls.setup2()

class Test790(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C790_%s.fits"
        cls.setup2()

