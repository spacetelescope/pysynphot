from __future__ import division
"""Module intended to replace the existing etc interface with the
refactored user interface."""
import spparser as P
from pysynphot.observation import Observation
from pysynphot import ObsBandpass
from pysynphot.observationmode import ObservationMode
from pysynphot import observationmode as ommod #needed for tabcheck task
import os, sys

mypid=os.getpid()

owarn={'partial':'Spectrum and bandpass only partially overlap. The spectrum was tapered to zero to perform the calculation',
       'none':'Spectrum and bandpass were disjoint!'}
odict={'partial':'taper',
       'none':None,
       'full':None}

def getparms(parlist):
    """ The ETC presently sends along a bunch of information in key-value
    pairs that pysynphot utterly ignores. This function builds a dictionary
    from the few elements it actually uses. """
    d={}
    keylist=['spectrum','output','obsmode','instrument','func','etcid']
             
    for pair in parlist:
        try:
            name,value=pair.split('=')
            if name in keylist:
                d[name]=value.strip('"')
        except ValueError,e:
            #Check to see if the string is empty
            if len(pair)>0:
                raise(e)
    return d

def parse_spec(syncommand):
    """Parse the synphot-classic command and return the resulting spectrum"""
    sp = P.interpret(P.parse(P.scan(syncommand)))
    return sp

def calcphot(parlist):
    """Calculate either effstim or efflam, depending on the input argument"""
    d=getparms(parlist)
    sp=parse_spec(d['spectrum'])
    bp=ObsBandpass(d['obsmode'])
    # obs=bp.observe(sp)
    
    ostat=bp.check_overlap(sp)
    
    try:
        obs=Observation(sp,bp,force=odict[ostat])
    except KeyError:
        obs=Observation(sp,bp,bp.wave,force=odict[ostat])

    obs.convert('counts')
    ans=obs.efflam()

    if ostat == 'full':
        return ans
    else:
        return ans, owarn[ostat]


def calcspec(parlist):
    """Calculate the spectrum & write it to a FITS file"""
    d=getparms(parlist)
    sp=parse_spec(d['spectrum'])
    sp.convert('counts')
    sp.writefits(d['output'])
    return d['output']

def countrate(parlist):
    """Return the pivot wavelength and countrate of the spectrum as
    observed through the obsmode, but based on the native waveset"""
    d=getparms(parlist)
    sp=parse_spec(d['spectrum'])
    bp=ObsBandpass(d['instrument'])


    #Check overlap status & proceed accordingly
    ostat=bp.check_overlap(sp)
    
    try:
        obs=Observation(sp,bp,force=odict[ostat])
    except KeyError:
        obs=Observation(sp,bp,bp.wave,force=odict[ostat])

    obs.convert('counts')
    efflam=obs.efflam()
    ans=obs.countrate(binned=False)

    if ostat == 'full':
        return ans,efflam
    else:
        return ans, efflam, owarn[ostat]

def specrate(parlist):
    """Return the countrate of the spectrum as observed through the
    obsmode, based on the binned wavelength set; and write the resulting
    spectrum to a file, returning the filename."""

    d=getparms(parlist)
    sp=parse_spec(d['spectrum'])
    bp=ObsBandpass(d['instrument'])
    
    #Check overlap status & proceed accordingly
    ostat=bp.check_overlap(sp)

    try:
        obs=Observation(sp,bp,force=odict[ostat])
    except KeyError:
        obs=Observation(sp,bp,bp.wave,force=odict[ostat])

    obs.convert('counts')
    try:
        obs.writefits(d['output'],binned=True)
    except KeyError:
        d['output']=None

    if ostat == 'full':
        return "%g;%s"%(obs.countrate(),d['output'])
    else:
        return "%g;%s;%s"%(obs.countrate(),d['output'],owarn[ostat])
    

def thermback(parlist):
    """Return the thermal background rate for the obsmode"""
    d=getparms(parlist)
    omode=ObservationMode(d['obsmode'])
    sp=omode.ThermalSpectrum()
    #Possibly bundle this so we can just do omode.thermback()
    ans = sp.integrate() * omode.pixscale**2 * omode.area
    return ans

def updatetabs(dummy):
    """Check for new GRAPH/COMP/THERM tables"""
    ommod.GRAPHTABLE = ommod._refTable(os.path.join('mtab','*_tmg.fits'))
    ommod.COMPTABLE  = ommod._refTable(os.path.join('mtab','*_tmc.fits'))
    try:
        ommod.THERMTABLE = ommod._refTable(os.path.join('mtab','*_tmt.fits'))
        msg="Success"
    except IOError, e:
        ommod.THERMTABLE = None
        msg= """Warning: %s
        No thermal calculations can be performed."""%str(e)
    return "%s;%s;%s;%s"%(ommod.GRAPHTABLE, ommod.COMPTABLE,
                          ommod.THERMTABLE, msg)

def showfiles(parlist):
    """For debugging: print tmg/tmc/tmt and showfiles to a file for the
    given obsmode.

    For nonserver use:
    foo='showfiles&obsmode="acs,hrc,f555w"&output="testme2.txt"'
    etc.showfiles(foo.split('&')[1:])
    
    """
    d=getparms(parlist)
    obsmode=d['obsmode']
    outname=d['output']
    
    ob=ommod.ObservationMode(obsmode)
    flist=[x for x in ob._throughput_filenames if x != 'clear']
    out=open(outname,'w')
    out.write("TMG: %s\n"%ommod.GRAPHTABLE)
    out.write("TMC: %s\n"%ommod.COMPTABLE)
    out.write("TMT: %s\n"%ommod.THERMTABLE)
    out.write("\nObsmode %s:\n"%obsmode)
    for fname in flist:
        out.write("%s\n"%fname)
    out.close()
    return(outname)
    
def Suicide(dummy):
    """Kill this process"""

    try:
        os.kill(mypid,9)
    except AttributeError, e:
        #We're probably on a Windows platform. Try this instead:
        os.popen('TASKKILL /PID '+str(mypid)+' /F')

def ping(dummy):
    """Respond with my process id so the caller knows I'm alive"""
    return str(mypid)


def version(dummy):
    """Return subversion version string"""
    from pysynphot.svn_version import __svn_version__, setupdate
    return __svn_version__+"; "+str(setupdate)

#This defines the set of tasks available for the ETC server to perform.
#Note that there are two distinct calls to calcphot that we might
#want to actually discriminate by name, eventually.

tasks = {'calcphot':           calcphot,
         'calcspec':           calcspec,
         'countrate':          countrate,
         'showfiles':          showfiles,
         'SpecSourcerateSpec': specrate,
         'thermback':          thermback,
         'updatetabs':         updatetabs,
         'version':            version,
         'quit':               Suicide,
         'ping':               ping}

#Define an extra task for the IRAF user interface

def etccalc(obsmode, spectrum, filename=None):
    bp=ObsBandpass(obsmode)
    sp=parse_spec(spectrum)
    try:
        obs=Observation(sp,bp)
    except KeyError:
        obs=Observation(sp,bp,bp.wave)

    obs.convert('counts')
    if (filename is not None):
        if not filename.endswith('.fits'):
            filename=filename+'.fits'
        obs.writefits(filename)
        sp.writefits(filename.replace('.fits','_sp.fits'))
        bp.writefits(filename.replace('.fits','_bp.fits'))

    return obs.countrate(), obs.efflam(), obs.pivot()
