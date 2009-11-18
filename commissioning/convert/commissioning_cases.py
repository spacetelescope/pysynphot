from pytools import testutil
import sys
import conv_base

class CommCase1(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(10000)"
        self.fname="C1_%s.fits"
        self.setup2()

class CommCase2(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000)"
        self.fname="C2_%s.fits"
        self.setup2()

class CommCase3(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5000.0)"
        self.fname="C3_%s.fits"
        self.setup2()

class CommCase4(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(50000)"
        self.fname="C4_%s.fits"
        self.setup2()

class CommCase5(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(5500)"
        self.fname="C5_%s.fits"
        self.setup2()

class CommCase6(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(6200)"
        self.fname="C6_%s.fits"
        self.setup2()

class CommCase7(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="bb(7700)"
        self.fname="C7_%s.fits"
        self.setup2()

class CommCase8(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,15000,0.0,3.5)"
        self.fname="C8_%s.fits"
        self.setup2()

class CommCase9(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,45000,0.0,4.5)"
        self.fname="C9_%s.fits"
        self.setup2()

class CommCase10(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,4750,0.0,1.0)"
        self.fname="C10_%s.fits"
        self.setup2()

class CommCase11(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,6250,0.0,4.5)"
        self.fname="C11_%s.fits"
        self.setup2()

class CommCase12(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(ck04models,7750,0.0,2.0)"
        self.fname="C12_%s.fits"
        self.setup2()

class CommCase13(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,11900,0.0,4.0)"
        self.fname="C13_%s.fits"
        self.setup2()

class CommCase14(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,15400,0.0,3.9)"
        self.fname="C14_%s.fits"
        self.setup2()

class CommCase15(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,18700,0.0,3.9)"
        self.fname="C15_%s.fits"
        self.setup2()

class CommCase16(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,25400,0.0,3.9)"
        self.fname="C16_%s.fits"
        self.setup2()

class CommCase17(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,30000,0.0,4.0)"
        self.fname="C17_%s.fits"
        self.setup2()

class CommCase18(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,33000.,0.0,4.0)"
        self.fname="C18_%s.fits"
        self.setup2()

class CommCase19(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,3500,0.0,4.6)"
        self.fname="C19_%s.fits"
        self.setup2()

class CommCase20(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,38000.,0.0,4.5)"
        self.fname="C20_%s.fits"
        self.setup2()

class CommCase21(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4060,0.0,4.5)"
        self.fname="C21_%s.fits"
        self.setup2()

class CommCase22(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,44500,0.0,5.0)"
        self.fname="C22_%s.fits"
        self.setup2()

class CommCase23(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4560,0.0,4.5)"
        self.fname="C23_%s.fits"
        self.setup2()

class CommCase24(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,4850,0.0,1.1)"
        self.fname="C24_%s.fits"
        self.setup2()

class CommCase25(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5250,0.0,4.5)"
        self.fname="C25_%s.fits"
        self.setup2()

class CommCase26(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5570,0.0,4.5)"
        self.fname="C26_%s.fits"
        self.setup2()

class CommCase27(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5770,0.0,4.5)"
        self.fname="C27_%s.fits"
        self.setup2()

class CommCase28(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,5860,0.0,4.4)"
        self.fname="C28_%s.fits"
        self.setup2()

class CommCase29(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6200,0.0,4.4)"
        self.fname="C29_%s.fits"
        self.setup2()

class CommCase30(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6440,0.0,4.3)"
        self.fname="C30_%s.fits"
        self.setup2()

class CommCase31(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,6890,0.0,4.3)"
        self.fname="C31_%s.fits"
        self.setup2()

class CommCase32(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7200,0.0,4.3)"
        self.fname="C32_%s.fits"
        self.setup2()

class CommCase33(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,7700,0.0,1.7)"
        self.fname="C33_%s.fits"
        self.setup2()

class CommCase34(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8200,0.0,4.3)"
        self.fname="C34_%s.fits"
        self.setup2()

class CommCase35(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,8720,0.0,4.2)"
        self.fname="C35_%s.fits"
        self.setup2()

class CommCase36(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="icat(k93models,9230,0.0,4.1)"
        self.fname="C36_%s.fits"
        self.setup2()

class CommCase37(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-0.5,flam)"
        self.fname="C37_%s.fits"
        self.setup2()

class CommCase38(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.0,flam)"
        self.fname="C38_%s.fits"
        self.setup2()

class CommCase39(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-1.5,flam)"
        self.fname="C39_%s.fits"
        self.setup2()

class CommCase40(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,-2.0,flam)"
        self.fname="C40_%s.fits"
        self.setup2()

class CommCase41(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="pl(4000.0,0.0,flam)"
        self.fname="C41_%s.fits"
        self.setup2()

class CommCase42(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, flam)"
        self.fname="C42_%s.fits"
        self.setup2()

class CommCase43(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, obmag)"
        self.fname="C43_%s.fits"
        self.setup2()

class CommCase44(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, photlam)"
        self.fname="C44_%s.fits"
        self.setup2()

class CommCase45(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, vegamag)"
        self.fname="C45_%s.fits"
        self.setup2()

class CommCase46(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, flam)"
        self.fname="C46_%s.fits"
        self.setup2()

class CommCase47(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, obmag)"
        self.fname="C47_%s.fits"
        self.setup2()

class CommCase48(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, photlam)"
        self.fname="C48_%s.fits"
        self.setup2()

class CommCase49(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, vegamag)"
        self.fname="C49_%s.fits"
        self.setup2()

class CommCase50(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, flam)"
        self.fname="C50_%s.fits"
        self.setup2()

class CommCase51(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, obmag)"
        self.fname="C51_%s.fits"
        self.setup2()

class CommCase52(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, photlam)"
        self.fname="C52_%s.fits"
        self.setup2()

class CommCase53(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, vegamag)"
        self.fname="C53_%s.fits"
        self.setup2()

class CommCase54(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, flam)"
        self.fname="C54_%s.fits"
        self.setup2()

class CommCase55(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, obmag)"
        self.fname="C55_%s.fits"
        self.setup2()

class CommCase56(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, photlam)"
        self.fname="C56_%s.fits"
        self.setup2()

class CommCase57(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, vegamag)"
        self.fname="C57_%s.fits"
        self.setup2()

class CommCase58(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, flam)"
        self.fname="C58_%s.fits"
        self.setup2()

class CommCase59(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, obmag)"
        self.fname="C59_%s.fits"
        self.setup2()

class CommCase60(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, photlam)"
        self.fname="C60_%s.fits"
        self.setup2()

class CommCase61(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, vegamag)"
        self.fname="C61_%s.fits"
        self.setup2()

class CommCase62(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, flam)"
        self.fname="C62_%s.fits"
        self.setup2()

class CommCase63(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, obmag)"
        self.fname="C63_%s.fits"
        self.setup2()

class CommCase64(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, photlam)"
        self.fname="C64_%s.fits"
        self.setup2()

class CommCase65(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, vegamag)"
        self.fname="C65_%s.fits"
        self.setup2()

class CommCase66(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, flam)"
        self.fname="C66_%s.fits"
        self.setup2()

class CommCase67(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, obmag)"
        self.fname="C67_%s.fits"
        self.setup2()

class CommCase68(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, photlam)"
        self.fname="C68_%s.fits"
        self.setup2()

class CommCase69(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, vegamag)"
        self.fname="C69_%s.fits"
        self.setup2()

class CommCase70(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, flam)"
        self.fname="C70_%s.fits"
        self.setup2()

class CommCase71(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, obmag)"
        self.fname="C71_%s.fits"
        self.setup2()

class CommCase72(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, photlam)"
        self.fname="C72_%s.fits"
        self.setup2()

class CommCase73(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, vegamag)"
        self.fname="C73_%s.fits"
        self.setup2()

class CommCase74(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, flam)"
        self.fname="C74_%s.fits"
        self.setup2()

class CommCase75(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, obmag)"
        self.fname="C75_%s.fits"
        self.setup2()

class CommCase76(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, photlam)"
        self.fname="C76_%s.fits"
        self.setup2()

class CommCase77(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, vegamag)"
        self.fname="C77_%s.fits"
        self.setup2()

class CommCase78(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, flam)"
        self.fname="C78_%s.fits"
        self.setup2()

class CommCase79(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, obmag)"
        self.fname="C79_%s.fits"
        self.setup2()

class CommCase80(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, photlam)"
        self.fname="C80_%s.fits"
        self.setup2()

class CommCase81(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, vegamag)"
        self.fname="C81_%s.fits"
        self.setup2()

class CommCase82(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, flam)"
        self.fname="C82_%s.fits"
        self.setup2()

class CommCase83(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, obmag)"
        self.fname="C83_%s.fits"
        self.setup2()

class CommCase84(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, photlam)"
        self.fname="C84_%s.fits"
        self.setup2()

class CommCase85(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, vegamag)"
        self.fname="C85_%s.fits"
        self.setup2()

class CommCase86(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, flam)"
        self.fname="C86_%s.fits"
        self.setup2()

class CommCase87(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, obmag)"
        self.fname="C87_%s.fits"
        self.setup2()

class CommCase88(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, photlam)"
        self.fname="C88_%s.fits"
        self.setup2()

class CommCase89(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, vegamag)"
        self.fname="C89_%s.fits"
        self.setup2()

class CommCase90(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, flam)"
        self.fname="C90_%s.fits"
        self.setup2()

class CommCase91(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, obmag)"
        self.fname="C91_%s.fits"
        self.setup2()

class CommCase92(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, photlam)"
        self.fname="C92_%s.fits"
        self.setup2()

class CommCase93(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, vegamag)"
        self.fname="C93_%s.fits"
        self.setup2()

class CommCase94(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, flam)"
        self.fname="C94_%s.fits"
        self.setup2()

class CommCase95(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, obmag)"
        self.fname="C95_%s.fits"
        self.setup2()

class CommCase96(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, photlam)"
        self.fname="C96_%s.fits"
        self.setup2()

class CommCase97(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, vegamag)"
        self.fname="C97_%s.fits"
        self.setup2()

class CommCase98(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, flam)"
        self.fname="C98_%s.fits"
        self.setup2()

class CommCase99(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, obmag)"
        self.fname="C99_%s.fits"
        self.setup2()

class CommCase100(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, photlam)"
        self.fname="C100_%s.fits"
        self.setup2()

class CommCase101(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, vegamag)"
        self.fname="C101_%s.fits"
        self.setup2()

class CommCase102(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, flam)"
        self.fname="C102_%s.fits"
        self.setup2()

class CommCase103(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, obmag)"
        self.fname="C103_%s.fits"
        self.setup2()

class CommCase104(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, photlam)"
        self.fname="C104_%s.fits"
        self.setup2()

class CommCase105(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, vegamag)"
        self.fname="C105_%s.fits"
        self.setup2()

class CommCase106(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),1.0e-14,photnu)"
        self.fname="C106_%s.fits"
        self.setup2()

class CommCase107(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),1.0e-27,fnu)"
        self.fname="C107_%s.fits"
        self.setup2()

class CommCase108(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),1.0e-4,photlam)"
        self.fname="C108_%s.fits"
        self.setup2()

class CommCase109(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),10,mjy)"
        self.fname="C109_%s.fits"
        self.setup2()

class CommCase110(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),18,stmag)"
        self.fname="C110_%s.fits"
        self.setup2()

class CommCase111(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),2.0e-7,jy)"
        self.fname="C111_%s.fits"
        self.setup2()

class CommCase112(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),23,abmag)"
        self.fname="C112_%s.fits"
        self.setup2()

class CommCase113(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),5,obmag)"
        self.fname="C113_%s.fits"
        self.setup2()

class CommCase114(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(bessell,h),5000,counts)"
        self.fname="C114_%s.fits"
        self.setup2()

class CommCase115(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(nicmos,2,f237m),25000,counts)"
        self.fname="C115_%s.fits"
        self.setup2()

class CommCase116(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(bb(5000),band(nicmos,3,f108n),30,mjy)"
        self.fname="C116_%s.fits"
        self.setup2()

class CommCase117(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, flam)"
        self.fname="C117_%s.fits"
        self.setup2()

class CommCase118(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, obmag)"
        self.fname="C118_%s.fits"
        self.setup2()

class CommCase119(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, photlam)"
        self.fname="C119_%s.fits"
        self.setup2()

class CommCase120(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, vegamag)"
        self.fname="C120_%s.fits"
        self.setup2()

class CommCase121(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, flam)"
        self.fname="C121_%s.fits"
        self.setup2()

class CommCase122(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, obmag)"
        self.fname="C122_%s.fits"
        self.setup2()

class CommCase123(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, photlam)"
        self.fname="C123_%s.fits"
        self.setup2()

class CommCase124(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, vegamag)"
        self.fname="C124_%s.fits"
        self.setup2()

class CommCase125(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, flam)"
        self.fname="C125_%s.fits"
        self.setup2()

class CommCase126(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, obmag)"
        self.fname="C126_%s.fits"
        self.setup2()

class CommCase127(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, photlam)"
        self.fname="C127_%s.fits"
        self.setup2()

class CommCase128(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, vegamag)"
        self.fname="C128_%s.fits"
        self.setup2()

class CommCase129(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, flam)"
        self.fname="C129_%s.fits"
        self.setup2()

class CommCase130(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, obmag)"
        self.fname="C130_%s.fits"
        self.setup2()

class CommCase131(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, photlam)"
        self.fname="C131_%s.fits"
        self.setup2()

class CommCase132(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, vegamag)"
        self.fname="C132_%s.fits"
        self.setup2()

class CommCase133(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, flam)"
        self.fname="C133_%s.fits"
        self.setup2()

class CommCase134(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, obmag)"
        self.fname="C134_%s.fits"
        self.setup2()

class CommCase135(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, photlam)"
        self.fname="C135_%s.fits"
        self.setup2()

class CommCase136(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, vegamag)"
        self.fname="C136_%s.fits"
        self.setup2()

class CommCase137(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, flam)"
        self.fname="C137_%s.fits"
        self.setup2()

class CommCase138(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, obmag)"
        self.fname="C138_%s.fits"
        self.setup2()

class CommCase139(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, photlam)"
        self.fname="C139_%s.fits"
        self.setup2()

class CommCase140(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, vegamag)"
        self.fname="C140_%s.fits"
        self.setup2()

class CommCase141(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, flam)"
        self.fname="C141_%s.fits"
        self.setup2()

class CommCase142(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, obmag)"
        self.fname="C142_%s.fits"
        self.setup2()

class CommCase143(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, photlam)"
        self.fname="C143_%s.fits"
        self.setup2()

class CommCase144(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, vegamag)"
        self.fname="C144_%s.fits"
        self.setup2()

class CommCase145(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, flam)"
        self.fname="C145_%s.fits"
        self.setup2()

class CommCase146(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, obmag)"
        self.fname="C146_%s.fits"
        self.setup2()

class CommCase147(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, photlam)"
        self.fname="C147_%s.fits"
        self.setup2()

class CommCase148(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, vegamag)"
        self.fname="C148_%s.fits"
        self.setup2()

class CommCase149(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, flam)"
        self.fname="C149_%s.fits"
        self.setup2()

class CommCase150(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, obmag)"
        self.fname="C150_%s.fits"
        self.setup2()

class CommCase151(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, photlam)"
        self.fname="C151_%s.fits"
        self.setup2()

class CommCase152(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, vegamag)"
        self.fname="C152_%s.fits"
        self.setup2()

class CommCase153(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, flam)"
        self.fname="C153_%s.fits"
        self.setup2()

class CommCase154(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, obmag)"
        self.fname="C154_%s.fits"
        self.setup2()

class CommCase155(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, photlam)"
        self.fname="C155_%s.fits"
        self.setup2()

class CommCase156(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, vegamag)"
        self.fname="C156_%s.fits"
        self.setup2()

class CommCase157(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, flam)"
        self.fname="C157_%s.fits"
        self.setup2()

class CommCase158(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, obmag)"
        self.fname="C158_%s.fits"
        self.setup2()

class CommCase159(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, photlam)"
        self.fname="C159_%s.fits"
        self.setup2()

class CommCase160(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, vegamag)"
        self.fname="C160_%s.fits"
        self.setup2()

class CommCase161(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, flam)"
        self.fname="C161_%s.fits"
        self.setup2()

class CommCase162(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, obmag)"
        self.fname="C162_%s.fits"
        self.setup2()

class CommCase163(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, photlam)"
        self.fname="C163_%s.fits"
        self.setup2()

class CommCase164(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, vegamag)"
        self.fname="C164_%s.fits"
        self.setup2()

class CommCase165(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, flam)"
        self.fname="C165_%s.fits"
        self.setup2()

class CommCase166(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, obmag)"
        self.fname="C166_%s.fits"
        self.setup2()

class CommCase167(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, photlam)"
        self.fname="C167_%s.fits"
        self.setup2()

class CommCase168(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, vegamag)"
        self.fname="C168_%s.fits"
        self.setup2()

class CommCase169(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, flam)"
        self.fname="C169_%s.fits"
        self.setup2()

class CommCase170(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, obmag)"
        self.fname="C170_%s.fits"
        self.setup2()

class CommCase171(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, photlam)"
        self.fname="C171_%s.fits"
        self.setup2()

class CommCase172(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, vegamag)"
        self.fname="C172_%s.fits"
        self.setup2()

class CommCase173(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),0.5,jy)"
        self.fname="C173_%s.fits"
        self.setup2()

class CommCase174(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.0e-14,photnu)"
        self.fname="C174_%s.fits"
        self.setup2()

class CommCase175(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.0e-4,photlam)"
        self.fname="C175_%s.fits"
        self.setup2()

class CommCase176(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.e-27,fnu)"
        self.fname="C176_%s.fits"
        self.setup2()

class CommCase177(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),10000,counts)"
        self.fname="C177_%s.fits"
        self.setup2()

class CommCase178(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),5,obmag)"
        self.fname="C178_%s.fits"
        self.setup2()

class CommCase179(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,3,f110w),18,stmag)"
        self.fname="C179_%s.fits"
        self.setup2()

class CommCase180(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,3,f110w),23,abmag)"
        self.fname="C180_%s.fits"
        self.setup2()

