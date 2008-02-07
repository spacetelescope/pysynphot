"""Initial test-running script for pysynphot.
 -->> *** You must set PYSYN_CDBS and PYSYN_USERDATA for these tests to run!!
 -->> *** Stdout and Stderr from this script should be piped to a log file.

Warning: PYSYN_USERDATA should not contain any hyphens ('-'). This
directory is used to construct the names of test files. The
synphot syntax parser will interpret them as a minus sign that terminates
the filename, and some tests will then have errors.
"""

import sys, os, time
from pytools import testutil

#=====================================================
#           CONFIGURE TESTS HERE
#=====================================================
tlist=['newobs_cases',
       'cos_etc_test',
       'cos_fuv_cases',
       'cos_nuv_cases',
       'ui_test',
       'other_etc_test',
       'ticket82',
       'ticket21'
       ]
#=====================================================

#Doublecheck environment
for symbol in ('PYSYN_CDBS','PYSYN_USERDATA'):
    if symbol not in os.environ:
        raise EnvironmentError("%s must be set to run these tests"%symbol)

#open the summary file
now=time.gmtime()
fname='pysyn_summary.log'
fh=open(fname,'w')
fh.write("%s\n"%time.asctime())

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

