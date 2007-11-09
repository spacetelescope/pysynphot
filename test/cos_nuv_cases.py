from cos_etc_test import ETCTestCase
from pysynphot.newetc import parse_spec
from pysynphot import ObsBandpass
from pytools import testutil
import sys



class C1(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g185m,c1786')
        self.ref_rate=4.8e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV1.fits'


class C2(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c1786')
        self.ref_rate=1494.47
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV2.fits'


class C3(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g185m,c1817')
        self.ref_rate=6e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV3.fits'


class C4(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c1817')
        self.ref_rate=1548.66
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV4.fits'


class C5(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g185m,c1835')
        self.ref_rate=6.4e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV5.fits'


class C6(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c1835')
        self.ref_rate=1559.37
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV6.fits'


class C7(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g185m,c1850')
        self.ref_rate=6.7e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV7.fits'


class C8(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c1850')
        self.ref_rate=1571.19
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV8.fits'


class C9(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g185m,c1864')
        self.ref_rate=7.7e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV9.fits'


class C10(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c1864')
        self.ref_rate=1587.16
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV10.fits'


class C11(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g185m,c1882')
        self.ref_rate=9.5e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV11.fits'


class C12(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c1882')
        self.ref_rate=1614.5
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV12.fits'


class C13(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g185m,c1890')
        self.ref_rate=0.000102
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV13.fits'


class C14(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(spec(qso_template.fits),box(1850.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c2010')
        self.ref_rate=72.6473
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV92.fits'


class C15(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(z(spec(qso_template.fits),0.2),box(1850.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c2010')
        self.ref_rate=47.2336
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV93.fits'


class C16(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(pl(4000.0,-1.0,flam),box(1850.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c2010')
        self.ref_rate=74.8768
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV94.fits'


class C17(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(pl(4000.0,-1.5,flam),box(1850.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c2010')
        self.ref_rate=71.8377
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV95.fits'


class C18(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(bb(10000.0),box(1850.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c2010')
        self.ref_rate=100.172
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV96.fits'


class C19(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(bb(40000.0),box(1850.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c2010')
        self.ref_rate=64.6011
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV97.fits'


class C20(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.1,gal1),box(1850.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g185m,c1786')
        self.ref_rate=1180.17
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV98.fits'


class C21(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g225m,c2186')
        self.ref_rate=0.000517
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV104.fits'


class C22(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,nuv,g225m,c2186')
        self.ref_rate=1460.12
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV105.fits'


class C23(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g225m,c2186')
        self.ref_rate=0.001553
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV106.fits'


class C24(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g225m,c2186')
        self.ref_rate=0.000892
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV107.fits'


class C25(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g225m,c2186')
        self.ref_rate=0.000899
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV108.fits'


class C26(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,nuv,g225m,c2186')
        self.ref_rate=0.000906
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV109.fits'


if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        if 'verbose' in sys.argv:
            testutil.testall(__name__,2)
        else:
            testutil.testall(__name__)
