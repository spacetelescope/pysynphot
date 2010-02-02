import unittest

from pysynphot.observationmode import _ThermalObservationMode
from pysynphot.obsbandpass import ObsBandpass

class TestException(unittest.TestCase):
    #Making a ThermalObservationMode for an obsmode that
    #has no support for thermal calculations should raise
    #an exception.
    def setUp(self):
        self.ostring='acs,hrc,f555w'

    def test1(self):
        self.assertRaises(NotImplementedError,
                          _ThermalObservationMode,
                          self.ostring)

class TestThermal(unittest.TestCase):
    def setUp(self):
        self.ostring='nicmos,3,f222m'

    def test1(self):
        try:
            self.omode = _ThermalObservationMode(self.ostring)
        except Exception, e:
            self.fail(str(e))
