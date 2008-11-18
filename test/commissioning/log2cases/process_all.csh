#! /bin/csh 
setenv PYTHONPATH ../:{$PYTHONPATH}
set inst = (acs stis nicmos wfc3)
foreach k ($inst)
   echo "####### $k ########"
   process_{$k}.csh >& process_{$k}.log
   grep "^#" process_{$k}.log
end
