"""This module defines the ETC interface for pysynphot.
Although the names of the classes defined here are identical to the
names of synphot tasks, they do NOT correspond to those tasks. They
perform a strictly limited subset of the functionality available in
those tasks.

The tasks in the dictionary at the end of this module map the
task names provided by the ETC to the classes that perform the
relevant calculations. It is included by server.py to instantiate
an ETC server."""

import os
import time

import pyfits

import spectrum
import units
import locations
import observationmode
import observation
import spparser as P

debug = 1

class Calcspec(object):

    def __init__(self, parameters):
        for parameter in parameters:
             name,value = parameter.split('=')
             if name == 'spectrum':
                 self._spectrum = value.strip('"')
             elif name == 'output':
                 self._output = value.strip('"')

    def run(self):

        if self._spectrum == ""      or \
           self._spectrum == "null"  or \
           self._output   == ""      or \
           self._output   == "null":
            return "NaN"

        t1 = time.time()
        sp = P.interpret(P.parse(P.scan(self._spectrum)))
        t2 = time.time()

        if debug >= 1:
            print 'elapsed time in calcspec: ', str(t2-t1), 'sec.  spectrum is:', \
                  self._spectrum

        sp.writefits(self._output)
        return sp

class Calcphot(object):

    def __init__(self, parameters):
        for parameter in parameters:
             name,value = parameter.split('=')
             if name == 'spectrum':
                 self._spectrum = value.strip('"')
             elif name == 'obsmode':
                 self._obsmode = value.strip('"')

    def _compute(self, func):

        if self._spectrum == ""      or \
           self._spectrum == "null"  or \
           self._obsmode  == ""      or \
           self._obsmode  == "null":
            return "NaN"

        t1 = time.time()
        ob = self._buildObservation()
        result = ob.calcphot(func=func)
        t2 = time.time()

        self.observed_spectrum = ob.observed_spectrum

        if debug >= 1:
            print 'elapsed time in calcphot: ', str(t2-t1), 'sec.  obsmode is:', \
                  self._obsmode

        return result

    def _buildObservation(self):
        self._om = observationmode.ObservationMode(self._obsmode)
        sp = P.interpret(P.parse(P.scan(self._spectrum)))
        return observation.Observation(sp, self._om)

    def run(self):
        efflam = self._compute('efflam')

        if debug >= 2:
            print "efflam =", str(efflam)

        return efflam


class Countrate(Calcphot):

    def __init__(self, parameters):
        for parameter in parameters:
             name,value = parameter.split('=')
             if name == 'spectrum':
                 self._spectrum = value.strip('"')
             elif name == 'instrument':
                 self._obsmode = value.strip('"')

    def run(self):
        effstim = self._compute('effstim')

        if debug >= 2:
            print "effstim =", str(effstim)

        return effstim

##        if self._spectrum.startswith("rn"):
##            return (0.1759472, 5879.578)
##        else:
##            return (32.03496, 5879.578)


class SpecSourcerateSpec(Countrate):
    
    def __init__(self, parameters):
        Countrate.__init__(self, parameters)

        self._filename = None

        for parameter in parameters:
             name,value = parameter.split('=')
             if name == 'output':
                 self._filename = value.strip('"').replace('\\','/')

    def run(self):

        if self._spectrum == ""      or \
           self._spectrum == "null"  or \
           self._obsmode  == ""      or \
           self._obsmode  == "null":
            return "NaN;"

        t1 = time.time()
        ob = self._buildObservation()
        effstim = ob.calcphot(func='spec')
        t2 = time.time()

        self.observed_spectrum = ob.observed_spectrum

        if self._filename != None:
            if debug >= 1:
                print 'elapsed time: ', str(t2-t1), 'sec.  obsmode is:', \
                      self._obsmode


            self.observed_spectrum.writefits(self._filename)
            return str(effstim) + ';' + self._filename
        else:
            return str(effstim) + ';None'


class Thermback(Countrate):

    def __init__(self, parameters):

        for parameter in parameters:
             name,value = parameter.split('=')
             if name == 'obsmode':
                 self._obsmode = value.strip('"')

    def _compute(self,func):

        if self._obsmode  == ""      or \
           self._obsmode  == "null":
            return "NaN"

        t1 = time.time()
        self._om = observationmode.ObservationMode(self._obsmode)
        sp = self._om.ThermalSpectrum()
        result = sp.integrate() * self._om.pixscale**2 * units.HSTAREA
        t2 = time.time()

        self.observed_spectrum = sp

        if debug >= 1:
            print 'elapsed time in calcphot: ', str(t2-t1), 'sec.  obsmode is:', \
                  self._obsmode

        return str(result)


#This defines the set of tasks available for the ETC server to perform.
tasks = {'calcphot':           Calcphot,
         'calcspec':           Calcspec,
         'countrate':          Countrate,
         'SpecSourcerateSpec': SpecSourcerateSpec,
         'thermback':          Thermback}

