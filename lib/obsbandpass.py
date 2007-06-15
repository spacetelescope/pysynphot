"""The ObsBandpass user interface needs to support either the usual
(acs,hrc,f555w) obsmode style that produce a set of chained throughput
files; or something like (johnson,v) that has a single throughput file.
Thus ObsBandpass must be a factory function, returning either an
ObsModeBandpass (ack, terrible name) or a TabularSpectralElement."""

from observationmode import ObservationMode
from spectrum import CompositeSpectralElement, TabularSpectralElement
import wavetable

def ObsBandpass(obstring):
    """ Temporarily create an Obsmode to determine whether an
    ObsModeBandpass or a TabularSpectralElement will be returned."""
    ob=ObservationMode(obstring)
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

    def __str__(self):
        """Defer to ObservationMode component """
        return self.obsmode._obsmode

    def __len__(self):
        """Defer to ObservationMode component """
        return len(self.obsmode)
    
    def showfiles(self):
        """Defer to ObservationMode component """
        return self.obsmode.showfiles()

    
            
        
