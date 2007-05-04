import os

    
#Replace cdbs_roots lookup with an environment variable
rootdir   = os.environ['PYSYN_CDBS']

#Data directory is now installed locally
specdir   = os.path.join(os.path.dirname(__file__),'data')+os.path.sep

#Eliminate use of temporary directory; use python tmpfile utilities instead

CAT_TEMPLATE = os.path.join(rootdir,'grid','*','catalog.fits')
KUR_TEMPLATE = os.path.join(rootdir,'grid','*')


VegaFile = os.path.join(specdir,'vega.fits')

# There are throughput files mixed with spectrum files (the ETC mixes
# then together in spectral expressions); the throughput files must
# be explictly listed here.
throughputfiles = [os.path.join(specdir,'thru.fits')] 

#Define wavecat file explicitly
wavecat = os.path.join(specdir,'wavecat.dat')

def getBandFileName(band):
    return os.path.join(specdir,band.replace(',','_')+'.fits')

def irafconvert(iraffilename):
    '''Convert the IRAF file name (in directory$file format) to its
    unix equivalent

    Input:    string iraffilename
    Output:   returns string unixfilename
              If '$' not found in the input string, just return
              the input string
              Non-string input raises an AttributeError'''
    ## This dictionary maps IRAF-specific directory names for synphot
    ## directories into their Unix equivalents.

    convertdic = {'crrefer$':rootdir,
                  'crotacomp$':rootdir+'comp/ota/',
                  'cracscomp$':rootdir+'comp/acs/',
                  'crcalobs$':rootdir+'calobs/',
                  'crcalspec$':rootdir+'calspec/',
                  'croldcalspec$':rootdir+'oldcalspec/',
                  'crcomp$':rootdir+'comp/',
                  'crfgs$':rootdir+'fgs/',
                  'crfields$':rootdir+'fields/',
                  'crmodewave$':rootdir+'modewave/',
                  'crcostarcomp$':rootdir+'comp/costar/',
                  'cracscomp$':rootdir+'comp/acs/',
                  'crfoccomp$':rootdir+'comp/foc/',
                  'crfoscomp$':rootdir+'comp/fos/',
                  'crfgscomp$':rootdir+'comp/fgs/',
                  'crhrscomp$':rootdir+'comp/hrs/',
                  'crhspcomp$':rootdir+'comp/hsp/',
                  'crotacomp$':rootdir+'comp/ota/',
                  'crnicmoscomp$':rootdir+'comp/nicmos/',
                  'crnonhstcomp$':rootdir+'comp/nonhst/',
                  'crstiscomp$':rootdir+'comp/stis/',
                  'crstiscomp$':rootdir+'comp/stis/',
                  'crwfc3comp$':rootdir+'comp/wfc3/',
                  'crcoscomp$':rootdir+'comp/cos/',
                  'coscomp$':rootdir+'comp/cos/',
                  'crwave$':rootdir+'crwave/',
                  'crwfpccomp$':rootdir+'comp/wfpc/',
                  'crwfpc2comp$':rootdir+'comp/wfpc2/',
                  'crgrid$':rootdir+'grid/',
                  'crgridbz77$':rootdir+'grid/bz77/',
                  'crgridgs$':rootdir+'grid/gunnstryker/',
                  'crgridjac$':rootdir+'grid/jacobi/',
                  'crgridbpgs$':rootdir+'grid/bpgs/',
                  'crgridbk$':rootdir+'grid/bkmodels/',
                  'crgridk93$':rootdir+'grid/k93models/',
                  'crgridagn$':rootdir+'grid/agn/',
                  'crgridgalactic$':rootdir+'grid/galactic/',
                  'crgridkc96$':rootdir+'grid/kc96/',
                  'synphot$': os.path.dirname(__file__)+os.path.sep}

    ## If no $ sign found, just return the filename unchanged
    unixfilename = iraffilename
    dollarpos = iraffilename.find('$')
    if dollarpos != -1:
        irafdir = iraffilename[:dollarpos+1].lstrip()
        unixfilename = iraffilename.replace(irafdir,convertdic[irafdir])
    return unixfilename
