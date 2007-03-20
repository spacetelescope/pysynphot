""" Try out an ObsBandpass that inherits from both ObservationMode
and SpectralElement; see if it has the look&feel I'm expecting."""

from observationmode import ObservationMode
from spectrum import CompositeSpectralElement
import wavetable

class ObsBandpass(CompositeSpectralElement):
    """Bandpass instantiated from an obsmode string"""

    def __init__(self,obstring):
        """Instantiate a COmpositeSpectralElement by means of an
        ObservationMode created from the obstring"""
        
        ob=ObservationMode(obstring)
        #fill in components etc here
        chain=ob.components[0].throughput*ob.components[1].throughput
        for i in range(2,len(ob)-2):
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

    
            
        
