#! /bin/csh
# Parse the new logfile
python ../parselog.py nicmosPysynphotLog_13oct.txt 
#Remove thermback cases from the new logfile
grep -v thermback nicmosPysynphotLog_13oct_parsed.txt > nicmos_etc_cases_13oct_parsed.txt
grep thermback nicmosPysynphotLog_13oct_parsed.txt > nicmos_etc_thermback_cases_13oct_parsed.txt
#Non-thermback first:
echo "*******  nicmos_etc_cases  *******"
#Create the pickled dictionary from the original set
echo "# Original non-thermback"
python ../gencases.py nicmos_etc_cases.txt
#Link/rename things
#link new name to old-ish name
ln -s nicmos_etc_cases_13oct_parsed.txt nicmos_etc_cases_parsed.txt
ln -s nicmos_etc_cases.pickle nicmos_etc_cases_parsed.pickle
#Generate from the new logfile
echo ""
echo "# New non-thermback"
python ../gencases.py nicmos_etc_cases_parsed.txt nicmos_etc_cases_subset.txt
#
# Now the thermback cases. 
echo "*******  nicmos_etc_thermback_cases  *********"
#Create the pickled dictionary from the original set
echo "# Original thermback"
python ../gencases.py nicmos_etc_thermback_cases.txt
#Link/rename things
ln -s nicmos_etc_thermback_cases_13oct_parsed.txt nicmos_etc_thermback_cases_parsed.txt
ln -s nicmos_etc_thermback_cases.pickle nicmos_etc_thermback_cases_parsed.pickle
#Generate from the new logfile.
#Subset info is in the same main subset file.
echo ""
echo "# New thermback"
python ../gencases.py nicmos_etc_thermback_cases_parsed.txt nicmos_etc_cases_subset.txt
