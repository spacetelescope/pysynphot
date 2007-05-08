import os
import time
import traceback
import threading, Queue
import SocketServer
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

    ##        filename = locations.temporary + "obsp" + \
    ##                   str((self._spectrum + self._obsmode).__hash__()) + \
    ##                   ".fits"


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


class RequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "Server connected from " + str(self.client_address)
        while True:
            receivedData = self.request.recv(8192)
            if not receivedData:
                break
            if debug >= 2:
                print "Server received: " + receivedData

            result = queueManager.processRequest(receivedData)

            self.request.sendall(result)

        self.request.close()
        print "Server disconnected from " + str(self.client_address)


class QueueManager(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self._requestQueue = Queue.Queue()
        self._resultQueue = Queue.Queue()
        self.start()

    def processRequest(self, requestString):
        self._requestQueue.put(requestString)
        return self._resultQueue.get()

    def run(self):
        while True:
            try:
                requestString = self._requestQueue.get()
                tokens = requestString.split('&')
                task = factory(tokens[0], tokens[1:])
                self._resultQueue.put(str(task.run()))
            except Exception:
                self._resultQueue.put("ERROR")
                traceback.print_exc()


class ServerDispatcher(threading.Thread):
    def run(self):
        global queueManager
        queueManager = QueueManager()

        srv = SocketServer.ThreadingTCPServer(('',8881),RequestHandler)
        srv.allow_reuse_address = True
        print "Creating TCP server: " + str(srv)
        srv.serve_forever()


tasks = {'calcphot':           Calcphot,
         'calcspec':           Calcspec,
         'countrate':          Countrate,
         'SpecSourcerateSpec': SpecSourcerateSpec,
         'thermback':          Thermback}

def factory(task, *args, **kwargs):
    return apply(tasks[task], args, kwargs)


