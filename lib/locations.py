import sys


cdbs_roots = {'win32':  'C:/cdbs/',
              'sunos5': '/data/cdbs1/',
              'linux2': '/data/cdbs1/'}
data_roots = {'win32':  'C:/specman/data/',
              'sunos5': '/data/ra1/busko/specman/data/',
              'linux2': '/data/ra1/busko/specman/data/'}


rootdir = cdbs_roots[sys.platform]
specdir = data_roots[sys.platform]
testdata = cdbs_roots[sys.platform] + 'calspec/feige66_002.fits'

##pat = '/../data/'
##for p in sys.path:
##    filename = p + pat + 'vega.fits'
##    if os.path.exists(filename):
##        specdir = p + pat

utable = specdir + 'u.fits'
btable = specdir + 'b.fits'
vtable = specdir + 'v.fits'
rtable = specdir + 'r.fits'
itable = specdir + 'i.fits'

magtable = {'u': utable,
            'b': btable,
            'v': vtable,
            'r': rtable,
            'i': itable}

VegaFile = specdir + 'vega.fits'
