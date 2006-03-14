import locations
import spectrum  # circular import.....

class Magnitude(object):
    '''Base class for Magnitudes'''

    def calcTotalFlux(self, inSpectrum):
        '''Calculate the flux of our target spectrum through the selected
        filter'''
        filteredflux = inSpectrum*self._throughput
        return filteredflux.integrate()
    
    def calcVegaFlux(self):
        '''Calculate the flux of the Vega standard spectrum through the
        selected filter'''
        vegaspec = spectrum.TabularSourceSpectrum(locations.VegaFile)
        filteredvega = vegaspec*self._throughput
        return filteredvega.integrate()

class VMag(Magnitude):
    def __init__(self, value):
        self.value = value
        self._throughputFile = locations.magtable['v']
        self._throughput = spectrum.TabularSpectralElement(self._throughputFile)


class BMag(Magnitude):
    def __init__(self, value):
        self.value = value
        self._throughputFile = locations.magtable['b']
        self._throughput = spectrum.TabularSpectralElement(self._throughputFile)


class UMag(Magnitude):
    def __init__(self, value):
        self.value = value
        self._throughputFile = locations.magtable['u']
        self._throughput = spectrum.TabularSpectralElement(self._throughputFile)


class RMag(Magnitude):
    def __init__(self, value):
        self.value = value
        self._throughputFile = locations.magtable['r']
        self._throughput = spectrum.TabularSpectralElement(self._throughputFile)


class IMag(Magnitude):
    def __init__(self, value):
        self.value = value
        self.ThroughputFile = locations.Magtable['i']
        self.throughput = spectrum.TabularSpectralElement(self.ThroughputFile)


