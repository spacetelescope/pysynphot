import os

    
#Replace cdbs_roots lookup with an environment variable
rootdir   = os.environ['PYSYN_CDBS']

#Data directory is now installed locally
specdir   = os.path.join(os.path.dirname(__file__),'data')+os.path.sep

#Eliminate use of temporary directory; use python tmpfile utilities instead

CAT_TEMPLATE = os.path.join(rootdir,'grid','*','catalog.fits')
KUR_TEMPLATE = os.path.join(rootdir,'grid','*')


VegaFile = os.path.join(specdir,'vega.fits')


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

    convertdic = {'crrefer':rootdir,
                  'crotacomp':os.path.join(rootdir,'comp','ota'),
                  'cracscomp':os.path.join(rootdir,'comp','acs'),
                  'crcalobs':os.path.join(rootdir,'calobs'),
                  'crcalspec':os.path.join(rootdir,'calspec'),
                  'croldcalspec':os.path.join(rootdir,'oldcalspec'),
                  'crcomp':os.path.join(rootdir,'comp'),
                  'crfgs':os.path.join(rootdir,'fgs'),
                  'crfields':os.path.join(rootdir,'fields'),
                  'crmodewave':os.path.join(rootdir,'modewave'),
                  'crcostarcomp':os.path.join(rootdir,'comp','costar'),
                  'cracscomp':os.path.join(rootdir,'comp','acs'),
                  'crfoccomp':os.path.join(rootdir,'comp','foc'),
                  'crfoscomp':os.path.join(rootdir,'comp','fos'),
                  'crfgscomp':os.path.join(rootdir,'comp','fgs'),
                  'crhrscomp':os.path.join(rootdir,'comp','hrs'),
                  'crhspcomp':os.path.join(rootdir,'comp','hsp'),
                  'crotacomp':os.path.join(rootdir,'comp','ota'),
                  'crnicmoscomp':os.path.join(rootdir,'comp','nicmos'),
                  'crnonhstcomp':os.path.join(rootdir,'comp','nonhst'),
                  'crstiscomp':os.path.join(rootdir,'comp','stis'),
                  'crstiscomp':os.path.join(rootdir,'comp','stis'),
                  'crwfc3comp':os.path.join(rootdir,'comp','wfc3'),
                  'crcoscomp':os.path.join(rootdir,'comp','cos'),
                  'coscomp':os.path.join(rootdir,'comp','cos'),
                  'crwave':os.path.join(rootdir,'crwave'),
                  'crwfpccomp':os.path.join(rootdir,'comp','wfpc'),
                  'crwfpc2comp':os.path.join(rootdir,'comp','wfpc2'),
                  'crgrid':os.path.join(rootdir,'grid'),
                  'crgridbz77':os.path.join(rootdir,'grid','bz77'),
                  'crgridgs':os.path.join(rootdir,'grid','gunnstryker'),
                  'crgridjac':os.path.join(rootdir,'grid','jacobi'),
                  'crgridbpgs':os.path.join(rootdir,'grid','bpgs'),
                  'crgridbk':os.path.join(rootdir,'grid','bkmodels'),
                  'crgridk93':os.path.join(rootdir,'grid','k93models'),
                  'crgridagn':os.path.join(rootdir,'grid','agn'),
                  'crgridgalactic':os.path.join(rootdir,'grid','galactic'),
                  'crgridkc96':os.path.join(rootdir,'grid','kc96'),
                  'synphot': os.path.dirname(__file__)+os.path.sep}

    ## If no $ sign found, just return the filename unchanged
    if '$' in iraffilename:
        irafdir,basename=iraffilename.split('$')
        unixdir=convertdic[irafdir]
        unixfilename=os.path.join(unixdir,basename)
        return unixfilename
    else:
        return iraffilename
