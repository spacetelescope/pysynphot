#! /bin/csh
#Create the pickled dictionary from the original set
echo "# Original"
python gencases.py stis_etc_cases.txt
#Parse the new logfile
python parselog.py stisPysynphotLog_9oct.txt
#Link/rename things
ln -s stisPysynphotLog_9oct_parsed.txt stis_etc_cases_parsed.txt
ln -s stis_etc_cases.pickle stis_etc_cases_parsed.pickle
#Generate from the new logfile
echo "# New"
python gencases.py stis_etc_cases_parsed.txt stis_etc_cases_subset.txt
