#! /bin/csh
#To keep our namespaces, the finally-created .py files have to be
#renamed to the original scheme.
set flist = (`ls *parsed.py`)
foreach fname ($flist)
   set k = `basename $fname _parsed.py`
   cp -f $fname ../{$k}.py
end
