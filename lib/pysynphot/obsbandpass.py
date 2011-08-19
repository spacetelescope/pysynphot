from __future__ import division
"""The ObsBandpass user interface needs to support either the usual
(acs,hrc,f555w) obsmode style that produce a set of chained throughput
files; or something like (johnson,v) that has a single throughput file.
Thus ObsBandpass must be a factory function, returning either an
ObsModeBandpass (ack, terrible name) or a TabularSpectralElement."""

import numpy as np

from observationmode import ObservationMode
from spectrum import CompositeSpectralElement, TabularSpectralElement
import wavetable
import units
import pysynphot.exceptions as exceptions

def ObsBandpass(obstring, graphtable=None, comptable=None, component_dict={}):
    """ obsband = ObsBandpass(string specifying obsmode; for details
    see the Synphot Data User's Guide,
    U{http://www.stsci.edu/hst/HST_overview/documents/synphot/hst_synphotTOC.html}"""

    ##Temporarily create an Obsmode to determine whether an
    ##ObsModeBandpass or a TabularSpectralElement will be returned.
    ob=ObservationMode(obstring,graphtable=graphtable,
                       comptable=comptable,component_dict=component_dict)
    if len(ob) > 1:
        return ObsModeBandpass(ob)
    else:
        return TabularSpectralElement(ob.components[0].throughput_name)
    
