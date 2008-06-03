from pysynphot import newetc
import sys,os

def run(cmdfile):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    pattern="""class %sCase%d(%sCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.setglobal(__file__)
        self.runpy()\n"""
    f=open(cmdfile)
    out=open(cmdfile.replace('.txt','.py'),'w')
    out.write("""from pytools import testutil
import sys
from basecase import calcphotCase, calcspecCase, countrateCase,SpecSourcerateSpecCase\n
""")


    count={'countrate':0,'calcspec':0,'calcphot':0,'SpecSourcerateSpec':0}
    for line in f:
    
    #parse the line
        parts=line.split('&')
        cmd=(parts[0])[1:] #strip off leading quote
        count[cmd]+=1
        kwd=newetc.getparms(parts[1:])
        

        #do the substitutions
        try:
           obsmode=kwd['instrument']
        except KeyError:
           obsmode=kwd.get('obsmode','None')

        #fix the CDBS specification
        kwd['spectrum']=kwd['spectrum'].replace('/cdbs',os.environ['PYSYN_CDBS'])
        defn=pattern%(cmd,count[cmd],cmd,obsmode,kwd['spectrum'])
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
        print "%s:%d"%(k,count[k])
        out.write("# %s:%d\n"%(k,count[k]))
    out.close()

if __name__ == '__main__':
    run(sys.argv[1])
