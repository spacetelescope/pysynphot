from __future__ import division
"""The ObsBandpass user interface needs to support either the usual
(acs,hrc,f555w) obsmode style that produce a set of chained throughput
files; or something like (johnson,v) that has a single throughput file.
Thus ObsBandpass must be a factory function, returning either an
ObsModeBandpass (ack, terrible name) or a TabularSpectralElement."""

from observationmode import ObservationMode
from spectrum import CompositeSpectralElement, TabularSpectralElement
import wavetable

def ObsBandpass(obstring, graphtable=None, comptable=None):
    """ obsband = ObsBandpass(string specifying obsmode; for details
    see the Synphot Data User's Guide,
    U{http://www.stsci.edu/hst/HST_overview/documents/synphot/hst_synphotTOC.html}"""

    ##Temporarily create an Obsmode to determine whether an
    ##ObsModeBandpass or a TabularSpectralElement will be returned.
    ob=ObservationMode(obstring,graphtable=graphtable,
                       comptable=comptable)
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

        
        
