import sys

cdbs_roots = {'win32':  'C:/cdbs/',
              'sunos5': '/data/cdbs1/',
              'linux2': '/data/cdbs1/'}
data_roots = {'win32':  'C:/pysynphot/data/',
              'sunos5': '/data/ra1/busko/pysynphot/data/',
              'linux2': '/data/ra1/busko/pysynphot/data/'}

temp_roots = {'win32':  'C:/TEMP/',
              'sunos5': '/data/ra1/busko/tmp/',
              'linux2': '/tmp/'}

rootdir   = cdbs_roots[sys.platform]

specdir   = data_roots[sys.platform]
wavecat   = specdir + 'wavecat/'

temporary = temp_roots[sys.platform]

CAT_TEMPLATE = cdbs_roots[sys.platform] + 'grid/*/catalog.fits'
KUR_TEMPLATE = cdbs_roots[sys.platform] + 'grid/*'

##pat = '/../data/'
##for p in sys.path:
##    filename = p + pat + 'vega.fits'
##    if os.path.exists(filename):
##        specdir = p + pat

VegaFile = specdir + 'vega.fits'

# There are throughput files mixed with spectrum files (the ETC mixes
# then together in spectral expressions); the throughput files must
# be explictly listed here.
throughputfiles = [specdir+'thru.fits'] 


def getBandFileName(band):
    return specdir + band.replace(',','_') + '.fits'


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
                  'synphot$': wavecat}

    ## If no $ sign found, just return the filename unchanged
    unixfilename = iraffilename

    dollarpos = iraffilename.find('$')

    if dollarpos != -1:
        irafdir = iraffilename[:dollarpos+1].lstrip()
        unixfilename = iraffilename.replace(irafdir,convertdic[irafdir])

    return unixfilename




