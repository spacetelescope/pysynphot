import os
import sys
sys.path.append('..')
import conv_base
conv_base.HERE = os.path.abspath(os.path.dirname(__file__))

class Test1101(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd"
        cls.spectrum="rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        cls.fname="C1101_%s.fits"
        cls.setup2()

class Test1102(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        cls.fname="C1102_%s.fits"
        cls.setup2()

class Test1103(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1103_%s.fits"
        cls.setup2()

class Test1104(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        cls.fname="C1104_%s.fits"
        cls.setup2()

class Test1105(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        cls.fname="C1105_%s.fits"
        cls.setup2()

class Test1106(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1106_%s.fits"
        cls.setup2()

class Test1107(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1107_%s.fits"
        cls.setup2()

class Test1108(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1108_%s.fits"
        cls.setup2()

class Test1109(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1109_%s.fits"
        cls.setup2()

class Test1110(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f25nd5"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        cls.fname="C1110_%s.fits"
        cls.setup2()

class Test1111(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f25nd5"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1111_%s.fits"
        cls.setup2()

class Test1112(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1112_%s.fits"
        cls.setup2()

class Test1113(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1113_%s.fits"
        cls.setup2()

class Test1114(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1114_%s.fits"
        cls.setup2()

class Test1115(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1115_%s.fits"
        cls.setup2()

class Test1116(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oii"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1116_%s.fits"
        cls.setup2()

class Test1117(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1117_%s.fits"
        cls.setup2()

class Test1118(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oiii"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1118_%s.fits"
        cls.setup2()

class Test1119(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oiii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1119_%s.fits"
        cls.setup2()

class Test1120(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1120_%s.fits"
        cls.setup2()

class Test1121(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1121_%s.fits"
        cls.setup2()

class Test1122(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        cls.fname="C1122_%s.fits"
        cls.setup2()

class Test1123(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1123_%s.fits"
        cls.setup2()

class Test1124(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230mb,c1995"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1124_%s.fits"
        cls.setup2()

class Test1125(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230mb,c1995,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1125_%s.fits"
        cls.setup2()

class Test1126(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        cls.fname="C1126_%s.fits"
        cls.setup2()

class Test1127(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1127_%s.fits"
        cls.setup2()

class Test1128(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1128_%s.fits"
        cls.setup2()

class Test1129(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1129_%s.fits"
        cls.setup2()

class Test1130(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1130_%s.fits"
        cls.setup2()

class Test1131(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23.5,vegamag)"
        cls.fname="C1131_%s.fits"
        cls.setup2()

class Test1132(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        cls.fname="C1132_%s.fits"
        cls.setup2()

class Test1133(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1133_%s.fits"
        cls.setup2()

class Test1134(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1134_%s.fits"
        cls.setup2()

class Test1135(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1135_%s.fits"
        cls.setup2()

class Test1136(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194,s52x2"
        cls.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        cls.fname="C1136_%s.fits"
        cls.setup2()

class Test1137(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1137_%s.fits"
        cls.setup2()

class Test1138(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1138_%s.fits"
        cls.setup2()

class Test1139(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1139_%s.fits"
        cls.setup2()

class Test1140(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1140_%s.fits"
        cls.setup2()

class Test1141(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1141_%s.fits"
        cls.setup2()

class Test1142(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1142_%s.fits"
        cls.setup2()

class Test1143(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1143_%s.fits"
        cls.setup2()

class Test1144(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),0.03),band(johnson,v),18,vegamag)"
        cls.fname="C1144_%s.fits"
        cls.setup2()

class Test1145(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),1.0),band(johnson,v),18,vegamag)"
        cls.fname="C1145_%s.fits"
        cls.setup2()

class Test1146(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,v),18,vegamag)"
        cls.fname="C1146_%s.fits"
        cls.setup2()

class Test1147(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23,vegamag)"
        cls.fname="C1147_%s.fits"
        cls.setup2()

class Test1148(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24.5,vegamag)"
        cls.fname="C1148_%s.fits"
        cls.setup2()

class Test1149(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1149_%s.fits"
        cls.setup2()

class Test1150(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750m,c7283"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1150_%s.fits"
        cls.setup2()

class Test1151(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750m,c7283,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1151_%s.fits"
        cls.setup2()

class Test1152(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        cls.fname="C1152_%s.fits"
        cls.setup2()

class Test1153(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1153_%s.fits"
        cls.setup2()

class Test1154(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1154_%s.fits"
        cls.setup2()

class Test1155(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1155_%s.fits"
        cls.setup2()

class Test1156(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        cls.fname="C1156_%s.fits"
        cls.setup2()

class Test1157(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1157_%s.fits"
        cls.setup2()

class Test1158(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1158_%s.fits"
        cls.setup2()

class Test1159(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140h,c1416"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1159_%s.fits"
        cls.setup2()

class Test1160(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140h,c1416,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1160_%s.fits"
        cls.setup2()

class Test1161(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1161_%s.fits"
        cls.setup2()

class Test1162(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1162_%s.fits"
        cls.setup2()

class Test1163(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1163_%s.fits"
        cls.setup2()

class Test1164(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        cls.spectrum="em(1425.0,0.043487548828125,1.0E-10,flam)"
        cls.fname="C1164_%s.fits"
        cls.setup2()

class Test1165(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        cls.spectrum="em(1425.0,1.0,1.0E-10,flam)"
        cls.fname="C1165_%s.fits"
        cls.setup2()

class Test1166(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),10,vegamag)"
        cls.fname="C1166_%s.fits"
        cls.setup2()

class Test1167(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),6,vegamag)"
        cls.fname="C1167_%s.fits"
        cls.setup2()

class Test1168(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),7,vegamag)"
        cls.fname="C1168_%s.fits"
        cls.setup2()

class Test1169(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        cls.fname="C1169_%s.fits"
        cls.setup2()

class Test1170(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1170_%s.fits"
        cls.setup2()

class Test1171(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25lya"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1171_%s.fits"
        cls.setup2()

class Test1172(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25lya"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1172_%s.fits"
        cls.setup2()

class Test1173(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25nd3"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1173_%s.fits"
        cls.setup2()

class Test1174(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25nd3"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1174_%s.fits"
        cls.setup2()

class Test1175(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq1"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1175_%s.fits"
        cls.setup2()

class Test1176(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq1"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1176_%s.fits"
        cls.setup2()

class Test1177(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq3"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1177_%s.fits"
        cls.setup2()

class Test1178(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq3"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1178_%s.fits"
        cls.setup2()

class Test1179(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1179_%s.fits"
        cls.setup2()

class Test1180(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25qtz"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1180_%s.fits"
        cls.setup2()

class Test1181(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25srf2"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1181_%s.fits"
        cls.setup2()

class Test1182(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25srf2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1182_%s.fits"
        cls.setup2()

class Test1183(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1183_%s.fits"
        cls.setup2()

class Test1184(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1184_%s.fits"
        cls.setup2()

class Test1185(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x01"
        cls.spectrum="rn(spec(ngc1068_template.fits),band(johnson,v),9,vegamag)"
        cls.fname="C1185_%s.fits"
        cls.setup2()

class Test1186(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),13,vegamag)"
        cls.fname="C1186_%s.fits"
        cls.setup2()

class Test1187(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14,vegamag)"
        cls.fname="C1187_%s.fits"
        cls.setup2()

class Test1188(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14.1,vegamag)"
        cls.fname="C1188_%s.fits"
        cls.setup2()

class Test1189(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),27.5,vegamag)"
        cls.fname="C1189_%s.fits"
        cls.setup2()

class Test1190(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits),band(johnson,v),12.77,vegamag)"
        cls.fname="C1190_%s.fits"
        cls.setup2()

class Test1191(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/grw_70d5824_stis_001.fits),band(johnson,v),10.516,vegamag)"
        cls.fname="C1191_%s.fits"
        cls.setup2()

class Test1192(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/grw_70d5824_stis_001.fits)"
        cls.fname="C1192_%s.fits"
        cls.setup2()

class Test1193(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140m,c1567"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1193_%s.fits"
        cls.setup2()

class Test1194(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140m,c1567,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1194_%s.fits"
        cls.setup2()

class Test1195(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/g191b2b_mod_004.fits"
        cls.fname="C1195_%s.fits"
        cls.setup2()

class Test1196(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd153_mod_004.fits"
        cls.fname="C1196_%s.fits"
        cls.setup2()

class Test1197(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd71_mod_005.fits"
        cls.fname="C1197_%s.fits"
        cls.setup2()

class Test1198(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1215a.fits"
        cls.fname="C1198_%s.fits"
        cls.setup2()

class Test1199(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1302a.fits"
        cls.fname="C1199_%s.fits"
        cls.setup2()

class Test1200(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1356a.fits"
        cls.fname="C1200_%s.fits"
        cls.setup2()

class Test1201(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el2471a.fits"
        cls.fname="C1201_%s.fits"
        cls.setup2()

class Test1202(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/g191b2b_mod_004.fits"
        cls.fname="C1202_%s.fits"
        cls.setup2()

class Test1203(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd153_mod_004.fits"
        cls.fname="C1203_%s.fits"
        cls.setup2()

class Test1204(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd71_mod_005.fits"
        cls.fname="C1204_%s.fits"
        cls.setup2()

class Test1205(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/g191b2b_mod_004.fits"
        cls.fname="C1205_%s.fits"
        cls.setup2()

class Test1206(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd153_mod_004.fits"
        cls.fname="C1206_%s.fits"
        cls.setup2()

class Test1207(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd71_mod_005.fits"
        cls.fname="C1207_%s.fits"
        cls.setup2()

class Test1208(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/g191b2b_mod_004.fits"
        cls.fname="C1208_%s.fits"
        cls.setup2()

class Test1209(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd153_mod_004.fits"
        cls.fname="C1209_%s.fits"
        cls.setup2()

class Test1210(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd71_mod_005.fits"
        cls.fname="C1210_%s.fits"
        cls.setup2()

class Test1211(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/g191b2b_mod_004.fits"
        cls.fname="C1211_%s.fits"
        cls.setup2()

class Test1212(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd153_mod_004.fits"
        cls.fname="C1212_%s.fits"
        cls.setup2()

class Test1213(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="$PYSYN_CDBScalspec/gd71_mod_005.fits"
        cls.fname="C1213_%s.fits"
        cls.setup2()

class Test1214(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1214_%s.fits"
        cls.setup2()

class Test1215(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1215_%s.fits"
        cls.setup2()

class Test1216(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1216_%s.fits"
        cls.setup2()

class Test1217(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1217_%s.fits"
        cls.setup2()

class Test1218(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(bb(50000),band(johnson,v),10.516,vegamag)"
        cls.fname="C1218_%s.fits"
        cls.setup2()

class Test1219(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10.516,vegamag)"
        cls.fname="C1219_%s.fits"
        cls.setup2()

class Test1220(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1220_%s.fits"
        cls.setup2()

class Test1221(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(pl(4000.0,0.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1221_%s.fits"
        cls.setup2()

class Test1222(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits),band(johnson,v),10.516,vegamag)"
        cls.fname="C1222_%s.fits"
        cls.setup2()

class Test1223(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits),box(2000.0,1.0),1.0e-12,flam)"
        cls.fname="C1223_%s.fits"
        cls.setup2()

class Test1224(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1224_%s.fits"
        cls.setup2()

class Test1225(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1225_%s.fits"
        cls.setup2()

class Test1226(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1226_%s.fits"
        cls.setup2()

class Test1227(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        cls.fname="C1227_%s.fits"
        cls.setup2()

class Test1228(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        cls.spectrum="spec($PYSYN_CDBS/calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1228_%s.fits"
        cls.setup2()

class Test1229(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ciii"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1229_%s.fits"
        cls.setup2()

class Test1230(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ciii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1230_%s.fits"
        cls.setup2()

class Test1231(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn182"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1231_%s.fits"
        cls.setup2()

class Test1232(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn182"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1232_%s.fits"
        cls.setup2()

class Test1233(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn270"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1233_%s.fits"
        cls.setup2()

class Test1234(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn270"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1234_%s.fits"
        cls.setup2()

class Test1235(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25mgii"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1235_%s.fits"
        cls.setup2()

class Test1236(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25mgii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1236_%s.fits"
        cls.setup2()

class Test1237(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25nd5"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1237_%s.fits"
        cls.setup2()

class Test1238(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25nd5"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1238_%s.fits"
        cls.setup2()

class Test1239(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1239_%s.fits"
        cls.setup2()

class Test1240(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1240_%s.fits"
        cls.setup2()

class Test1241(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq4"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1241_%s.fits"
        cls.setup2()

class Test1242(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq4"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1242_%s.fits"
        cls.setup2()

class Test1243(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1243_%s.fits"
        cls.setup2()

class Test1244(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1244_%s.fits"
        cls.setup2()

class Test1245(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1245_%s.fits"
        cls.setup2()

class Test1246(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25srf2"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1246_%s.fits"
        cls.setup2()

class Test1247(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25srf2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1247_%s.fits"
        cls.setup2()

class Test1248(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1248_%s.fits"
        cls.setup2()

class Test1249(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1249_%s.fits"
        cls.setup2()

class Test1250(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,gal1),band(johnson,v),15,vegamag)"
        cls.fname="C1250_%s.fits"
        cls.setup2()

class Test1251(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,lmc),band(johnson,v),15,vegamag)"
        cls.fname="C1251_%s.fits"
        cls.setup2()

class Test1252(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,smc),band(johnson,v),15,vegamag)"
        cls.fname="C1252_%s.fits"
        cls.setup2()

class Test1253(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,xgal),band(johnson,v),15,vegamag)"
        cls.fname="C1253_%s.fits"
        cls.setup2()

class Test1254(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24,vegamag)"
        cls.fname="C1254_%s.fits"
        cls.setup2()

class Test1255(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/grw_70d5824_stis_001.fits)"
        cls.fname="C1255_%s.fits"
        cls.setup2()

class Test1256(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230m,c2818"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1256_%s.fits"
        cls.setup2()

class Test1257(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230m,c2818,s52x2"
        cls.spectrum="spec($PYSYN_CDBS/calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1257_%s.fits"
        cls.setup2()

class Test1258(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1258_%s.fits"
        cls.setup2()

class Test1259(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism,s52x01"
        cls.spectrum="spec(HS20270651.dat)"
        cls.fname="C1259_%s.fits"
        cls.setup2()

class Test1260(conv_base.CommCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism,s52x2"
        cls.spectrum="spec(HS20270651.dat)"
        cls.fname="C1260_%s.fits"
        cls.setup2()

