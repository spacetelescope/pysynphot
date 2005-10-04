import pyfits
import numarray
import observationmode
import spectrum

class Observation:

    def __init__(self, source, observationmode):

        self.source = source
        self.observationmode = observationmode

    def calcphot(self):

        countratespectrum = self.source * self.observationmode.Sensitivity()

        countrate = countratespectrum.integrate()

        return countrate
