from pysynphot import etc
import sys,os

def run(cmdfile):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    pattern="""class %sCase%d(basecase.%sCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.setglobal(__file__)
        self.runpy()\n"""
    f=open(cmdfile)
    out=open(cmdfile.replace('.txt','.py'),'w')
    out.write("""from pytools import testutil
import sys
import basecase
""")


    count={'countrate':0,'calcspec':0,'calcphot':0,'SpecSourcerateSpec':0,'thermback':0}
    dupcatcher={}
    dupcounter={'countrate':0,'calcspec':0,'calcphot':0,'SpecSourcerateSpec':0,'thermback':0}
    for line in f:
    
    #parse the line
        parts=line.split('&')
        cmd=(parts[0])[1:] #strip off leading quote
        count[cmd]+=1
        kwd=etc.getparms(parts[1:])
        

        #do the substitutions
        try:
           obsmode=kwd['instrument']
        except KeyError:
           obsmode=kwd.get('obsmode','None')

        #fix the CDBS specification
        try:
            kwd['spectrum']=kwd['spectrum'].replace('/cdbs',os.environ['PYSYN_CDBS'])
        except KeyError:
            kwd['spectrum']=None
            
        defn=pattern%(cmd,count[cmd],cmd,obsmode,kwd['spectrum'])
        ktuple=(cmd,obsmode,kwd['spectrum'])
        
        if ktuple in dupcatcher:
           dupcounter[cmd]+=1
        else:
           casename="%sCase%d"%(cmd,count[cmd])
           dupcatcher[ktuple]=casename
           out.write(defn)


    out.write("""\n\n
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
""")

    f.close()

    for k in count:
        total= "%s:%d-%d=%d\n"%(k,count[k],dupcounter[k],count[k]-dupcounter[k])
        sys.stdout.write(total)
        out.write(total)
    out.close()

if __name__ == '__main__':
    run(sys.argv[1])
