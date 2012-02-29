from __future__ import division
import os, warnings, glob, re
import pyfits


def _refTable(template):
    try:
        names = glob.glob(os.path.join(os.environ['PYSYN_CDBS'], template))
        names.sort()
    except KeyError:
        warnings.warn("PYSYN_CDBS is undefined; cannot find %s file"%template,
                      UserWarning)
        return None

    try:
        return names[-1]
    except IndexError:
        msg= "No files found for %s."%os.path.join(os.environ['PYSYN_CDBS'],
                                                   template)
        raise IOError(msg)

#Replace cdbs_roots lookup with an environment variable
try:
    rootdir = os.environ['PYSYN_CDBS']
except KeyError:
    warnings.warn("PYSYN_CDBS is undefined; functionality will be SEVERELY crippled.",UserWarning)
    rootdir = ''

#Data directory is now installed locally
specdir   = os.path.join(os.path.dirname(__file__),'data')+os.path.sep

#Eliminate use of temporary directory; use python tmpfile utilities instead

CAT_TEMPLATE = os.path.join(rootdir,'grid','*','catalog.fits')
KUR_TEMPLATE = os.path.join(rootdir,'grid','*')

#Vega
VegaFile = os.path.join(specdir,'alpha_lyr_stis_005.fits')


extdir = os.path.join('grid','extinction')
RedLaws = {}

def _get_RedLaws():
    global RedLaws

    # get all the fits files in $PYSYN_CDBS/grid/extinction/
    globstr = os.path.join(rootdir,extdir,'*.fits')
    files = glob.glob(globstr)

    # replace ###.fits at the end of file names with *.fits
    # and get a unique set
    files = set([f[:-8] + '*.fits' for f in files])

    # use _refTable to get the most recent version of each extinction file
    # and add that to the RedLaws dict
    for f in files:
        lawf = _refTable(f)

        key = pyfits.getval(lawf,'shortnm')

        RedLaws[key.lower()] = lawf

# load the extintion law file names
_get_RedLaws()

#RedLaws={'mwavg':   'milkyway_diffuse_*.fits',
#         'mwdense': 'milkyway_dense_*.fits',
#         'lmcavg':  'lmc_diffuse_*.fits',
#         'lmc30dor':'lmc_30dorshell_*.fits',
#         'smcbar':  'smc_bar_*.fits',
#         'xgalsb':  'xgal_starburst_*.fits'
#           }
#
#for k in RedLaws:
#    try:
#        RedLaws[k]=_refTable(os.path.join(extdir,RedLaws[k]))
#    except IOError,e:
#        print 'Cannot open %s: %s'%(RedLaws[k],str(e))


#Define wavecat file explicitly
wavecat = os.path.join(specdir,'wavecat.dat')

## This dictionary maps IRAF-specific directory names for synphot
## directories into their Unix equivalents.

#BUG: supports only a single variable in a string
#............basically this is a weak routine that should be made
#............more robust
#BUG: this dictionary should be in a data file
CONVERTDICT = {'crrefer':rootdir,
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
              'mtab':os.path.join(rootdir,'mtab'),
              'synphot': os.path.dirname(__file__) + os.path.sep,
              # PATH for JWST instrument files
              'crjwstotecomp':os.path.join(rootdir,'comp','jwstote'),
              # PATH for JWST MIRI instrument files
              'crmiricomp':os.path.join(rootdir,'comp','miri'),
              # PATH for JWST NIRCam instrument files
              'crnircamcomp':os.path.join(rootdir,'comp','nircam'),
              # PATH for JWST NIRSpec instrument files
              'crnirspeccomp':os.path.join(rootdir,'comp','nirspec'),
              }

def irafconvert(iraffilename):
    '''Convert the IRAF file name (in directory$file format) to its
    unix equivalent

    Input:    string iraffilename
    Output:   returns string unixfilename
          If '$' not found in the input string, just return
          the input string
          Non-string input raises an AttributeError'''
    convertdict = CONVERTDICT

    # remove duplicate separators and extraneous relative paths
    iraffilename = os.path.normpath(iraffilename)

    #BUG: supports environment variables only as the leading element in the
    #     filename
    if iraffilename.startswith('$'):
        #Then this is an environment variable.
        #Use a regex to pull off the front piece.
        pat = re.compile('\$(\w*)')
        match = re.match(pat,iraffilename)
        dirname = match.group(1)
        unixdir = os.environ[dirname]
        basename = iraffilename[match.end()+1:] #1 to omit leading slash
        unixfilename = os.path.join(unixdir, basename)
        return unixfilename
    elif '$' in iraffilename:
        #Then it's an iraf-style variable
        irafdir,basename=iraffilename.split('$')
        unixdir=convertdict[irafdir]
        unixfilename=os.path.join(unixdir,basename)
        return unixfilename
    else:
        #If no $ sign found, just return the filename unchanged
        return iraffilename


