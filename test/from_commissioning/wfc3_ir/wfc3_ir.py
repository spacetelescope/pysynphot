import os
import sys
sys.path.append('..')
import conv_base
conv_base.HERE = os.path.abspath(os.path.dirname(__file__))

class Test1261(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1261_%s.fits"
        cls.setup2()

class Test1262(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1262_%s.fits"
        cls.setup2()

class Test1263(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1263_%s.fits"
        cls.setup2()

class Test1264(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1264_%s.fits"
        cls.setup2()

class Test1265(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1265_%s.fits"
        cls.setup2()

class Test1266(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        cls.fname="C1266_%s.fits"
        cls.setup2()

class Test1267(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        cls.fname="C1267_%s.fits"
        cls.setup2()

class Test1268(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        cls.fname="C1268_%s.fits"
        cls.setup2()

class Test1269(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1269_%s.fits"
        cls.setup2()

class Test1270(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1270_%s.fits"
        cls.setup2()

class Test1271(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1271_%s.fits"
        cls.setup2()

class Test1272(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1272_%s.fits"
        cls.setup2()

class Test1273(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1273_%s.fits"
        cls.setup2()

class Test1274(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1274_%s.fits"
        cls.setup2()

class Test1275(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1275_%s.fits"
        cls.setup2()

class Test1276(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1276_%s.fits"
        cls.setup2()

class Test1277(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1277_%s.fits"
        cls.setup2()

class Test1278(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1278_%s.fits"
        cls.setup2()

class Test1279(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1279_%s.fits"
        cls.setup2()

class Test1280(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1280_%s.fits"
        cls.setup2()

class Test1281(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1281_%s.fits"
        cls.setup2()

class Test1282(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1282_%s.fits"
        cls.setup2()

class Test1283(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1283_%s.fits"
        cls.setup2()

class Test1284(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1284_%s.fits"
        cls.setup2()

class Test1285(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1285_%s.fits"
        cls.setup2()

class Test1286(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1286_%s.fits"
        cls.setup2()

class Test1287(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1287_%s.fits"
        cls.setup2()

class Test1288(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1288_%s.fits"
        cls.setup2()

class Test1289(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1289_%s.fits"
        cls.setup2()

class Test1290(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1290_%s.fits"
        cls.setup2()

class Test1291(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1291_%s.fits"
        cls.setup2()

class Test1292(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1292_%s.fits"
        cls.setup2()

class Test1293(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1293_%s.fits"
        cls.setup2()

class Test1294(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1294_%s.fits"
        cls.setup2()

class Test1295(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1295_%s.fits"
        cls.setup2()

class Test1296(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1296_%s.fits"
        cls.setup2()

class Test1297(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1297_%s.fits"
        cls.setup2()

class Test1298(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1298_%s.fits"
        cls.setup2()

class Test1299(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1299_%s.fits"
        cls.setup2()

class Test1300(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        cls.fname="C1300_%s.fits"
        cls.setup2()

class Test1301(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        cls.fname="C1301_%s.fits"
        cls.setup2()

class Test1302(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        cls.fname="C1302_%s.fits"
        cls.setup2()

class Test1303(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        cls.fname="C1303_%s.fits"
        cls.setup2()

class Test1304(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        cls.fname="C1304_%s.fits"
        cls.setup2()

class Test1305(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        cls.fname="C1305_%s.fits"
        cls.setup2()

class Test1306(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1306_%s.fits"
        cls.setup2()

class Test1307(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1307_%s.fits"
        cls.setup2()

class Test1308(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1308_%s.fits"
        cls.setup2()

class Test1309(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1309_%s.fits"
        cls.setup2()

class Test1310(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1310_%s.fits"
        cls.setup2()

class Test1311(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1311_%s.fits"
        cls.setup2()

class Test1312(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1312_%s.fits"
        cls.setup2()

class Test1313(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1313_%s.fits"
        cls.setup2()

class Test1314(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f126n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1314_%s.fits"
        cls.setup2()

class Test1315(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f126n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1315_%s.fits"
        cls.setup2()

class Test1316(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f126n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1316_%s.fits"
        cls.setup2()

class Test1317(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f127m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1317_%s.fits"
        cls.setup2()

class Test1318(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f127m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1318_%s.fits"
        cls.setup2()

class Test1319(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f127m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1319_%s.fits"
        cls.setup2()

class Test1320(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f128n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1320_%s.fits"
        cls.setup2()

class Test1321(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f128n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1321_%s.fits"
        cls.setup2()

class Test1322(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f128n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1322_%s.fits"
        cls.setup2()

class Test1323(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f130n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1323_%s.fits"
        cls.setup2()

class Test1324(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f130n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1324_%s.fits"
        cls.setup2()

class Test1325(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f130n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1325_%s.fits"
        cls.setup2()

class Test1326(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1326_%s.fits"
        cls.setup2()

class Test1327(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1327_%s.fits"
        cls.setup2()

class Test1328(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(13200.0,5.0,1.0E-13,flam)"
        cls.fname="C1328_%s.fits"
        cls.setup2()

class Test1329(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1329_%s.fits"
        cls.setup2()

class Test1330(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f139m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1330_%s.fits"
        cls.setup2()

class Test1331(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f139m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1331_%s.fits"
        cls.setup2()

class Test1332(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f139m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1332_%s.fits"
        cls.setup2()

class Test1333(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1333_%s.fits"
        cls.setup2()

class Test1334(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1334_%s.fits"
        cls.setup2()

class Test1335(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1335_%s.fits"
        cls.setup2()

class Test1336(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1336_%s.fits"
        cls.setup2()

class Test1337(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1337_%s.fits"
        cls.setup2()

class Test1338(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(egal.dat),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1338_%s.fits"
        cls.setup2()

class Test1339(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(egal.dat),1.0),band(johnson,b),28.0,vegamag)"
        cls.fname="C1339_%s.fits"
        cls.setup2()

class Test1340(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,b),28.0,vegamag)"
        cls.fname="C1340_%s.fits"
        cls.setup2()

class Test1341(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(spiral.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1341_%s.fits"
        cls.setup2()

class Test1342(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(spiral.fits),2.0),band(johnson,b),28.0,vegamag)"
        cls.fname="C1342_%s.fits"
        cls.setup2()

class Test1343(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1343_%s.fits"
        cls.setup2()

class Test1344(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1344_%s.fits"
        cls.setup2()

class Test1345(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1345_%s.fits"
        cls.setup2()

class Test1346(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        cls.fname="C1346_%s.fits"
        cls.setup2()

class Test1347(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        cls.fname="C1347_%s.fits"
        cls.setup2()

class Test1348(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        cls.fname="C1348_%s.fits"
        cls.setup2()

class Test1349(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        cls.fname="C1349_%s.fits"
        cls.setup2()

class Test1350(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1350_%s.fits"
        cls.setup2()

class Test1351(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1351_%s.fits"
        cls.setup2()

class Test1352(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1352_%s.fits"
        cls.setup2()

class Test1353(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1353_%s.fits"
        cls.setup2()

class Test1354(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1354_%s.fits"
        cls.setup2()

class Test1355(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1355_%s.fits"
        cls.setup2()

class Test1356(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1356_%s.fits"
        cls.setup2()

class Test1357(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1357_%s.fits"
        cls.setup2()

class Test1358(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1358_%s.fits"
        cls.setup2()

class Test1359(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1359_%s.fits"
        cls.setup2()

class Test1360(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1360_%s.fits"
        cls.setup2()

class Test1361(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1361_%s.fits"
        cls.setup2()

class Test1362(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1362_%s.fits"
        cls.setup2()

class Test1363(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1363_%s.fits"
        cls.setup2()

class Test1364(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1364_%s.fits"
        cls.setup2()

class Test1365(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1365_%s.fits"
        cls.setup2()

class Test1366(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1366_%s.fits"
        cls.setup2()

class Test1367(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1367_%s.fits"
        cls.setup2()

class Test1368(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1368_%s.fits"
        cls.setup2()

class Test1369(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1369_%s.fits"
        cls.setup2()

class Test1370(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1370_%s.fits"
        cls.setup2()

class Test1371(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1371_%s.fits"
        cls.setup2()

class Test1372(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1372_%s.fits"
        cls.setup2()

class Test1373(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1373_%s.fits"
        cls.setup2()

class Test1374(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1374_%s.fits"
        cls.setup2()

class Test1375(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1375_%s.fits"
        cls.setup2()

class Test1376(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1376_%s.fits"
        cls.setup2()

class Test1377(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1377_%s.fits"
        cls.setup2()

class Test1378(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1378_%s.fits"
        cls.setup2()

class Test1379(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1379_%s.fits"
        cls.setup2()

class Test1380(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1380_%s.fits"
        cls.setup2()

class Test1381(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1381_%s.fits"
        cls.setup2()

class Test1382(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1382_%s.fits"
        cls.setup2()

class Test1383(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1383_%s.fits"
        cls.setup2()

class Test1384(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1384_%s.fits"
        cls.setup2()

class Test1385(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1385_%s.fits"
        cls.setup2()

class Test1386(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1386_%s.fits"
        cls.setup2()

class Test1387(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1387_%s.fits"
        cls.setup2()

class Test1388(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1388_%s.fits"
        cls.setup2()

class Test1389(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1389_%s.fits"
        cls.setup2()

class Test1390(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1390_%s.fits"
        cls.setup2()

class Test1391(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1391_%s.fits"
        cls.setup2()

class Test1392(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1392_%s.fits"
        cls.setup2()

class Test1393(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1393_%s.fits"
        cls.setup2()

class Test1394(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1394_%s.fits"
        cls.setup2()

class Test1395(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1395_%s.fits"
        cls.setup2()

class Test1396(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1396_%s.fits"
        cls.setup2()

class Test1397(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1397_%s.fits"
        cls.setup2()

class Test1398(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1398_%s.fits"
        cls.setup2()

class Test1399(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1399_%s.fits"
        cls.setup2()

class Test1400(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1400_%s.fits"
        cls.setup2()

class Test1401(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1401_%s.fits"
        cls.setup2()

class Test1402(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1402_%s.fits"
        cls.setup2()

class Test1403(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1403_%s.fits"
        cls.setup2()

class Test1404(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1404_%s.fits"
        cls.setup2()

class Test1405(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1405_%s.fits"
        cls.setup2()

class Test1406(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1406_%s.fits"
        cls.setup2()

class Test1407(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1407_%s.fits"
        cls.setup2()

class Test1408(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1408_%s.fits"
        cls.setup2()

class Test1409(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1409_%s.fits"
        cls.setup2()

class Test1410(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1410_%s.fits"
        cls.setup2()

class Test1411(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1411_%s.fits"
        cls.setup2()

class Test1412(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1412_%s.fits"
        cls.setup2()

class Test1413(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1413_%s.fits"
        cls.setup2()

class Test1414(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1414_%s.fits"
        cls.setup2()

class Test1415(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1415_%s.fits"
        cls.setup2()

class Test1416(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1416_%s.fits"
        cls.setup2()

class Test1417(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1417_%s.fits"
        cls.setup2()

class Test1418(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1418_%s.fits"
        cls.setup2()

class Test1419(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1419_%s.fits"
        cls.setup2()

class Test1420(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1420_%s.fits"
        cls.setup2()

class Test1421(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1421_%s.fits"
        cls.setup2()

class Test1422(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1422_%s.fits"
        cls.setup2()

class Test1423(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1423_%s.fits"
        cls.setup2()

class Test1424(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1424_%s.fits"
        cls.setup2()

class Test1425(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1425_%s.fits"
        cls.setup2()

class Test1426(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1426_%s.fits"
        cls.setup2()

class Test1427(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1427_%s.fits"
        cls.setup2()

class Test1428(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1428_%s.fits"
        cls.setup2()

class Test1429(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f164n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1429_%s.fits"
        cls.setup2()

class Test1430(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f164n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1430_%s.fits"
        cls.setup2()

class Test1431(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1431_%s.fits"
        cls.setup2()

class Test1432(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f167n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1432_%s.fits"
        cls.setup2()

class Test1433(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f167n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1433_%s.fits"
        cls.setup2()

class Test1434(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f167n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1434_%s.fits"
        cls.setup2()

class Test1435(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1435_%s.fits"
        cls.setup2()

class Test1436(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1436_%s.fits"
        cls.setup2()

class Test1437(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        cls.fname="C1437_%s.fits"
        cls.setup2()

class Test1438(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1438_%s.fits"
        cls.setup2()

class Test1439(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1439_%s.fits"
        cls.setup2()

class Test1440(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        cls.fname="C1440_%s.fits"
        cls.setup2()

class Test1441(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C1441_%s.fits"
        cls.setup2()

class Test1442(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C1442_%s.fits"
        cls.setup2()

class Test1443(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C1443_%s.fits"
        cls.setup2()

class Test1444(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        cls.fname="C1444_%s.fits"
        cls.setup2()

class Test1445(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        cls.fname="C1445_%s.fits"
        cls.setup2()

class Test1446(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        cls.fname="C1446_%s.fits"
        cls.setup2()

class Test1447(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        cls.fname="C1447_%s.fits"
        cls.setup2()

class Test1448(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1448_%s.fits"
        cls.setup2()

class Test1449(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(z(spec($PYSYN_CDBS/calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        cls.fname="C1449_%s.fits"
        cls.setup2()

class Test1450(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1450_%s.fits"
        cls.setup2()

class Test1451(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1451_%s.fits"
        cls.setup2()

class Test1452(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1452_%s.fits"
        cls.setup2()

class Test1453(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1453_%s.fits"
        cls.setup2()

class Test1454(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        cls.fname="C1454_%s.fits"
        cls.setup2()

class Test1455(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        cls.fname="C1455_%s.fits"
        cls.setup2()

class Test1456(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        cls.fname="C1456_%s.fits"
        cls.setup2()

class Test1457(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        cls.fname="C1457_%s.fits"
        cls.setup2()

class Test1458(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        cls.fname="C1458_%s.fits"
        cls.setup2()

class Test1459(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        cls.fname="C1459_%s.fits"
        cls.setup2()

class Test1460(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C1460_%s.fits"
        cls.setup2()

class Test1461(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C1461_%s.fits"
        cls.setup2()

class Test1462(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C1462_%s.fits"
        cls.setup2()

class Test1463(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1463_%s.fits"
        cls.setup2()

class Test1464(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1464_%s.fits"
        cls.setup2()

class Test1465(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1465_%s.fits"
        cls.setup2()

class Test1466(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1466_%s.fits"
        cls.setup2()

class Test1467(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1467_%s.fits"
        cls.setup2()

class Test1468(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1468_%s.fits"
        cls.setup2()

class Test1469(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1469_%s.fits"
        cls.setup2()

class Test1470(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1470_%s.fits"
        cls.setup2()

class Test1471(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1471_%s.fits"
        cls.setup2()

class Test1472(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1472_%s.fits"
        cls.setup2()

class Test1473(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1473_%s.fits"
        cls.setup2()

class Test1474(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1474_%s.fits"
        cls.setup2()

class Test1475(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1475_%s.fits"
        cls.setup2()

class Test1476(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1476_%s.fits"
        cls.setup2()

class Test1477(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1477_%s.fits"
        cls.setup2()

class Test1478(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1478_%s.fits"
        cls.setup2()

class Test1479(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1479_%s.fits"
        cls.setup2()

class Test1480(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1480_%s.fits"
        cls.setup2()

class Test1481(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1481_%s.fits"
        cls.setup2()

class Test1482(conv_base.ThermCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1482_%s.fits"
        cls.setup2()

