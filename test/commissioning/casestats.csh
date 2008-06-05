#! /bin/csh
# Grep -I through the log files produced by a test run to count up
# passes, failures, and unique obsmode/spectrum combinations that
# went into each of them.
#
# First get the prefix associated with the set of tests.
# If none is supplied, prompt for one.
#.....................................................................
if ( "$1" == "" ) then
  echo -n "Enter test run prefix: "
  set idstring = $<
else
  set idstring = $1
endif
#
#Collect stats from the full set
set ntests = `ls -1 $idstring*.log | wc -l`
set ncases = `ls $idstring*Case*.log | awk -F . '{print $3}' | sort -u | wc -l`
set nobs=`grep da_obs $idstring*.log | awk '{print $2}' | sort -u | wc -l`
set nspec=`grep da_spec $idstring*.log | awk '{print $2}' | sort -u | wc -l`
echo Test statistics for "$idstring*.log":
echo $ncases test cases
echo $ntests total tests
echo $nobs unique obsmodes
echo $nspec unique spectra
echo ================================================
#
# Work with one type of test at a time
foreach tname (`ls $idstring*.log | awk -F . '{print $4}' | sort -u`)

# Count the total number of tests
  set ntests = `ls -1 $idstring*$tname.log | wc -l`
  echo $tname : $ntests total tests
# Count the number that failed
  set files=`grep -l Status=F $idstring*$tname.log`
  set nfailed = `grep -i -l Status=F $idstring*$tname.log | wc -l` 
  echo Failed cases: $nfailed
# Count the number of unique obsmodes in the failures

  set nobs = `grep -i da_obsmode $files | awk '{print $2}' | sort -u | wc -l`
  echo Unique obsmodes: $nobs
# Count the number of unique spectra in the failures
  set nspec = `grep -i da_spectrum $files | awk '{print $2}' | sort -u | wc -l`
  echo -n Unique spectra: $nspec
  echo 
  echo -------------------------------------------------------
  echo

  end
