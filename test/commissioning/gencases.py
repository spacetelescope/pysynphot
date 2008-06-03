from pysynphot import newetc

def run(cmdfile):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    pattern="""class %sCase%d(%sCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.runpy()\n"""
    f=open(cmdfile)
    out=open(cmdfile.replace('.txt','.py'),'w')
    

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


        defn=pattern%(cmd,count[cmd],cmd,obsmode,kwd['spectrum'])
        out.write(defn)

    out.close()
    f.close()

    for k in count:
        print "%s:%d"%(k,count[k])
