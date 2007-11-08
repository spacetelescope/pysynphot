"""Initial test-running script for pysynphot.
 -->> *** You must set PYSYN_CDBS and PYSYN_USERDATA for these tests to run!!
 -->> *** Stdout and Stderr from this script should be piped to a log file.
"""

import sys, os, time
from pytools import testutil

#=====================================================
#           CONFIGURE TESTS HERE
#=====================================================
tlist=['newobs_cases']
#       'cos_etc_test',
#       'cos_fuv_cases',
#       'cos_nuv_cases']
#=====================================================

#Doublecheck environment
for symbol in ('PYSYN_CDBS','PYSYN_USERDATA'):
    if symbol not in os.environ:
        raise EnvironmentError("%s must be set to run these tests"%symbol)

#open the summary file
now=time.gmtime()
fname='%s_%s_%s_%s_%s_%s'%(now.tm_year,now.tm_mon,now.tm_mday,
                           now.tm_hour,now.tm_min,'pysyn_summary.log')
fh=open(fname,'w')

#Run the tests
failed=0
summary=[]
for tname in tlist:
    result=testutil.testall(tname)
    fh.write("%s: %s\n"%(tname,str(result)))
    fh.flush()
    if (len(result.errors) > 0) or (len(result.failures) > 0):
        failed=1

#Clean up & go home
fh.close()
sys.exit(failed)

