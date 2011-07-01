from __future__ import division
"""This module defines classes used to define reddening laws and
extinctions."""
import pyfits
from spectrum import ArraySpectralElement
import Cache
import extinction #temporary(?) backwards compatibility

class CustomRedLaw(object):
    def __init__(self,
                 wave=None,
                 waveunits='InverseMicrons',
                 Avscaled=None,
                 name='Unknown Reddening Law',
                 litref=None):

        self.wave=wave
        self.waveunits=waveunits
        self.obscuration=Avscaled
        self.name=name
        self.litref=litref

    def reddening(self,extval):
        """Compute the reddening for the provided value of the extinction."""
        T = 10.0**(-0.4*extval*self.obscuration)
        ans=ArraySpectralElement(wave=self.wave,
                                 waveunits=self.waveunits,
                                 throughput=T,
                                 name='%s(Av=%g)'%(self.name,extval)
                                 )
        ans.citation = self.litref
        return ans

class RedLaw(CustomRedLaw):
    """Defines a reddening law from a FITS file."""
    def __init__(self,filename):
        f=pyfits.open(filename)
        d=f[1].data
        CustomRedLaw.__init__(self,
                              wave=d.field('wavelength'),
                              waveunits=f[1].header['tunit1'],
                              Avscaled=d.field('Av/E(B-V)'),
                              litref=f[0].header['litref'],
                              name=f[0].header['shortnm'])
        f.close()

def Extinction(extval,name=None):
   """
   extinction = Extinction(extinction (E(B-V)) in magnitudes,
                           'reddening law')
                              
   Factory function to return the right kind of reddening.
   If no name is provided, the average Milky Way extinction will
   be used. Extinction laws are defined in data files that must be
   installed with the CDBS files. Presently, the following extinction
   laws are supported:
     gal3      Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 3.10.
     lmc30dor  Gordon et al. (2003, ApJ, 594, 279) R_V = 2.76.
     lmcavg    Gordon et al. (2003, ApJ, 594, 279) R_V = 3.41.
     mwavg     Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 3.10.
     mwdense   Cardelli, Clayton, & Mathis (1989, ApJ, 345, 245) R_V = 5.00.
     smcbar    Gordon et al. (2003, ApJ, 594, 279) R_V=2.74.
     xgalsb    Calzetti et al. (2000. ApJ, 533, 682)

   """
   try:
       ext=Cache.RedLaws[name].reddening(extval)
   except AttributeError:
       #The cache hasn't yet been filled.
       Cache.RedLaws[name]=RedLaw(Cache.RedLaws[name])
       ext=Cache.RedLaws[name].reddening(extval)
   except KeyError:
       #There's no reddening law by that name. See if we've been
       #given a filename from which we can read one.
       try:
           Cache.RedLaws[name]=RedLaw(name)
           ext=Cache.RedLaws[name].reddening(extval)
       except IOError:
           #If not, see if it's an old extinction law
           try:
               ext=extinction.Extinction(extval,name)
           except KeyError:
               raise ValueError('No extinction law has been defined for "%s", and no such file exists'%name)
   return ext
