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
                "--install-data="+os.path.join(dir,"pysynphot")
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
    print sys.prefix
    r = setup(name = "pysynphot",
              version = "0.21dev",
              description  = 'Python Synthetic Photometry Utilities',
              fullname     = 'AstroLib Pysynphot',
              license      = 'BSD',
              author = "Robert Jedrzejewski, Ivo Busko, Vicki Laidler",
              author_email = "help@stsci.edu",
              url = "http://projects.scipy.org/astropy/astrolib",
              platforms = ["Linux","Solaris","Mac OS X"],
              packages=['pysynphot'],
              package_dir={'pysynphot':'lib'},
              #py_modules=['spectrum','observationmode','observation']
              #cmdclass = {'install_data':smart_install_data},
	      #data_files = [('pysynphot/data',['pysynphot/data/*.fits',
              #                    '../data/*.dat',
              #                     'data/wavecat/data'])]
              )

    return r

def main():
    args = sys.argv
    dolocal()
    dosetup()


if __name__ == "__main__":
    main()


