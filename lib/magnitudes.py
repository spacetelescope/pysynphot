import locations

class Magnitude:
    '''Base class for Magnitudes'''

    def CalcTotalFlux(self, InSpectrum):
        '''Calculate the flux of our target spectrum through the selected
        filter'''
        filteredflux = InSpectrum*self.throughput
        TotalFlux = filteredflux.integrate()
        return TotalFlux
    
    def CalcVegaFlux(self):
        '''Calculate the flux of the Vega standard spectrum through the
        selected filter'''
        vegaspec = spectrum.TabularSourceSpectrum(locations.VegaFile)
        filteredvega = vegaspec*self.throughput

        VegaFlux = filteredvega.integrate()
        
        return VegaFlux

class VMag(Magnitude):
    '''V Magnitude'''
    def __init__(self, value):
        self.value = value
        self.ThroughputFile = locations.Magtable['v']
        self.throughput = spectrum.TabularSpectralElement(self.ThroughputFile)


class BMag(Magnitude):
    '''B Magnitude'''
    def __init__(self, value):
        self.value = value
        self.ThroughputFile = locations.Magtable['b']
        self.throughput = spectrum.TabularSpectralElement(self.ThroughputFile)


class UMag(Magnitude):
    '''U Vagnitude'''
    def __init__(self, value):
        self.value = value
        self.ThroughputFile = locations.Magtable['u']
        self.throughput = spectrum.TabularSpectralElement(self.ThroughputFile)


class RMag(Magnitude):
    '''R Magnitude'''
    def __init__(self, value):
        self.value = value
        self.ThroughputFile = locations.Magtable['r']
        self.throughput = spectrum.TabularSpectralElement(self.ThroughputFile)


class IMag(Magnitude):
    '''I Magnitude'''
    def __init__(self, value):
        self.value = value
        self.ThroughputFile = locations.Magtable['i']
        self.throughput = spectrum.TabularSpectralElement(self.ThroughputFile)


