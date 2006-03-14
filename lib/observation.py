import string
import numarray
import observationmode
import spectrum

class Observation(object):

    def __init__(self, source, observationmode):

        self.source = source
        self.observationmode = observationmode

    def calcphot(self,func='effstim'):
        calculator = _factory(func, self.source,
                              self.observationmode.Throughput(),
                              self.observationmode.area) 
        return calculator._compute()


class _CalcphotCalculator(object):
    ''' Base class for all calcphot calculators. '''
    def __init__(self, source, throughput, area):
        self._countratespectrum = source * throughput
        self._area = area

class _EffstimCalculator(_CalcphotCalculator):
    ''' Computes effstim result for calcphot function.
    Only 'counts' units are supported for now (result is
    expresed in counts/s/hstarea units)
    '''
    def _compute(self):
        return self._countratespectrum.integrate() * self._area

class _EfflamCalculator(_CalcphotCalculator):
    ''' Computes efflam result for calcphot function.
    '''
    def _compute(self):
        wave = self._countratespectrum.GetWaveSet()
        countwave = self._countratespectrum(wave) * wave
        num = (countwave * wave).sum()
        den = countwave.sum()

        return num / den


_calculatorClasses = {'effstim': _EffstimCalculator,
                      'efflam' : _EfflamCalculator}

def _factory(func, *args, **kwargs):
    return apply(_calculatorClasses[string.lower(func)], args, kwargs)















