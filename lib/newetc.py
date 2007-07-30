"""Module intended to replace the existing etc interface with the
refactored user interface."""
import spparser as P
from pysynphot.newobservation import Observation
from pysynphot import ObsBandpass
from pysynphot.observationmode import ObservationMode

def getparms(parlist):
    """ The ETC presently sends along a bunch of information in key-value
    pairs that pysynphot utterly ignores. This function builds a dictionary
    from the few elements it actually uses. """
    d={}
    keylist=['spectrum','output','obsmode','instrument','func']
             
    for pair in parlist:
        name,value=pair.split('=')
        if name in keylist:
            d[name]=value.strip('"')
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
    obs=Observation(sp,bp)
    obs.convert('counts')
    ans=obs.efflam()
    
    return ans

def calcspec(parlist):
    """Calculate the spectrum & write it to a FITS file"""
    d=getparms(parlist)
    sp=parse_spec(d['spectrum'])
    sp.convert('counts')
    sp.writefits(d['output'])
    return d['output']

def countrate(parlist):
    """Return the pivot wavelength and countrate of the spectrum as
    observed through the obsmode using the appropriate binset"""
    d=getparms(parlist)
    sp=parse_spec(d['spectrum'])
    bp=ObsBandpass(d['instrument'])
    # obs=bp.observe(sp)
    obs=Observation(sp,bp)
    obs.convert('counts')
    piv=obs.pivot()
    ans=obs.countrate()
    return ans,piv

def specrate(parlist):
    """Like countrate, but write the computed spectrum to a fits file
    and only return the countrate, not the pivot wavelength."""
    d=getparms(parlist)
    sp=parse_spec(d['spectrum'])
    bp=ObsBandpass(d['instrument'])
    # obs=bp.observe(sp)
    obs=Observation(sp,bp)
    obs.convert('counts')
    try:
        obs.writefits(d['output'],binned=True)
    except KeyError:
        d['output']=None
    return "%f;%s"%(obs.countrate(),d['output'])

def thermback(parlist):
    """Return the thermal background rate for the obsmode"""
    d=getparms(parlist)
    omode=ObservationMode(d['obsmode'])
    sp=omode.ThermalSpectrum()
    #Possibly bundle this so we can just do omode.thermback()
    ans = sp.integrate() * omode.pixscale**2 * omode.area
    return ans


def Suicide(dummy):
    """Kill this process"""
    mypid=os.getpid()
    os.kill(mypid,9)

#This defines the set of tasks available for the ETC server to perform.
#Note that there are two distinct calls to calcphot that we might
#want to actually discriminate by name, eventually.

tasks = {'calcphot':           calcphot,
         'calcspec':           calcspec,
         'countrate':          countrate,
         'SpecSourcerateSpec': specrate,
         'thermback':          thermback,
         'quit':               Suicide}
