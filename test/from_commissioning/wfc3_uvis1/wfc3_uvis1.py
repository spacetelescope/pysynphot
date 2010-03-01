import os
import sys
sys.path.append('..')
import conv_base
conv_base.HERE = os.path.abspath(os.path.dirname(__file__))

class Test1483(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1483_%s.fits"
        cls.setup2()

class Test1484(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1484_%s.fits"
        cls.setup2()

class Test1485(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f200lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1485_%s.fits"
        cls.setup2()

class Test1486(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1486_%s.fits"
        cls.setup2()

class Test1487(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1487_%s.fits"
        cls.setup2()

class Test1488(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f218w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1488_%s.fits"
        cls.setup2()

class Test1489(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1489_%s.fits"
        cls.setup2()

class Test1490(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1490_%s.fits"
        cls.setup2()

class Test1491(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        cls.fname="C1491_%s.fits"
        cls.setup2()

class Test1492(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        cls.fname="C1492_%s.fits"
        cls.setup2()

class Test1493(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        cls.fname="C1493_%s.fits"
        cls.setup2()

class Test1494(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        cls.fname="C1494_%s.fits"
        cls.setup2()

class Test1495(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1495_%s.fits"
        cls.setup2()

class Test1496(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1496_%s.fits"
        cls.setup2()

class Test1497(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1497_%s.fits"
        cls.setup2()

class Test1498(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1498_%s.fits"
        cls.setup2()

class Test1499(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1499_%s.fits"
        cls.setup2()

class Test1500(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1500_%s.fits"
        cls.setup2()

class Test1501(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f275w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1501_%s.fits"
        cls.setup2()

class Test1502(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1502_%s.fits"
        cls.setup2()

class Test1503(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1503_%s.fits"
        cls.setup2()

class Test1504(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f280n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1504_%s.fits"
        cls.setup2()

class Test1505(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        cls.fname="C1505_%s.fits"
        cls.setup2()

class Test1506(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        cls.fname="C1506_%s.fits"
        cls.setup2()

class Test1507(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        cls.fname="C1507_%s.fits"
        cls.setup2()

class Test1508(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        cls.fname="C1508_%s.fits"
        cls.setup2()

class Test1509(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        cls.fname="C1509_%s.fits"
        cls.setup2()

class Test1510(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        cls.fname="C1510_%s.fits"
        cls.setup2()

class Test1511(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1511_%s.fits"
        cls.setup2()

class Test1512(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1512_%s.fits"
        cls.setup2()

class Test1513(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1513_%s.fits"
        cls.setup2()

class Test1514(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1514_%s.fits"
        cls.setup2()

class Test1515(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1515_%s.fits"
        cls.setup2()

class Test1516(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1516_%s.fits"
        cls.setup2()

class Test1517(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1517_%s.fits"
        cls.setup2()

class Test1518(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1518_%s.fits"
        cls.setup2()

class Test1519(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1519_%s.fits"
        cls.setup2()

class Test1520(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1520_%s.fits"
        cls.setup2()

class Test1521(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f336w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1521_%s.fits"
        cls.setup2()

class Test1522(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1522_%s.fits"
        cls.setup2()

class Test1523(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1523_%s.fits"
        cls.setup2()

class Test1524(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f343n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1524_%s.fits"
        cls.setup2()

class Test1525(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1525_%s.fits"
        cls.setup2()

class Test1526(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1526_%s.fits"
        cls.setup2()

class Test1527(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f350lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1527_%s.fits"
        cls.setup2()

class Test1528(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1528_%s.fits"
        cls.setup2()

class Test1529(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1529_%s.fits"
        cls.setup2()

class Test1530(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f373n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1530_%s.fits"
        cls.setup2()

class Test1531(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1531_%s.fits"
        cls.setup2()

class Test1532(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1532_%s.fits"
        cls.setup2()

class Test1533(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1533_%s.fits"
        cls.setup2()

class Test1534(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1534_%s.fits"
        cls.setup2()

class Test1535(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1535_%s.fits"
        cls.setup2()

class Test1536(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1536_%s.fits"
        cls.setup2()

class Test1537(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1537_%s.fits"
        cls.setup2()

class Test1538(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1538_%s.fits"
        cls.setup2()

class Test1539(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f395n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1539_%s.fits"
        cls.setup2()

class Test1540(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1540_%s.fits"
        cls.setup2()

class Test1541(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1541_%s.fits"
        cls.setup2()

class Test1542(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f410m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1542_%s.fits"
        cls.setup2()

class Test1543(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1543_%s.fits"
        cls.setup2()

class Test1544(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1544_%s.fits"
        cls.setup2()

class Test1545(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f438w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1545_%s.fits"
        cls.setup2()

class Test1546(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1546_%s.fits"
        cls.setup2()

class Test1547(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1547_%s.fits"
        cls.setup2()

class Test1548(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f467m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1548_%s.fits"
        cls.setup2()

class Test1549(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1549_%s.fits"
        cls.setup2()

class Test1550(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1550_%s.fits"
        cls.setup2()

class Test1551(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f469n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1551_%s.fits"
        cls.setup2()

class Test1552(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1552_%s.fits"
        cls.setup2()

class Test1553(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1553_%s.fits"
        cls.setup2()

class Test1554(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1554_%s.fits"
        cls.setup2()

class Test1555(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1555_%s.fits"
        cls.setup2()

class Test1556(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1556_%s.fits"
        cls.setup2()

class Test1557(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1557_%s.fits"
        cls.setup2()

class Test1558(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1558_%s.fits"
        cls.setup2()

class Test1559(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1559_%s.fits"
        cls.setup2()

class Test1560(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f487n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1560_%s.fits"
        cls.setup2()

class Test1561(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1561_%s.fits"
        cls.setup2()

class Test1562(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1562_%s.fits"
        cls.setup2()

class Test1563(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        cls.fname="C1563_%s.fits"
        cls.setup2()

class Test1564(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1564_%s.fits"
        cls.setup2()

class Test1565(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1565_%s.fits"
        cls.setup2()

class Test1566(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1566_%s.fits"
        cls.setup2()

class Test1567(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f547m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1567_%s.fits"
        cls.setup2()

class Test1568(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1568_%s.fits"
        cls.setup2()

class Test1569(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1569_%s.fits"
        cls.setup2()

class Test1570(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1570_%s.fits"
        cls.setup2()

class Test1571(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1571_%s.fits"
        cls.setup2()

class Test1572(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1572_%s.fits"
        cls.setup2()

class Test1573(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1573_%s.fits"
        cls.setup2()

class Test1574(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1574_%s.fits"
        cls.setup2()

class Test1575(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1575_%s.fits"
        cls.setup2()

class Test1576(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1576_%s.fits"
        cls.setup2()

class Test1577(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1577_%s.fits"
        cls.setup2()

class Test1578(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1578_%s.fits"
        cls.setup2()

class Test1579(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1579_%s.fits"
        cls.setup2()

class Test1580(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1580_%s.fits"
        cls.setup2()

class Test1581(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1581_%s.fits"
        cls.setup2()

class Test1582(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1582_%s.fits"
        cls.setup2()

class Test1583(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1583_%s.fits"
        cls.setup2()

class Test1584(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1584_%s.fits"
        cls.setup2()

class Test1585(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1585_%s.fits"
        cls.setup2()

class Test1586(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1586_%s.fits"
        cls.setup2()

class Test1587(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1587_%s.fits"
        cls.setup2()

class Test1588(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1588_%s.fits"
        cls.setup2()

class Test1589(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1589_%s.fits"
        cls.setup2()

class Test1590(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1590_%s.fits"
        cls.setup2()

class Test1591(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1591_%s.fits"
        cls.setup2()

class Test1592(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1592_%s.fits"
        cls.setup2()

class Test1593(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1593_%s.fits"
        cls.setup2()

class Test1594(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1594_%s.fits"
        cls.setup2()

class Test1595(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1595_%s.fits"
        cls.setup2()

class Test1596(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1596_%s.fits"
        cls.setup2()

class Test1597(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1597_%s.fits"
        cls.setup2()

class Test1598(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1598_%s.fits"
        cls.setup2()

class Test1599(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1599_%s.fits"
        cls.setup2()

class Test1600(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1600_%s.fits"
        cls.setup2()

class Test1601(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f600lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1601_%s.fits"
        cls.setup2()

class Test1602(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1602_%s.fits"
        cls.setup2()

class Test1603(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1603_%s.fits"
        cls.setup2()

class Test1604(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1604_%s.fits"
        cls.setup2()

class Test1605(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1605_%s.fits"
        cls.setup2()

class Test1606(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1606_%s.fits"
        cls.setup2()

class Test1607(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1607_%s.fits"
        cls.setup2()

class Test1608(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1608_%s.fits"
        cls.setup2()

class Test1609(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1609_%s.fits"
        cls.setup2()

class Test1610(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1610_%s.fits"
        cls.setup2()

class Test1611(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1611_%s.fits"
        cls.setup2()

class Test1612(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1612_%s.fits"
        cls.setup2()

class Test1613(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1613_%s.fits"
        cls.setup2()

class Test1614(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1614_%s.fits"
        cls.setup2()

class Test1615(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1615_%s.fits"
        cls.setup2()

class Test1616(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1616_%s.fits"
        cls.setup2()

class Test1617(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1617_%s.fits"
        cls.setup2()

class Test1618(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1618_%s.fits"
        cls.setup2()

class Test1619(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1619_%s.fits"
        cls.setup2()

class Test1620(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1620_%s.fits"
        cls.setup2()

class Test1621(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1621_%s.fits"
        cls.setup2()

class Test1622(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1622_%s.fits"
        cls.setup2()

class Test1623(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1623_%s.fits"
        cls.setup2()

class Test1624(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1624_%s.fits"
        cls.setup2()

class Test1625(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1625_%s.fits"
        cls.setup2()

class Test1626(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1626_%s.fits"
        cls.setup2()

class Test1627(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1627_%s.fits"
        cls.setup2()

class Test1628(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1628_%s.fits"
        cls.setup2()

class Test1629(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1629_%s.fits"
        cls.setup2()

class Test1630(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1630_%s.fits"
        cls.setup2()

class Test1631(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f621m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1631_%s.fits"
        cls.setup2()

class Test1632(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1632_%s.fits"
        cls.setup2()

class Test1633(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1633_%s.fits"
        cls.setup2()

class Test1634(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1634_%s.fits"
        cls.setup2()

class Test1635(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1635_%s.fits"
        cls.setup2()

class Test1636(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1636_%s.fits"
        cls.setup2()

class Test1637(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f631n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1637_%s.fits"
        cls.setup2()

class Test1638(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1638_%s.fits"
        cls.setup2()

class Test1639(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1639_%s.fits"
        cls.setup2()

class Test1640(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f645n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1640_%s.fits"
        cls.setup2()

class Test1641(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1641_%s.fits"
        cls.setup2()

class Test1642(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1642_%s.fits"
        cls.setup2()

class Test1643(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f656n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1643_%s.fits"
        cls.setup2()

class Test1644(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1644_%s.fits"
        cls.setup2()

class Test1645(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1645_%s.fits"
        cls.setup2()

class Test1646(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f657n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1646_%s.fits"
        cls.setup2()

class Test1647(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1647_%s.fits"
        cls.setup2()

class Test1648(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1648_%s.fits"
        cls.setup2()

class Test1649(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1649_%s.fits"
        cls.setup2()

class Test1650(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1650_%s.fits"
        cls.setup2()

class Test1651(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1651_%s.fits"
        cls.setup2()

class Test1652(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f665n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1652_%s.fits"
        cls.setup2()

class Test1653(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1653_%s.fits"
        cls.setup2()

class Test1654(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1654_%s.fits"
        cls.setup2()

class Test1655(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f673n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1655_%s.fits"
        cls.setup2()

class Test1656(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1656_%s.fits"
        cls.setup2()

class Test1657(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1657_%s.fits"
        cls.setup2()

class Test1658(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f680n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1658_%s.fits"
        cls.setup2()

class Test1659(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1659_%s.fits"
        cls.setup2()

class Test1660(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1660_%s.fits"
        cls.setup2()

class Test1661(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f689m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1661_%s.fits"
        cls.setup2()

class Test1662(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1662_%s.fits"
        cls.setup2()

class Test1663(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1663_%s.fits"
        cls.setup2()

class Test1664(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f763m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1664_%s.fits"
        cls.setup2()

class Test1665(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1665_%s.fits"
        cls.setup2()

class Test1666(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1666_%s.fits"
        cls.setup2()

class Test1667(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1667_%s.fits"
        cls.setup2()

class Test1668(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1668_%s.fits"
        cls.setup2()

class Test1669(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1669_%s.fits"
        cls.setup2()

class Test1670(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1670_%s.fits"
        cls.setup2()

class Test1671(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1671_%s.fits"
        cls.setup2()

class Test1672(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1672_%s.fits"
        cls.setup2()

class Test1673(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1673_%s.fits"
        cls.setup2()

class Test1674(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1674_%s.fits"
        cls.setup2()

class Test1675(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1675_%s.fits"
        cls.setup2()

class Test1676(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1676_%s.fits"
        cls.setup2()

class Test1677(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1677_%s.fits"
        cls.setup2()

class Test1678(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1678_%s.fits"
        cls.setup2()

class Test1679(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1679_%s.fits"
        cls.setup2()

class Test1680(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1680_%s.fits"
        cls.setup2()

class Test1681(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1681_%s.fits"
        cls.setup2()

class Test1682(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1682_%s.fits"
        cls.setup2()

class Test1683(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1683_%s.fits"
        cls.setup2()

class Test1684(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1684_%s.fits"
        cls.setup2()

class Test1685(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1685_%s.fits"
        cls.setup2()

class Test1686(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1686_%s.fits"
        cls.setup2()

class Test1687(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1687_%s.fits"
        cls.setup2()

class Test1688(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1688_%s.fits"
        cls.setup2()

class Test1689(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1689_%s.fits"
        cls.setup2()

class Test1690(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1690_%s.fits"
        cls.setup2()

class Test1691(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1691_%s.fits"
        cls.setup2()

class Test1692(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1692_%s.fits"
        cls.setup2()

class Test1693(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1693_%s.fits"
        cls.setup2()

class Test1694(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1694_%s.fits"
        cls.setup2()

class Test1695(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1695_%s.fits"
        cls.setup2()

class Test1696(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1696_%s.fits"
        cls.setup2()

class Test1697(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1697_%s.fits"
        cls.setup2()

class Test1698(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1698_%s.fits"
        cls.setup2()

class Test1699(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1699_%s.fits"
        cls.setup2()

class Test1700(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1700_%s.fits"
        cls.setup2()

class Test1701(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1701_%s.fits"
        cls.setup2()

class Test1702(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1702_%s.fits"
        cls.setup2()

class Test1703(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1703_%s.fits"
        cls.setup2()

class Test1704(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1704_%s.fits"
        cls.setup2()

class Test1705(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1705_%s.fits"
        cls.setup2()

class Test1706(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1706_%s.fits"
        cls.setup2()

class Test1707(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1707_%s.fits"
        cls.setup2()

class Test1708(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1708_%s.fits"
        cls.setup2()

class Test1709(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1709_%s.fits"
        cls.setup2()

class Test1710(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1710_%s.fits"
        cls.setup2()

class Test1711(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1711_%s.fits"
        cls.setup2()

class Test1712(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1712_%s.fits"
        cls.setup2()

class Test1713(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1713_%s.fits"
        cls.setup2()

class Test1714(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1714_%s.fits"
        cls.setup2()

class Test1715(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1715_%s.fits"
        cls.setup2()

class Test1716(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1716_%s.fits"
        cls.setup2()

class Test1717(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1717_%s.fits"
        cls.setup2()

class Test1718(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1718_%s.fits"
        cls.setup2()

class Test1719(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1719_%s.fits"
        cls.setup2()

class Test1720(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1720_%s.fits"
        cls.setup2()

class Test1721(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1721_%s.fits"
        cls.setup2()

class Test1722(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1722_%s.fits"
        cls.setup2()

class Test1723(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1723_%s.fits"
        cls.setup2()

class Test1724(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1724_%s.fits"
        cls.setup2()

class Test1725(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1725_%s.fits"
        cls.setup2()

class Test1726(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1726_%s.fits"
        cls.setup2()

class Test1727(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1727_%s.fits"
        cls.setup2()

class Test1728(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1728_%s.fits"
        cls.setup2()

class Test1729(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1729_%s.fits"
        cls.setup2()

class Test1730(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1730_%s.fits"
        cls.setup2()

class Test1731(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1731_%s.fits"
        cls.setup2()

class Test1732(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1732_%s.fits"
        cls.setup2()

class Test1733(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1733_%s.fits"
        cls.setup2()

class Test1734(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1734_%s.fits"
        cls.setup2()

class Test1735(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1735_%s.fits"
        cls.setup2()

class Test1736(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1736_%s.fits"
        cls.setup2()

class Test1737(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1737_%s.fits"
        cls.setup2()

class Test1738(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1738_%s.fits"
        cls.setup2()

class Test1739(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1739_%s.fits"
        cls.setup2()

class Test1740(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1740_%s.fits"
        cls.setup2()

class Test1741(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1741_%s.fits"
        cls.setup2()

class Test1742(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1742_%s.fits"
        cls.setup2()

class Test1743(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1743_%s.fits"
        cls.setup2()

class Test1744(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1744_%s.fits"
        cls.setup2()

class Test1745(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f845m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1745_%s.fits"
        cls.setup2()

class Test1746(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1746_%s.fits"
        cls.setup2()

class Test1747(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1747_%s.fits"
        cls.setup2()

class Test1748(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        cls.fname="C1748_%s.fits"
        cls.setup2()

class Test1749(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        cls.fname="C1749_%s.fits"
        cls.setup2()

class Test1750(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        cls.fname="C1750_%s.fits"
        cls.setup2()

class Test1751(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1751_%s.fits"
        cls.setup2()

class Test1752(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1752_%s.fits"
        cls.setup2()

class Test1753(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1753_%s.fits"
        cls.setup2()

class Test1754(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1754_%s.fits"
        cls.setup2()

class Test1755(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1755_%s.fits"
        cls.setup2()

class Test1756(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1756_%s.fits"
        cls.setup2()

class Test1757(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f953n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1757_%s.fits"
        cls.setup2()

class Test1758(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1758_%s.fits"
        cls.setup2()

class Test1759(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1759_%s.fits"
        cls.setup2()

class Test1760(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq232n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1760_%s.fits"
        cls.setup2()

class Test1761(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1761_%s.fits"
        cls.setup2()

class Test1762(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1762_%s.fits"
        cls.setup2()

class Test1763(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq243n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1763_%s.fits"
        cls.setup2()

class Test1764(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1764_%s.fits"
        cls.setup2()

class Test1765(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1765_%s.fits"
        cls.setup2()

class Test1766(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq378n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1766_%s.fits"
        cls.setup2()

class Test1767(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1767_%s.fits"
        cls.setup2()

class Test1768(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1768_%s.fits"
        cls.setup2()

class Test1769(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq387n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1769_%s.fits"
        cls.setup2()

class Test1770(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1770_%s.fits"
        cls.setup2()

class Test1771(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1771_%s.fits"
        cls.setup2()

class Test1772(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq422m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1772_%s.fits"
        cls.setup2()

class Test1773(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1773_%s.fits"
        cls.setup2()

class Test1774(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1774_%s.fits"
        cls.setup2()

class Test1775(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq436n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1775_%s.fits"
        cls.setup2()

class Test1776(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1776_%s.fits"
        cls.setup2()

class Test1777(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1777_%s.fits"
        cls.setup2()

class Test1778(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq437n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1778_%s.fits"
        cls.setup2()

class Test1779(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1779_%s.fits"
        cls.setup2()

class Test1780(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1780_%s.fits"
        cls.setup2()

class Test1781(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq492n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1781_%s.fits"
        cls.setup2()

class Test1782(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1782_%s.fits"
        cls.setup2()

class Test1783(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1783_%s.fits"
        cls.setup2()

class Test1784(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1784_%s.fits"
        cls.setup2()

class Test1785(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1785_%s.fits"
        cls.setup2()

class Test1786(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1786_%s.fits"
        cls.setup2()

class Test1787(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1787_%s.fits"
        cls.setup2()

class Test1788(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1788_%s.fits"
        cls.setup2()

class Test1789(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1789_%s.fits"
        cls.setup2()

class Test1790(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1790_%s.fits"
        cls.setup2()

class Test1791(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1791_%s.fits"
        cls.setup2()

class Test1792(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1792_%s.fits"
        cls.setup2()

class Test1793(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1793_%s.fits"
        cls.setup2()

class Test1794(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1794_%s.fits"
        cls.setup2()

class Test1795(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1795_%s.fits"
        cls.setup2()

class Test1796(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1796_%s.fits"
        cls.setup2()

class Test1797(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1797_%s.fits"
        cls.setup2()

class Test1798(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1798_%s.fits"
        cls.setup2()

class Test1799(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1799_%s.fits"
        cls.setup2()

class Test1800(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1800_%s.fits"
        cls.setup2()

class Test1801(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1801_%s.fits"
        cls.setup2()

class Test1802(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1802_%s.fits"
        cls.setup2()

class Test1803(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1803_%s.fits"
        cls.setup2()

class Test1804(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1804_%s.fits"
        cls.setup2()

class Test1805(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1805_%s.fits"
        cls.setup2()

class Test1806(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1806_%s.fits"
        cls.setup2()

class Test1807(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1807_%s.fits"
        cls.setup2()

class Test1808(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1808_%s.fits"
        cls.setup2()

class Test1809(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1809_%s.fits"
        cls.setup2()

class Test1810(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1810_%s.fits"
        cls.setup2()

class Test1811(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1811_%s.fits"
        cls.setup2()

class Test1812(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1812_%s.fits"
        cls.setup2()

class Test1813(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1813_%s.fits"
        cls.setup2()

class Test1814(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1814_%s.fits"
        cls.setup2()

class Test1815(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1815_%s.fits"
        cls.setup2()

class Test1816(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1816_%s.fits"
        cls.setup2()

class Test1817(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1817_%s.fits"
        cls.setup2()

class Test1818(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        cls.fname="C1818_%s.fits"
        cls.setup2()

class Test1819(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        cls.fname="C1819_%s.fits"
        cls.setup2()

class Test1820(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        cls.fname="C1820_%s.fits"
        cls.setup2()

class Test1821(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        cls.fname="C1821_%s.fits"
        cls.setup2()

class Test1822(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        cls.fname="C1822_%s.fits"
        cls.setup2()

class Test1823(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        cls.fname="C1823_%s.fits"
        cls.setup2()

class Test1824(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1824_%s.fits"
        cls.setup2()

class Test1825(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1825_%s.fits"
        cls.setup2()

class Test1826(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        cls.fname="C1826_%s.fits"
        cls.setup2()

class Test1827(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1827_%s.fits"
        cls.setup2()

class Test1828(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1828_%s.fits"
        cls.setup2()

class Test1829(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        cls.fname="C1829_%s.fits"
        cls.setup2()

class Test1830(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C1830_%s.fits"
        cls.setup2()

class Test1831(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C1831_%s.fits"
        cls.setup2()

class Test1832(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C1832_%s.fits"
        cls.setup2()

class Test1833(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        cls.fname="C1833_%s.fits"
        cls.setup2()

class Test1834(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        cls.fname="C1834_%s.fits"
        cls.setup2()

class Test1835(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        cls.fname="C1835_%s.fits"
        cls.setup2()

class Test1836(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1836_%s.fits"
        cls.setup2()

class Test1837(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1837_%s.fits"
        cls.setup2()

class Test1838(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1838_%s.fits"
        cls.setup2()

class Test1839(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1839_%s.fits"
        cls.setup2()

class Test1840(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1840_%s.fits"
        cls.setup2()

class Test1841(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1841_%s.fits"
        cls.setup2()

class Test1842(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1842_%s.fits"
        cls.setup2()

class Test1843(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1843_%s.fits"
        cls.setup2()

class Test1844(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1844_%s.fits"
        cls.setup2()

class Test1845(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1845_%s.fits"
        cls.setup2()

class Test1846(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1846_%s.fits"
        cls.setup2()

class Test1847(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1847_%s.fits"
        cls.setup2()

class Test1848(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1848_%s.fits"
        cls.setup2()

class Test1849(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1849_%s.fits"
        cls.setup2()

class Test1850(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        cls.fname="C1850_%s.fits"
        cls.setup2()

class Test1851(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1851_%s.fits"
        cls.setup2()

class Test1852(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        cls.fname="C1852_%s.fits"
        cls.setup2()

class Test1853(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1853_%s.fits"
        cls.setup2()

class Test1854(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1854_%s.fits"
        cls.setup2()

class Test1855(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1855_%s.fits"
        cls.setup2()

class Test1856(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1856_%s.fits"
        cls.setup2()

class Test1857(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1857_%s.fits"
        cls.setup2()

class Test1858(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1858_%s.fits"
        cls.setup2()

class Test1859(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1859_%s.fits"
        cls.setup2()

class Test1860(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1860_%s.fits"
        cls.setup2()

class Test1861(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1861_%s.fits"
        cls.setup2()

