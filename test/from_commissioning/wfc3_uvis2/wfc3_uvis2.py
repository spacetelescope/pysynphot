import os
import sys
sys.path.append('..')
import conv_base
conv_base.HERE = os.path.abspath(os.path.dirname(__file__))

class Test1862(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1862_%s.fits"
        cls.setup2()

class Test1863(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1863_%s.fits"
        cls.setup2()

class Test1864(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f200lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1864_%s.fits"
        cls.setup2()

class Test1865(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1865_%s.fits"
        cls.setup2()

class Test1866(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1866_%s.fits"
        cls.setup2()

class Test1867(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f218w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1867_%s.fits"
        cls.setup2()

class Test1868(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1868_%s.fits"
        cls.setup2()

class Test1869(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1869_%s.fits"
        cls.setup2()

class Test1870(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        cls.fname="C1870_%s.fits"
        cls.setup2()

class Test1871(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        cls.fname="C1871_%s.fits"
        cls.setup2()

class Test1872(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        cls.fname="C1872_%s.fits"
        cls.setup2()

class Test1873(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        cls.fname="C1873_%s.fits"
        cls.setup2()

class Test1874(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1874_%s.fits"
        cls.setup2()

class Test1875(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1875_%s.fits"
        cls.setup2()

class Test1876(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1876_%s.fits"
        cls.setup2()

class Test1877(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1877_%s.fits"
        cls.setup2()

class Test1878(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1878_%s.fits"
        cls.setup2()

class Test1879(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1879_%s.fits"
        cls.setup2()

class Test1880(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f275w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1880_%s.fits"
        cls.setup2()

class Test1881(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1881_%s.fits"
        cls.setup2()

class Test1882(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1882_%s.fits"
        cls.setup2()

class Test1883(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f280n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1883_%s.fits"
        cls.setup2()

class Test1884(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        cls.fname="C1884_%s.fits"
        cls.setup2()

class Test1885(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        cls.fname="C1885_%s.fits"
        cls.setup2()

class Test1886(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        cls.fname="C1886_%s.fits"
        cls.setup2()

class Test1887(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        cls.fname="C1887_%s.fits"
        cls.setup2()

class Test1888(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        cls.fname="C1888_%s.fits"
        cls.setup2()

class Test1889(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        cls.fname="C1889_%s.fits"
        cls.setup2()

class Test1890(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1890_%s.fits"
        cls.setup2()

class Test1891(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1891_%s.fits"
        cls.setup2()

class Test1892(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1892_%s.fits"
        cls.setup2()

class Test1893(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1893_%s.fits"
        cls.setup2()

class Test1894(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1894_%s.fits"
        cls.setup2()

class Test1895(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1895_%s.fits"
        cls.setup2()

class Test1896(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1896_%s.fits"
        cls.setup2()

class Test1897(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1897_%s.fits"
        cls.setup2()

class Test1898(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1898_%s.fits"
        cls.setup2()

class Test1899(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1899_%s.fits"
        cls.setup2()

class Test1900(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f336w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1900_%s.fits"
        cls.setup2()

class Test1901(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1901_%s.fits"
        cls.setup2()

class Test1902(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1902_%s.fits"
        cls.setup2()

class Test1903(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f343n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1903_%s.fits"
        cls.setup2()

class Test1904(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1904_%s.fits"
        cls.setup2()

class Test1905(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1905_%s.fits"
        cls.setup2()

class Test1906(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f350lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1906_%s.fits"
        cls.setup2()

class Test1907(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1907_%s.fits"
        cls.setup2()

class Test1908(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1908_%s.fits"
        cls.setup2()

class Test1909(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f373n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1909_%s.fits"
        cls.setup2()

class Test1910(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1910_%s.fits"
        cls.setup2()

class Test1911(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1911_%s.fits"
        cls.setup2()

class Test1912(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1912_%s.fits"
        cls.setup2()

class Test1913(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1913_%s.fits"
        cls.setup2()

class Test1914(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1914_%s.fits"
        cls.setup2()

class Test1915(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1915_%s.fits"
        cls.setup2()

class Test1916(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1916_%s.fits"
        cls.setup2()

class Test1917(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1917_%s.fits"
        cls.setup2()

class Test1918(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1918_%s.fits"
        cls.setup2()

class Test1919(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1919_%s.fits"
        cls.setup2()

class Test1920(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1920_%s.fits"
        cls.setup2()

class Test1921(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1921_%s.fits"
        cls.setup2()

class Test1922(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1922_%s.fits"
        cls.setup2()

class Test1923(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1923_%s.fits"
        cls.setup2()

class Test1924(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1924_%s.fits"
        cls.setup2()

class Test1925(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1925_%s.fits"
        cls.setup2()

class Test1926(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1926_%s.fits"
        cls.setup2()

class Test1927(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1927_%s.fits"
        cls.setup2()

class Test1928(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1928_%s.fits"
        cls.setup2()

class Test1929(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1929_%s.fits"
        cls.setup2()

class Test1930(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1930_%s.fits"
        cls.setup2()

class Test1931(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1931_%s.fits"
        cls.setup2()

class Test1932(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1932_%s.fits"
        cls.setup2()

class Test1933(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1933_%s.fits"
        cls.setup2()

class Test1934(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1934_%s.fits"
        cls.setup2()

class Test1935(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1935_%s.fits"
        cls.setup2()

class Test1936(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1936_%s.fits"
        cls.setup2()

class Test1937(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1937_%s.fits"
        cls.setup2()

class Test1938(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1938_%s.fits"
        cls.setup2()

class Test1939(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1939_%s.fits"
        cls.setup2()

class Test1940(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1940_%s.fits"
        cls.setup2()

class Test1941(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1941_%s.fits"
        cls.setup2()

class Test1942(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        cls.fname="C1942_%s.fits"
        cls.setup2()

class Test1943(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1943_%s.fits"
        cls.setup2()

class Test1944(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1944_%s.fits"
        cls.setup2()

class Test1945(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1945_%s.fits"
        cls.setup2()

class Test1946(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1946_%s.fits"
        cls.setup2()

class Test1947(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1947_%s.fits"
        cls.setup2()

class Test1948(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1948_%s.fits"
        cls.setup2()

class Test1949(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1949_%s.fits"
        cls.setup2()

class Test1950(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1950_%s.fits"
        cls.setup2()

class Test1951(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1951_%s.fits"
        cls.setup2()

class Test1952(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1952_%s.fits"
        cls.setup2()

class Test1953(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1953_%s.fits"
        cls.setup2()

class Test1954(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1954_%s.fits"
        cls.setup2()

class Test1955(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1955_%s.fits"
        cls.setup2()

class Test1956(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1956_%s.fits"
        cls.setup2()

class Test1957(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1957_%s.fits"
        cls.setup2()

class Test1958(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1958_%s.fits"
        cls.setup2()

class Test1959(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1959_%s.fits"
        cls.setup2()

class Test1960(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1960_%s.fits"
        cls.setup2()

class Test1961(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1961_%s.fits"
        cls.setup2()

class Test1962(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1962_%s.fits"
        cls.setup2()

class Test1963(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1963_%s.fits"
        cls.setup2()

class Test1964(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1964_%s.fits"
        cls.setup2()

class Test1965(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1965_%s.fits"
        cls.setup2()

class Test1966(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1966_%s.fits"
        cls.setup2()

class Test1967(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1967_%s.fits"
        cls.setup2()

class Test1968(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1968_%s.fits"
        cls.setup2()

class Test1969(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1969_%s.fits"
        cls.setup2()

class Test1970(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1970_%s.fits"
        cls.setup2()

class Test1971(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1971_%s.fits"
        cls.setup2()

class Test1972(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1972_%s.fits"
        cls.setup2()

class Test1973(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1973_%s.fits"
        cls.setup2()

class Test1974(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1974_%s.fits"
        cls.setup2()

class Test1975(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1975_%s.fits"
        cls.setup2()

class Test1976(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1976_%s.fits"
        cls.setup2()

class Test1977(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1977_%s.fits"
        cls.setup2()

class Test1978(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1978_%s.fits"
        cls.setup2()

class Test1979(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1979_%s.fits"
        cls.setup2()

class Test1980(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f600lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1980_%s.fits"
        cls.setup2()

class Test1981(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1981_%s.fits"
        cls.setup2()

class Test1982(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1982_%s.fits"
        cls.setup2()

class Test1983(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1983_%s.fits"
        cls.setup2()

class Test1984(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1984_%s.fits"
        cls.setup2()

class Test1985(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1985_%s.fits"
        cls.setup2()

class Test1986(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1986_%s.fits"
        cls.setup2()

class Test1987(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1987_%s.fits"
        cls.setup2()

class Test1988(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1988_%s.fits"
        cls.setup2()

class Test1989(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1989_%s.fits"
        cls.setup2()

class Test1990(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1990_%s.fits"
        cls.setup2()

class Test1991(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1991_%s.fits"
        cls.setup2()

class Test1992(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1992_%s.fits"
        cls.setup2()

class Test1993(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1993_%s.fits"
        cls.setup2()

class Test1994(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1994_%s.fits"
        cls.setup2()

class Test1995(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1995_%s.fits"
        cls.setup2()

class Test1996(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1996_%s.fits"
        cls.setup2()

class Test1997(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1997_%s.fits"
        cls.setup2()

class Test1998(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1998_%s.fits"
        cls.setup2()

class Test1999(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1999_%s.fits"
        cls.setup2()

class Test2000(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2000_%s.fits"
        cls.setup2()

class Test2001(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2001_%s.fits"
        cls.setup2()

class Test2002(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2002_%s.fits"
        cls.setup2()

class Test2003(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2003_%s.fits"
        cls.setup2()

class Test2004(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C2004_%s.fits"
        cls.setup2()

class Test2005(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2005_%s.fits"
        cls.setup2()

class Test2006(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2006_%s.fits"
        cls.setup2()

class Test2007(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2007_%s.fits"
        cls.setup2()

class Test2008(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2008_%s.fits"
        cls.setup2()

class Test2009(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2009_%s.fits"
        cls.setup2()

class Test2010(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f621m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2010_%s.fits"
        cls.setup2()

class Test2011(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2011_%s.fits"
        cls.setup2()

class Test2012(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2012_%s.fits"
        cls.setup2()

class Test2013(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2013_%s.fits"
        cls.setup2()

class Test2014(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2014_%s.fits"
        cls.setup2()

class Test2015(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2015_%s.fits"
        cls.setup2()

class Test2016(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f631n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2016_%s.fits"
        cls.setup2()

class Test2017(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2017_%s.fits"
        cls.setup2()

class Test2018(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2018_%s.fits"
        cls.setup2()

class Test2019(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f645n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2019_%s.fits"
        cls.setup2()

class Test2020(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2020_%s.fits"
        cls.setup2()

class Test2021(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2021_%s.fits"
        cls.setup2()

class Test2022(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f656n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2022_%s.fits"
        cls.setup2()

class Test2023(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2023_%s.fits"
        cls.setup2()

class Test2024(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2024_%s.fits"
        cls.setup2()

class Test2025(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f657n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2025_%s.fits"
        cls.setup2()

class Test2026(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2026_%s.fits"
        cls.setup2()

class Test2027(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2027_%s.fits"
        cls.setup2()

class Test2028(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2028_%s.fits"
        cls.setup2()

class Test2029(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2029_%s.fits"
        cls.setup2()

class Test2030(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2030_%s.fits"
        cls.setup2()

class Test2031(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f665n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2031_%s.fits"
        cls.setup2()

class Test2032(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2032_%s.fits"
        cls.setup2()

class Test2033(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2033_%s.fits"
        cls.setup2()

class Test2034(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f673n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2034_%s.fits"
        cls.setup2()

class Test2035(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2035_%s.fits"
        cls.setup2()

class Test2036(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2036_%s.fits"
        cls.setup2()

class Test2037(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f680n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2037_%s.fits"
        cls.setup2()

class Test2038(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2038_%s.fits"
        cls.setup2()

class Test2039(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2039_%s.fits"
        cls.setup2()

class Test2040(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f689m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2040_%s.fits"
        cls.setup2()

class Test2041(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2041_%s.fits"
        cls.setup2()

class Test2042(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2042_%s.fits"
        cls.setup2()

class Test2043(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f763m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2043_%s.fits"
        cls.setup2()

class Test2044(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2044_%s.fits"
        cls.setup2()

class Test2045(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2045_%s.fits"
        cls.setup2()

class Test2046(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2046_%s.fits"
        cls.setup2()

class Test2047(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2047_%s.fits"
        cls.setup2()

class Test2048(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2048_%s.fits"
        cls.setup2()

class Test2049(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2049_%s.fits"
        cls.setup2()

class Test2050(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2050_%s.fits"
        cls.setup2()

class Test2051(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2051_%s.fits"
        cls.setup2()

class Test2052(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2052_%s.fits"
        cls.setup2()

class Test2053(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2053_%s.fits"
        cls.setup2()

class Test2054(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2054_%s.fits"
        cls.setup2()

class Test2055(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2055_%s.fits"
        cls.setup2()

class Test2056(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2056_%s.fits"
        cls.setup2()

class Test2057(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2057_%s.fits"
        cls.setup2()

class Test2058(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2058_%s.fits"
        cls.setup2()

class Test2059(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2059_%s.fits"
        cls.setup2()

class Test2060(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2060_%s.fits"
        cls.setup2()

class Test2061(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2061_%s.fits"
        cls.setup2()

class Test2062(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2062_%s.fits"
        cls.setup2()

class Test2063(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2063_%s.fits"
        cls.setup2()

class Test2064(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2064_%s.fits"
        cls.setup2()

class Test2065(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2065_%s.fits"
        cls.setup2()

class Test2066(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2066_%s.fits"
        cls.setup2()

class Test2067(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2067_%s.fits"
        cls.setup2()

class Test2068(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2068_%s.fits"
        cls.setup2()

class Test2069(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2069_%s.fits"
        cls.setup2()

class Test2070(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2070_%s.fits"
        cls.setup2()

class Test2071(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2071_%s.fits"
        cls.setup2()

class Test2072(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2072_%s.fits"
        cls.setup2()

class Test2073(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2073_%s.fits"
        cls.setup2()

class Test2074(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2074_%s.fits"
        cls.setup2()

class Test2075(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2075_%s.fits"
        cls.setup2()

class Test2076(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2076_%s.fits"
        cls.setup2()

class Test2077(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2077_%s.fits"
        cls.setup2()

class Test2078(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2078_%s.fits"
        cls.setup2()

class Test2079(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2079_%s.fits"
        cls.setup2()

class Test2080(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2080_%s.fits"
        cls.setup2()

class Test2081(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2081_%s.fits"
        cls.setup2()

class Test2082(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2082_%s.fits"
        cls.setup2()

class Test2083(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2083_%s.fits"
        cls.setup2()

class Test2084(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2084_%s.fits"
        cls.setup2()

class Test2085(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2085_%s.fits"
        cls.setup2()

class Test2086(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2086_%s.fits"
        cls.setup2()

class Test2087(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2087_%s.fits"
        cls.setup2()

class Test2088(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2088_%s.fits"
        cls.setup2()

class Test2089(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2089_%s.fits"
        cls.setup2()

class Test2090(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2090_%s.fits"
        cls.setup2()

class Test2091(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2091_%s.fits"
        cls.setup2()

class Test2092(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2092_%s.fits"
        cls.setup2()

class Test2093(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2093_%s.fits"
        cls.setup2()

class Test2094(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2094_%s.fits"
        cls.setup2()

class Test2095(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2095_%s.fits"
        cls.setup2()

class Test2096(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2096_%s.fits"
        cls.setup2()

class Test2097(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2097_%s.fits"
        cls.setup2()

class Test2098(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2098_%s.fits"
        cls.setup2()

class Test2099(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2099_%s.fits"
        cls.setup2()

class Test2100(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2100_%s.fits"
        cls.setup2()

class Test2101(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2101_%s.fits"
        cls.setup2()

class Test2102(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2102_%s.fits"
        cls.setup2()

class Test2103(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2103_%s.fits"
        cls.setup2()

class Test2104(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2104_%s.fits"
        cls.setup2()

class Test2105(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2105_%s.fits"
        cls.setup2()

class Test2106(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2106_%s.fits"
        cls.setup2()

class Test2107(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2107_%s.fits"
        cls.setup2()

class Test2108(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2108_%s.fits"
        cls.setup2()

class Test2109(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2109_%s.fits"
        cls.setup2()

class Test2110(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2110_%s.fits"
        cls.setup2()

class Test2111(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2111_%s.fits"
        cls.setup2()

class Test2112(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2112_%s.fits"
        cls.setup2()

class Test2113(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2113_%s.fits"
        cls.setup2()

class Test2114(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2114_%s.fits"
        cls.setup2()

class Test2115(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2115_%s.fits"
        cls.setup2()

class Test2116(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2116_%s.fits"
        cls.setup2()

class Test2117(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2117_%s.fits"
        cls.setup2()

class Test2118(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2118_%s.fits"
        cls.setup2()

class Test2119(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2119_%s.fits"
        cls.setup2()

class Test2120(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2120_%s.fits"
        cls.setup2()

class Test2121(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2121_%s.fits"
        cls.setup2()

class Test2122(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2122_%s.fits"
        cls.setup2()

class Test2123(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2123_%s.fits"
        cls.setup2()

class Test2124(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f845m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2124_%s.fits"
        cls.setup2()

class Test2125(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2125_%s.fits"
        cls.setup2()

class Test2126(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2126_%s.fits"
        cls.setup2()

class Test2127(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        cls.fname="C2127_%s.fits"
        cls.setup2()

class Test2128(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        cls.fname="C2128_%s.fits"
        cls.setup2()

class Test2129(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        cls.fname="C2129_%s.fits"
        cls.setup2()

class Test2130(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2130_%s.fits"
        cls.setup2()

class Test2131(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2131_%s.fits"
        cls.setup2()

class Test2132(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2132_%s.fits"
        cls.setup2()

class Test2133(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2133_%s.fits"
        cls.setup2()

class Test2134(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2134_%s.fits"
        cls.setup2()

class Test2135(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2135_%s.fits"
        cls.setup2()

class Test2136(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f953n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2136_%s.fits"
        cls.setup2()

class Test2137(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2137_%s.fits"
        cls.setup2()

class Test2138(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2138_%s.fits"
        cls.setup2()

class Test2139(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq232n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2139_%s.fits"
        cls.setup2()

class Test2140(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2140_%s.fits"
        cls.setup2()

class Test2141(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2141_%s.fits"
        cls.setup2()

class Test2142(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq243n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2142_%s.fits"
        cls.setup2()

class Test2143(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2143_%s.fits"
        cls.setup2()

class Test2144(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2144_%s.fits"
        cls.setup2()

class Test2145(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq378n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2145_%s.fits"
        cls.setup2()

class Test2146(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2146_%s.fits"
        cls.setup2()

class Test2147(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2147_%s.fits"
        cls.setup2()

class Test2148(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq387n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2148_%s.fits"
        cls.setup2()

class Test2149(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2149_%s.fits"
        cls.setup2()

class Test2150(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2150_%s.fits"
        cls.setup2()

class Test2151(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq422m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2151_%s.fits"
        cls.setup2()

class Test2152(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2152_%s.fits"
        cls.setup2()

class Test2153(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2153_%s.fits"
        cls.setup2()

class Test2154(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq436n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2154_%s.fits"
        cls.setup2()

class Test2155(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2155_%s.fits"
        cls.setup2()

class Test2156(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2156_%s.fits"
        cls.setup2()

class Test2157(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq437n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2157_%s.fits"
        cls.setup2()

class Test2158(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2158_%s.fits"
        cls.setup2()

class Test2159(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2159_%s.fits"
        cls.setup2()

class Test2160(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq492n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2160_%s.fits"
        cls.setup2()

class Test2161(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2161_%s.fits"
        cls.setup2()

class Test2162(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2162_%s.fits"
        cls.setup2()

class Test2163(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq508n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2163_%s.fits"
        cls.setup2()

class Test2164(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2164_%s.fits"
        cls.setup2()

class Test2165(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2165_%s.fits"
        cls.setup2()

class Test2166(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq575n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2166_%s.fits"
        cls.setup2()

class Test2167(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2167_%s.fits"
        cls.setup2()

class Test2168(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2168_%s.fits"
        cls.setup2()

class Test2169(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq619n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2169_%s.fits"
        cls.setup2()

class Test2170(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2170_%s.fits"
        cls.setup2()

class Test2171(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2171_%s.fits"
        cls.setup2()

class Test2172(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq634n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2172_%s.fits"
        cls.setup2()

class Test2173(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2173_%s.fits"
        cls.setup2()

class Test2174(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2174_%s.fits"
        cls.setup2()

class Test2175(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq672n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2175_%s.fits"
        cls.setup2()

class Test2176(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2176_%s.fits"
        cls.setup2()

class Test2177(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2177_%s.fits"
        cls.setup2()

class Test2178(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq674n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2178_%s.fits"
        cls.setup2()

class Test2179(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2179_%s.fits"
        cls.setup2()

class Test2180(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2180_%s.fits"
        cls.setup2()

class Test2181(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq727n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2181_%s.fits"
        cls.setup2()

class Test2182(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2182_%s.fits"
        cls.setup2()

class Test2183(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2183_%s.fits"
        cls.setup2()

class Test2184(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq750n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2184_%s.fits"
        cls.setup2()

class Test2185(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2185_%s.fits"
        cls.setup2()

class Test2186(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2186_%s.fits"
        cls.setup2()

class Test2187(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq889n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2187_%s.fits"
        cls.setup2()

class Test2188(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2188_%s.fits"
        cls.setup2()

class Test2189(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2189_%s.fits"
        cls.setup2()

class Test2190(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq906n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2190_%s.fits"
        cls.setup2()

class Test2191(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2191_%s.fits"
        cls.setup2()

class Test2192(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2192_%s.fits"
        cls.setup2()

class Test2193(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq924n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2193_%s.fits"
        cls.setup2()

class Test2194(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2194_%s.fits"
        cls.setup2()

class Test2195(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2195_%s.fits"
        cls.setup2()

class Test2196(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq937n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2196_%s.fits"
        cls.setup2()

class Test2197(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        cls.fname="C2197_%s.fits"
        cls.setup2()

class Test2198(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        cls.fname="C2198_%s.fits"
        cls.setup2()

class Test2199(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        cls.fname="C2199_%s.fits"
        cls.setup2()

class Test2200(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        cls.fname="C2200_%s.fits"
        cls.setup2()

class Test2201(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        cls.fname="C2201_%s.fits"
        cls.setup2()

class Test2202(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        cls.fname="C2202_%s.fits"
        cls.setup2()

class Test2203(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        cls.fname="C2203_%s.fits"
        cls.setup2()

class Test2204(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        cls.fname="C2204_%s.fits"
        cls.setup2()

class Test2205(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        cls.fname="C2205_%s.fits"
        cls.setup2()

class Test2206(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C2206_%s.fits"
        cls.setup2()

class Test2207(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C2207_%s.fits"
        cls.setup2()

class Test2208(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        cls.fname="C2208_%s.fits"
        cls.setup2()

class Test2209(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C2209_%s.fits"
        cls.setup2()

class Test2210(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C2210_%s.fits"
        cls.setup2()

class Test2211(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C2211_%s.fits"
        cls.setup2()

class Test2212(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        cls.fname="C2212_%s.fits"
        cls.setup2()

class Test2213(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        cls.fname="C2213_%s.fits"
        cls.setup2()

class Test2214(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        cls.fname="C2214_%s.fits"
        cls.setup2()

class Test2215(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2215_%s.fits"
        cls.setup2()

class Test2216(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2216_%s.fits"
        cls.setup2()

class Test2217(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2217_%s.fits"
        cls.setup2()

class Test2218(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2218_%s.fits"
        cls.setup2()

class Test2219(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2219_%s.fits"
        cls.setup2()

class Test2220(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2220_%s.fits"
        cls.setup2()

class Test2221(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2221_%s.fits"
        cls.setup2()

class Test2222(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2222_%s.fits"
        cls.setup2()

class Test2223(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2223_%s.fits"
        cls.setup2()

class Test2224(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2224_%s.fits"
        cls.setup2()

class Test2225(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2225_%s.fits"
        cls.setup2()

class Test2226(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2226_%s.fits"
        cls.setup2()

class Test2227(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2227_%s.fits"
        cls.setup2()

class Test2228(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2228_%s.fits"
        cls.setup2()

class Test2229(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        cls.fname="C2229_%s.fits"
        cls.setup2()

class Test2230(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        cls.fname="C2230_%s.fits"
        cls.setup2()

class Test2231(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        cls.fname="C2231_%s.fits"
        cls.setup2()

class Test2232(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2232_%s.fits"
        cls.setup2()

class Test2233(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2233_%s.fits"
        cls.setup2()

class Test2234(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2234_%s.fits"
        cls.setup2()

class Test2235(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2235_%s.fits"
        cls.setup2()

class Test2236(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2236_%s.fits"
        cls.setup2()

class Test2237(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2237_%s.fits"
        cls.setup2()

class Test2238(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2238_%s.fits"
        cls.setup2()

class Test2239(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2239_%s.fits"
        cls.setup2()

class Test2240(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2240_%s.fits"
        cls.setup2()

