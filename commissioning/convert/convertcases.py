import sys,os
import sqlite3

def run(casefile,subsetfile=None, lookupfile=None):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    #Define the test case pattern
    pattern="""class CommCase%d(ParentCase):
    def setUp(self):
        self.obsmode="%s"
        self.spectrum="%s"
        self.fname="C%s_%s.fits"
        self.setup2()\n\n"""

    #Open the database
    db = sqlite3.connect("/ssbwebv1/data1/pandokia/pdk/c3/db/pdk.db")


    #Open the main output files

    out=open(casefile,'w')
    out.write("""from pytools import testutil
import sys
import basecase

""")

    count=0

    #Select unique (obsmode,spectrum) pairs from our database table of
    #commissioning tests. Sort them by obsmode.
    
    c = db.execute(""" SELECT DISTINCT obsmode, spectrum
                       FROM synpysyn
                       ORDER BY obsmode""")

    #Now loop over them, and define test cases.
    for x in c:
       obsmode, spectrum = x
       count+=1
       defn=pattern%(count,obsmode,spectrum,count,"%s")
       out.write(defn)

    out.write("""\n\n
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
""")

    out.close()



if __name__ == '__main__':
    run(*sys.argv[1:])
    
