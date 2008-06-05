#! /bin/csh
# Pull only the pysynphot commands out of an ETC logfile
# *** Run this first, then run the resulting .txt file through
# *** gencases.py.
#.....................................................................
if ( "$1" == "" ) then
  echo -n "Enter filename: "
  set fname = $<
else
  set fname = $1
endif

set outname=`echo $fname | sed 's/\.log$/.txt/'  ` 
grep command $fname | awk '{print $4}' > $outname
