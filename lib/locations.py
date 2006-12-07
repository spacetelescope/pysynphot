import sys

cdbs_roots = {'win32':  'C:/cdbs/',
              'sunos5': '/data/cdbs1/',
              'linux2': '/data/cdbs1/'}
data_roots = {'win32':  'C:/specman/data/',
              'sunos5': '/data/ra1/busko/specman/data/',
              'linux2': '/data/ra1/busko/specman/data/'}
user_roots = {'win32':  'C:/specmandata/',
              'sunos5': '/data/ra1/busko/specmandata/',
              'linux2': '/usr/stsci/APT/'}

temp_roots = {'win32':  'C:/TEMP/',
              'sunos5': '/data/ra1/busko/tmp/',
              'linux2': '/tmp/'}

rootdir   = cdbs_roots[sys.platform]
testdata  = rootdir + 'calspec/feige66_002.fits'

specdir   = data_roots[sys.platform]
wavecat   = specdir + 'wavecat/'

userdir   = user_roots[sys.platform]
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







