from pysynphot.etctest_base_class import ETCTestCase
from pysynphot.newetc import parse_spec
from pysynphot import ObsBandpass, locations
from pysynphot import observationmode #to check on comptable
import testutil
import sys, os


print "%s:"%os.path.basename(__file__)
print "   Tests are being run with %s"%observationmode.COMPTABLE
print "   ETC comparison results were computed with r1j2146sm_tmc.fits"

testdir   = os.path.join(os.path.abspath(os.path.dirname(__file__)),'data')
#Also set the version of Vega for similar reasons
locations.VegaFile=os.path.join(testdir,
                                'alpha_lyr_stis_002.fits')
print "Using Vega spectrum: %s"%locations.VegaFile

class C1(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=28.9958
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV1.fits'



class C2(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=9017.31
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV2.fits'


class C3(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g130m,c1300')
        self.ref_rate=28.9958
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV3.fits'


class C4(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1310.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1300')
        self.ref_rate=9066.23
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV4.fits'


class C5(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g130m,c1309')
        self.ref_rate=26.5409
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV5.fits'


class C6(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1309')
        self.ref_rate=9472.55
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV6.fits'


class C7(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g130m,c1318')
        self.ref_rate=26.5469
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV7.fits'


class C8(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1330.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1318')
        self.ref_rate=9610.83
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV8.fits'


class C9(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g130m,c1327')
        self.ref_rate=29.2789
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV9.fits'


class C10(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1340.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1327')
        self.ref_rate=9684.13
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV10.fits'


class C11(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=3.75908e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV11.fits'
        self.accuracy=1e-2

class C12(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=15258.7
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV12.fits'


class C13(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1589')
        self.ref_rate=3.9e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV13.fits'
        self.accuracy=1e-2

class C14(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1589')
        self.ref_rate=15334.1
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV14.fits'


class C15(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1600')
        self.ref_rate=4.5e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV15.fits'
        self.accuracy=1e-2

class C16(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1600')
        self.ref_rate=15206.3
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV16.fits'


class C17(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1611')
        self.ref_rate=4.8e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV17.fits'
        self.accuracy=1e-2

class C18(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1611')
        self.ref_rate=14538.9
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV18.fits'


class C19(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1623')
        self.ref_rate=4.8e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV19.fits'
        self.accuracy=1e-2

class C20(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(2000.0,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1623')
        self.ref_rate=13659.4
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV20.fits'


class C21(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g140l,c1105')
        self.ref_rate=19.5333
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV21.fits'


class C22(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,33000.,0.0,4.0),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1105')
        self.ref_rate=695.416
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV22.fits'


class C23(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=1.97318
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV23.fits'


class C24(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,33000.,0.0,4.0),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=540.65
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV24.fits'


class C25(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230,boa')
        self.ref_rate=0.019732
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV25.fits'


class C26(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,33000.,0.0,4.0),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230,boa')
        self.ref_rate=5.4065
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV26.fits'


class C27(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(unit(1.0,flam),box(1309.0,1.0),1.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1309')
        self.ref_rate=4709.37
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV27.fits'


class C28(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=547.498
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV28.fits'


class C29(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,38000.,0.0,4.5),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=542.302
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV29.fits'


class C30(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,30000,0.0,4.0),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=556.808
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV30.fits'


class C31(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=588.07
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV31.fits'


class C32(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,18700,0.0,3.9),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=553.784
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV32.fits'


class C33(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,15400,0.0,3.9),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=498.295
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV33.fits'


class C34(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,11900,0.0,4.0),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=421.237
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV34.fits'


class C35(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,9230,0.0,4.1),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=381.215
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV35.fits'


class C36(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,8720,0.0,4.2),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=706.731
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV36.fits'


class C37(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,8200,0.0,4.3),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=5957.58
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV37.fits'


class C38(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,6890,0.0,4.3),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=28538.1
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV38.fits'


class C39(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(us1.dat)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=4836.31
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV39.fits'


class C40(ETCTestCase):
    def setparms(self):
        spname=os.path.join(os.environ['PYSYN_CDBS'],
                            'calspec',
                            'gd50_004.fits')
        self.sp=parse_spec('rn(spec(%s),box(1499.9999999999998,1.0),1.00E-14,flam)'%spname)
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=557.267
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV40.fits'


class C41(ETCTestCase):
    def setparms(self):
        spname=os.path.join(os.environ['PYSYN_CDBS'],
                            'calspec',
                            'feige110_stis_001.fits')
        self.sp=parse_spec('rn(spec(%s),box(1499.9999999999998,1.0),1.00E-14,flam)'%spname)
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=616.373
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV41.fits'


class C42(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(spec(qso_template.fits),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=549.397
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV42.fits'


class C43(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(z(spec(qso_template.fits),0.2),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=369.741
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV43.fits'


class C44(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(pl(4000.0,-1.0,flam),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=521.403
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV44.fits'


class C45(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(pl(4000.0,-1.5,flam),box(1499.9999999999998,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g140l,c1230')
        self.ref_rate=529.95
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV45.fits'


class C46(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(bb(10000.0),box(2000.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1600')
        self.ref_rate=190.373
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV46.fits'


class C47(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(bb(40000.0),box(2000.0,1.0),1.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1600')
        self.ref_rate=821.994
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV47.fits'


class C48(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.1,gal1),box(1320.0000000000002,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=8653.94
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV48.fits'


class C49(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.15,gal1),box(1320.0000000000002,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=8491.3
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV49.fits'


class C50(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),2.00E-13,flam)*ebmvx(0.15,gal1)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=2448.38
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV50.fits'


class C51(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),band(johnson,u),16,vegamag)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1309')
        self.ref_rate=2177.42
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV51.fits'


class C52(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),band(johnson,b),16,vegamag)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1309')
        self.ref_rate=6495.2
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV52.fits'


class C53(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),band(johnson,v),16,vegamag)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1309')
        self.ref_rate=8657.44
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV53.fits'


class C54(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate= 2.16641e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV54.fits'
        self.accuracy=1e-2

class C55(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=6.52681e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV55.fits'
        self.accuracy=1e-2

class C56(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=3.75132e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV56.fits'
        self.accuracy=1e-2

class C57(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=3.8e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV57.fits'
        self.accuracy=1e-2

class C58(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*0.5')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=3.8e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV58.fits'
        self.accuracy=1e-2

class C59(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.1+spec(el1302a.fits)*0.066666667+spec(el1356a.fits)*0.0060+spec(el2471a.fits)*0.0050)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=3.75908e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV59.fits'
        self.accuracy=1e-2

class C60(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate= 3.75908e-05
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV60.fits'
        self.accuracy=1e-2

class C61(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.1,lmc),box(1320.0000000000002,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=8558.69
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV61.fits'


class C62(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.1,smc),box(1320.0000000000002,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=8374.42
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV62.fits'


class C63(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.1,xgal),box(1320.0000000000002,1.0),2.00E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=8761.14
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV63.fits'


class C64(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,25400,0.0,3.9),box(2000.0,1.0),2.00E-13,flam)+em(1590.0,3.0,6.0E-13,flam)')
        self.bp=ObsBandpass('cos,fuv,g160m,c1577')
        self.ref_rate=15325.8
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV64.fits'


class C65(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),2.00E-14,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=901.731
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV65.fits'


class C66(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),2.00E-15,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=90.1731
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV66.fits'


class C67(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),2.00E-16,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=9.01731
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV67.fits'


class C68(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),2.00E-17,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=0.901731
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV68.fits'


class C69(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),1.00E-16,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1291')
        self.ref_rate=4.50865
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV69.fits'


class C70(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1310.0,1.0),1.00E-16,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1300')
        self.ref_rate=4.53311
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV70.fits'


class C71(ETCTestCase):
    def setparms(self):
        self.sp=parse_spec('rn(icat(k93models,44500,0.0,5.0),box(1320.0000000000002,1.0),1.00E-16,flam)')
        self.bp=ObsBandpass('cos,fuv,g130m,c1309')
        self.ref_rate=4.73628
        self.cmd='SpecSourcerateSpec'
        self.fname='specAV71.fits'



if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        if 'verbose' in sys.argv:
            testutil.testall(__name__,2)
        else:
            testutil.testall(__name__)
            


                            
