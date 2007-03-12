from distutils.core import setup, Extension
import sys, os.path, string, shutil, glob, os, re
from distutils.command.install_data import install_data



ver = sys.version_info
python_exec = 'python' + str(ver[0]) + '.' + str(ver[1])


def dolocal():
    """Adds a command line option --local=<install-dir> which is an abbreviation for
    'put all of thispackage in <install-dir>/thispackage'."""
    if "--help" in sys.argv:
        print >>sys.stderr
        print >>sys.stderr, " options:"
        print >>sys.stderr, "--local=<install-dir>    same as --install-lib=<install-dir>"
    for a in sys.argv:
        if a.startswith("--local="):
            dir =  os.path.abspath(a.split("=")[1])
            sys.argv.extend([
                "--install-lib="+dir,
                "--install-data="+os.path.join(dir,"coords")
                ])
            sys.argv.remove(a)

class smart_install_data(install_data):
    def run(self):
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)


tpmsrc = glob.glob('src/tpm/*.c')
tpmsrc.extend(['src/blackbox.c','src/pytpm_wrap.c'])

        
def dosetup():
    r = setup(name = "specman",
              version = "0.2",
              description  = 'Python Spectrum Manipulation Utilities',
              fullname     = 'AstroLib Specman',
              license      = 'BSD',
              author = "Robert Jedrzejewski, Ivo Busko, Vicki Laidler",
              author_email = "help@stsci.edu",
              url = "http://projects.scipy.org/astropy/astrolib",
              platforms = ["Linux","Solaris","Mac OS X"],
              packages=['specman'],
              package_dir={'specman':'lib'}
              #py_modules=['spectrum','observationmode','observation']
              #cmdclass = {'install_data':smart_install_data},
	      #data_files = [('coords',['lib/LICENSE.txt','src/tpm/TPM_LICENSE.txt'])]
              )

    return r

def main():
    args = sys.argv
    dolocal()
    dosetup()


if __name__ == "__main__":
    main()




## from distutils.core import setup
## setup(name='specman',
##       version='0.1',
##       description='Python Spectrum Manipulation Utilities',
##       author='Robert Jedrzejewski',
##       author_email='help@stsci.edu',
##       url='http://astropy.scipy.org/svn/astropy/',
##       py_modules=['spectrum','observationmode','observation'],
##      )
