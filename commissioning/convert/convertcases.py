import sys,os
import sqlite3

def run(casefile,subsetfile=None, lookupfile=None):
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    #Define the test case pattern
    pattern="""class CommCase%d(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="%s"
        cls.spectrum="%s"
        cls.fname="C%s_%s.fits"
        cls.setup2()\n\n"""

    #Open the database
    db = sqlite3.connect("/ssbwebv1/data1/pandokia/pdk/c3/db/pdk.db")


    #Open the main output files

    out=open(casefile,'w')
    out.write("""import sys
import conv_base

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

    out.close()



if __name__ == '__main__':
    run(*sys.argv[1:])
    
