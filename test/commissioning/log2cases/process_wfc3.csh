#! /bin/csh 
#First do the non-IR cases
echo "### WFC3 UVIS1 Imaging"
#Create the pickled dictionary from the original set
echo "# Original"
python ../gencases.py wfc3_uvis1_imaging_61_cases.txt
#Parse the new logfile
python ../parselog.py wfc3UVIS1ImagingPysynphotLog.txt

#Link/rename things
ln -s wfc3UVIS1ImagingPysynphotLog_parsed.txt wfc3_uvis1_imaging_61_cases_parsed.txt
ln -s wfc3_uvis1_imaging_61_cases.pickle wfc3_uvis1_imaging_61_cases_parsed.pickle
#Generate from the new logfile
echo "# New"
python ../gencases.py wfc3_uvis1_imaging_61_cases_parsed.txt wfc3_uvis1_imaging_61_cases_subset.txt


#####################
echo "### WFC3 UVIS2 Imaging"
#Create the pickled dictionary from the original set
echo "# Original"
python ../gencases.py wfc3_uvis2_imaging_18_cases.txt
#Parse the new logfile
python ../parselog.py wfc3UVIS2ImagingPysynphotLog.txt

#Link/rename things
ln -s wfc3UVIS2ImagingPysynphotLog_parsed.txt wfc3_uvis2_imaging_18_cases_parsed.txt
ln -s wfc3_uvis2_imaging_18_cases.pickle wfc3_uvis2_imaging_18_cases_parsed.pickle
#Generate from the new logfile
echo "# New"
python ../gencases.py wfc3_uvis2_imaging_18_cases_parsed.txt wfc3_uvis2_imaging_18_cases_subset.txt

#########################
echo "### WFC3 UVIS1 Spec"
#Create the pickled dictionary from the original set
echo "# Original"
python ../gencases.py wfc3_uvis1_spec_62_cases.txt
#Parse the new logfile
python ../parselog.py wfc3UVIS1SpecPysynphotLog.txt

#Link/rename things
ln -s wfc3UVIS1SpecPysynphotLog_parsed.txt wfc3_uvis1_spec_62_cases_parsed.txt
ln -s wfc3_uvis1_spec_62_cases.pickle wfc3_uvis1_spec_62_cases_parsed.pickle
#Generate from the new logfile
echo "# New"
python ../gencases.py wfc3_uvis1_spec_62_cases_parsed.txt wfc3_uvis1_spec_62_cases_subset.txt

#######################
echo "### WFC3 UVIS2 Spec"
#Create the pickled dictionary from the original set
echo "# Original"
python ../gencases.py wfc3_uvis2_spec_18_cases.txt
#Parse the new logfile
python ../parselog.py wfc3UVIS2SpecPysynphotLog.txt

#Link/rename things
ln -s wfc3UVIS2SpecPysynphotLog_parsed.txt wfc3_uvis2_spec_18_cases_parsed.txt
ln -s wfc3_uvis2_spec_18_cases.pickle wfc3_uvis2_spec_18_cases_parsed.pickle
#Generate from the new logfile
echo "# New"
python ../gencases.py wfc3_uvis2_spec_18_cases_parsed.txt wfc3_uvis2_spec_18_cases_subset.txt

#############################
#Now do the IR cases, which will be harder.
echo "### WFC3 IR Imaging"
#
# Parse the new logfile
python ../parselog.py wfc3IRImagingPysynphotLog.txt
#Remove thermback cases from the new logfile
grep -v thermback  wfc3IRImagingPysynphotLog_parsed.txt > wfc3_irim_cases_parsed.txt
grep thermback  wfc3IRImagingPysynphotLog_parsed.txt > wfc3_irim_thermback_parsed.txt

#Non-thermback first:
echo "*******  wfc3_ir_imaging_cases  *******"
#Create the pickled dictionary from the original set
echo "# Original non-thermback"
python ../gencases.py wfc3_ir_imaging_78_cases.txt
#Link/rename things
#link new name to old-ish name
ln -s wfc3_irim_cases_parsed.txt wfc3_ir_imaging_78_cases_parsed.txt
ln -s wfc3_irim_cases_parsed.pickle wfc3_ir_imaging_78_cases_parsed.pickle
#Generate from the new logfile
echo "# New non-thermback"
python ../gencases.py wfc3_ir_imaging_78_cases_parsed.txt wfc3_ir_imaging_78_cases_subset.txt
#
# Now the thermback cases. 
echo "*******  wfc3_ir_imaging_thermback *********"
#Create the pickled dictionary from the original set
echo "# Original thermback"
python ../gencases.py wfc3_ir_imaging_80_thermback.txt 
#Link/rename things
#link new name to old-ish name
ln -s wfc3_irim_thermback_parsed.txt wfc3_ir_imaging_80_thermback_parsed.txt
ln -s wfc3_irim_thermback_parsed.pickle wfc3_ir_imaging_80_thermback_parsed.pickle
#Generate from the new logfile.
echo "# New thermback"
python ../gencases.py wfc3_ir_imaging_80_thermback_parsed.txt wfc3_ir_imaging_80_thermback_subset.txt


#############################
echo "### WFC3 IR Spec"
#
# Parse the new logfile
python ../parselog.py wfc3IRSpecPysynphotLog.txt
#Remove thermback cases from the new logfile
grep -v thermback  wfc3IRSpecPysynphotLog_parsed.txt > wfc3_irsp_cases_parsed.txt
grep thermback  wfc3IRSpecPysynphotLog_parsed.txt > wfc3_irsp_thermback_parsed.txt

#Non-thermback first:
echo "*******  wfc3_ir_spec_cases  *******"
#Create the pickled dictionary from the original set
echo "# Original non-thermback"
python ../gencases.py wfc3_ir_spec_61_cases.txt
#Link/rename things
#link new name to old-ish name
ln -s wfc3_irsp_cases_parsed.txt wfc3_ir_spec_61_cases_parsed.txt
ln -s wfc3_irsp_cases_parsed.pickle wfc3_ir_spec_61_cases_parsed.pickle
#Generate from the new logfile
echo "# New non-thermback"
python ../gencases.py wfc3_ir_spec_61_cases_parsed.txt wfc3_ir_spec_61_cases_subset.txt
#
# Now the thermback cases. 
echo "*******  wfc3_ir_spec_thermback *********"
#Create the pickled dictionary from the original set
echo "# Original thermback"
python ../gencases.py wfc3_ir_spec_62_thermback.txt 
#Link/rename things
#link new name to old-ish name
ln -s wfc3_irsp_thermback_parsed.txt wfc3_ir_spec_62_thermback_parsed.txt
ln -s wfc3_irsp_thermback_parsed.pickle wfc3_ir_spec_62_thermback_parsed.pickle
#Generate from the new logfile. There are no subsets for this class.
echo "# New thermback"
python ../gencases.py wfc3_ir_spec_62_thermback_parsed.txt 
