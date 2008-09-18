from pysynphot import etc
import sys,os

def run(cmdfile,subsetfile=None):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    #Define the test case pattern
    pattern="""class %sCase%d(basecase.%sCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.subset=%s
        self.setglobal(__file__)
        self.runpy()\n"""

    #Process the subsetfile if present
    subsetflag={}
    if subsetfile is not None:
        #Then this file contains a list of case names that should have a
        #subset flag set.
        f=open(subsetfile)
        for line in f:
            if not line.startswith('#') and len(line.strip())>0:
                cols=line.strip().split()
                subsetflag[cols[0]]=True
        f.close()

    #Open the main input and output files
    f=open(cmdfile)
    out=open(cmdfile.replace('.txt','.py'),'w')
    out.write("""from pytools import testutil
import sys
import basecase
""")

    #Set up some bookkeeping
    count={'countrate':0,'calcspec':0,'calcphot':0,'SpecSourcerateSpec':0,'thermback':0}
    dupcatcher={}
    dupcounter={'countrate':0,'calcspec':0,'calcphot':0,'SpecSourcerateSpec':0,'thermback':0}

    #Now start the main loop
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

        #Construct the name and pattern
        casename="%sCase%d"%(cmd,count[cmd])
        ktuple=(cmd,obsmode,kwd['spectrum'])
        

        
        if ktuple in dupcatcher:
           dupcounter[cmd]+=1
           dupcatcher[ktuple].append(casename)
        else:
           dupcatcher[ktuple]=[casename]
           defn=pattern%(cmd,count[cmd],cmd,obsmode,kwd['spectrum'],subsetflag.get(casename,False))
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
        total= "#%s:%d-%d=%d\n"%(k,count[k],dupcounter[k],count[k]-dupcounter[k])
        sys.stdout.write(total)
        out.write(total)
    out.close()
    return dupcatcher

if __name__ == '__main__':
    dups = run(*sys.argv[1:])