class ObsModeBandpass(CompositeSpectralElement):
    """Bandpass instantiated from an obsmode string"""

    def __init__(self,ob):
        """Instantiate a COmpositeSpectralElement by means of an
        ObservationMode (which the caller must have already created from
        an  obstring"""
        
        #Chain the individual components
        chain=ob.components[0].throughput*ob.components[1].throughput
        
        for i in range(2,len(ob)-1):
            chain = chain*ob.components[i].throughput
        
        CompositeSpectralElement.__init__(self,chain,
                                          ob.components[-1].throughput)
        
            
        self.obsmode=ob
        self.name=self.obsmode._obsmode #str(self.obsmode)

        #Check for valid bounds
        self._checkbounds()
        
        try:
            self.binset = self.obsmode.bandWave()
        except AttributeError:
            # this is to catch an error raised when the self.obsmode object does not
            # have a binset attribute because of some problem with the obsmode
            # used to instatiate it.
            pass

    def __str__(self):
        """Defer to ObservationMode component """
        return self.name #self.obsmode._obsmode

    def __len__(self):
        """Defer to ObservationMode component """
        return len(self.obsmode)
    
    def showfiles(self):
        """Defer to ObservationMode component """
        return self.obsmode.showfiles()


    def _checkbounds(self):
        thru=self.throughput
        if thru[0] != 0 or thru[-1] != 0:
            print "Warning: throughput for this obsmode is not bounded by zeros. Endpoints: thru[0]=%g, thru[-1]=%g"%(thru[0],thru[-1])

    def thermback(self):
        """Expose the thermal background calculation presently hidden
        in the obsmode class.
        Only bandpasses for which thermal information has been supplied in the graph
        table supports this method; all others will raise a NotImplementedError.
        """

        #The obsmode.ThermalSpectrum method will raise an exception if there is
        #no thermal information, and that will just propagate up.
        sp=self.obsmode.ThermalSpectrum()

        #Thermback is always provided in this non-standard set of units.
        #This code was copied from etc.py.
        ans = sp.integrate() * (self.obsmode.pixscale**2 *
                                self.obsmode.area)
        return ans

    def pixel_range(self, waverange, waveunits=None, round='round'):
        """
        Returns the number of wavelength bins within `waverange`.
        
        Parameters
        ----------
        waverange : array_like
            A sequence containing the wavelength range of interest. Only the
            first and last elements are used. Assumed to be in increasing order.
            
        waveunits : str, optional
            The units of the wavelengths given in `waverange`. Defaults to None.
            If None, the wavelengths are assumed to be in the units of the
            `waveunits` attribute.
            
        round : {'round','min','max',None}, optional
            How to deal with pixels at the edges of the wavelength range. All
            of the options, except None, will return an integer number of pixels.
            Defaults to 'round'.
            
            When set to 'round' end pixels are included in the count if
            the wavelength range includes at least half of the end pixel.
            
            When set to 'min' only pixels wholly within `waverange` are counted.
            
            When set to 'max' end pixels that are within `waverange` by any
            margin are counted.
            
            When set to None the exact number of encompassed pixels, including
            fractional pixels, is returned
            
        Returns
        -------
        num : int or float
            Number of wavelength bins within `waverange`. 
            
        Raises
        ------
        ValueError
            If `round` is not an allowed value.
            
        pysynphot.exceptions.OverlapError
            If `waverange` exceeds the bounds of the `binset` attribute.
        
        """
        # make sure that the round keyword is valid
        if round not in ('round','min','max',None):
            raise ValueError("round keyword must be one of ('round','ciel','floor',None)")
        
        # start by converting waverange to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)
            
            # convert to angstroms and then whatever self.waveunits is
            wave1 = waveunits.ToAngstrom(waverange[0])
            wave2 = waveunits.ToAngstrom(waverange[-1])
            
            wave1 = units.Angstrom().Convert(wave1, self.waveunits.name)
            wave2 = units.Angstrom().Convert(wave2, self.waveunits.name)
        else:
            wave1 = waverange[0]
            wave2 = waverange[-1]
            
        # make sure the specified waverange is within our .binset
        minwave = self.binset[0] - (self.binset[0:2].mean() - self.binset[0])
        if wave1 < minwave:
            raise exceptions.OverlapError("Lower bound of waverange is outside of binset. Min = %f" % minwave)
         
        maxwave = self.binset[-1] + (self.binset[-1] - self.binset[-2:].mean())
        if wave2 > maxwave:
            raise exceptions.OverlapError("Upper bound of waverange is outside of binset. Max = %f" % maxwave)
        
        # if the wavelength ends are the same return 0
        if wave1 == wave2:
            return 0
        
        # find where the wavelength endpoints fall.
        if round == 'round':
            ind1 = self.binset.searchsorted(wave1, side='left')
            ind2 = self.binset.searchsorted(wave2, side='right')
        
            num = ind2 - ind1
        else:
            raise NotImplementedError("Support for round=%s is not yet available." % repr(round))
        
        return num
        
    def wave_range(self, cenwave, npix, waveunits=None, round=None):
        """
        Get the wavelength range covered by a number of pixels, `npix`, centered
        on wavelength `cenwave`.
        
        Parameters
        ----------
        cenwave : float
            Central wavelength of range.
            
        npix : int
            Number of pixels in range, centered on `cenwave`.
            
        waveunits : str, optional
            Wavelength units of `cenwave` and the returned wavelength range.
            Defaults to None. If None, the wavelengths are assumed to be in 
            the units of the `waveunits` attribute.
            
        round : {None,'round','min','max'}, optional
            How to deal with pixels at the edges of the wavelength range. All
            of the options, except None, will return a wavelength range that
            encompasses an integer number of pixels, and that number may not
            be equal to `npix`.
            Defaults to None.
            
            When set to None an exact wavelength range is returned. The returned
            range may not correspond to to an integer number of pixels.
            
            When set to 'round' the returned wavelength range encompasses
            an end pixel if at least half of the pixel is included.
            
            When set to 'min' the returned wavelength range is shrunk so that
            it includes an integer number of pixels.
            
            When set to 'max' the returned wavelength range is expanded so that
            it includes an integer number of pixels.
            
        Returns
        -------
        waverange : tuple of floats
            The range of wavelengths spanned by `npix` centered on `cenwave`.
            
        Raises
        ------
        ValueError
            If `round` is not an allowed value.
        
        pysynphot.exceptions.OverlapError
            If `cenwave` is not within the `binset` attribute, or the returned `waverange` would
            exceed the limits of the `binset` attribute.
        
        """
        # make sure that the round keyword is valid
        if round not in (None,'round','min','max'):
            raise ValueError("round keyword must be one of (None,'round','min','max')")
        
        # convert cenwave from waveunits to self.waveunits, if necessary
        if waveunits is not None:
            waveunits = units.Units(waveunits)
            
            # convert to angstroms and then whatever self.waveunits is
            cenwave = waveunits.ToAngstrom(cenwave)
            cenwave = units.Angstrom().Convert(cenwave, self.waveunits.name)
        
        # make sure cenwave is within binset
        if cenwave < self.binset[0]:
            raise exceptions.OverlapError("cenwave is not within binset. Min = %f" % self.binset[0])
        elif cenwave > self.binset[-1]:
            raise exceptions.OverlapError("cenwave is not within binset. Max = %f" % self.binset[-1])
                
        # first figure out what index the central wavelength falls at
        diff = self.binset - cenwave
        ind = np.where(np.abs(diff) == np.abs(diff).min())[0][0]
        
        # now figure out the fractional index
        if diff[ind] < 0:
            frac_ind = float(ind) + diff[ind] / (diff[ind] - diff[ind-1])
        elif diff[ind] > 0:
            frac_ind = float(ind) + diff[ind] / (diff[ind+1] - diff[ind])
        else:
            frac_ind = float(ind)
        
        # then figure out the fractional indices of the ends
        frac_ind1 = frac_ind - npix/2.
        frac_ind2 = frac_ind + npix/2.
        
        # check ends
        if frac_ind1 < -0.5:
            raise exceptions.OverlapError("Lower wavelength range is below allowed binset.")
            
        if frac_ind2 > self.binset.shape[0] - 0.5:
            raise exceptions.OverlapError("Upper wavelength range is above allowed binset.")
        
        # translate ends to wavelength
        if round == 'round':
            # calculate lower end of wavelength range
            f, i = np.modf(frac_ind1)
            i = int(i)
            
            if f > 0:
                # end is somewhere greater than binset[0] so we can just
                # interpolate between two neighboring values going with upper edge
                wave1 = self.binset[i:i+2].mean()
            elif f == 0 and i > 0:
                # end is somewhere greater than binset[0] so we can just
                # interpolate between two neighboring values going with lower edge
                wave1 = self.binset[i-1:i+1].mean()
            else:
                # end is below the lowest binset value, but not by enough to
                # trigger an exception
                wave1 = self.binset[0] - (self.binset[0:2].mean() - self.binset[0])
                
            # calculate upper end of wavelength range
            f, i = np.modf(frac_ind2)
            i = int(i)
            
            if i < self.binset.shape[0] - 2:
                # end is somewhere below binset[-1] so we can just interpolate
                # between two neighboring values, going with the upper edge.
                wave2 = self.binset[i:i+2].mean()
            else:
                # end is above highest binset value but not by enough to
                # trigger an exception
                wave2 = self.binset[-1] + (self.binset[-1] - self.binset[-2:].mean())
        
        else:
            raise NotImplementedError("Support for round=%s is not yet available." % repr(round))
        
        # translate ends to waveunits, if necessary
        if waveunits is not None:
            # convert to angstroms
            wave1 = self.waveunits.ToAngstrom(wave1)
            wave2 = self.waveunits.ToAngstrom(wave2)
            
            # then to waveunits
            wave1 = units.Angstrom().Convert(wave1, waveunits.name)
            wave2 = units.Angstrom().Convert(wave2, waveunits.name)
            
        return wave1, wave2
