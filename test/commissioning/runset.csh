#! /bin/csh -x
#
# Generate a test run for all test cases, organizing the output into
# a subdirectory of the cwd.
#
# Presently hardcodes a bunch of information: where to get the test data,
# and the list of ***python modules*** that contain the tests. Uses 
# nosetests to run the tests.
#
# Accepts a run name as an argument, or prompts for one.
#.....................................................................
if ( "$1" == "" ) then
  echo -n "Enter test run name: "
  set rname = $<
else
  set rname = $1
endif

#..................................................
#Append the revision number; silly humans get it wrong
set revset = `svnversion | awk -F: '{print $2}'`
set dirname = {$rname}_r{$revset}
#...................................................
# Set up a test directory
mkdir $dirname
cd $dirname
tar -xzf /eng/ssb/syn_pysyn/testdata.tar.gz

#.........................................
# Hardcode the lists of tests for the moment.
set tlist = "acs_etc_cases nicmos_etc_cases stis_etc_cases wfc3_ir_imaging_78_cases wfc3_ir_spec_61_cases wfc3_uvis1_imaging_61_cases wfc3_uvis1_spec_62_cases wfc3_uvis2_imaging_18_cases wfc3_uvis2_spec_18_cases"

#.........................................
echo $PYTHONPATH
foreach tname ($tlist)
  echo $tname
###  nosetests $tname >& `echo "$tname" | sed 's/.py/.log/'`
  nosetests $tname >& $tname.log
end