class CommCase181(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C181_%s.fits"
        self.setup2()

class CommCase182(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C182_%s.fits"
        self.setup2()

class CommCase183(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C183_%s.fits"
        self.setup2()

class CommCase184(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C184_%s.fits"
        self.setup2()

class CommCase185(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C185_%s.fits"
        self.setup2()

class CommCase186(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C186_%s.fits"
        self.setup2()

class CommCase187(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C187_%s.fits"
        self.setup2()

class CommCase188(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C188_%s.fits"
        self.setup2()

class CommCase189(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C189_%s.fits"
        self.setup2()

class CommCase190(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C190_%s.fits"
        self.setup2()

class CommCase191(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C191_%s.fits"
        self.setup2()

class CommCase192(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C192_%s.fits"
        self.setup2()

class CommCase193(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.,mjy)"
        self.fname="C193_%s.fits"
        self.setup2()

class CommCase194(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.e-15,photnu)"
        self.fname="C194_%s.fits"
        self.setup2()

class CommCase195(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.e-26,fnu)"
        self.fname="C195_%s.fits"
        self.setup2()

class CommCase196(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.e-3,jy)"
        self.fname="C196_%s.fits"
        self.setup2()

class CommCase197(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),16.0,abmag)"
        self.fname="C197_%s.fits"
        self.setup2()

class CommCase198(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),16.0,stmag)"
        self.fname="C198_%s.fits"
        self.setup2()

class CommCase199(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C199_%s.fits"
        self.setup2()

class CommCase200(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C200_%s.fits"
        self.setup2()

class CommCase201(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C201_%s.fits"
        self.setup2()

class CommCase202(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C202_%s.fits"
        self.setup2()

class CommCase203(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C203_%s.fits"
        self.setup2()

class CommCase204(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C204_%s.fits"
        self.setup2()

class CommCase205(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C205_%s.fits"
        self.setup2()

class CommCase206(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C206_%s.fits"
        self.setup2()

class CommCase207(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C207_%s.fits"
        self.setup2()

class CommCase208(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C208_%s.fits"
        self.setup2()

class CommCase209(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C209_%s.fits"
        self.setup2()

class CommCase210(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C210_%s.fits"
        self.setup2()

class CommCase211(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.,mjy)"
        self.fname="C211_%s.fits"
        self.setup2()

class CommCase212(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.e-15,photnu)"
        self.fname="C212_%s.fits"
        self.setup2()

class CommCase213(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.e-26,fnu)"
        self.fname="C213_%s.fits"
        self.setup2()

class CommCase214(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.e-3,jy)"
        self.fname="C214_%s.fits"
        self.setup2()

class CommCase215(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),16.0,abmag)"
        self.fname="C215_%s.fits"
        self.setup2()

class CommCase216(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),16.0,stmag)"
        self.fname="C216_%s.fits"
        self.setup2()

class CommCase217(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C217_%s.fits"
        self.setup2()

class CommCase218(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C218_%s.fits"
        self.setup2()

class CommCase219(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C219_%s.fits"
        self.setup2()

class CommCase220(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C220_%s.fits"
        self.setup2()

class CommCase221(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C221_%s.fits"
        self.setup2()

class CommCase222(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C222_%s.fits"
        self.setup2()

class CommCase223(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C223_%s.fits"
        self.setup2()

class CommCase224(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C224_%s.fits"
        self.setup2()

class CommCase225(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C225_%s.fits"
        self.setup2()

class CommCase226(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C226_%s.fits"
        self.setup2()

class CommCase227(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C227_%s.fits"
        self.setup2()

class CommCase228(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C228_%s.fits"
        self.setup2()

class CommCase229(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.,mjy)"
        self.fname="C229_%s.fits"
        self.setup2()

class CommCase230(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.e-15,photnu)"
        self.fname="C230_%s.fits"
        self.setup2()

class CommCase231(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.e-26,fnu)"
        self.fname="C231_%s.fits"
        self.setup2()

class CommCase232(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.e-3,jy)"
        self.fname="C232_%s.fits"
        self.setup2()

class CommCase233(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),16.0,abmag)"
        self.fname="C233_%s.fits"
        self.setup2()

class CommCase234(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),16.0,stmag)"
        self.fname="C234_%s.fits"
        self.setup2()

class CommCase235(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C235_%s.fits"
        self.setup2()

class CommCase236(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C236_%s.fits"
        self.setup2()

class CommCase237(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C237_%s.fits"
        self.setup2()

class CommCase238(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C238_%s.fits"
        self.setup2()

class CommCase239(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C239_%s.fits"
        self.setup2()

class CommCase240(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C240_%s.fits"
        self.setup2()

class CommCase241(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C241_%s.fits"
        self.setup2()

class CommCase242(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C242_%s.fits"
        self.setup2()

class CommCase243(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C243_%s.fits"
        self.setup2()

class CommCase244(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C244_%s.fits"
        self.setup2()

class CommCase245(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C245_%s.fits"
        self.setup2()

class CommCase246(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C246_%s.fits"
        self.setup2()

class CommCase247(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.,mjy)"
        self.fname="C247_%s.fits"
        self.setup2()

class CommCase248(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.e-15,photnu)"
        self.fname="C248_%s.fits"
        self.setup2()

class CommCase249(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.e-26,fnu)"
        self.fname="C249_%s.fits"
        self.setup2()

class CommCase250(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.e-3,jy)"
        self.fname="C250_%s.fits"
        self.setup2()

class CommCase251(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),16.0,abmag)"
        self.fname="C251_%s.fits"
        self.setup2()

class CommCase252(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),16.0,stmag)"
        self.fname="C252_%s.fits"
        self.setup2()

class CommCase253(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C253_%s.fits"
        self.setup2()

class CommCase254(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C254_%s.fits"
        self.setup2()

class CommCase255(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C255_%s.fits"
        self.setup2()

class CommCase256(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C256_%s.fits"
        self.setup2()

class CommCase257(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C257_%s.fits"
        self.setup2()

class CommCase258(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C258_%s.fits"
        self.setup2()

class CommCase259(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C259_%s.fits"
        self.setup2()

class CommCase260(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C260_%s.fits"
        self.setup2()

class CommCase261(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C261_%s.fits"
        self.setup2()

class CommCase262(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C262_%s.fits"
        self.setup2()

class CommCase263(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C263_%s.fits"
        self.setup2()

class CommCase264(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C264_%s.fits"
        self.setup2()

class CommCase265(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.,mjy)"
        self.fname="C265_%s.fits"
        self.setup2()

class CommCase266(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.e-15,photnu)"
        self.fname="C266_%s.fits"
        self.setup2()

class CommCase267(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.e-26,fnu)"
        self.fname="C267_%s.fits"
        self.setup2()

class CommCase268(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.e-3,jy)"
        self.fname="C268_%s.fits"
        self.setup2()

class CommCase269(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),16.0,abmag)"
        self.fname="C269_%s.fits"
        self.setup2()

class CommCase270(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),16.0,stmag)"
        self.fname="C270_%s.fits"
        self.setup2()

class CommCase271(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C271_%s.fits"
        self.setup2()

class CommCase272(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C272_%s.fits"
        self.setup2()

class CommCase273(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C273_%s.fits"
        self.setup2()

class CommCase274(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C274_%s.fits"
        self.setup2()

class CommCase275(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C275_%s.fits"
        self.setup2()

class CommCase276(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C276_%s.fits"
        self.setup2()

class CommCase277(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C277_%s.fits"
        self.setup2()

class CommCase278(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C278_%s.fits"
        self.setup2()

class CommCase279(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C279_%s.fits"
        self.setup2()

class CommCase280(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C280_%s.fits"
        self.setup2()

class CommCase281(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C281_%s.fits"
        self.setup2()

class CommCase282(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C282_%s.fits"
        self.setup2()

class CommCase283(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.,mjy)"
        self.fname="C283_%s.fits"
        self.setup2()

class CommCase284(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.e-15,photnu)"
        self.fname="C284_%s.fits"
        self.setup2()

class CommCase285(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.e-26,fnu)"
        self.fname="C285_%s.fits"
        self.setup2()

class CommCase286(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.e-3,jy)"
        self.fname="C286_%s.fits"
        self.setup2()

class CommCase287(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),16.0,abmag)"
        self.fname="C287_%s.fits"
        self.setup2()

class CommCase288(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),16.0,stmag)"
        self.fname="C288_%s.fits"
        self.setup2()

class CommCase289(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C289_%s.fits"
        self.setup2()

class CommCase290(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C290_%s.fits"
        self.setup2()

class CommCase291(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C291_%s.fits"
        self.setup2()

class CommCase292(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C292_%s.fits"
        self.setup2()

class CommCase293(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C293_%s.fits"
        self.setup2()

class CommCase294(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C294_%s.fits"
        self.setup2()

class CommCase295(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C295_%s.fits"
        self.setup2()

class CommCase296(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C296_%s.fits"
        self.setup2()

class CommCase297(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C297_%s.fits"
        self.setup2()

class CommCase298(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C298_%s.fits"
        self.setup2()

class CommCase299(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C299_%s.fits"
        self.setup2()

class CommCase300(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C300_%s.fits"
        self.setup2()

class CommCase301(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.,mjy)"
        self.fname="C301_%s.fits"
        self.setup2()

class CommCase302(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        self.fname="C302_%s.fits"
        self.setup2()

class CommCase303(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        self.fname="C303_%s.fits"
        self.setup2()

class CommCase304(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        self.fname="C304_%s.fits"
        self.setup2()

class CommCase305(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        self.fname="C305_%s.fits"
        self.setup2()

class CommCase306(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        self.fname="C306_%s.fits"
        self.setup2()

class CommCase307(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.,mjy)"
        self.fname="C307_%s.fits"
        self.setup2()

class CommCase308(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        self.fname="C308_%s.fits"
        self.setup2()

class CommCase309(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        self.fname="C309_%s.fits"
        self.setup2()

class CommCase310(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        self.fname="C310_%s.fits"
        self.setup2()

class CommCase311(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        self.fname="C311_%s.fits"
        self.setup2()

class CommCase312(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        self.fname="C312_%s.fits"
        self.setup2()

class CommCase313(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C313_%s.fits"
        self.setup2()

class CommCase314(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C314_%s.fits"
        self.setup2()

class CommCase315(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C315_%s.fits"
        self.setup2()

class CommCase316(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C316_%s.fits"
        self.setup2()

class CommCase317(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C317_%s.fits"
        self.setup2()

class CommCase318(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C318_%s.fits"
        self.setup2()

class CommCase319(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C319_%s.fits"
        self.setup2()

class CommCase320(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C320_%s.fits"
        self.setup2()

class CommCase321(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C321_%s.fits"
        self.setup2()

class CommCase322(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C322_%s.fits"
        self.setup2()

class CommCase323(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C323_%s.fits"
        self.setup2()

class CommCase324(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C324_%s.fits"
        self.setup2()

class CommCase325(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.,mjy)"
        self.fname="C325_%s.fits"
        self.setup2()

class CommCase326(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        self.fname="C326_%s.fits"
        self.setup2()

class CommCase327(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        self.fname="C327_%s.fits"
        self.setup2()

class CommCase328(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        self.fname="C328_%s.fits"
        self.setup2()

class CommCase329(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        self.fname="C329_%s.fits"
        self.setup2()

class CommCase330(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        self.fname="C330_%s.fits"
        self.setup2()

class CommCase331(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.,mjy)"
        self.fname="C331_%s.fits"
        self.setup2()

class CommCase332(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        self.fname="C332_%s.fits"
        self.setup2()

class CommCase333(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        self.fname="C333_%s.fits"
        self.setup2()

class CommCase334(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        self.fname="C334_%s.fits"
        self.setup2()

class CommCase335(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        self.fname="C335_%s.fits"
        self.setup2()

class CommCase336(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        self.fname="C336_%s.fits"
        self.setup2()

class CommCase337(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C337_%s.fits"
        self.setup2()

class CommCase338(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C338_%s.fits"
        self.setup2()

class CommCase339(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C339_%s.fits"
        self.setup2()

class CommCase340(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C340_%s.fits"
        self.setup2()

class CommCase341(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C341_%s.fits"
        self.setup2()

class CommCase342(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C342_%s.fits"
        self.setup2()

class CommCase343(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C343_%s.fits"
        self.setup2()

class CommCase344(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C344_%s.fits"
        self.setup2()

class CommCase345(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C345_%s.fits"
        self.setup2()

class CommCase346(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C346_%s.fits"
        self.setup2()

class CommCase347(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C347_%s.fits"
        self.setup2()

class CommCase348(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C348_%s.fits"
        self.setup2()

class CommCase349(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.,mjy)"
        self.fname="C349_%s.fits"
        self.setup2()

class CommCase350(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        self.fname="C350_%s.fits"
        self.setup2()

class CommCase351(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        self.fname="C351_%s.fits"
        self.setup2()

class CommCase352(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        self.fname="C352_%s.fits"
        self.setup2()

class CommCase353(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        self.fname="C353_%s.fits"
        self.setup2()

class CommCase354(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        self.fname="C354_%s.fits"
        self.setup2()

class CommCase355(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.,mjy)"
        self.fname="C355_%s.fits"
        self.setup2()

class CommCase356(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        self.fname="C356_%s.fits"
        self.setup2()

class CommCase357(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        self.fname="C357_%s.fits"
        self.setup2()

class CommCase358(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        self.fname="C358_%s.fits"
        self.setup2()

class CommCase359(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        self.fname="C359_%s.fits"
        self.setup2()

class CommCase360(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        self.fname="C360_%s.fits"
        self.setup2()

class CommCase361(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C361_%s.fits"
        self.setup2()

class CommCase362(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C362_%s.fits"
        self.setup2()

class CommCase363(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C363_%s.fits"
        self.setup2()

class CommCase364(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C364_%s.fits"
        self.setup2()

class CommCase365(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C365_%s.fits"
        self.setup2()

class CommCase366(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C366_%s.fits"
        self.setup2()

class CommCase367(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C367_%s.fits"
        self.setup2()

class CommCase368(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C368_%s.fits"
        self.setup2()

class CommCase369(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C369_%s.fits"
        self.setup2()

class CommCase370(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C370_%s.fits"
        self.setup2()

class CommCase371(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C371_%s.fits"
        self.setup2()

class CommCase372(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C372_%s.fits"
        self.setup2()

class CommCase373(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.,mjy)"
        self.fname="C373_%s.fits"
        self.setup2()

class CommCase374(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        self.fname="C374_%s.fits"
        self.setup2()

class CommCase375(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        self.fname="C375_%s.fits"
        self.setup2()

class CommCase376(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        self.fname="C376_%s.fits"
        self.setup2()

class CommCase377(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        self.fname="C377_%s.fits"
        self.setup2()

class CommCase378(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        self.fname="C378_%s.fits"
        self.setup2()

class CommCase379(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.,mjy)"
        self.fname="C379_%s.fits"
        self.setup2()

class CommCase380(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        self.fname="C380_%s.fits"
        self.setup2()

class CommCase381(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        self.fname="C381_%s.fits"
        self.setup2()

class CommCase382(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        self.fname="C382_%s.fits"
        self.setup2()

class CommCase383(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        self.fname="C383_%s.fits"
        self.setup2()

class CommCase384(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        self.fname="C384_%s.fits"
        self.setup2()

class CommCase385(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C385_%s.fits"
        self.setup2()

class CommCase386(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C386_%s.fits"
        self.setup2()

class CommCase387(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C387_%s.fits"
        self.setup2()

class CommCase388(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C388_%s.fits"
        self.setup2()

class CommCase389(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C389_%s.fits"
        self.setup2()

class CommCase390(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C390_%s.fits"
        self.setup2()

class CommCase391(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C391_%s.fits"
        self.setup2()

class CommCase392(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C392_%s.fits"
        self.setup2()

class CommCase393(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C393_%s.fits"
        self.setup2()

class CommCase394(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C394_%s.fits"
        self.setup2()

class CommCase395(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C395_%s.fits"
        self.setup2()

class CommCase396(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C396_%s.fits"
        self.setup2()

class CommCase397(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.,mjy)"
        self.fname="C397_%s.fits"
        self.setup2()

class CommCase398(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        self.fname="C398_%s.fits"
        self.setup2()

class CommCase399(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        self.fname="C399_%s.fits"
        self.setup2()

class CommCase400(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        self.fname="C400_%s.fits"
        self.setup2()

class CommCase401(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        self.fname="C401_%s.fits"
        self.setup2()

class CommCase402(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        self.fname="C402_%s.fits"
        self.setup2()

class CommCase403(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.,mjy)"
        self.fname="C403_%s.fits"
        self.setup2()

class CommCase404(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        self.fname="C404_%s.fits"
        self.setup2()

class CommCase405(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        self.fname="C405_%s.fits"
        self.setup2()

class CommCase406(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        self.fname="C406_%s.fits"
        self.setup2()

class CommCase407(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        self.fname="C407_%s.fits"
        self.setup2()

class CommCase408(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        self.fname="C408_%s.fits"
        self.setup2()

class CommCase409(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C409_%s.fits"
        self.setup2()

class CommCase410(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C410_%s.fits"
        self.setup2()

class CommCase411(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C411_%s.fits"
        self.setup2()

class CommCase412(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C412_%s.fits"
        self.setup2()

class CommCase413(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C413_%s.fits"
        self.setup2()

class CommCase414(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C414_%s.fits"
        self.setup2()

class CommCase415(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C415_%s.fits"
        self.setup2()

class CommCase416(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C416_%s.fits"
        self.setup2()

class CommCase417(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C417_%s.fits"
        self.setup2()

class CommCase418(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C418_%s.fits"
        self.setup2()

class CommCase419(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C419_%s.fits"
        self.setup2()

class CommCase420(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C420_%s.fits"
        self.setup2()

class CommCase421(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.,mjy)"
        self.fname="C421_%s.fits"
        self.setup2()

class CommCase422(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        self.fname="C422_%s.fits"
        self.setup2()

class CommCase423(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        self.fname="C423_%s.fits"
        self.setup2()

class CommCase424(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        self.fname="C424_%s.fits"
        self.setup2()

class CommCase425(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        self.fname="C425_%s.fits"
        self.setup2()

class CommCase426(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        self.fname="C426_%s.fits"
        self.setup2()

class CommCase427(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.,mjy)"
        self.fname="C427_%s.fits"
        self.setup2()

class CommCase428(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        self.fname="C428_%s.fits"
        self.setup2()

class CommCase429(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        self.fname="C429_%s.fits"
        self.setup2()

class CommCase430(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        self.fname="C430_%s.fits"
        self.setup2()

class CommCase431(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        self.fname="C431_%s.fits"
        self.setup2()

class CommCase432(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        self.fname="C432_%s.fits"
        self.setup2()

class CommCase433(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        self.fname="C433_%s.fits"
        self.setup2()

class CommCase434(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        self.fname="C434_%s.fits"
        self.setup2()

class CommCase435(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        self.fname="C435_%s.fits"
        self.setup2()

class CommCase436(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        self.fname="C436_%s.fits"
        self.setup2()

class CommCase437(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        self.fname="C437_%s.fits"
        self.setup2()

class CommCase438(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        self.fname="C438_%s.fits"
        self.setup2()

class CommCase439(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        self.fname="C439_%s.fits"
        self.setup2()

class CommCase440(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        self.fname="C440_%s.fits"
        self.setup2()

class CommCase441(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        self.fname="C441_%s.fits"
        self.setup2()

class CommCase442(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        self.fname="C442_%s.fits"
        self.setup2()

class CommCase443(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        self.fname="C443_%s.fits"
        self.setup2()

class CommCase444(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        self.fname="C444_%s.fits"
        self.setup2()

class CommCase445(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.,mjy)"
        self.fname="C445_%s.fits"
        self.setup2()

class CommCase446(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        self.fname="C446_%s.fits"
        self.setup2()

class CommCase447(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        self.fname="C447_%s.fits"
        self.setup2()

class CommCase448(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        self.fname="C448_%s.fits"
        self.setup2()

class CommCase449(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        self.fname="C449_%s.fits"
        self.setup2()

class CommCase450(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        self.fname="C450_%s.fits"
        self.setup2()

class CommCase451(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.,mjy)"
        self.fname="C451_%s.fits"
        self.setup2()

class CommCase452(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        self.fname="C452_%s.fits"
        self.setup2()

class CommCase453(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        self.fname="C453_%s.fits"
        self.setup2()

class CommCase454(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        self.fname="C454_%s.fits"
        self.setup2()

class CommCase455(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        self.fname="C455_%s.fits"
        self.setup2()

class CommCase456(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        self.fname="C456_%s.fits"
        self.setup2()

class CommCase457(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,1.0),band(nicmos,2,f205w),20,mjy)"
        self.fname="C457_%s.fits"
        self.setup2()

class CommCase458(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,1.5),band(nicmos,2,f237m),100000,counts)"
        self.fname="C458_%s.fits"
        self.setup2()

class CommCase459(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,h),1.0e-14,photnu)"
        self.fname="C459_%s.fits"
        self.setup2()

class CommCase460(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,h),1.0e-26,fnu)"
        self.fname="C460_%s.fits"
        self.setup2()

class CommCase461(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,k),5,obmag)"
        self.fname="C461_%s.fits"
        self.setup2()

class CommCase462(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(nicmos,2,f237m),0.5,jy)"
        self.fname="C462_%s.fits"
        self.setup2()

class CommCase463(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(nicmos,2,f237m),1.0e-4,photlam)"
        self.fname="C463_%s.fits"
        self.setup2()

class CommCase464(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="rn(z(crgridkc96$sb_template.fits,2.5),band(nicmos,3,f215n),20,mjy)"
        self.fname="C464_%s.fits"
        self.setup2()

class CommCase465(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.fname="C465_%s.fits"
        self.setup2()

class CommCase466(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits)"
        self.fname="C466_%s.fits"
        self.setup2()

class CommCase467(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits)"
        self.fname="C467_%s.fits"
        self.setup2()

class CommCase468(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits)"
        self.fname="C468_%s.fits"
        self.setup2()

class CommCase469(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits)"
        self.fname="C469_%s.fits"
        self.setup2()

class CommCase470(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits)"
        self.fname="C470_%s.fits"
        self.setup2()

class CommCase471(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="None"
        self.spectrum="spec(egal.dat)"
        self.fname="C471_%s.fits"
        self.setup2()

class CommCase472(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C472_%s.fits"
        self.setup2()

class CommCase473(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.fname="C473_%s.fits"
        self.setup2()

class CommCase474(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C474_%s.fits"
        self.setup2()

class CommCase475(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.fname="C475_%s.fits"
        self.setup2()

class CommCase476(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.fname="C476_%s.fits"
        self.setup2()

class CommCase477(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        self.fname="C477_%s.fits"
        self.setup2()

class CommCase478(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        self.fname="C478_%s.fits"
        self.setup2()

class CommCase479(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,coron,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        self.fname="C479_%s.fits"
        self.setup2()

class CommCase480(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C480_%s.fits"
        self.setup2()

class CommCase481(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C481_%s.fits"
        self.setup2()

class CommCase482(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C482_%s.fits"
        self.setup2()

class CommCase483(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.fname="C483_%s.fits"
        self.setup2()

class CommCase484(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C484_%s.fits"
        self.setup2()

class CommCase485(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C485_%s.fits"
        self.setup2()

class CommCase486(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C486_%s.fits"
        self.setup2()

class CommCase487(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C487_%s.fits"
        self.setup2()

class CommCase488(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C488_%s.fits"
        self.setup2()

class CommCase489(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C489_%s.fits"
        self.setup2()

class CommCase490(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C490_%s.fits"
        self.setup2()

class CommCase491(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C491_%s.fits"
        self.setup2()

class CommCase492(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C492_%s.fits"
        self.setup2()

class CommCase493(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C493_%s.fits"
        self.setup2()

class CommCase494(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C494_%s.fits"
        self.setup2()

class CommCase495(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        self.fname="C495_%s.fits"
        self.setup2()

class CommCase496(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C496_%s.fits"
        self.setup2()

class CommCase497(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C497_%s.fits"
        self.setup2()

class CommCase498(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C498_%s.fits"
        self.setup2()

class CommCase499(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C499_%s.fits"
        self.setup2()

class CommCase500(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C500_%s.fits"
        self.setup2()

class CommCase501(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C501_%s.fits"
        self.setup2()

class CommCase502(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C502_%s.fits"
        self.setup2()

class CommCase503(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C503_%s.fits"
        self.setup2()

class CommCase504(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C504_%s.fits"
        self.setup2()

class CommCase505(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C505_%s.fits"
        self.setup2()

class CommCase506(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C506_%s.fits"
        self.setup2()

class CommCase507(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.fname="C507_%s.fits"
        self.setup2()

class CommCase508(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C508_%s.fits"
        self.setup2()

class CommCase509(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C509_%s.fits"
        self.setup2()

class CommCase510(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C510_%s.fits"
        self.setup2()

class CommCase511(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C511_%s.fits"
        self.setup2()

class CommCase512(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C512_%s.fits"
        self.setup2()

class CommCase513(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C513_%s.fits"
        self.setup2()

class CommCase514(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C514_%s.fits"
        self.setup2()

class CommCase515(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C515_%s.fits"
        self.setup2()

class CommCase516(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C516_%s.fits"
        self.setup2()

class CommCase517(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C517_%s.fits"
        self.setup2()

class CommCase518(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C518_%s.fits"
        self.setup2()

class CommCase519(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C519_%s.fits"
        self.setup2()

class CommCase520(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C520_%s.fits"
        self.setup2()

class CommCase521(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C521_%s.fits"
        self.setup2()

class CommCase522(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C522_%s.fits"
        self.setup2()

class CommCase523(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C523_%s.fits"
        self.setup2()

class CommCase524(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C524_%s.fits"
        self.setup2()

class CommCase525(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C525_%s.fits"
        self.setup2()

class CommCase526(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C526_%s.fits"
        self.setup2()

class CommCase527(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C527_%s.fits"
        self.setup2()

class CommCase528(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C528_%s.fits"
        self.setup2()

class CommCase529(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C529_%s.fits"
        self.setup2()

class CommCase530(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C530_%s.fits"
        self.setup2()

class CommCase531(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C531_%s.fits"
        self.setup2()

class CommCase532(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C532_%s.fits"
        self.setup2()

class CommCase533(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C533_%s.fits"
        self.setup2()

class CommCase534(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C534_%s.fits"
        self.setup2()

class CommCase535(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        self.fname="C535_%s.fits"
        self.setup2()

class CommCase536(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        self.fname="C536_%s.fits"
        self.setup2()

class CommCase537(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C537_%s.fits"
        self.setup2()

class CommCase538(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        self.fname="C538_%s.fits"
        self.setup2()

class CommCase539(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w,coron"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C539_%s.fits"
        self.setup2()

class CommCase540(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C540_%s.fits"
        self.setup2()

class CommCase541(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C541_%s.fits"
        self.setup2()

class CommCase542(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C542_%s.fits"
        self.setup2()

class CommCase543(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C543_%s.fits"
        self.setup2()

class CommCase544(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C544_%s.fits"
        self.setup2()

class CommCase545(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C545_%s.fits"
        self.setup2()

class CommCase546(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C546_%s.fits"
        self.setup2()

class CommCase547(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C547_%s.fits"
        self.setup2()

class CommCase548(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C548_%s.fits"
        self.setup2()

class CommCase549(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C549_%s.fits"
        self.setup2()

class CommCase550(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C550_%s.fits"
        self.setup2()

class CommCase551(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C551_%s.fits"
        self.setup2()

class CommCase552(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C552_%s.fits"
        self.setup2()

class CommCase553(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C553_%s.fits"
        self.setup2()

class CommCase554(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C554_%s.fits"
        self.setup2()

class CommCase555(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C555_%s.fits"
        self.setup2()

class CommCase556(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C556_%s.fits"
        self.setup2()

class CommCase557(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C557_%s.fits"
        self.setup2()

class CommCase558(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C558_%s.fits"
        self.setup2()

class CommCase559(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C559_%s.fits"
        self.setup2()

class CommCase560(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C560_%s.fits"
        self.setup2()

class CommCase561(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.fname="C561_%s.fits"
        self.setup2()

class CommCase562(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C562_%s.fits"
        self.setup2()

class CommCase563(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C563_%s.fits"
        self.setup2()

class CommCase564(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C564_%s.fits"
        self.setup2()

class CommCase565(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C565_%s.fits"
        self.setup2()

class CommCase566(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C566_%s.fits"
        self.setup2()

class CommCase567(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.fname="C567_%s.fits"
        self.setup2()

class CommCase568(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C568_%s.fits"
        self.setup2()

class CommCase569(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C569_%s.fits"
        self.setup2()

class CommCase570(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C570_%s.fits"
        self.setup2()

class CommCase571(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C571_%s.fits"
        self.setup2()

class CommCase572(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C572_%s.fits"
        self.setup2()

class CommCase573(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C573_%s.fits"
        self.setup2()

class CommCase574(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C574_%s.fits"
        self.setup2()

class CommCase575(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C575_%s.fits"
        self.setup2()

class CommCase576(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C576_%s.fits"
        self.setup2()

class CommCase577(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C577_%s.fits"
        self.setup2()

class CommCase578(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C578_%s.fits"
        self.setup2()

class CommCase579(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.fname="C579_%s.fits"
        self.setup2()

class CommCase580(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.fname="C580_%s.fits"
        self.setup2()

class CommCase581(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.fname="C581_%s.fits"
        self.setup2()

class CommCase582(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.fname="C582_%s.fits"
        self.setup2()

class CommCase583(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.fname="C583_%s.fits"
        self.setup2()

class CommCase584(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C584_%s.fits"
        self.setup2()

class CommCase585(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C585_%s.fits"
        self.setup2()

class CommCase586(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C586_%s.fits"
        self.setup2()

class CommCase587(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.fname="C587_%s.fits"
        self.setup2()

class CommCase588(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C588_%s.fits"
        self.setup2()

class CommCase589(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.fname="C589_%s.fits"
        self.setup2()

class CommCase590(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C590_%s.fits"
        self.setup2()

class CommCase591(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C591_%s.fits"
        self.setup2()

class CommCase592(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.fname="C592_%s.fits"
        self.setup2()

class CommCase593(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C593_%s.fits"
        self.setup2()

class CommCase594(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C594_%s.fits"
        self.setup2()

class CommCase595(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C595_%s.fits"
        self.setup2()

class CommCase596(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr459m#4592"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C596_%s.fits"
        self.setup2()

class CommCase597(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C597_%s.fits"
        self.setup2()

class CommCase598(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr505n#5050"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C598_%s.fits"
        self.setup2()

class CommCase599(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C599_%s.fits"
        self.setup2()

class CommCase600(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,fr656n#6560"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C600_%s.fits"
        self.setup2()

class CommCase601(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        self.fname="C601_%s.fits"
        self.setup2()

class CommCase602(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C602_%s.fits"
        self.setup2()

class CommCase603(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C603_%s.fits"
        self.setup2()

class CommCase604(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C604_%s.fits"
        self.setup2()

class CommCase605(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C605_%s.fits"
        self.setup2()

class CommCase606(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.fname="C606_%s.fits"
        self.setup2()

class CommCase607(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C607_%s.fits"
        self.setup2()

class CommCase608(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C608_%s.fits"
        self.setup2()

class CommCase609(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C609_%s.fits"
        self.setup2()

class CommCase610(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="em(4000.0,10.0,1.0E-16,flam)"
        self.fname="C610_%s.fits"
        self.setup2()

class CommCase611(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C611_%s.fits"
        self.setup2()

class CommCase612(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C612_%s.fits"
        self.setup2()

class CommCase613(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C613_%s.fits"
        self.setup2()

class CommCase614(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C614_%s.fits"
        self.setup2()

class CommCase615(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.fname="C615_%s.fits"
        self.setup2()

class CommCase616(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C616_%s.fits"
        self.setup2()

class CommCase617(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C617_%s.fits"
        self.setup2()

class CommCase618(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,hrc,pr200l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C618_%s.fits"
        self.setup2()

class CommCase619(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C619_%s.fits"
        self.setup2()

class CommCase620(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.fname="C620_%s.fits"
        self.setup2()

class CommCase621(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C621_%s.fits"
        self.setup2()

class CommCase622(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C622_%s.fits"
        self.setup2()

class CommCase623(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f115lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C623_%s.fits"
        self.setup2()

class CommCase624(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C624_%s.fits"
        self.setup2()

class CommCase625(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f122m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C625_%s.fits"
        self.setup2()

class CommCase626(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.fname="C626_%s.fits"
        self.setup2()

class CommCase627(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        self.fname="C627_%s.fits"
        self.setup2()

class CommCase628(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f125lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C628_%s.fits"
        self.setup2()

class CommCase629(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C629_%s.fits"
        self.setup2()

class CommCase630(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f140lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C630_%s.fits"
        self.setup2()

class CommCase631(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        self.fname="C631_%s.fits"
        self.setup2()

class CommCase632(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        self.fname="C632_%s.fits"
        self.setup2()

class CommCase633(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C633_%s.fits"
        self.setup2()

class CommCase634(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        self.fname="C634_%s.fits"
        self.setup2()

class CommCase635(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C635_%s.fits"
        self.setup2()

class CommCase636(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f150lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C636_%s.fits"
        self.setup2()

class CommCase637(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C637_%s.fits"
        self.setup2()

class CommCase638(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,f165lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C638_%s.fits"
        self.setup2()

class CommCase639(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        self.fname="C639_%s.fits"
        self.setup2()

class CommCase640(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C640_%s.fits"
        self.setup2()

class CommCase641(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C641_%s.fits"
        self.setup2()

class CommCase642(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C642_%s.fits"
        self.setup2()

class CommCase643(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C643_%s.fits"
        self.setup2()

class CommCase644(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.fname="C644_%s.fits"
        self.setup2()

class CommCase645(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C645_%s.fits"
        self.setup2()

class CommCase646(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C646_%s.fits"
        self.setup2()

class CommCase647(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C647_%s.fits"
        self.setup2()

class CommCase648(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr110l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.fname="C648_%s.fits"
        self.setup2()

class CommCase649(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        self.fname="C649_%s.fits"
        self.setup2()

class CommCase650(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C650_%s.fits"
        self.setup2()

class CommCase651(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C651_%s.fits"
        self.setup2()

class CommCase652(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C652_%s.fits"
        self.setup2()

class CommCase653(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C653_%s.fits"
        self.setup2()

class CommCase654(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.fname="C654_%s.fits"
        self.setup2()

class CommCase655(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C655_%s.fits"
        self.setup2()

class CommCase656(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C656_%s.fits"
        self.setup2()

class CommCase657(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,sbc,pr130l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.fname="C657_%s.fits"
        self.setup2()

class CommCase658(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C658_%s.fits"
        self.setup2()

class CommCase659(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C659_%s.fits"
        self.setup2()

class CommCase660(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C660_%s.fits"
        self.setup2()

class CommCase661(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C661_%s.fits"
        self.setup2()

class CommCase662(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C662_%s.fits"
        self.setup2()

class CommCase663(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C663_%s.fits"
        self.setup2()

class CommCase664(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C664_%s.fits"
        self.setup2()

class CommCase665(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C665_%s.fits"
        self.setup2()

class CommCase666(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C666_%s.fits"
        self.setup2()

class CommCase667(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C667_%s.fits"
        self.setup2()

class CommCase668(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C668_%s.fits"
        self.setup2()

class CommCase669(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C669_%s.fits"
        self.setup2()

class CommCase670(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C670_%s.fits"
        self.setup2()

class CommCase671(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C671_%s.fits"
        self.setup2()

class CommCase672(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C672_%s.fits"
        self.setup2()

class CommCase673(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C673_%s.fits"
        self.setup2()

class CommCase674(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C674_%s.fits"
        self.setup2()

class CommCase675(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C675_%s.fits"
        self.setup2()

class CommCase676(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C676_%s.fits"
        self.setup2()

class CommCase677(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C677_%s.fits"
        self.setup2()

class CommCase678(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C678_%s.fits"
        self.setup2()

class CommCase679(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C679_%s.fits"
        self.setup2()

class CommCase680(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C680_%s.fits"
        self.setup2()

class CommCase681(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C681_%s.fits"
        self.setup2()

class CommCase682(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C682_%s.fits"
        self.setup2()

class CommCase683(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C683_%s.fits"
        self.setup2()

class CommCase684(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C684_%s.fits"
        self.setup2()

class CommCase685(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.fname="C685_%s.fits"
        self.setup2()

class CommCase686(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C686_%s.fits"
        self.setup2()

class CommCase687(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C687_%s.fits"
        self.setup2()

class CommCase688(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C688_%s.fits"
        self.setup2()

class CommCase689(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C689_%s.fits"
        self.setup2()

class CommCase690(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.fname="C690_%s.fits"
        self.setup2()

class CommCase691(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w,pol_v"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C691_%s.fits"
        self.setup2()

class CommCase692(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C692_%s.fits"
        self.setup2()

class CommCase693(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C693_%s.fits"
        self.setup2()

class CommCase694(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C694_%s.fits"
        self.setup2()

class CommCase695(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C695_%s.fits"
        self.setup2()

class CommCase696(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C696_%s.fits"
        self.setup2()

class CommCase697(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C697_%s.fits"
        self.setup2()

class CommCase698(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C698_%s.fits"
        self.setup2()

class CommCase699(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C699_%s.fits"
        self.setup2()

class CommCase700(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C700_%s.fits"
        self.setup2()

class CommCase701(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C701_%s.fits"
        self.setup2()

class CommCase702(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C702_%s.fits"
        self.setup2()

class CommCase703(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C703_%s.fits"
        self.setup2()

class CommCase704(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C704_%s.fits"
        self.setup2()

class CommCase705(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C705_%s.fits"
        self.setup2()

class CommCase706(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C706_%s.fits"
        self.setup2()

class CommCase707(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C707_%s.fits"
        self.setup2()

class CommCase708(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C708_%s.fits"
        self.setup2()

class CommCase709(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C709_%s.fits"
        self.setup2()

class CommCase710(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C710_%s.fits"
        self.setup2()

class CommCase711(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C711_%s.fits"
        self.setup2()

class CommCase712(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C712_%s.fits"
        self.setup2()

class CommCase713(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C713_%s.fits"
        self.setup2()

class CommCase714(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C714_%s.fits"
        self.setup2()

class CommCase715(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C715_%s.fits"
        self.setup2()

class CommCase716(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C716_%s.fits"
        self.setup2()

class CommCase717(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C717_%s.fits"
        self.setup2()

class CommCase718(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C718_%s.fits"
        self.setup2()

class CommCase719(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C719_%s.fits"
        self.setup2()

class CommCase720(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C720_%s.fits"
        self.setup2()

class CommCase721(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C721_%s.fits"
        self.setup2()

class CommCase722(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C722_%s.fits"
        self.setup2()

class CommCase723(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C723_%s.fits"
        self.setup2()

class CommCase724(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C724_%s.fits"
        self.setup2()

class CommCase725(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C725_%s.fits"
        self.setup2()

class CommCase726(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C726_%s.fits"
        self.setup2()

class CommCase727(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C727_%s.fits"
        self.setup2()

class CommCase728(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C728_%s.fits"
        self.setup2()

class CommCase729(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C729_%s.fits"
        self.setup2()

class CommCase730(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C730_%s.fits"
        self.setup2()

class CommCase731(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C731_%s.fits"
        self.setup2()

class CommCase732(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        self.fname="C732_%s.fits"
        self.setup2()

class CommCase733(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C733_%s.fits"
        self.setup2()

class CommCase734(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C734_%s.fits"
        self.setup2()

class CommCase735(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr1016n#10000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C735_%s.fits"
        self.setup2()

class CommCase736(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        self.fname="C736_%s.fits"
        self.setup2()

class CommCase737(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C737_%s.fits"
        self.setup2()

class CommCase738(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        self.fname="C738_%s.fits"
        self.setup2()

class CommCase739(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        self.fname="C739_%s.fits"
        self.setup2()

class CommCase740(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        self.fname="C740_%s.fits"
        self.setup2()

class CommCase741(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        self.fname="C741_%s.fits"
        self.setup2()

class CommCase742(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        self.fname="C742_%s.fits"
        self.setup2()

class CommCase743(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C743_%s.fits"
        self.setup2()

class CommCase744(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C744_%s.fits"
        self.setup2()

class CommCase745(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C745_%s.fits"
        self.setup2()

class CommCase746(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.fname="C746_%s.fits"
        self.setup2()

class CommCase747(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        self.fname="C747_%s.fits"
        self.setup2()

class CommCase748(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C748_%s.fits"
        self.setup2()

class CommCase749(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.fname="C749_%s.fits"
        self.setup2()

class CommCase750(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C750_%s.fits"
        self.setup2()

class CommCase751(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3880"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C751_%s.fits"
        self.setup2()

class CommCase752(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C752_%s.fits"
        self.setup2()

class CommCase753(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr388n#3881"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C753_%s.fits"
        self.setup2()

class CommCase754(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C754_%s.fits"
        self.setup2()

class CommCase755(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr423n#4230"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C755_%s.fits"
        self.setup2()

class CommCase756(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        self.fname="C756_%s.fits"
        self.setup2()

class CommCase757(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4590"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C757_%s.fits"
        self.setup2()

class CommCase758(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C758_%s.fits"
        self.setup2()

class CommCase759(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr459m#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C759_%s.fits"
        self.setup2()

class CommCase760(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C760_%s.fits"
        self.setup2()

class CommCase761(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr462n#4620"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C761_%s.fits"
        self.setup2()

class CommCase762(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C762_%s.fits"
        self.setup2()

class CommCase763(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr505n#5000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C763_%s.fits"
        self.setup2()

class CommCase764(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C764_%s.fits"
        self.setup2()

class CommCase765(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr551n#5500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C765_%s.fits"
        self.setup2()

class CommCase766(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C766_%s.fits"
        self.setup2()

class CommCase767(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr601n#6000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C767_%s.fits"
        self.setup2()

class CommCase768(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C768_%s.fits"
        self.setup2()

class CommCase769(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr647m#6470"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C769_%s.fits"
        self.setup2()

class CommCase770(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C770_%s.fits"
        self.setup2()

class CommCase771(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr656n#6500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C771_%s.fits"
        self.setup2()

class CommCase772(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C772_%s.fits"
        self.setup2()

class CommCase773(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr716n#7100"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C773_%s.fits"
        self.setup2()

class CommCase774(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C774_%s.fits"
        self.setup2()

class CommCase775(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr782n#7900"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C775_%s.fits"
        self.setup2()

class CommCase776(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C776_%s.fits"
        self.setup2()

class CommCase777(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr853n#8500"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C777_%s.fits"
        self.setup2()

class CommCase778(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C778_%s.fits"
        self.setup2()

class CommCase779(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr914m#9000"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C779_%s.fits"
        self.setup2()

class CommCase780(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        self.fname="C780_%s.fits"
        self.setup2()

class CommCase781(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,fr931n#9300"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C781_%s.fits"
        self.setup2()

class CommCase782(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        self.fname="C782_%s.fits"
        self.setup2()

class CommCase783(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        self.fname="C783_%s.fits"
        self.setup2()

class CommCase784(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        self.fname="C784_%s.fits"
        self.setup2()

class CommCase785(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C785_%s.fits"
        self.setup2()

class CommCase786(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C786_%s.fits"
        self.setup2()

class CommCase787(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        self.fname="C787_%s.fits"
        self.setup2()

class CommCase788(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C788_%s.fits"
        self.setup2()

class CommCase789(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C789_%s.fits"
        self.setup2()

class CommCase790(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="acs,wfc1,g800l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C790_%s.fits"
        self.setup2()

class CommCase791(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="None"
        self.fname="C791_%s.fits"
        self.setup2()

class CommCase792(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C792_%s.fits"
        self.setup2()

class CommCase793(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C793_%s.fits"
        self.setup2()

class CommCase794(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C794_%s.fits"
        self.setup2()

class CommCase795(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f090m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C795_%s.fits"
        self.setup2()

class CommCase796(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="None"
        self.fname="C796_%s.fits"
        self.setup2()

class CommCase797(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C797_%s.fits"
        self.setup2()

class CommCase798(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f095n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C798_%s.fits"
        self.setup2()

class CommCase799(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="None"
        self.fname="C799_%s.fits"
        self.setup2()

class CommCase800(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C800_%s.fits"
        self.setup2()

class CommCase801(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f097n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C801_%s.fits"
        self.setup2()

class CommCase802(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="None"
        self.fname="C802_%s.fits"
        self.setup2()

class CommCase803(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C803_%s.fits"
        self.setup2()

class CommCase804(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C804_%s.fits"
        self.setup2()

class CommCase805(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="None"
        self.fname="C805_%s.fits"
        self.setup2()

class CommCase806(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C806_%s.fits"
        self.setup2()

class CommCase807(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C807_%s.fits"
        self.setup2()

class CommCase808(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="None"
        self.fname="C808_%s.fits"
        self.setup2()

class CommCase809(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        self.fname="C809_%s.fits"
        self.setup2()

class CommCase810(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C810_%s.fits"
        self.setup2()

class CommCase811(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C811_%s.fits"
        self.setup2()

class CommCase812(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C812_%s.fits"
        self.setup2()

class CommCase813(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C813_%s.fits"
        self.setup2()

class CommCase814(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C814_%s.fits"
        self.setup2()

class CommCase815(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C815_%s.fits"
        self.setup2()

class CommCase816(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C816_%s.fits"
        self.setup2()

class CommCase817(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C817_%s.fits"
        self.setup2()

class CommCase818(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C818_%s.fits"
        self.setup2()

class CommCase819(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C819_%s.fits"
        self.setup2()

class CommCase820(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C820_%s.fits"
        self.setup2()

class CommCase821(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C821_%s.fits"
        self.setup2()

class CommCase822(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C822_%s.fits"
        self.setup2()

class CommCase823(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C823_%s.fits"
        self.setup2()

class CommCase824(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C824_%s.fits"
        self.setup2()

class CommCase825(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C825_%s.fits"
        self.setup2()

class CommCase826(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C826_%s.fits"
        self.setup2()

class CommCase827(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C827_%s.fits"
        self.setup2()

class CommCase828(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C828_%s.fits"
        self.setup2()

class CommCase829(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C829_%s.fits"
        self.setup2()

class CommCase830(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C830_%s.fits"
        self.setup2()

class CommCase831(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C831_%s.fits"
        self.setup2()

class CommCase832(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C832_%s.fits"
        self.setup2()

class CommCase833(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C833_%s.fits"
        self.setup2()

class CommCase834(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C834_%s.fits"
        self.setup2()

class CommCase835(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C835_%s.fits"
        self.setup2()

class CommCase836(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C836_%s.fits"
        self.setup2()

class CommCase837(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C837_%s.fits"
        self.setup2()

class CommCase838(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C838_%s.fits"
        self.setup2()

class CommCase839(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C839_%s.fits"
        self.setup2()

class CommCase840(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C840_%s.fits"
        self.setup2()

class CommCase841(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C841_%s.fits"
        self.setup2()

class CommCase842(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal3),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C842_%s.fits"
        self.setup2()

class CommCase843(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C843_%s.fits"
        self.setup2()

class CommCase844(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C844_%s.fits"
        self.setup2()

class CommCase845(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        self.fname="C845_%s.fits"
        self.setup2()

class CommCase846(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        self.fname="C846_%s.fits"
        self.setup2()

class CommCase847(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(cousins,i),15,vegamag)"
        self.fname="C847_%s.fits"
        self.setup2()

class CommCase848(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),15,vegamag)"
        self.fname="C848_%s.fits"
        self.setup2()

class CommCase849(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,k),20,vegamag)"
        self.fname="C849_%s.fits"
        self.setup2()

class CommCase850(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C850_%s.fits"
        self.setup2()

class CommCase851(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),20,vegamag)"
        self.fname="C851_%s.fits"
        self.setup2()

class CommCase852(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),15,vegamag)"
        self.fname="C852_%s.fits"
        self.setup2()

class CommCase853(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f160w),15,vegamag)"
        self.fname="C853_%s.fits"
        self.setup2()

class CommCase854(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),15,vegamag)"
        self.fname="C854_%s.fits"
        self.setup2()

class CommCase855(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-06,jy)"
        self.fname="C855_%s.fits"
        self.setup2()

class CommCase856(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C856_%s.fits"
        self.setup2()

class CommCase857(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal1)"
        self.fname="C857_%s.fits"
        self.setup2()

class CommCase858(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal3)"
        self.fname="C858_%s.fits"
        self.setup2()

class CommCase859(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,lmc)"
        self.fname="C859_%s.fits"
        self.setup2()

class CommCase860(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,xgal)"
        self.fname="C860_%s.fits"
        self.setup2()

class CommCase861(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)+em(10000.0,10.0,1.0E-13,flam)"
        self.fname="C861_%s.fits"
        self.setup2()

class CommCase862(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-06,jy)"
        self.fname="C862_%s.fits"
        self.setup2()

class CommCase863(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-13,flam)"
        self.fname="C863_%s.fits"
        self.setup2()

class CommCase864(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-06,jy)"
        self.fname="C864_%s.fits"
        self.setup2()

class CommCase865(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-13,flam)"
        self.fname="C865_%s.fits"
        self.setup2()

class CommCase866(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(unit(1.0,fnu),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C866_%s.fits"
        self.setup2()

class CommCase867(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.5),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C867_%s.fits"
        self.setup2()

class CommCase868(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),1.0),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C868_%s.fits"
        self.setup2()

class CommCase869(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C869_%s.fits"
        self.setup2()

class CommCase870(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="rn(z(spec(qso_template.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        self.fname="C870_%s.fits"
        self.setup2()

class CommCase871(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        self.fname="C871_%s.fits"
        self.setup2()

class CommCase872(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.fname="C872_%s.fits"
        self.setup2()

class CommCase873(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.fname="C873_%s.fits"
        self.setup2()

class CommCase874(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C874_%s.fits"
        self.setup2()

class CommCase875(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.628378447488586,vegamag)"
        self.fname="C875_%s.fits"
        self.setup2()

class CommCase876(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.0086,vegamag)"
        self.fname="C876_%s.fits"
        self.setup2()

class CommCase877(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C877_%s.fits"
        self.setup2()

class CommCase878(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.26738684931507,vegamag)"
        self.fname="C878_%s.fits"
        self.setup2()

class CommCase879(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.40573333333333,vegamag)"
        self.fname="C879_%s.fits"
        self.setup2()

class CommCase880(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C880_%s.fits"
        self.setup2()

class CommCase881(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.808112328767123,vegamag)"
        self.fname="C881_%s.fits"
        self.setup2()

class CommCase882(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.9514,vegamag)"
        self.fname="C882_%s.fits"
        self.setup2()

class CommCase883(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.964448767123287,vegamag)"
        self.fname="C883_%s.fits"
        self.setup2()

class CommCase884(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.067600000000002,vegamag)"
        self.fname="C884_%s.fits"
        self.setup2()

class CommCase885(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.1514,vegamag)"
        self.fname="C885_%s.fits"
        self.setup2()

class CommCase886(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C886_%s.fits"
        self.setup2()

class CommCase887(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),28.0,vegamag)"
        self.fname="C887_%s.fits"
        self.setup2()

class CommCase888(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        self.fname="C888_%s.fits"
        self.setup2()

class CommCase889(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        self.fname="C889_%s.fits"
        self.setup2()

class CommCase890(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.5"
        self.fname="C890_%s.fits"
        self.setup2()

class CommCase891(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*1.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C891_%s.fits"
        self.setup2()

class CommCase892(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C892_%s.fits"
        self.setup2()

class CommCase893(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f110w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C893_%s.fits"
        self.setup2()

class CommCase894(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="None"
        self.fname="C894_%s.fits"
        self.setup2()

class CommCase895(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C895_%s.fits"
        self.setup2()

class CommCase896(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C896_%s.fits"
        self.setup2()

class CommCase897(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="None"
        self.fname="C897_%s.fits"
        self.setup2()

class CommCase898(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C898_%s.fits"
        self.setup2()

class CommCase899(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C899_%s.fits"
        self.setup2()

class CommCase900(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="None"
        self.fname="C900_%s.fits"
        self.setup2()

class CommCase901(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C901_%s.fits"
        self.setup2()

class CommCase902(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f145m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C902_%s.fits"
        self.setup2()

class CommCase903(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="None"
        self.fname="C903_%s.fits"
        self.setup2()

class CommCase904(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C904_%s.fits"
        self.setup2()

class CommCase905(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C905_%s.fits"
        self.setup2()

class CommCase906(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C906_%s.fits"
        self.setup2()

class CommCase907(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.fname="C907_%s.fits"
        self.setup2()

class CommCase908(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.fname="C908_%s.fits"
        self.setup2()

class CommCase909(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C909_%s.fits"
        self.setup2()

class CommCase910(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C910_%s.fits"
        self.setup2()

class CommCase911(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="None"
        self.fname="C911_%s.fits"
        self.setup2()

class CommCase912(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C912_%s.fits"
        self.setup2()

class CommCase913(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C913_%s.fits"
        self.setup2()

class CommCase914(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="None"
        self.fname="C914_%s.fits"
        self.setup2()

class CommCase915(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C915_%s.fits"
        self.setup2()

class CommCase916(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C916_%s.fits"
        self.setup2()

class CommCase917(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C917_%s.fits"
        self.setup2()

class CommCase918(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="None"
        self.fname="C918_%s.fits"
        self.setup2()

class CommCase919(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C919_%s.fits"
        self.setup2()

class CommCase920(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C920_%s.fits"
        self.setup2()

class CommCase921(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="None"
        self.fname="C921_%s.fits"
        self.setup2()

class CommCase922(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C922_%s.fits"
        self.setup2()

class CommCase923(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f170m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C923_%s.fits"
        self.setup2()

class CommCase924(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="None"
        self.fname="C924_%s.fits"
        self.setup2()

class CommCase925(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C925_%s.fits"
        self.setup2()

class CommCase926(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C926_%s.fits"
        self.setup2()

class CommCase927(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="None"
        self.fname="C927_%s.fits"
        self.setup2()

class CommCase928(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C928_%s.fits"
        self.setup2()

class CommCase929(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C929_%s.fits"
        self.setup2()

class CommCase930(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="None"
        self.fname="C930_%s.fits"
        self.setup2()

class CommCase931(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C931_%s.fits"
        self.setup2()

class CommCase932(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,1,pol0s"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C932_%s.fits"
        self.setup2()

class CommCase933(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="None"
        self.fname="C933_%s.fits"
        self.setup2()

class CommCase934(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C934_%s.fits"
        self.setup2()

class CommCase935(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C935_%s.fits"
        self.setup2()

class CommCase936(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C936_%s.fits"
        self.setup2()

class CommCase937(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.fname="C937_%s.fits"
        self.setup2()

class CommCase938(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.fname="C938_%s.fits"
        self.setup2()

class CommCase939(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C939_%s.fits"
        self.setup2()

class CommCase940(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C940_%s.fits"
        self.setup2()

class CommCase941(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="None"
        self.fname="C941_%s.fits"
        self.setup2()

class CommCase942(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C942_%s.fits"
        self.setup2()

class CommCase943(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C943_%s.fits"
        self.setup2()

class CommCase944(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C944_%s.fits"
        self.setup2()

class CommCase945(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.fname="C945_%s.fits"
        self.setup2()

class CommCase946(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.fname="C946_%s.fits"
        self.setup2()

class CommCase947(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C947_%s.fits"
        self.setup2()

class CommCase948(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C948_%s.fits"
        self.setup2()

class CommCase949(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="None"
        self.fname="C949_%s.fits"
        self.setup2()

class CommCase950(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C950_%s.fits"
        self.setup2()

class CommCase951(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C951_%s.fits"
        self.setup2()

class CommCase952(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C952_%s.fits"
        self.setup2()

class CommCase953(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f165m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C953_%s.fits"
        self.setup2()

class CommCase954(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="None"
        self.fname="C954_%s.fits"
        self.setup2()

class CommCase955(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C955_%s.fits"
        self.setup2()

class CommCase956(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f171m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C956_%s.fits"
        self.setup2()

class CommCase957(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="None"
        self.fname="C957_%s.fits"
        self.setup2()

class CommCase958(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C958_%s.fits"
        self.setup2()

class CommCase959(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f180m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C959_%s.fits"
        self.setup2()

class CommCase960(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="None"
        self.fname="C960_%s.fits"
        self.setup2()

class CommCase961(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C961_%s.fits"
        self.setup2()

class CommCase962(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C962_%s.fits"
        self.setup2()

class CommCase963(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="None"
        self.fname="C963_%s.fits"
        self.setup2()

class CommCase964(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C964_%s.fits"
        self.setup2()

class CommCase965(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f187w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C965_%s.fits"
        self.setup2()

class CommCase966(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="None"
        self.fname="C966_%s.fits"
        self.setup2()

class CommCase967(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C967_%s.fits"
        self.setup2()

class CommCase968(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C968_%s.fits"
        self.setup2()

class CommCase969(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="None"
        self.fname="C969_%s.fits"
        self.setup2()

class CommCase970(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C970_%s.fits"
        self.setup2()

class CommCase971(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f204m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C971_%s.fits"
        self.setup2()

class CommCase972(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="None"
        self.fname="C972_%s.fits"
        self.setup2()

class CommCase973(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C973_%s.fits"
        self.setup2()

class CommCase974(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f205w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C974_%s.fits"
        self.setup2()

class CommCase975(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="None"
        self.fname="C975_%s.fits"
        self.setup2()

class CommCase976(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C976_%s.fits"
        self.setup2()

class CommCase977(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f207m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C977_%s.fits"
        self.setup2()

class CommCase978(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="None"
        self.fname="C978_%s.fits"
        self.setup2()

class CommCase979(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C979_%s.fits"
        self.setup2()

class CommCase980(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C980_%s.fits"
        self.setup2()

class CommCase981(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="None"
        self.fname="C981_%s.fits"
        self.setup2()

class CommCase982(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C982_%s.fits"
        self.setup2()

class CommCase983(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f216n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C983_%s.fits"
        self.setup2()

class CommCase984(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="None"
        self.fname="C984_%s.fits"
        self.setup2()

class CommCase985(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C985_%s.fits"
        self.setup2()

class CommCase986(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C986_%s.fits"
        self.setup2()

class CommCase987(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C987_%s.fits"
        self.setup2()

class CommCase988(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C988_%s.fits"
        self.setup2()

class CommCase989(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="None"
        self.fname="C989_%s.fits"
        self.setup2()

class CommCase990(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C990_%s.fits"
        self.setup2()

class CommCase991(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,f237m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C991_%s.fits"
        self.setup2()

class CommCase992(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="None"
        self.fname="C992_%s.fits"
        self.setup2()

class CommCase993(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C993_%s.fits"
        self.setup2()

class CommCase994(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,2,pol0l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C994_%s.fits"
        self.setup2()

class CommCase995(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="None"
        self.fname="C995_%s.fits"
        self.setup2()

class CommCase996(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C996_%s.fits"
        self.setup2()

class CommCase997(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f108n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C997_%s.fits"
        self.setup2()

class CommCase998(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="None"
        self.fname="C998_%s.fits"
        self.setup2()

class CommCase999(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(10000),band(bessell,h),20,vegamag)"
        self.fname="C999_%s.fits"
        self.setup2()

class CommCase1000(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C1000_%s.fits"
        self.setup2()

class CommCase1001(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500)*ebmvx(0.5,lmc),band(bessell,h),20,vegamag)"
        self.fname="C1001_%s.fits"
        self.setup2()

class CommCase1002(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C1002_%s.fits"
        self.setup2()

class CommCase1003(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1003_%s.fits"
        self.setup2()

class CommCase1004(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(bessell,h),20,vegamag)"
        self.fname="C1004_%s.fits"
        self.setup2()

class CommCase1005(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(bessell,h),20,vegamag)"
        self.fname="C1005_%s.fits"
        self.setup2()

class CommCase1006(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(bessell,h),20,vegamag)"
        self.fname="C1006_%s.fits"
        self.setup2()

class CommCase1007(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(bessell,h),20,vegamag)"
        self.fname="C1007_%s.fits"
        self.setup2()

class CommCase1008(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(bessell,h),20,vegamag)"
        self.fname="C1008_%s.fits"
        self.setup2()

class CommCase1009(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(spec(egal.dat),band(bessell,h),20,vegamag)"
        self.fname="C1009_%s.fits"
        self.setup2()

class CommCase1010(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="rn(unit(1.0,flam),band(bessell,h),20,vegamag)"
        self.fname="C1010_%s.fits"
        self.setup2()

class CommCase1011(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1011_%s.fits"
        self.setup2()

class CommCase1012(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="None"
        self.fname="C1012_%s.fits"
        self.setup2()

class CommCase1013(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1013_%s.fits"
        self.setup2()

class CommCase1014(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f113n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1014_%s.fits"
        self.setup2()

class CommCase1015(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="None"
        self.fname="C1015_%s.fits"
        self.setup2()

class CommCase1016(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1016_%s.fits"
        self.setup2()

class CommCase1017(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(bb(5500),band(bessell,h),23.5,vegamag)"
        self.fname="C1017_%s.fits"
        self.setup2()

class CommCase1018(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1018_%s.fits"
        self.setup2()

class CommCase1019(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1019_%s.fits"
        self.setup2()

class CommCase1020(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1020_%s.fits"
        self.setup2()

class CommCase1021(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1021_%s.fits"
        self.setup2()

class CommCase1022(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1022_%s.fits"
        self.setup2()

class CommCase1023(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1023_%s.fits"
        self.setup2()

class CommCase1024(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1024_%s.fits"
        self.setup2()

class CommCase1025(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1025_%s.fits"
        self.setup2()

class CommCase1026(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1026_%s.fits"
        self.setup2()

class CommCase1027(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1027_%s.fits"
        self.setup2()

class CommCase1028(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1028_%s.fits"
        self.setup2()

class CommCase1029(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f150w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1029_%s.fits"
        self.setup2()

class CommCase1030(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="None"
        self.fname="C1030_%s.fits"
        self.setup2()

class CommCase1031(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C1031_%s.fits"
        self.setup2()

class CommCase1032(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C1032_%s.fits"
        self.setup2()

class CommCase1033(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1033_%s.fits"
        self.setup2()

class CommCase1034(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        self.fname="C1034_%s.fits"
        self.setup2()

class CommCase1035(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        self.fname="C1035_%s.fits"
        self.setup2()

class CommCase1036(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        self.fname="C1036_%s.fits"
        self.setup2()

class CommCase1037(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1037_%s.fits"
        self.setup2()

class CommCase1038(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="None"
        self.fname="C1038_%s.fits"
        self.setup2()

class CommCase1039(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1039_%s.fits"
        self.setup2()

class CommCase1040(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1040_%s.fits"
        self.setup2()

class CommCase1041(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="None"
        self.fname="C1041_%s.fits"
        self.setup2()

class CommCase1042(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1042_%s.fits"
        self.setup2()

class CommCase1043(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f166n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1043_%s.fits"
        self.setup2()

class CommCase1044(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="None"
        self.fname="C1044_%s.fits"
        self.setup2()

class CommCase1045(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C1045_%s.fits"
        self.setup2()

class CommCase1046(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C1046_%s.fits"
        self.setup2()

class CommCase1047(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1047_%s.fits"
        self.setup2()

class CommCase1048(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f175w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1048_%s.fits"
        self.setup2()

class CommCase1049(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="None"
        self.fname="C1049_%s.fits"
        self.setup2()

class CommCase1050(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1050_%s.fits"
        self.setup2()

class CommCase1051(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f187n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1051_%s.fits"
        self.setup2()

class CommCase1052(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="None"
        self.fname="C1052_%s.fits"
        self.setup2()

class CommCase1053(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1053_%s.fits"
        self.setup2()

class CommCase1054(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f190n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1054_%s.fits"
        self.setup2()

class CommCase1055(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="None"
        self.fname="C1055_%s.fits"
        self.setup2()

class CommCase1056(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1056_%s.fits"
        self.setup2()

class CommCase1057(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f196n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1057_%s.fits"
        self.setup2()

class CommCase1058(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="None"
        self.fname="C1058_%s.fits"
        self.setup2()

class CommCase1059(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1059_%s.fits"
        self.setup2()

class CommCase1060(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f200n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1060_%s.fits"
        self.setup2()

class CommCase1061(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="None"
        self.fname="C1061_%s.fits"
        self.setup2()

class CommCase1062(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1062_%s.fits"
        self.setup2()

class CommCase1063(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f212n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1063_%s.fits"
        self.setup2()

class CommCase1064(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="None"
        self.fname="C1064_%s.fits"
        self.setup2()

class CommCase1065(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1065_%s.fits"
        self.setup2()

class CommCase1066(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f215n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1066_%s.fits"
        self.setup2()

class CommCase1067(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="None"
        self.fname="C1067_%s.fits"
        self.setup2()

class CommCase1068(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        self.fname="C1068_%s.fits"
        self.setup2()

class CommCase1069(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        self.fname="C1069_%s.fits"
        self.setup2()

class CommCase1070(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1070_%s.fits"
        self.setup2()

class CommCase1071(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f222m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1071_%s.fits"
        self.setup2()

class CommCase1072(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="None"
        self.fname="C1072_%s.fits"
        self.setup2()

class CommCase1073(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        self.fname="C1073_%s.fits"
        self.setup2()

class CommCase1074(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,f240m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1074_%s.fits"
        self.setup2()

class CommCase1075(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="None"
        self.fname="C1075_%s.fits"
        self.setup2()

class CommCase1076(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(bb(5000.0),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1076_%s.fits"
        self.setup2()

class CommCase1077(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1077_%s.fits"
        self.setup2()

class CommCase1078(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1078_%s.fits"
        self.setup2()

class CommCase1079(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1079_%s.fits"
        self.setup2()

class CommCase1080(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1080_%s.fits"
        self.setup2()

class CommCase1081(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.fname="C1081_%s.fits"
        self.setup2()

class CommCase1082(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.fname="C1082_%s.fits"
        self.setup2()

class CommCase1083(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.fname="C1083_%s.fits"
        self.setup2()

class CommCase1084(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.fname="C1084_%s.fits"
        self.setup2()

class CommCase1085(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.fname="C1085_%s.fits"
        self.setup2()

class CommCase1086(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.fname="C1086_%s.fits"
        self.setup2()

class CommCase1087(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.fname="C1087_%s.fits"
        self.setup2()

class CommCase1088(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.fname="C1088_%s.fits"
        self.setup2()

class CommCase1089(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1089_%s.fits"
        self.setup2()

class CommCase1090(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1090_%s.fits"
        self.setup2()

class CommCase1091(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1091_%s.fits"
        self.setup2()

class CommCase1092(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1092_%s.fits"
        self.setup2()

class CommCase1093(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1093_%s.fits"
        self.setup2()

class CommCase1094(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.fname="C1094_%s.fits"
        self.setup2()

class CommCase1095(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C1095_%s.fits"
        self.setup2()

class CommCase1096(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1096_%s.fits"
        self.setup2()

class CommCase1097(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1097_%s.fits"
        self.setup2()

class CommCase1098(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1098_%s.fits"
        self.setup2()

class CommCase1099(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.fname="C1099_%s.fits"
        self.setup2()

class CommCase1100(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1100_%s.fits"
        self.setup2()

class CommCase1101(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1101_%s.fits"
        self.setup2()

class CommCase1102(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g096"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1102_%s.fits"
        self.setup2()

class CommCase1103(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="None"
        self.fname="C1103_%s.fits"
        self.setup2()

class CommCase1104(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1104_%s.fits"
        self.setup2()

class CommCase1105(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1105_%s.fits"
        self.setup2()

class CommCase1106(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1106_%s.fits"
        self.setup2()

class CommCase1107(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.fname="C1107_%s.fits"
        self.setup2()

class CommCase1108(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.fname="C1108_%s.fits"
        self.setup2()

class CommCase1109(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.fname="C1109_%s.fits"
        self.setup2()

class CommCase1110(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.fname="C1110_%s.fits"
        self.setup2()

class CommCase1111(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.fname="C1111_%s.fits"
        self.setup2()

class CommCase1112(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.fname="C1112_%s.fits"
        self.setup2()

class CommCase1113(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.fname="C1113_%s.fits"
        self.setup2()

class CommCase1114(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.fname="C1114_%s.fits"
        self.setup2()

class CommCase1115(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-05,jy)"
        self.fname="C1115_%s.fits"
        self.setup2()

class CommCase1116(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-06,jy)"
        self.fname="C1116_%s.fits"
        self.setup2()

class CommCase1117(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-12,flam)"
        self.fname="C1117_%s.fits"
        self.setup2()

class CommCase1118(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-13,flam)"
        self.fname="C1118_%s.fits"
        self.setup2()

class CommCase1119(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1119_%s.fits"
        self.setup2()

class CommCase1120(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1120_%s.fits"
        self.setup2()

class CommCase1121(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1121_%s.fits"
        self.setup2()

class CommCase1122(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.fname="C1122_%s.fits"
        self.setup2()

class CommCase1123(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C1123_%s.fits"
        self.setup2()

class CommCase1124(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1124_%s.fits"
        self.setup2()

class CommCase1125(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1125_%s.fits"
        self.setup2()

class CommCase1126(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.fname="C1126_%s.fits"
        self.setup2()

class CommCase1127(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1127_%s.fits"
        self.setup2()

class CommCase1128(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1128_%s.fits"
        self.setup2()

class CommCase1129(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g141"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1129_%s.fits"
        self.setup2()

class CommCase1130(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="None"
        self.fname="C1130_%s.fits"
        self.setup2()

class CommCase1131(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1131_%s.fits"
        self.setup2()

class CommCase1132(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1132_%s.fits"
        self.setup2()

class CommCase1133(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1133_%s.fits"
        self.setup2()

class CommCase1134(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        self.fname="C1134_%s.fits"
        self.setup2()

class CommCase1135(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        self.fname="C1135_%s.fits"
        self.setup2()

class CommCase1136(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        self.fname="C1136_%s.fits"
        self.setup2()

class CommCase1137(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        self.fname="C1137_%s.fits"
        self.setup2()

class CommCase1138(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        self.fname="C1138_%s.fits"
        self.setup2()

class CommCase1139(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        self.fname="C1139_%s.fits"
        self.setup2()

class CommCase1140(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        self.fname="C1140_%s.fits"
        self.setup2()

class CommCase1141(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        self.fname="C1141_%s.fits"
        self.setup2()

class CommCase1142(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1142_%s.fits"
        self.setup2()

class CommCase1143(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1143_%s.fits"
        self.setup2()

class CommCase1144(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        self.fname="C1144_%s.fits"
        self.setup2()

class CommCase1145(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        self.fname="C1145_%s.fits"
        self.setup2()

class CommCase1146(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C1146_%s.fits"
        self.setup2()

class CommCase1147(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1147_%s.fits"
        self.setup2()

class CommCase1148(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1148_%s.fits"
        self.setup2()

class CommCase1149(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        self.fname="C1149_%s.fits"
        self.setup2()

class CommCase1150(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        self.fname="C1150_%s.fits"
        self.setup2()

class CommCase1151(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1151_%s.fits"
        self.setup2()

class CommCase1152(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="nicmos,3,g206"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        self.fname="C1152_%s.fits"
        self.setup2()

class CommCase1153(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd"
        self.spectrum="rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        self.fname="C1153_%s.fits"
        self.setup2()

class CommCase1154(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        self.fname="C1154_%s.fits"
        self.setup2()

class CommCase1155(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.fname="C1155_%s.fits"
        self.setup2()

class CommCase1156(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        self.fname="C1156_%s.fits"
        self.setup2()

class CommCase1157(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.fname="C1157_%s.fits"
        self.setup2()

class CommCase1158(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C1158_%s.fits"
        self.setup2()

class CommCase1159(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1159_%s.fits"
        self.setup2()

class CommCase1160(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1160_%s.fits"
        self.setup2()

class CommCase1161(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,50ccd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1161_%s.fits"
        self.setup2()

class CommCase1162(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.fname="C1162_%s.fits"
        self.setup2()

class CommCase1163(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1163_%s.fits"
        self.setup2()

class CommCase1164(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.fname="C1164_%s.fits"
        self.setup2()

class CommCase1165(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1165_%s.fits"
        self.setup2()

class CommCase1166(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1166_%s.fits"
        self.setup2()

class CommCase1167(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1167_%s.fits"
        self.setup2()

class CommCase1168(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1168_%s.fits"
        self.setup2()

class CommCase1169(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1169_%s.fits"
        self.setup2()

class CommCase1170(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1170_%s.fits"
        self.setup2()

class CommCase1171(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,f28x50oiii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1171_%s.fits"
        self.setup2()

class CommCase1172(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1172_%s.fits"
        self.setup2()

class CommCase1173(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1173_%s.fits"
        self.setup2()

class CommCase1174(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        self.fname="C1174_%s.fits"
        self.setup2()

class CommCase1175(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230lb,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1175_%s.fits"
        self.setup2()

class CommCase1176(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230mb,c1995"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1176_%s.fits"
        self.setup2()

class CommCase1177(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g230mb,c1995,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1177_%s.fits"
        self.setup2()

class CommCase1178(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        self.fname="C1178_%s.fits"
        self.setup2()

class CommCase1179(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.fname="C1179_%s.fits"
        self.setup2()

class CommCase1180(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.fname="C1180_%s.fits"
        self.setup2()

class CommCase1181(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1181_%s.fits"
        self.setup2()

class CommCase1182(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1182_%s.fits"
        self.setup2()

class CommCase1183(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23.5,vegamag)"
        self.fname="C1183_%s.fits"
        self.setup2()

class CommCase1184(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        self.fname="C1184_%s.fits"
        self.setup2()

class CommCase1185(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1185_%s.fits"
        self.setup2()

class CommCase1186(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1186_%s.fits"
        self.setup2()

class CommCase1187(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1187_%s.fits"
        self.setup2()

class CommCase1188(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194,s52x2"
        self.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        self.fname="C1188_%s.fits"
        self.setup2()

class CommCase1189(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g430m,c4194,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1189_%s.fits"
        self.setup2()

class CommCase1190(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.fname="C1190_%s.fits"
        self.setup2()

class CommCase1191(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1191_%s.fits"
        self.setup2()

class CommCase1192(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1192_%s.fits"
        self.setup2()

class CommCase1193(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1193_%s.fits"
        self.setup2()

class CommCase1194(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1194_%s.fits"
        self.setup2()

class CommCase1195(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.fname="C1195_%s.fits"
        self.setup2()

class CommCase1196(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),0.03),band(johnson,v),18,vegamag)"
        self.fname="C1196_%s.fits"
        self.setup2()

class CommCase1197(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),1.0),band(johnson,v),18,vegamag)"
        self.fname="C1197_%s.fits"
        self.setup2()

class CommCase1198(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x02"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,v),18,vegamag)"
        self.fname="C1198_%s.fits"
        self.setup2()

class CommCase1199(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23,vegamag)"
        self.fname="C1199_%s.fits"
        self.setup2()

class CommCase1200(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24.5,vegamag)"
        self.fname="C1200_%s.fits"
        self.setup2()

class CommCase1201(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750l,c7751,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1201_%s.fits"
        self.setup2()

class CommCase1202(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750m,c7283"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1202_%s.fits"
        self.setup2()

class CommCase1203(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,g750m,c7283,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1203_%s.fits"
        self.setup2()

class CommCase1204(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        self.fname="C1204_%s.fits"
        self.setup2()

class CommCase1205(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        self.fname="C1205_%s.fits"
        self.setup2()

class CommCase1206(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1206_%s.fits"
        self.setup2()

class CommCase1207(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,ccd,s03x005nd"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1207_%s.fits"
        self.setup2()

class CommCase1208(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.fname="C1208_%s.fits"
        self.setup2()

class CommCase1209(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.fname="C1209_%s.fits"
        self.setup2()

class CommCase1210(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1210_%s.fits"
        self.setup2()

class CommCase1211(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140h,c1416"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1211_%s.fits"
        self.setup2()

class CommCase1212(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140h,c1416,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.fname="C1212_%s.fits"
        self.setup2()

class CommCase1213(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.fname="C1213_%s.fits"
        self.setup2()

class CommCase1214(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1214_%s.fits"
        self.setup2()

class CommCase1215(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.fname="C1215_%s.fits"
        self.setup2()

class CommCase1216(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        self.spectrum="em(1425.0,0.043487548828125,1.0E-10,flam)"
        self.fname="C1216_%s.fits"
        self.setup2()

class CommCase1217(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        self.spectrum="em(1425.0,1.0,1.0E-10,flam)"
        self.fname="C1217_%s.fits"
        self.setup2()

class CommCase1218(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),10,vegamag)"
        self.fname="C1218_%s.fits"
        self.setup2()

class CommCase1219(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),6,vegamag)"
        self.fname="C1219_%s.fits"
        self.setup2()

class CommCase1220(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),7,vegamag)"
        self.fname="C1220_%s.fits"
        self.setup2()

class CommCase1221(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        self.fname="C1221_%s.fits"
        self.setup2()

class CommCase1222(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.fname="C1222_%s.fits"
        self.setup2()

class CommCase1223(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1223_%s.fits"
        self.setup2()

class CommCase1224(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25lya"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1224_%s.fits"
        self.setup2()

class CommCase1225(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1225_%s.fits"
        self.setup2()

class CommCase1226(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25nd3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1226_%s.fits"
        self.setup2()

class CommCase1227(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1227_%s.fits"
        self.setup2()

class CommCase1228(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq1"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1228_%s.fits"
        self.setup2()

class CommCase1229(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1229_%s.fits"
        self.setup2()

class CommCase1230(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25ndq3"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1230_%s.fits"
        self.setup2()

class CommCase1231(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.fname="C1231_%s.fits"
        self.setup2()

class CommCase1232(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1232_%s.fits"
        self.setup2()

class CommCase1233(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.fname="C1233_%s.fits"
        self.setup2()

class CommCase1234(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1234_%s.fits"
        self.setup2()

class CommCase1235(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1235_%s.fits"
        self.setup2()

class CommCase1236(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1236_%s.fits"
        self.setup2()

class CommCase1237(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x01"
        self.spectrum="rn(spec(ngc1068_template.fits),band(johnson,v),9,vegamag)"
        self.fname="C1237_%s.fits"
        self.setup2()

class CommCase1238(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),13,vegamag)"
        self.fname="C1238_%s.fits"
        self.setup2()

class CommCase1239(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14,vegamag)"
        self.fname="C1239_%s.fits"
        self.setup2()

class CommCase1240(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14.1,vegamag)"
        self.fname="C1240_%s.fits"
        self.setup2()

class CommCase1241(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),27.5,vegamag)"
        self.fname="C1241_%s.fits"
        self.setup2()

class CommCase1242(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),12.77,vegamag)"
        self.fname="C1242_%s.fits"
        self.setup2()

class CommCase1243(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),band(johnson,v),10.516,vegamag)"
        self.fname="C1243_%s.fits"
        self.setup2()

class CommCase1244(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        self.fname="C1244_%s.fits"
        self.setup2()

class CommCase1245(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140m,c1567"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1245_%s.fits"
        self.setup2()

class CommCase1246(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,fuvmama,g140m,c1567,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1246_%s.fits"
        self.setup2()

class CommCase1247(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C1247_%s.fits"
        self.setup2()

class CommCase1248(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C1248_%s.fits"
        self.setup2()

class CommCase1249(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C1249_%s.fits"
        self.setup2()

class CommCase1250(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="el1215a.fits"
        self.fname="C1250_%s.fits"
        self.setup2()

class CommCase1251(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="el1302a.fits"
        self.fname="C1251_%s.fits"
        self.setup2()

class CommCase1252(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="el1356a.fits"
        self.fname="C1252_%s.fits"
        self.setup2()

class CommCase1253(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="el2471a.fits"
        self.fname="C1253_%s.fits"
        self.setup2()

class CommCase1254(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C1254_%s.fits"
        self.setup2()

class CommCase1255(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C1255_%s.fits"
        self.setup2()

class CommCase1256(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C1256_%s.fits"
        self.setup2()

class CommCase1257(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C1257_%s.fits"
        self.setup2()

class CommCase1258(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C1258_%s.fits"
        self.setup2()

class CommCase1259(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C1259_%s.fits"
        self.setup2()

class CommCase1260(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C1260_%s.fits"
        self.setup2()

class CommCase1261(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C1261_%s.fits"
        self.setup2()

class CommCase1262(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C1262_%s.fits"
        self.setup2()

class CommCase1263(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.fname="C1263_%s.fits"
        self.setup2()

class CommCase1264(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.fname="C1264_%s.fits"
        self.setup2()

class CommCase1265(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.fname="C1265_%s.fits"
        self.setup2()

class CommCase1266(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.fname="C1266_%s.fits"
        self.setup2()

class CommCase1267(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        self.fname="C1267_%s.fits"
        self.setup2()

class CommCase1268(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,25mama"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1268_%s.fits"
        self.setup2()

class CommCase1269(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1269_%s.fits"
        self.setup2()

class CommCase1270(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(bb(50000),band(johnson,v),10.516,vegamag)"
        self.fname="C1270_%s.fits"
        self.setup2()

class CommCase1271(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10.516,vegamag)"
        self.fname="C1271_%s.fits"
        self.setup2()

class CommCase1272(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),10.516,vegamag)"
        self.fname="C1272_%s.fits"
        self.setup2()

class CommCase1273(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(pl(4000.0,0.0,flam),band(johnson,v),10.516,vegamag)"
        self.fname="C1273_%s.fits"
        self.setup2()

class CommCase1274(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),band(johnson,v),10.516,vegamag)"
        self.fname="C1274_%s.fits"
        self.setup2()

class CommCase1275(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),box(2000.0,1.0),1.0e-12,flam)"
        self.fname="C1275_%s.fits"
        self.setup2()

class CommCase1276(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="rn(unit(1.0,flam),band(johnson,v),10.516,vegamag)"
        self.fname="C1276_%s.fits"
        self.setup2()

class CommCase1277(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.fname="C1277_%s.fits"
        self.setup2()

class CommCase1278(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1278_%s.fits"
        self.setup2()

class CommCase1279(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        self.fname="C1279_%s.fits"
        self.setup2()

class CommCase1280(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        self.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        self.fname="C1280_%s.fits"
        self.setup2()

class CommCase1281(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1281_%s.fits"
        self.setup2()

class CommCase1282(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ciii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1282_%s.fits"
        self.setup2()

class CommCase1283(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1283_%s.fits"
        self.setup2()

class CommCase1284(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn182"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1284_%s.fits"
        self.setup2()

class CommCase1285(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1285_%s.fits"
        self.setup2()

class CommCase1286(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25cn270"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1286_%s.fits"
        self.setup2()

class CommCase1287(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1287_%s.fits"
        self.setup2()

class CommCase1288(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25mgii"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1288_%s.fits"
        self.setup2()

class CommCase1289(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1289_%s.fits"
        self.setup2()

class CommCase1290(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25nd5"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1290_%s.fits"
        self.setup2()

class CommCase1291(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1291_%s.fits"
        self.setup2()

class CommCase1292(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1292_%s.fits"
        self.setup2()

class CommCase1293(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1293_%s.fits"
        self.setup2()

class CommCase1294(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25ndq4"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1294_%s.fits"
        self.setup2()

class CommCase1295(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        self.fname="C1295_%s.fits"
        self.setup2()

class CommCase1296(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        self.fname="C1296_%s.fits"
        self.setup2()

class CommCase1297(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25qtz"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1297_%s.fits"
        self.setup2()

class CommCase1298(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        self.fname="C1298_%s.fits"
        self.setup2()

class CommCase1299(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,f25srf2"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1299_%s.fits"
        self.setup2()

class CommCase1300(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1300_%s.fits"
        self.setup2()

class CommCase1301(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1301_%s.fits"
        self.setup2()

class CommCase1302(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,gal1),band(johnson,v),15,vegamag)"
        self.fname="C1302_%s.fits"
        self.setup2()

class CommCase1303(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,lmc),band(johnson,v),15,vegamag)"
        self.fname="C1303_%s.fits"
        self.setup2()

class CommCase1304(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,smc),band(johnson,v),15,vegamag)"
        self.fname="C1304_%s.fits"
        self.setup2()

class CommCase1305(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,xgal),band(johnson,v),15,vegamag)"
        self.fname="C1305_%s.fits"
        self.setup2()

class CommCase1306(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24,vegamag)"
        self.fname="C1306_%s.fits"
        self.setup2()

class CommCase1307(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230l,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        self.fname="C1307_%s.fits"
        self.setup2()

class CommCase1308(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230m,c2818"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1308_%s.fits"
        self.setup2()

class CommCase1309(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,g230m,c2818,s52x2"
        self.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        self.fname="C1309_%s.fits"
        self.setup2()

class CommCase1310(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1310_%s.fits"
        self.setup2()

class CommCase1311(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism,s52x01"
        self.spectrum="spec(HS20270651.dat)"
        self.fname="C1311_%s.fits"
        self.setup2()

class CommCase1312(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="stis,nuvmama,prism,s52x2"
        self.spectrum="spec(HS20270651.dat)"
        self.fname="C1312_%s.fits"
        self.setup2()

class CommCase1313(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="None"
        self.fname="C1313_%s.fits"
        self.setup2()

class CommCase1314(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1314_%s.fits"
        self.setup2()

class CommCase1315(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1315_%s.fits"
        self.setup2()

class CommCase1316(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f098m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1316_%s.fits"
        self.setup2()

class CommCase1317(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="None"
        self.fname="C1317_%s.fits"
        self.setup2()

class CommCase1318(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1318_%s.fits"
        self.setup2()

class CommCase1319(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1319_%s.fits"
        self.setup2()

class CommCase1320(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.fname="C1320_%s.fits"
        self.setup2()

class CommCase1321(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.fname="C1321_%s.fits"
        self.setup2()

class CommCase1322(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.fname="C1322_%s.fits"
        self.setup2()

class CommCase1323(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1323_%s.fits"
        self.setup2()

class CommCase1324(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1324_%s.fits"
        self.setup2()

class CommCase1325(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1325_%s.fits"
        self.setup2()

class CommCase1326(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f105w"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1326_%s.fits"
        self.setup2()

class CommCase1327(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="None"
        self.fname="C1327_%s.fits"
        self.setup2()

class CommCase1328(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1328_%s.fits"
        self.setup2()

class CommCase1329(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1329_%s.fits"
        self.setup2()

class CommCase1330(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1330_%s.fits"
        self.setup2()

class CommCase1331(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1331_%s.fits"
        self.setup2()

class CommCase1332(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1332_%s.fits"
        self.setup2()

class CommCase1333(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1333_%s.fits"
        self.setup2()

class CommCase1334(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1334_%s.fits"
        self.setup2()

class CommCase1335(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1335_%s.fits"
        self.setup2()

class CommCase1336(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1336_%s.fits"
        self.setup2()

class CommCase1337(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1337_%s.fits"
        self.setup2()

class CommCase1338(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1338_%s.fits"
        self.setup2()

class CommCase1339(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1339_%s.fits"
        self.setup2()

class CommCase1340(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1340_%s.fits"
        self.setup2()

class CommCase1341(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1341_%s.fits"
        self.setup2()

class CommCase1342(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1342_%s.fits"
        self.setup2()

class CommCase1343(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1343_%s.fits"
        self.setup2()

class CommCase1344(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1344_%s.fits"
        self.setup2()

class CommCase1345(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1345_%s.fits"
        self.setup2()

class CommCase1346(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1346_%s.fits"
        self.setup2()

class CommCase1347(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1347_%s.fits"
        self.setup2()

class CommCase1348(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1348_%s.fits"
        self.setup2()

class CommCase1349(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1349_%s.fits"
        self.setup2()

class CommCase1350(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1350_%s.fits"
        self.setup2()

class CommCase1351(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1351_%s.fits"
        self.setup2()

class CommCase1352(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1352_%s.fits"
        self.setup2()

class CommCase1353(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1353_%s.fits"
        self.setup2()

class CommCase1354(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f110w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1354_%s.fits"
        self.setup2()

class CommCase1355(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="None"
        self.fname="C1355_%s.fits"
        self.setup2()

class CommCase1356(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.fname="C1356_%s.fits"
        self.setup2()

class CommCase1357(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.fname="C1357_%s.fits"
        self.setup2()

class CommCase1358(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.fname="C1358_%s.fits"
        self.setup2()

class CommCase1359(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.fname="C1359_%s.fits"
        self.setup2()

class CommCase1360(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.fname="C1360_%s.fits"
        self.setup2()

class CommCase1361(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.fname="C1361_%s.fits"
        self.setup2()

class CommCase1362(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1362_%s.fits"
        self.setup2()

class CommCase1363(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1363_%s.fits"
        self.setup2()

class CommCase1364(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1364_%s.fits"
        self.setup2()

class CommCase1365(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1365_%s.fits"
        self.setup2()

class CommCase1366(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1366_%s.fits"
        self.setup2()

class CommCase1367(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1367_%s.fits"
        self.setup2()

class CommCase1368(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1368_%s.fits"
        self.setup2()

class CommCase1369(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f125w"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1369_%s.fits"
        self.setup2()

class CommCase1370(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="None"
        self.fname="C1370_%s.fits"
        self.setup2()

class CommCase1371(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1371_%s.fits"
        self.setup2()

class CommCase1372(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1372_%s.fits"
        self.setup2()

class CommCase1373(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f126n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1373_%s.fits"
        self.setup2()

class CommCase1374(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="None"
        self.fname="C1374_%s.fits"
        self.setup2()

class CommCase1375(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1375_%s.fits"
        self.setup2()

class CommCase1376(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1376_%s.fits"
        self.setup2()

class CommCase1377(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f127m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1377_%s.fits"
        self.setup2()

class CommCase1378(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="None"
        self.fname="C1378_%s.fits"
        self.setup2()

class CommCase1379(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1379_%s.fits"
        self.setup2()

class CommCase1380(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1380_%s.fits"
        self.setup2()

class CommCase1381(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f128n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1381_%s.fits"
        self.setup2()

class CommCase1382(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="None"
        self.fname="C1382_%s.fits"
        self.setup2()

class CommCase1383(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1383_%s.fits"
        self.setup2()

class CommCase1384(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1384_%s.fits"
        self.setup2()

class CommCase1385(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f130n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1385_%s.fits"
        self.setup2()

class CommCase1386(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="None"
        self.fname="C1386_%s.fits"
        self.setup2()

class CommCase1387(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1387_%s.fits"
        self.setup2()

class CommCase1388(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1388_%s.fits"
        self.setup2()

class CommCase1389(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(13200.0,5.0,1.0E-13,flam)"
        self.fname="C1389_%s.fits"
        self.setup2()

class CommCase1390(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f132n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1390_%s.fits"
        self.setup2()

class CommCase1391(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="None"
        self.fname="C1391_%s.fits"
        self.setup2()

class CommCase1392(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1392_%s.fits"
        self.setup2()

class CommCase1393(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1393_%s.fits"
        self.setup2()

class CommCase1394(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f139m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1394_%s.fits"
        self.setup2()

class CommCase1395(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="None"
        self.fname="C1395_%s.fits"
        self.setup2()

class CommCase1396(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1396_%s.fits"
        self.setup2()

class CommCase1397(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1397_%s.fits"
        self.setup2()

class CommCase1398(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C1398_%s.fits"
        self.setup2()

class CommCase1399(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C1399_%s.fits"
        self.setup2()

class CommCase1400(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C1400_%s.fits"
        self.setup2()

class CommCase1401(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C1401_%s.fits"
        self.setup2()

class CommCase1402(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(egal.dat),1.0),band(johnson,b),28.0,vegamag)"
        self.fname="C1402_%s.fits"
        self.setup2()

class CommCase1403(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,b),28.0,vegamag)"
        self.fname="C1403_%s.fits"
        self.setup2()

class CommCase1404(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C1404_%s.fits"
        self.setup2()

class CommCase1405(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="rn(z(spec(spiral.fits),2.0),band(johnson,b),28.0,vegamag)"
        self.fname="C1405_%s.fits"
        self.setup2()

class CommCase1406(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f140w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1406_%s.fits"
        self.setup2()

class CommCase1407(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="None"
        self.fname="C1407_%s.fits"
        self.setup2()

class CommCase1408(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1408_%s.fits"
        self.setup2()

class CommCase1409(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1409_%s.fits"
        self.setup2()

class CommCase1410(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.fname="C1410_%s.fits"
        self.setup2()

class CommCase1411(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.fname="C1411_%s.fits"
        self.setup2()

class CommCase1412(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.fname="C1412_%s.fits"
        self.setup2()

class CommCase1413(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.fname="C1413_%s.fits"
        self.setup2()

class CommCase1414(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1414_%s.fits"
        self.setup2()

class CommCase1415(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.fname="C1415_%s.fits"
        self.setup2()

class CommCase1416(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1416_%s.fits"
        self.setup2()

class CommCase1417(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f153m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.fname="C1417_%s.fits"
        self.setup2()

class CommCase1418(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="None"
        self.fname="C1418_%s.fits"
        self.setup2()

class CommCase1419(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1419_%s.fits"
        self.setup2()

class CommCase1420(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1420_%s.fits"
        self.setup2()

class CommCase1421(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1421_%s.fits"
        self.setup2()

class CommCase1422(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1422_%s.fits"
        self.setup2()

class CommCase1423(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1423_%s.fits"
        self.setup2()

class CommCase1424(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1424_%s.fits"
        self.setup2()

class CommCase1425(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1425_%s.fits"
        self.setup2()

class CommCase1426(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1426_%s.fits"
        self.setup2()

class CommCase1427(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1427_%s.fits"
        self.setup2()

class CommCase1428(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1428_%s.fits"
        self.setup2()

class CommCase1429(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1429_%s.fits"
        self.setup2()

class CommCase1430(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1430_%s.fits"
        self.setup2()

class CommCase1431(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1431_%s.fits"
        self.setup2()

class CommCase1432(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1432_%s.fits"
        self.setup2()

class CommCase1433(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1433_%s.fits"
        self.setup2()

class CommCase1434(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1434_%s.fits"
        self.setup2()

class CommCase1435(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1435_%s.fits"
        self.setup2()

class CommCase1436(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1436_%s.fits"
        self.setup2()

class CommCase1437(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1437_%s.fits"
        self.setup2()

class CommCase1438(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1438_%s.fits"
        self.setup2()

class CommCase1439(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1439_%s.fits"
        self.setup2()

class CommCase1440(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1440_%s.fits"
        self.setup2()

class CommCase1441(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1441_%s.fits"
        self.setup2()

class CommCase1442(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1442_%s.fits"
        self.setup2()

class CommCase1443(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1443_%s.fits"
        self.setup2()

class CommCase1444(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1444_%s.fits"
        self.setup2()

class CommCase1445(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1445_%s.fits"
        self.setup2()

class CommCase1446(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1446_%s.fits"
        self.setup2()

class CommCase1447(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1447_%s.fits"
        self.setup2()

class CommCase1448(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1448_%s.fits"
        self.setup2()

class CommCase1449(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1449_%s.fits"
        self.setup2()

class CommCase1450(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1450_%s.fits"
        self.setup2()

class CommCase1451(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1451_%s.fits"
        self.setup2()

class CommCase1452(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1452_%s.fits"
        self.setup2()

class CommCase1453(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1453_%s.fits"
        self.setup2()

class CommCase1454(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1454_%s.fits"
        self.setup2()

class CommCase1455(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1455_%s.fits"
        self.setup2()

class CommCase1456(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1456_%s.fits"
        self.setup2()

class CommCase1457(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1457_%s.fits"
        self.setup2()

class CommCase1458(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1458_%s.fits"
        self.setup2()

class CommCase1459(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1459_%s.fits"
        self.setup2()

class CommCase1460(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1460_%s.fits"
        self.setup2()

class CommCase1461(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1461_%s.fits"
        self.setup2()

class CommCase1462(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1462_%s.fits"
        self.setup2()

class CommCase1463(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1463_%s.fits"
        self.setup2()

class CommCase1464(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1464_%s.fits"
        self.setup2()

class CommCase1465(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1465_%s.fits"
        self.setup2()

class CommCase1466(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1466_%s.fits"
        self.setup2()

class CommCase1467(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1467_%s.fits"
        self.setup2()

class CommCase1468(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1468_%s.fits"
        self.setup2()

class CommCase1469(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1469_%s.fits"
        self.setup2()

class CommCase1470(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1470_%s.fits"
        self.setup2()

class CommCase1471(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1471_%s.fits"
        self.setup2()

class CommCase1472(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1472_%s.fits"
        self.setup2()

class CommCase1473(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1473_%s.fits"
        self.setup2()

class CommCase1474(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1474_%s.fits"
        self.setup2()

class CommCase1475(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1475_%s.fits"
        self.setup2()

class CommCase1476(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1476_%s.fits"
        self.setup2()

class CommCase1477(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1477_%s.fits"
        self.setup2()

class CommCase1478(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1478_%s.fits"
        self.setup2()

class CommCase1479(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1479_%s.fits"
        self.setup2()

class CommCase1480(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1480_%s.fits"
        self.setup2()

class CommCase1481(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1481_%s.fits"
        self.setup2()

class CommCase1482(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1482_%s.fits"
        self.setup2()

class CommCase1483(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1483_%s.fits"
        self.setup2()

class CommCase1484(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1484_%s.fits"
        self.setup2()

class CommCase1485(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1485_%s.fits"
        self.setup2()

class CommCase1486(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1486_%s.fits"
        self.setup2()

class CommCase1487(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1487_%s.fits"
        self.setup2()

class CommCase1488(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1488_%s.fits"
        self.setup2()

class CommCase1489(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1489_%s.fits"
        self.setup2()

class CommCase1490(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1490_%s.fits"
        self.setup2()

class CommCase1491(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1491_%s.fits"
        self.setup2()

class CommCase1492(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1492_%s.fits"
        self.setup2()

class CommCase1493(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f160w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1493_%s.fits"
        self.setup2()

class CommCase1494(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="None"
        self.fname="C1494_%s.fits"
        self.setup2()

class CommCase1495(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1495_%s.fits"
        self.setup2()

class CommCase1496(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1496_%s.fits"
        self.setup2()

class CommCase1497(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f164n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1497_%s.fits"
        self.setup2()

class CommCase1498(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="None"
        self.fname="C1498_%s.fits"
        self.setup2()

class CommCase1499(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1499_%s.fits"
        self.setup2()

class CommCase1500(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1500_%s.fits"
        self.setup2()

class CommCase1501(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,f167n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1501_%s.fits"
        self.setup2()

class CommCase1502(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.fname="C1502_%s.fits"
        self.setup2()

class CommCase1503(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.fname="C1503_%s.fits"
        self.setup2()

class CommCase1504(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.fname="C1504_%s.fits"
        self.setup2()

class CommCase1505(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        self.fname="C1505_%s.fits"
        self.setup2()

class CommCase1506(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.fname="C1506_%s.fits"
        self.setup2()

class CommCase1507(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.fname="C1507_%s.fits"
        self.setup2()

class CommCase1508(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.fname="C1508_%s.fits"
        self.setup2()

class CommCase1509(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.fname="C1509_%s.fits"
        self.setup2()

class CommCase1510(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.fname="C1510_%s.fits"
        self.setup2()

class CommCase1511(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.fname="C1511_%s.fits"
        self.setup2()

class CommCase1512(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.fname="C1512_%s.fits"
        self.setup2()

class CommCase1513(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        self.fname="C1513_%s.fits"
        self.setup2()

class CommCase1514(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.fname="C1514_%s.fits"
        self.setup2()

class CommCase1515(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.fname="C1515_%s.fits"
        self.setup2()

class CommCase1516(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.fname="C1516_%s.fits"
        self.setup2()

class CommCase1517(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="None"
        self.fname="C1517_%s.fits"
        self.setup2()

class CommCase1518(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1518_%s.fits"
        self.setup2()

class CommCase1519(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1519_%s.fits"
        self.setup2()

class CommCase1520(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1520_%s.fits"
        self.setup2()

class CommCase1521(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g102,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1521_%s.fits"
        self.setup2()

class CommCase1522(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.fname="C1522_%s.fits"
        self.setup2()

class CommCase1523(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.fname="C1523_%s.fits"
        self.setup2()

class CommCase1524(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.fname="C1524_%s.fits"
        self.setup2()

class CommCase1525(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.fname="C1525_%s.fits"
        self.setup2()

class CommCase1526(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.fname="C1526_%s.fits"
        self.setup2()

class CommCase1527(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.fname="C1527_%s.fits"
        self.setup2()

class CommCase1528(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.fname="C1528_%s.fits"
        self.setup2()

class CommCase1529(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.fname="C1529_%s.fits"
        self.setup2()

class CommCase1530(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.fname="C1530_%s.fits"
        self.setup2()

class CommCase1531(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1531_%s.fits"
        self.setup2()

class CommCase1532(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1532_%s.fits"
        self.setup2()

class CommCase1533(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1533_%s.fits"
        self.setup2()

class CommCase1534(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1534_%s.fits"
        self.setup2()

class CommCase1535(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1535_%s.fits"
        self.setup2()

class CommCase1536(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1536_%s.fits"
        self.setup2()

class CommCase1537(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1537_%s.fits"
        self.setup2()

class CommCase1538(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1538_%s.fits"
        self.setup2()

class CommCase1539(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1539_%s.fits"
        self.setup2()

class CommCase1540(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1540_%s.fits"
        self.setup2()

class CommCase1541(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1541_%s.fits"
        self.setup2()

class CommCase1542(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1542_%s.fits"
        self.setup2()

class CommCase1543(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1543_%s.fits"
        self.setup2()

class CommCase1544(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1544_%s.fits"
        self.setup2()

class CommCase1545(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="None"
        self.fname="C1545_%s.fits"
        self.setup2()

class CommCase1546(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1546_%s.fits"
        self.setup2()

class CommCase1547(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1547_%s.fits"
        self.setup2()

class CommCase1548(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1548_%s.fits"
        self.setup2()

class CommCase1549(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1549_%s.fits"
        self.setup2()

class CommCase1550(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1550_%s.fits"
        self.setup2()

class CommCase1551(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,ir,g141,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1551_%s.fits"
        self.setup2()

class CommCase1552(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1552_%s.fits"
        self.setup2()

class CommCase1553(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1553_%s.fits"
        self.setup2()

class CommCase1554(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1554_%s.fits"
        self.setup2()

class CommCase1555(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1555_%s.fits"
        self.setup2()

class CommCase1556(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1556_%s.fits"
        self.setup2()

class CommCase1557(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1557_%s.fits"
        self.setup2()

class CommCase1558(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1558_%s.fits"
        self.setup2()

class CommCase1559(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1559_%s.fits"
        self.setup2()

class CommCase1560(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.fname="C1560_%s.fits"
        self.setup2()

class CommCase1561(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.fname="C1561_%s.fits"
        self.setup2()

class CommCase1562(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.fname="C1562_%s.fits"
        self.setup2()

class CommCase1563(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.fname="C1563_%s.fits"
        self.setup2()

class CommCase1564(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1564_%s.fits"
        self.setup2()

class CommCase1565(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.fname="C1565_%s.fits"
        self.setup2()

class CommCase1566(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1566_%s.fits"
        self.setup2()

class CommCase1567(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.fname="C1567_%s.fits"
        self.setup2()

class CommCase1568(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1568_%s.fits"
        self.setup2()

class CommCase1569(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1569_%s.fits"
        self.setup2()

class CommCase1570(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1570_%s.fits"
        self.setup2()

class CommCase1571(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1571_%s.fits"
        self.setup2()

class CommCase1572(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1572_%s.fits"
        self.setup2()

class CommCase1573(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1573_%s.fits"
        self.setup2()

class CommCase1574(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.fname="C1574_%s.fits"
        self.setup2()

class CommCase1575(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.fname="C1575_%s.fits"
        self.setup2()

class CommCase1576(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.fname="C1576_%s.fits"
        self.setup2()

class CommCase1577(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.fname="C1577_%s.fits"
        self.setup2()

class CommCase1578(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.fname="C1578_%s.fits"
        self.setup2()

class CommCase1579(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.fname="C1579_%s.fits"
        self.setup2()

class CommCase1580(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1580_%s.fits"
        self.setup2()

class CommCase1581(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1581_%s.fits"
        self.setup2()

class CommCase1582(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1582_%s.fits"
        self.setup2()

class CommCase1583(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1583_%s.fits"
        self.setup2()

class CommCase1584(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1584_%s.fits"
        self.setup2()

class CommCase1585(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1585_%s.fits"
        self.setup2()

class CommCase1586(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1586_%s.fits"
        self.setup2()

class CommCase1587(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1587_%s.fits"
        self.setup2()

class CommCase1588(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1588_%s.fits"
        self.setup2()

class CommCase1589(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1589_%s.fits"
        self.setup2()

class CommCase1590(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1590_%s.fits"
        self.setup2()

class CommCase1591(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1591_%s.fits"
        self.setup2()

class CommCase1592(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1592_%s.fits"
        self.setup2()

class CommCase1593(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1593_%s.fits"
        self.setup2()

class CommCase1594(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1594_%s.fits"
        self.setup2()

class CommCase1595(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1595_%s.fits"
        self.setup2()

class CommCase1596(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1596_%s.fits"
        self.setup2()

class CommCase1597(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1597_%s.fits"
        self.setup2()

class CommCase1598(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1598_%s.fits"
        self.setup2()

class CommCase1599(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1599_%s.fits"
        self.setup2()

class CommCase1600(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1600_%s.fits"
        self.setup2()

class CommCase1601(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1601_%s.fits"
        self.setup2()

class CommCase1602(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1602_%s.fits"
        self.setup2()

class CommCase1603(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1603_%s.fits"
        self.setup2()

class CommCase1604(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1604_%s.fits"
        self.setup2()

class CommCase1605(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1605_%s.fits"
        self.setup2()

class CommCase1606(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1606_%s.fits"
        self.setup2()

class CommCase1607(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1607_%s.fits"
        self.setup2()

class CommCase1608(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1608_%s.fits"
        self.setup2()

class CommCase1609(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1609_%s.fits"
        self.setup2()

class CommCase1610(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1610_%s.fits"
        self.setup2()

class CommCase1611(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1611_%s.fits"
        self.setup2()

class CommCase1612(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1612_%s.fits"
        self.setup2()

class CommCase1613(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1613_%s.fits"
        self.setup2()

class CommCase1614(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1614_%s.fits"
        self.setup2()

class CommCase1615(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1615_%s.fits"
        self.setup2()

class CommCase1616(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1616_%s.fits"
        self.setup2()

class CommCase1617(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1617_%s.fits"
        self.setup2()

class CommCase1618(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1618_%s.fits"
        self.setup2()

class CommCase1619(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1619_%s.fits"
        self.setup2()

class CommCase1620(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1620_%s.fits"
        self.setup2()

class CommCase1621(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1621_%s.fits"
        self.setup2()

class CommCase1622(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1622_%s.fits"
        self.setup2()

class CommCase1623(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1623_%s.fits"
        self.setup2()

class CommCase1624(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1624_%s.fits"
        self.setup2()

class CommCase1625(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1625_%s.fits"
        self.setup2()

class CommCase1626(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1626_%s.fits"
        self.setup2()

class CommCase1627(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1627_%s.fits"
        self.setup2()

class CommCase1628(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1628_%s.fits"
        self.setup2()

class CommCase1629(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1629_%s.fits"
        self.setup2()

class CommCase1630(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1630_%s.fits"
        self.setup2()

class CommCase1631(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1631_%s.fits"
        self.setup2()

class CommCase1632(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.fname="C1632_%s.fits"
        self.setup2()

class CommCase1633(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1633_%s.fits"
        self.setup2()

class CommCase1634(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1634_%s.fits"
        self.setup2()

class CommCase1635(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1635_%s.fits"
        self.setup2()

class CommCase1636(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1636_%s.fits"
        self.setup2()

class CommCase1637(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1637_%s.fits"
        self.setup2()

class CommCase1638(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1638_%s.fits"
        self.setup2()

class CommCase1639(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C1639_%s.fits"
        self.setup2()

class CommCase1640(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C1640_%s.fits"
        self.setup2()

class CommCase1641(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C1641_%s.fits"
        self.setup2()

class CommCase1642(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C1642_%s.fits"
        self.setup2()

class CommCase1643(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C1643_%s.fits"
        self.setup2()

class CommCase1644(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C1644_%s.fits"
        self.setup2()

class CommCase1645(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C1645_%s.fits"
        self.setup2()

class CommCase1646(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C1646_%s.fits"
        self.setup2()

class CommCase1647(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C1647_%s.fits"
        self.setup2()

class CommCase1648(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C1648_%s.fits"
        self.setup2()

class CommCase1649(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C1649_%s.fits"
        self.setup2()

class CommCase1650(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C1650_%s.fits"
        self.setup2()

class CommCase1651(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C1651_%s.fits"
        self.setup2()

class CommCase1652(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C1652_%s.fits"
        self.setup2()

class CommCase1653(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C1653_%s.fits"
        self.setup2()

class CommCase1654(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C1654_%s.fits"
        self.setup2()

class CommCase1655(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C1655_%s.fits"
        self.setup2()

class CommCase1656(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C1656_%s.fits"
        self.setup2()

class CommCase1657(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C1657_%s.fits"
        self.setup2()

class CommCase1658(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C1658_%s.fits"
        self.setup2()

class CommCase1659(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C1659_%s.fits"
        self.setup2()

class CommCase1660(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C1660_%s.fits"
        self.setup2()

class CommCase1661(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C1661_%s.fits"
        self.setup2()

class CommCase1662(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C1662_%s.fits"
        self.setup2()

class CommCase1663(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C1663_%s.fits"
        self.setup2()

class CommCase1664(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C1664_%s.fits"
        self.setup2()

class CommCase1665(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C1665_%s.fits"
        self.setup2()

class CommCase1666(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C1666_%s.fits"
        self.setup2()

class CommCase1667(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1667_%s.fits"
        self.setup2()

class CommCase1668(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1668_%s.fits"
        self.setup2()

class CommCase1669(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1669_%s.fits"
        self.setup2()

class CommCase1670(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1670_%s.fits"
        self.setup2()

class CommCase1671(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1671_%s.fits"
        self.setup2()

class CommCase1672(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1672_%s.fits"
        self.setup2()

class CommCase1673(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1673_%s.fits"
        self.setup2()

class CommCase1674(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1674_%s.fits"
        self.setup2()

class CommCase1675(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1675_%s.fits"
        self.setup2()

class CommCase1676(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1676_%s.fits"
        self.setup2()

class CommCase1677(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1677_%s.fits"
        self.setup2()

class CommCase1678(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1678_%s.fits"
        self.setup2()

class CommCase1679(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1679_%s.fits"
        self.setup2()

class CommCase1680(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1680_%s.fits"
        self.setup2()

class CommCase1681(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1681_%s.fits"
        self.setup2()

class CommCase1682(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1682_%s.fits"
        self.setup2()

class CommCase1683(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1683_%s.fits"
        self.setup2()

class CommCase1684(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1684_%s.fits"
        self.setup2()

class CommCase1685(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1685_%s.fits"
        self.setup2()

class CommCase1686(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1686_%s.fits"
        self.setup2()

class CommCase1687(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1687_%s.fits"
        self.setup2()

class CommCase1688(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1688_%s.fits"
        self.setup2()

class CommCase1689(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C1689_%s.fits"
        self.setup2()

class CommCase1690(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C1690_%s.fits"
        self.setup2()

class CommCase1691(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C1691_%s.fits"
        self.setup2()

class CommCase1692(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1692_%s.fits"
        self.setup2()

class CommCase1693(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C1693_%s.fits"
        self.setup2()

class CommCase1694(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C1694_%s.fits"
        self.setup2()

class CommCase1695(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1695_%s.fits"
        self.setup2()

class CommCase1696(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1696_%s.fits"
        self.setup2()

class CommCase1697(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1697_%s.fits"
        self.setup2()

class CommCase1698(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1698_%s.fits"
        self.setup2()

class CommCase1699(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1699_%s.fits"
        self.setup2()

class CommCase1700(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1700_%s.fits"
        self.setup2()

class CommCase1701(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1701_%s.fits"
        self.setup2()

class CommCase1702(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1702_%s.fits"
        self.setup2()

class CommCase1703(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1703_%s.fits"
        self.setup2()

class CommCase1704(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1704_%s.fits"
        self.setup2()

class CommCase1705(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1705_%s.fits"
        self.setup2()

class CommCase1706(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1706_%s.fits"
        self.setup2()

class CommCase1707(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1707_%s.fits"
        self.setup2()

class CommCase1708(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1708_%s.fits"
        self.setup2()

class CommCase1709(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1709_%s.fits"
        self.setup2()

class CommCase1710(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1710_%s.fits"
        self.setup2()

class CommCase1711(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1711_%s.fits"
        self.setup2()

class CommCase1712(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1712_%s.fits"
        self.setup2()

class CommCase1713(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1713_%s.fits"
        self.setup2()

class CommCase1714(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1714_%s.fits"
        self.setup2()

class CommCase1715(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1715_%s.fits"
        self.setup2()

class CommCase1716(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1716_%s.fits"
        self.setup2()

class CommCase1717(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1717_%s.fits"
        self.setup2()

class CommCase1718(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1718_%s.fits"
        self.setup2()

class CommCase1719(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1719_%s.fits"
        self.setup2()

class CommCase1720(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1720_%s.fits"
        self.setup2()

class CommCase1721(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1721_%s.fits"
        self.setup2()

class CommCase1722(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1722_%s.fits"
        self.setup2()

class CommCase1723(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1723_%s.fits"
        self.setup2()

class CommCase1724(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1724_%s.fits"
        self.setup2()

class CommCase1725(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1725_%s.fits"
        self.setup2()

class CommCase1726(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1726_%s.fits"
        self.setup2()

class CommCase1727(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1727_%s.fits"
        self.setup2()

class CommCase1728(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1728_%s.fits"
        self.setup2()

class CommCase1729(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1729_%s.fits"
        self.setup2()

class CommCase1730(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1730_%s.fits"
        self.setup2()

class CommCase1731(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1731_%s.fits"
        self.setup2()

class CommCase1732(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1732_%s.fits"
        self.setup2()

class CommCase1733(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1733_%s.fits"
        self.setup2()

class CommCase1734(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1734_%s.fits"
        self.setup2()

class CommCase1735(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1735_%s.fits"
        self.setup2()

class CommCase1736(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1736_%s.fits"
        self.setup2()

class CommCase1737(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1737_%s.fits"
        self.setup2()

class CommCase1738(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1738_%s.fits"
        self.setup2()

class CommCase1739(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1739_%s.fits"
        self.setup2()

class CommCase1740(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1740_%s.fits"
        self.setup2()

class CommCase1741(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1741_%s.fits"
        self.setup2()

class CommCase1742(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1742_%s.fits"
        self.setup2()

class CommCase1743(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1743_%s.fits"
        self.setup2()

class CommCase1744(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1744_%s.fits"
        self.setup2()

class CommCase1745(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1745_%s.fits"
        self.setup2()

class CommCase1746(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1746_%s.fits"
        self.setup2()

class CommCase1747(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1747_%s.fits"
        self.setup2()

class CommCase1748(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1748_%s.fits"
        self.setup2()

class CommCase1749(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1749_%s.fits"
        self.setup2()

class CommCase1750(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1750_%s.fits"
        self.setup2()

class CommCase1751(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1751_%s.fits"
        self.setup2()

class CommCase1752(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1752_%s.fits"
        self.setup2()

class CommCase1753(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1753_%s.fits"
        self.setup2()

class CommCase1754(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1754_%s.fits"
        self.setup2()

class CommCase1755(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1755_%s.fits"
        self.setup2()

class CommCase1756(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1756_%s.fits"
        self.setup2()

class CommCase1757(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1757_%s.fits"
        self.setup2()

class CommCase1758(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1758_%s.fits"
        self.setup2()

class CommCase1759(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1759_%s.fits"
        self.setup2()

class CommCase1760(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1760_%s.fits"
        self.setup2()

class CommCase1761(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1761_%s.fits"
        self.setup2()

class CommCase1762(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1762_%s.fits"
        self.setup2()

class CommCase1763(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1763_%s.fits"
        self.setup2()

class CommCase1764(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1764_%s.fits"
        self.setup2()

class CommCase1765(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1765_%s.fits"
        self.setup2()

class CommCase1766(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1766_%s.fits"
        self.setup2()

class CommCase1767(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1767_%s.fits"
        self.setup2()

class CommCase1768(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1768_%s.fits"
        self.setup2()

class CommCase1769(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1769_%s.fits"
        self.setup2()

class CommCase1770(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1770_%s.fits"
        self.setup2()

class CommCase1771(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1771_%s.fits"
        self.setup2()

class CommCase1772(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1772_%s.fits"
        self.setup2()

class CommCase1773(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1773_%s.fits"
        self.setup2()

class CommCase1774(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1774_%s.fits"
        self.setup2()

class CommCase1775(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1775_%s.fits"
        self.setup2()

class CommCase1776(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1776_%s.fits"
        self.setup2()

class CommCase1777(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1777_%s.fits"
        self.setup2()

class CommCase1778(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1778_%s.fits"
        self.setup2()

class CommCase1779(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1779_%s.fits"
        self.setup2()

class CommCase1780(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1780_%s.fits"
        self.setup2()

class CommCase1781(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1781_%s.fits"
        self.setup2()

class CommCase1782(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1782_%s.fits"
        self.setup2()

class CommCase1783(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1783_%s.fits"
        self.setup2()

class CommCase1784(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1784_%s.fits"
        self.setup2()

class CommCase1785(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1785_%s.fits"
        self.setup2()

class CommCase1786(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1786_%s.fits"
        self.setup2()

class CommCase1787(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1787_%s.fits"
        self.setup2()

class CommCase1788(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1788_%s.fits"
        self.setup2()

class CommCase1789(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1789_%s.fits"
        self.setup2()

class CommCase1790(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1790_%s.fits"
        self.setup2()

class CommCase1791(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1791_%s.fits"
        self.setup2()

class CommCase1792(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1792_%s.fits"
        self.setup2()

class CommCase1793(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1793_%s.fits"
        self.setup2()

class CommCase1794(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1794_%s.fits"
        self.setup2()

class CommCase1795(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1795_%s.fits"
        self.setup2()

class CommCase1796(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1796_%s.fits"
        self.setup2()

class CommCase1797(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1797_%s.fits"
        self.setup2()

class CommCase1798(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1798_%s.fits"
        self.setup2()

class CommCase1799(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1799_%s.fits"
        self.setup2()

class CommCase1800(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1800_%s.fits"
        self.setup2()

class CommCase1801(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1801_%s.fits"
        self.setup2()

class CommCase1802(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1802_%s.fits"
        self.setup2()

class CommCase1803(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1803_%s.fits"
        self.setup2()

class CommCase1804(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1804_%s.fits"
        self.setup2()

class CommCase1805(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1805_%s.fits"
        self.setup2()

class CommCase1806(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1806_%s.fits"
        self.setup2()

class CommCase1807(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1807_%s.fits"
        self.setup2()

class CommCase1808(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1808_%s.fits"
        self.setup2()

class CommCase1809(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1809_%s.fits"
        self.setup2()

class CommCase1810(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1810_%s.fits"
        self.setup2()

class CommCase1811(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1811_%s.fits"
        self.setup2()

class CommCase1812(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1812_%s.fits"
        self.setup2()

class CommCase1813(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1813_%s.fits"
        self.setup2()

class CommCase1814(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1814_%s.fits"
        self.setup2()

class CommCase1815(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1815_%s.fits"
        self.setup2()

class CommCase1816(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1816_%s.fits"
        self.setup2()

class CommCase1817(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.fname="C1817_%s.fits"
        self.setup2()

class CommCase1818(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.fname="C1818_%s.fits"
        self.setup2()

class CommCase1819(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.fname="C1819_%s.fits"
        self.setup2()

class CommCase1820(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1820_%s.fits"
        self.setup2()

class CommCase1821(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1821_%s.fits"
        self.setup2()

class CommCase1822(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1822_%s.fits"
        self.setup2()

class CommCase1823(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1823_%s.fits"
        self.setup2()

class CommCase1824(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1824_%s.fits"
        self.setup2()

class CommCase1825(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1825_%s.fits"
        self.setup2()

class CommCase1826(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1826_%s.fits"
        self.setup2()

class CommCase1827(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1827_%s.fits"
        self.setup2()

class CommCase1828(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1828_%s.fits"
        self.setup2()

class CommCase1829(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1829_%s.fits"
        self.setup2()

class CommCase1830(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1830_%s.fits"
        self.setup2()

class CommCase1831(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1831_%s.fits"
        self.setup2()

class CommCase1832(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1832_%s.fits"
        self.setup2()

class CommCase1833(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1833_%s.fits"
        self.setup2()

class CommCase1834(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1834_%s.fits"
        self.setup2()

class CommCase1835(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1835_%s.fits"
        self.setup2()

class CommCase1836(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1836_%s.fits"
        self.setup2()

class CommCase1837(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1837_%s.fits"
        self.setup2()

class CommCase1838(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1838_%s.fits"
        self.setup2()

class CommCase1839(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1839_%s.fits"
        self.setup2()

class CommCase1840(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1840_%s.fits"
        self.setup2()

class CommCase1841(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1841_%s.fits"
        self.setup2()

class CommCase1842(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1842_%s.fits"
        self.setup2()

class CommCase1843(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1843_%s.fits"
        self.setup2()

class CommCase1844(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1844_%s.fits"
        self.setup2()

class CommCase1845(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1845_%s.fits"
        self.setup2()

class CommCase1846(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1846_%s.fits"
        self.setup2()

class CommCase1847(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1847_%s.fits"
        self.setup2()

class CommCase1848(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1848_%s.fits"
        self.setup2()

class CommCase1849(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1849_%s.fits"
        self.setup2()

class CommCase1850(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1850_%s.fits"
        self.setup2()

class CommCase1851(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1851_%s.fits"
        self.setup2()

class CommCase1852(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1852_%s.fits"
        self.setup2()

class CommCase1853(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1853_%s.fits"
        self.setup2()

class CommCase1854(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1854_%s.fits"
        self.setup2()

class CommCase1855(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1855_%s.fits"
        self.setup2()

class CommCase1856(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1856_%s.fits"
        self.setup2()

class CommCase1857(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1857_%s.fits"
        self.setup2()

class CommCase1858(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1858_%s.fits"
        self.setup2()

class CommCase1859(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1859_%s.fits"
        self.setup2()

class CommCase1860(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1860_%s.fits"
        self.setup2()

class CommCase1861(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1861_%s.fits"
        self.setup2()

class CommCase1862(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1862_%s.fits"
        self.setup2()

class CommCase1863(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1863_%s.fits"
        self.setup2()

class CommCase1864(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1864_%s.fits"
        self.setup2()

class CommCase1865(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1865_%s.fits"
        self.setup2()

class CommCase1866(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1866_%s.fits"
        self.setup2()

class CommCase1867(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1867_%s.fits"
        self.setup2()

class CommCase1868(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1868_%s.fits"
        self.setup2()

class CommCase1869(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1869_%s.fits"
        self.setup2()

class CommCase1870(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1870_%s.fits"
        self.setup2()

class CommCase1871(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1871_%s.fits"
        self.setup2()

class CommCase1872(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1872_%s.fits"
        self.setup2()

class CommCase1873(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1873_%s.fits"
        self.setup2()

class CommCase1874(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1874_%s.fits"
        self.setup2()

class CommCase1875(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1875_%s.fits"
        self.setup2()

class CommCase1876(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1876_%s.fits"
        self.setup2()

class CommCase1877(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1877_%s.fits"
        self.setup2()

class CommCase1878(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1878_%s.fits"
        self.setup2()

class CommCase1879(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1879_%s.fits"
        self.setup2()

class CommCase1880(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1880_%s.fits"
        self.setup2()

class CommCase1881(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1881_%s.fits"
        self.setup2()

class CommCase1882(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1882_%s.fits"
        self.setup2()

class CommCase1883(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1883_%s.fits"
        self.setup2()

class CommCase1884(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1884_%s.fits"
        self.setup2()

class CommCase1885(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1885_%s.fits"
        self.setup2()

class CommCase1886(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1886_%s.fits"
        self.setup2()

class CommCase1887(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.fname="C1887_%s.fits"
        self.setup2()

class CommCase1888(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.fname="C1888_%s.fits"
        self.setup2()

class CommCase1889(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.fname="C1889_%s.fits"
        self.setup2()

class CommCase1890(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.fname="C1890_%s.fits"
        self.setup2()

class CommCase1891(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.fname="C1891_%s.fits"
        self.setup2()

class CommCase1892(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.fname="C1892_%s.fits"
        self.setup2()

class CommCase1893(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.fname="C1893_%s.fits"
        self.setup2()

class CommCase1894(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.fname="C1894_%s.fits"
        self.setup2()

class CommCase1895(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.fname="C1895_%s.fits"
        self.setup2()

class CommCase1896(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        self.fname="C1896_%s.fits"
        self.setup2()

class CommCase1897(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.fname="C1897_%s.fits"
        self.setup2()

class CommCase1898(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.fname="C1898_%s.fits"
        self.setup2()

class CommCase1899(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.fname="C1899_%s.fits"
        self.setup2()

class CommCase1900(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.fname="C1900_%s.fits"
        self.setup2()

class CommCase1901(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.fname="C1901_%s.fits"
        self.setup2()

class CommCase1902(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.fname="C1902_%s.fits"
        self.setup2()

class CommCase1903(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.fname="C1903_%s.fits"
        self.setup2()

class CommCase1904(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        self.fname="C1904_%s.fits"
        self.setup2()

class CommCase1905(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1905_%s.fits"
        self.setup2()

class CommCase1906(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1906_%s.fits"
        self.setup2()

class CommCase1907(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1907_%s.fits"
        self.setup2()

class CommCase1908(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1908_%s.fits"
        self.setup2()

class CommCase1909(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1909_%s.fits"
        self.setup2()

class CommCase1910(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1910_%s.fits"
        self.setup2()

class CommCase1911(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1911_%s.fits"
        self.setup2()

class CommCase1912(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C1912_%s.fits"
        self.setup2()

class CommCase1913(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C1913_%s.fits"
        self.setup2()

class CommCase1914(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C1914_%s.fits"
        self.setup2()

class CommCase1915(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1915_%s.fits"
        self.setup2()

class CommCase1916(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C1916_%s.fits"
        self.setup2()

class CommCase1917(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C1917_%s.fits"
        self.setup2()

class CommCase1918(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C1918_%s.fits"
        self.setup2()

class CommCase1919(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.fname="C1919_%s.fits"
        self.setup2()

class CommCase1920(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.fname="C1920_%s.fits"
        self.setup2()

class CommCase1921(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.fname="C1921_%s.fits"
        self.setup2()

class CommCase1922(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1922_%s.fits"
        self.setup2()

class CommCase1923(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1923_%s.fits"
        self.setup2()

class CommCase1924(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1924_%s.fits"
        self.setup2()

class CommCase1925(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1925_%s.fits"
        self.setup2()

class CommCase1926(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1926_%s.fits"
        self.setup2()

class CommCase1927(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1927_%s.fits"
        self.setup2()

class CommCase1928(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1928_%s.fits"
        self.setup2()

class CommCase1929(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1929_%s.fits"
        self.setup2()

class CommCase1930(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis1,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1930_%s.fits"
        self.setup2()

class CommCase1931(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1931_%s.fits"
        self.setup2()

class CommCase1932(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1932_%s.fits"
        self.setup2()

class CommCase1933(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f200lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1933_%s.fits"
        self.setup2()

class CommCase1934(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1934_%s.fits"
        self.setup2()

class CommCase1935(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1935_%s.fits"
        self.setup2()

class CommCase1936(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f218w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1936_%s.fits"
        self.setup2()

class CommCase1937(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1937_%s.fits"
        self.setup2()

class CommCase1938(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1938_%s.fits"
        self.setup2()

class CommCase1939(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        self.fname="C1939_%s.fits"
        self.setup2()

class CommCase1940(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        self.fname="C1940_%s.fits"
        self.setup2()

class CommCase1941(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        self.fname="C1941_%s.fits"
        self.setup2()

class CommCase1942(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        self.fname="C1942_%s.fits"
        self.setup2()

class CommCase1943(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        self.fname="C1943_%s.fits"
        self.setup2()

class CommCase1944(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        self.fname="C1944_%s.fits"
        self.setup2()

class CommCase1945(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1945_%s.fits"
        self.setup2()

class CommCase1946(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f225w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        self.fname="C1946_%s.fits"
        self.setup2()

class CommCase1947(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1947_%s.fits"
        self.setup2()

class CommCase1948(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1948_%s.fits"
        self.setup2()

class CommCase1949(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f275w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1949_%s.fits"
        self.setup2()

class CommCase1950(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1950_%s.fits"
        self.setup2()

class CommCase1951(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1951_%s.fits"
        self.setup2()

class CommCase1952(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f280n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1952_%s.fits"
        self.setup2()

class CommCase1953(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        self.fname="C1953_%s.fits"
        self.setup2()

class CommCase1954(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        self.fname="C1954_%s.fits"
        self.setup2()

class CommCase1955(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        self.fname="C1955_%s.fits"
        self.setup2()

class CommCase1956(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        self.fname="C1956_%s.fits"
        self.setup2()

class CommCase1957(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        self.fname="C1957_%s.fits"
        self.setup2()

class CommCase1958(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        self.fname="C1958_%s.fits"
        self.setup2()

class CommCase1959(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1959_%s.fits"
        self.setup2()

class CommCase1960(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1960_%s.fits"
        self.setup2()

class CommCase1961(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1961_%s.fits"
        self.setup2()

class CommCase1962(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1962_%s.fits"
        self.setup2()

class CommCase1963(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1963_%s.fits"
        self.setup2()

class CommCase1964(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1964_%s.fits"
        self.setup2()

class CommCase1965(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1965_%s.fits"
        self.setup2()

class CommCase1966(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f300x"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1966_%s.fits"
        self.setup2()

class CommCase1967(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1967_%s.fits"
        self.setup2()

class CommCase1968(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1968_%s.fits"
        self.setup2()

class CommCase1969(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f336w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1969_%s.fits"
        self.setup2()

class CommCase1970(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1970_%s.fits"
        self.setup2()

class CommCase1971(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1971_%s.fits"
        self.setup2()

class CommCase1972(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f343n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1972_%s.fits"
        self.setup2()

class CommCase1973(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1973_%s.fits"
        self.setup2()

class CommCase1974(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1974_%s.fits"
        self.setup2()

class CommCase1975(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f350lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1975_%s.fits"
        self.setup2()

class CommCase1976(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1976_%s.fits"
        self.setup2()

class CommCase1977(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1977_%s.fits"
        self.setup2()

class CommCase1978(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f373n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1978_%s.fits"
        self.setup2()

class CommCase1979(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1979_%s.fits"
        self.setup2()

class CommCase1980(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1980_%s.fits"
        self.setup2()

class CommCase1981(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1981_%s.fits"
        self.setup2()

class CommCase1982(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1982_%s.fits"
        self.setup2()

class CommCase1983(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1983_%s.fits"
        self.setup2()

class CommCase1984(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f390w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1984_%s.fits"
        self.setup2()

class CommCase1985(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1985_%s.fits"
        self.setup2()

class CommCase1986(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1986_%s.fits"
        self.setup2()

class CommCase1987(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f395n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1987_%s.fits"
        self.setup2()

class CommCase1988(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1988_%s.fits"
        self.setup2()

class CommCase1989(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1989_%s.fits"
        self.setup2()

class CommCase1990(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f410m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1990_%s.fits"
        self.setup2()

class CommCase1991(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1991_%s.fits"
        self.setup2()

class CommCase1992(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1992_%s.fits"
        self.setup2()

class CommCase1993(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f438w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1993_%s.fits"
        self.setup2()

class CommCase1994(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1994_%s.fits"
        self.setup2()

class CommCase1995(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1995_%s.fits"
        self.setup2()

class CommCase1996(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f467m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1996_%s.fits"
        self.setup2()

class CommCase1997(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C1997_%s.fits"
        self.setup2()

class CommCase1998(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C1998_%s.fits"
        self.setup2()

class CommCase1999(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f469n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C1999_%s.fits"
        self.setup2()

class CommCase2000(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2000_%s.fits"
        self.setup2()

class CommCase2001(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2001_%s.fits"
        self.setup2()

class CommCase2002(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2002_%s.fits"
        self.setup2()

class CommCase2003(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2003_%s.fits"
        self.setup2()

class CommCase2004(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2004_%s.fits"
        self.setup2()

class CommCase2005(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f475x"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2005_%s.fits"
        self.setup2()

class CommCase2006(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2006_%s.fits"
        self.setup2()

class CommCase2007(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2007_%s.fits"
        self.setup2()

class CommCase2008(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f487n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2008_%s.fits"
        self.setup2()

class CommCase2009(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2009_%s.fits"
        self.setup2()

class CommCase2010(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2010_%s.fits"
        self.setup2()

class CommCase2011(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        self.fname="C2011_%s.fits"
        self.setup2()

class CommCase2012(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f502n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2012_%s.fits"
        self.setup2()

class CommCase2013(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2013_%s.fits"
        self.setup2()

class CommCase2014(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2014_%s.fits"
        self.setup2()

class CommCase2015(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f547m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2015_%s.fits"
        self.setup2()

class CommCase2016(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2016_%s.fits"
        self.setup2()

class CommCase2017(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2017_%s.fits"
        self.setup2()

class CommCase2018(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C2018_%s.fits"
        self.setup2()

class CommCase2019(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C2019_%s.fits"
        self.setup2()

class CommCase2020(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C2020_%s.fits"
        self.setup2()

class CommCase2021(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C2021_%s.fits"
        self.setup2()

class CommCase2022(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C2022_%s.fits"
        self.setup2()

class CommCase2023(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C2023_%s.fits"
        self.setup2()

class CommCase2024(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C2024_%s.fits"
        self.setup2()

class CommCase2025(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C2025_%s.fits"
        self.setup2()

class CommCase2026(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C2026_%s.fits"
        self.setup2()

class CommCase2027(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C2027_%s.fits"
        self.setup2()

class CommCase2028(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C2028_%s.fits"
        self.setup2()

class CommCase2029(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C2029_%s.fits"
        self.setup2()

class CommCase2030(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C2030_%s.fits"
        self.setup2()

class CommCase2031(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C2031_%s.fits"
        self.setup2()

class CommCase2032(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C2032_%s.fits"
        self.setup2()

class CommCase2033(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C2033_%s.fits"
        self.setup2()

class CommCase2034(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C2034_%s.fits"
        self.setup2()

class CommCase2035(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C2035_%s.fits"
        self.setup2()

class CommCase2036(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C2036_%s.fits"
        self.setup2()

class CommCase2037(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C2037_%s.fits"
        self.setup2()

class CommCase2038(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C2038_%s.fits"
        self.setup2()

class CommCase2039(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C2039_%s.fits"
        self.setup2()

class CommCase2040(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        self.fname="C2040_%s.fits"
        self.setup2()

class CommCase2041(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        self.fname="C2041_%s.fits"
        self.setup2()

class CommCase2042(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        self.fname="C2042_%s.fits"
        self.setup2()

class CommCase2043(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        self.fname="C2043_%s.fits"
        self.setup2()

class CommCase2044(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        self.fname="C2044_%s.fits"
        self.setup2()

class CommCase2045(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        self.fname="C2045_%s.fits"
        self.setup2()

class CommCase2046(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f555w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2046_%s.fits"
        self.setup2()

class CommCase2047(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2047_%s.fits"
        self.setup2()

class CommCase2048(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2048_%s.fits"
        self.setup2()

class CommCase2049(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f600lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2049_%s.fits"
        self.setup2()

class CommCase2050(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C2050_%s.fits"
        self.setup2()

class CommCase2051(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C2051_%s.fits"
        self.setup2()

class CommCase2052(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C2052_%s.fits"
        self.setup2()

class CommCase2053(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2053_%s.fits"
        self.setup2()

class CommCase2054(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2054_%s.fits"
        self.setup2()

class CommCase2055(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C2055_%s.fits"
        self.setup2()

class CommCase2056(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C2056_%s.fits"
        self.setup2()

class CommCase2057(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C2057_%s.fits"
        self.setup2()

class CommCase2058(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2058_%s.fits"
        self.setup2()

class CommCase2059(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C2059_%s.fits"
        self.setup2()

class CommCase2060(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2060_%s.fits"
        self.setup2()

class CommCase2061(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C2061_%s.fits"
        self.setup2()

class CommCase2062(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C2062_%s.fits"
        self.setup2()

class CommCase2063(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C2063_%s.fits"
        self.setup2()

class CommCase2064(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C2064_%s.fits"
        self.setup2()

class CommCase2065(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2065_%s.fits"
        self.setup2()

class CommCase2066(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2066_%s.fits"
        self.setup2()

class CommCase2067(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C2067_%s.fits"
        self.setup2()

class CommCase2068(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        self.fname="C2068_%s.fits"
        self.setup2()

class CommCase2069(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        self.fname="C2069_%s.fits"
        self.setup2()

class CommCase2070(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        self.fname="C2070_%s.fits"
        self.setup2()

class CommCase2071(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2071_%s.fits"
        self.setup2()

class CommCase2072(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        self.fname="C2072_%s.fits"
        self.setup2()

class CommCase2073(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        self.fname="C2073_%s.fits"
        self.setup2()

class CommCase2074(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2074_%s.fits"
        self.setup2()

class CommCase2075(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2075_%s.fits"
        self.setup2()

class CommCase2076(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f606w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2076_%s.fits"
        self.setup2()

class CommCase2077(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2077_%s.fits"
        self.setup2()

class CommCase2078(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2078_%s.fits"
        self.setup2()

class CommCase2079(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f621m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2079_%s.fits"
        self.setup2()

class CommCase2080(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2080_%s.fits"
        self.setup2()

class CommCase2081(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2081_%s.fits"
        self.setup2()

class CommCase2082(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f625w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2082_%s.fits"
        self.setup2()

class CommCase2083(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2083_%s.fits"
        self.setup2()

class CommCase2084(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2084_%s.fits"
        self.setup2()

class CommCase2085(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f631n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2085_%s.fits"
        self.setup2()

class CommCase2086(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2086_%s.fits"
        self.setup2()

class CommCase2087(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2087_%s.fits"
        self.setup2()

class CommCase2088(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f645n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2088_%s.fits"
        self.setup2()

class CommCase2089(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2089_%s.fits"
        self.setup2()

class CommCase2090(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2090_%s.fits"
        self.setup2()

class CommCase2091(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f656n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2091_%s.fits"
        self.setup2()

class CommCase2092(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2092_%s.fits"
        self.setup2()

class CommCase2093(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2093_%s.fits"
        self.setup2()

class CommCase2094(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f657n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2094_%s.fits"
        self.setup2()

class CommCase2095(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2095_%s.fits"
        self.setup2()

class CommCase2096(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2096_%s.fits"
        self.setup2()

class CommCase2097(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f658n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2097_%s.fits"
        self.setup2()

class CommCase2098(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2098_%s.fits"
        self.setup2()

class CommCase2099(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2099_%s.fits"
        self.setup2()

class CommCase2100(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f665n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2100_%s.fits"
        self.setup2()

class CommCase2101(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2101_%s.fits"
        self.setup2()

class CommCase2102(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2102_%s.fits"
        self.setup2()

class CommCase2103(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f673n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2103_%s.fits"
        self.setup2()

class CommCase2104(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2104_%s.fits"
        self.setup2()

class CommCase2105(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2105_%s.fits"
        self.setup2()

class CommCase2106(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f680n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2106_%s.fits"
        self.setup2()

class CommCase2107(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2107_%s.fits"
        self.setup2()

class CommCase2108(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2108_%s.fits"
        self.setup2()

class CommCase2109(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f689m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2109_%s.fits"
        self.setup2()

class CommCase2110(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2110_%s.fits"
        self.setup2()

class CommCase2111(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2111_%s.fits"
        self.setup2()

class CommCase2112(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f763m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2112_%s.fits"
        self.setup2()

class CommCase2113(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2113_%s.fits"
        self.setup2()

class CommCase2114(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2114_%s.fits"
        self.setup2()

class CommCase2115(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f775w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2115_%s.fits"
        self.setup2()

class CommCase2116(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2116_%s.fits"
        self.setup2()

class CommCase2117(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2117_%s.fits"
        self.setup2()

class CommCase2118(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2118_%s.fits"
        self.setup2()

class CommCase2119(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2119_%s.fits"
        self.setup2()

class CommCase2120(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2120_%s.fits"
        self.setup2()

class CommCase2121(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2121_%s.fits"
        self.setup2()

class CommCase2122(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2122_%s.fits"
        self.setup2()

class CommCase2123(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2123_%s.fits"
        self.setup2()

class CommCase2124(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2124_%s.fits"
        self.setup2()

class CommCase2125(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2125_%s.fits"
        self.setup2()

class CommCase2126(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2126_%s.fits"
        self.setup2()

class CommCase2127(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2127_%s.fits"
        self.setup2()

class CommCase2128(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2128_%s.fits"
        self.setup2()

class CommCase2129(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2129_%s.fits"
        self.setup2()

class CommCase2130(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2130_%s.fits"
        self.setup2()

class CommCase2131(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2131_%s.fits"
        self.setup2()

class CommCase2132(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2132_%s.fits"
        self.setup2()

class CommCase2133(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2133_%s.fits"
        self.setup2()

class CommCase2134(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2134_%s.fits"
        self.setup2()

class CommCase2135(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2135_%s.fits"
        self.setup2()

class CommCase2136(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2136_%s.fits"
        self.setup2()

class CommCase2137(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2137_%s.fits"
        self.setup2()

class CommCase2138(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2138_%s.fits"
        self.setup2()

class CommCase2139(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2139_%s.fits"
        self.setup2()

class CommCase2140(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2140_%s.fits"
        self.setup2()

class CommCase2141(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2141_%s.fits"
        self.setup2()

class CommCase2142(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2142_%s.fits"
        self.setup2()

class CommCase2143(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2143_%s.fits"
        self.setup2()

class CommCase2144(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2144_%s.fits"
        self.setup2()

class CommCase2145(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2145_%s.fits"
        self.setup2()

class CommCase2146(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2146_%s.fits"
        self.setup2()

class CommCase2147(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2147_%s.fits"
        self.setup2()

class CommCase2148(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2148_%s.fits"
        self.setup2()

class CommCase2149(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2149_%s.fits"
        self.setup2()

class CommCase2150(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2150_%s.fits"
        self.setup2()

class CommCase2151(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2151_%s.fits"
        self.setup2()

class CommCase2152(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2152_%s.fits"
        self.setup2()

class CommCase2153(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2153_%s.fits"
        self.setup2()

class CommCase2154(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2154_%s.fits"
        self.setup2()

class CommCase2155(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2155_%s.fits"
        self.setup2()

class CommCase2156(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2156_%s.fits"
        self.setup2()

class CommCase2157(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2157_%s.fits"
        self.setup2()

class CommCase2158(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2158_%s.fits"
        self.setup2()

class CommCase2159(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2159_%s.fits"
        self.setup2()

class CommCase2160(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2160_%s.fits"
        self.setup2()

class CommCase2161(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2161_%s.fits"
        self.setup2()

class CommCase2162(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2162_%s.fits"
        self.setup2()

class CommCase2163(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2163_%s.fits"
        self.setup2()

class CommCase2164(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2164_%s.fits"
        self.setup2()

class CommCase2165(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2165_%s.fits"
        self.setup2()

class CommCase2166(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2166_%s.fits"
        self.setup2()

class CommCase2167(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2167_%s.fits"
        self.setup2()

class CommCase2168(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2168_%s.fits"
        self.setup2()

class CommCase2169(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2169_%s.fits"
        self.setup2()

class CommCase2170(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2170_%s.fits"
        self.setup2()

class CommCase2171(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2171_%s.fits"
        self.setup2()

class CommCase2172(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2172_%s.fits"
        self.setup2()

class CommCase2173(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2173_%s.fits"
        self.setup2()

class CommCase2174(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2174_%s.fits"
        self.setup2()

class CommCase2175(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2175_%s.fits"
        self.setup2()

class CommCase2176(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2176_%s.fits"
        self.setup2()

class CommCase2177(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2177_%s.fits"
        self.setup2()

class CommCase2178(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2178_%s.fits"
        self.setup2()

class CommCase2179(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2179_%s.fits"
        self.setup2()

class CommCase2180(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2180_%s.fits"
        self.setup2()

class CommCase2181(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2181_%s.fits"
        self.setup2()

class CommCase2182(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2182_%s.fits"
        self.setup2()

class CommCase2183(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2183_%s.fits"
        self.setup2()

class CommCase2184(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2184_%s.fits"
        self.setup2()

class CommCase2185(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2185_%s.fits"
        self.setup2()

class CommCase2186(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2186_%s.fits"
        self.setup2()

class CommCase2187(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2187_%s.fits"
        self.setup2()

class CommCase2188(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2188_%s.fits"
        self.setup2()

class CommCase2189(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2189_%s.fits"
        self.setup2()

class CommCase2190(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f814w"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2190_%s.fits"
        self.setup2()

class CommCase2191(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2191_%s.fits"
        self.setup2()

class CommCase2192(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2192_%s.fits"
        self.setup2()

class CommCase2193(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f845m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2193_%s.fits"
        self.setup2()

class CommCase2194(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2194_%s.fits"
        self.setup2()

class CommCase2195(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2195_%s.fits"
        self.setup2()

class CommCase2196(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        self.fname="C2196_%s.fits"
        self.setup2()

class CommCase2197(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        self.fname="C2197_%s.fits"
        self.setup2()

class CommCase2198(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        self.fname="C2198_%s.fits"
        self.setup2()

class CommCase2199(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2199_%s.fits"
        self.setup2()

class CommCase2200(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2200_%s.fits"
        self.setup2()

class CommCase2201(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2201_%s.fits"
        self.setup2()

class CommCase2202(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f850lp"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2202_%s.fits"
        self.setup2()

class CommCase2203(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2203_%s.fits"
        self.setup2()

class CommCase2204(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2204_%s.fits"
        self.setup2()

class CommCase2205(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,f953n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2205_%s.fits"
        self.setup2()

class CommCase2206(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2206_%s.fits"
        self.setup2()

class CommCase2207(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2207_%s.fits"
        self.setup2()

class CommCase2208(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq232n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2208_%s.fits"
        self.setup2()

class CommCase2209(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2209_%s.fits"
        self.setup2()

class CommCase2210(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2210_%s.fits"
        self.setup2()

class CommCase2211(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq243n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2211_%s.fits"
        self.setup2()

class CommCase2212(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2212_%s.fits"
        self.setup2()

class CommCase2213(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2213_%s.fits"
        self.setup2()

class CommCase2214(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq378n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2214_%s.fits"
        self.setup2()

class CommCase2215(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2215_%s.fits"
        self.setup2()

class CommCase2216(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2216_%s.fits"
        self.setup2()

class CommCase2217(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq387n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2217_%s.fits"
        self.setup2()

class CommCase2218(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2218_%s.fits"
        self.setup2()

class CommCase2219(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2219_%s.fits"
        self.setup2()

class CommCase2220(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq422m"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2220_%s.fits"
        self.setup2()

class CommCase2221(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2221_%s.fits"
        self.setup2()

class CommCase2222(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2222_%s.fits"
        self.setup2()

class CommCase2223(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq436n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2223_%s.fits"
        self.setup2()

class CommCase2224(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2224_%s.fits"
        self.setup2()

class CommCase2225(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2225_%s.fits"
        self.setup2()

class CommCase2226(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq437n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2226_%s.fits"
        self.setup2()

class CommCase2227(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2227_%s.fits"
        self.setup2()

class CommCase2228(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2228_%s.fits"
        self.setup2()

class CommCase2229(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq492n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2229_%s.fits"
        self.setup2()

class CommCase2230(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2230_%s.fits"
        self.setup2()

class CommCase2231(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2231_%s.fits"
        self.setup2()

class CommCase2232(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq508n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2232_%s.fits"
        self.setup2()

class CommCase2233(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2233_%s.fits"
        self.setup2()

class CommCase2234(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2234_%s.fits"
        self.setup2()

class CommCase2235(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq575n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2235_%s.fits"
        self.setup2()

class CommCase2236(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2236_%s.fits"
        self.setup2()

class CommCase2237(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2237_%s.fits"
        self.setup2()

class CommCase2238(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq619n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2238_%s.fits"
        self.setup2()

class CommCase2239(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2239_%s.fits"
        self.setup2()

class CommCase2240(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2240_%s.fits"
        self.setup2()

class CommCase2241(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq634n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2241_%s.fits"
        self.setup2()

class CommCase2242(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2242_%s.fits"
        self.setup2()

class CommCase2243(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2243_%s.fits"
        self.setup2()

class CommCase2244(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq672n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2244_%s.fits"
        self.setup2()

class CommCase2245(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2245_%s.fits"
        self.setup2()

class CommCase2246(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2246_%s.fits"
        self.setup2()

class CommCase2247(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq674n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2247_%s.fits"
        self.setup2()

class CommCase2248(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2248_%s.fits"
        self.setup2()

class CommCase2249(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2249_%s.fits"
        self.setup2()

class CommCase2250(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq727n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2250_%s.fits"
        self.setup2()

class CommCase2251(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2251_%s.fits"
        self.setup2()

class CommCase2252(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2252_%s.fits"
        self.setup2()

class CommCase2253(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq750n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2253_%s.fits"
        self.setup2()

class CommCase2254(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2254_%s.fits"
        self.setup2()

class CommCase2255(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2255_%s.fits"
        self.setup2()

class CommCase2256(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq889n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2256_%s.fits"
        self.setup2()

class CommCase2257(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2257_%s.fits"
        self.setup2()

class CommCase2258(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2258_%s.fits"
        self.setup2()

class CommCase2259(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq906n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2259_%s.fits"
        self.setup2()

class CommCase2260(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2260_%s.fits"
        self.setup2()

class CommCase2261(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2261_%s.fits"
        self.setup2()

class CommCase2262(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq924n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2262_%s.fits"
        self.setup2()

class CommCase2263(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        self.fname="C2263_%s.fits"
        self.setup2()

class CommCase2264(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        self.fname="C2264_%s.fits"
        self.setup2()

class CommCase2265(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,fq937n"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2265_%s.fits"
        self.setup2()

class CommCase2266(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        self.fname="C2266_%s.fits"
        self.setup2()

class CommCase2267(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        self.fname="C2267_%s.fits"
        self.setup2()

class CommCase2268(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        self.fname="C2268_%s.fits"
        self.setup2()

class CommCase2269(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        self.fname="C2269_%s.fits"
        self.setup2()

class CommCase2270(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        self.fname="C2270_%s.fits"
        self.setup2()

class CommCase2271(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        self.fname="C2271_%s.fits"
        self.setup2()

class CommCase2272(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        self.fname="C2272_%s.fits"
        self.setup2()

class CommCase2273(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        self.fname="C2273_%s.fits"
        self.setup2()

class CommCase2274(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        self.fname="C2274_%s.fits"
        self.setup2()

class CommCase2275(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        self.fname="C2275_%s.fits"
        self.setup2()

class CommCase2276(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        self.fname="C2276_%s.fits"
        self.setup2()

class CommCase2277(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        self.fname="C2277_%s.fits"
        self.setup2()

class CommCase2278(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        self.fname="C2278_%s.fits"
        self.setup2()

class CommCase2279(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        self.fname="C2279_%s.fits"
        self.setup2()

class CommCase2280(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        self.fname="C2280_%s.fits"
        self.setup2()

class CommCase2281(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        self.fname="C2281_%s.fits"
        self.setup2()

class CommCase2282(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        self.fname="C2282_%s.fits"
        self.setup2()

class CommCase2283(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        self.fname="C2283_%s.fits"
        self.setup2()

class CommCase2284(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2284_%s.fits"
        self.setup2()

class CommCase2285(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2285_%s.fits"
        self.setup2()

class CommCase2286(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2286_%s.fits"
        self.setup2()

class CommCase2287(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2287_%s.fits"
        self.setup2()

class CommCase2288(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2288_%s.fits"
        self.setup2()

class CommCase2289(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2289_%s.fits"
        self.setup2()

class CommCase2290(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2290_%s.fits"
        self.setup2()

class CommCase2291(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        self.fname="C2291_%s.fits"
        self.setup2()

class CommCase2292(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        self.fname="C2292_%s.fits"
        self.setup2()

class CommCase2293(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        self.fname="C2293_%s.fits"
        self.setup2()

class CommCase2294(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2294_%s.fits"
        self.setup2()

class CommCase2295(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        self.fname="C2295_%s.fits"
        self.setup2()

class CommCase2296(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        self.fname="C2296_%s.fits"
        self.setup2()

class CommCase2297(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        self.fname="C2297_%s.fits"
        self.setup2()

class CommCase2298(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        self.fname="C2298_%s.fits"
        self.setup2()

class CommCase2299(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        self.fname="C2299_%s.fits"
        self.setup2()

class CommCase2300(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280"
        self.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        self.fname="C2300_%s.fits"
        self.setup2()

class CommCase2301(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2301_%s.fits"
        self.setup2()

class CommCase2302(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2302_%s.fits"
        self.setup2()

class CommCase2303(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2303_%s.fits"
        self.setup2()

class CommCase2304(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2304_%s.fits"
        self.setup2()

class CommCase2305(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2305_%s.fits"
        self.setup2()

class CommCase2306(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2306_%s.fits"
        self.setup2()

class CommCase2307(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2307_%s.fits"
        self.setup2()

class CommCase2308(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2308_%s.fits"
        self.setup2()

class CommCase2309(conv_base.ParentCase):
    def setUp(self):
        self.obsmode="wfc3,uvis2,g280,bkg"
        self.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        self.fname="C2309_%s.fits"
        self.setup2()




if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
