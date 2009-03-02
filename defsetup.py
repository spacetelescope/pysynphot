
pkg = 'pysynphot'

setupargs = {
    'version'       :      	"0.60d",
    'description'   :       'Python Synthetic Photometry Utilities',
    'fullname'      :       'AstroLib Pysynphot',
    'license'       :       'BSD',
    'author'        :     	"Robert Jedrzejewski, Ivo Busko, Vicki Laidler",
    'author_email'  :      	"help@stsci.edu",
    'url'           :  		"http://projects.scipy.org/astropy/astrolib",
    'platforms'     :      	["Linux","Solaris","Mac OS X", "Win"],
    'requires'      :       ['pyfits','numpy'],
    'data_files'    :     	[ ( pkg+'/data', [ 'data/generic/*', 'data/wavecat/*' ] )
                                
                            ]
    }

