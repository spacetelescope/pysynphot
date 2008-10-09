EXTRAP.PY

PURPOSE:
=======
This script was written to automatically force the endpoints of a 
synphot throughput file to zero. 

- it can safely be run on files that already meet this condition; it
  will detect that the file does not need to be changed.

- it can handle simple files (wavelength/throughput only),
  parameterized files (wavelength + many throughput), and simple files
  with an error column (wave, thru, error). If an error column is
  present, the error value of the extra points is set to 100. It does
  not know how to handle the case of a parameterized file with error
  columns, and will raise an exception if it encounters one.

- it automatically updates the version number in the filename and
  writes history into the primary header

FILES:
=====
This directory also contains one file of each known type that can be
used for testing:

hst_ota_007_syn.fits:      no change necessary
acs_hrc_win_005_syn.fits:  simple file
acs_sbc_aper_002_syn.fits: parameterized file
wfpc2_f814w_006_syn.fits:  simple file + error


Usage:
=====
- From the shell:
    python extrap.py *syn.fits

  The script will correctly handle the shell expansion of the
  filenames, and loop over all of them, printing the return value.

- From within python:
     import extrap
     extrap.run(fname,outdir='update')

  If run from within the python interpreter, an optional 'outdir'
  keyword can be supplied so that the new files will be written to
  this directory, which will be created if it does not already exist. 

  Typical use from the shell would include a loop:

     import glob
     flist=glob.glob('/some/dir/*_syn.fits')
     for fname in flist: 
        extrap.run(fname,outdir='other/dir/')
