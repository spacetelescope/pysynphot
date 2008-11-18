#! /bin/csh
#Create the pickled dictionary from the original set
echo "# Original"
python ../gencases.py acs_etc_cases.txt
#Parse the new logfile
python ../parselog.py acsPysynphotLog_9oct.txt
#Link/rename things
ln -s acsPysynphotLog_9oct_parsed.txt acs_etc_cases_parsed.txt
ln -s acs_etc_cases.pickle acs_etc_cases_parsed.pickle
#Generate from the new logfile
echo "# New"
python ../gencases.py acs_etc_cases_parsed.txt acs_etc_cases_subset.txt
