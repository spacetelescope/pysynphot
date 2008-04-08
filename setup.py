from distutils.core import setup, Extension
import sys, os.path, string, shutil, glob, os, re
from distutils.command.install_data import install_data
import glob, time
import commands

#Determine the python version
ver = sys.version_info
python_exec = 'python' + str(ver[0]) + '.' + str(ver[1])


#Determine & save the revision number for the ETC
warning=""
vfname=os.path.join('data','generic','versioninfo.dat')
try :
    # If the version file already exists, it was created when the
    # source distribution was being assembled.  All we need to
    # do is read it from the file.
    f=open(vfname,"r")
    revset=f.readline()
    f.close()
except IOError:
    # If we can't read the file, then we need to generate the file
    warning=""
    stat,revset=commands.getstatusoutput('svnversion .')
    if stat != 0:
        warning="cannot extract svnversion information\n"
        revset='unavailable'
    if revset.find('exported') >= 0 :
        warning="this copy was exported - no version information\n"
        revset='unavailable'
    if revset.find("M") >= 0 :
        warning="this copy is modified\n"

    revset=revset+'; build date %s\n'%time.ctime()
        
    f=open(vfname,'w')
    f.write(revset)
    f.close()

    #Determine & save the full svn info string for humans
    #No need to test against status; the info will be self-explanatory
    here=os.path.abspath(os.curdir)
    info=commands.getoutput('svn info %s'%here)
    vfname=os.path.join('data','generic','taginfo.dat')
    f=open(vfname,'w')
    f.write(info)
    f.close()

# "python setup.py assemble" causes it to only to assemble
# the source distribution; we have collected the version
# information into the files by now, so we're done.
if len(sys.argv) == 2 and sys.argv[1] == 'prep' :
    if warning :
        print "unable to store useful version information"
        print warning
        sys.exit(1)
    else :
        sys.exit(0)

#------------------------------------------------------------
# WARNING WARNING WARNING: Any changes made to the datafiles
# must also be reflected in stsci_python/cfg_pysynphot.py.
#------------------------------------------------------------
#Define the datafiles that are part of this package
DATA_FILES = glob.glob(os.path.join('data', 'generic', '*'))
WAVECAT_FILES = glob.glob(os.path.join('data', 'wavecat', '*'))
DATA_FILES_DIR = os.path.join('pysynphot', 'data')
testfiles = glob.glob(os.path.join('test','etctest_base_class.py'))

PYSYNPHOT_DATA_FILES = [(DATA_FILES_DIR,DATA_FILES),
                        (DATA_FILES_DIR, WAVECAT_FILES),
                        ('pysynphot',testfiles)]
#------------------------------------------------------------

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
                ])
            sys.argv.remove(a)

class smart_install_data(install_data):
    def run(self):
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)


def dosetup():
    print sys.prefix
    r = setup(name = "pysynphot",
              version = "0.3dev%rs"%revset.strip(),
              description  = 'Python Synthetic Photometry Utilities',
              fullname     = 'AstroLib Pysynphot',
              license      = 'BSD',
              author = "Robert Jedrzejewski, Ivo Busko, Vicki Laidler",
              author_email = "help@stsci.edu",
              url = "http://projects.scipy.org/astropy/astrolib",
              platforms = ["Linux","Solaris","Mac OS X", "Win"],
              packages=['pysynphot'],
              package_dir={'pysynphot':'lib'},
              requires=['pyfits','numpy'],
              cmdclass = {'install_data':smart_install_data},
              data_files = PYSYNPHOT_DATA_FILES
              )

    return r

def main():
    args = sys.argv
    dolocal()
    dosetup()
    if warning != "" :
        print """\n \n \n \n \n \n \n
        X        X        X       X        X       X      X\n
        X    WARNING, """ + warning + """
        X    Pysynphot installation was performed anyway.\n
        X        X        X       X        X       X      X\n
        \n \n \n \n"""
        sys.exit(1)

if __name__ == "__main__":
    main()


