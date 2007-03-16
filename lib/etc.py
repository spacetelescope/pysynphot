import os
import time
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

        if debug >= 1:
            print 'elapsed time: ', str(t2-t1), 'sec.  obsmode is:', \
                  self._obsmode

##        filename = locations.temporary + "obsp" + \
##                   str((self._spectrum + self._obsmode).__hash__()) + \
##                   ".fits"

        writer = SpectrumWriter(self._filename, self.observed_spectrum);
        writer.write()

        return str(effstim) + ';' + self._filename 


class SpectrumWriter(object):

    def __init__(self, filename, spectrum):
        self._filename = filename
        self._spectrum = spectrum

    def write(self):
        try:
            os.remove(self._filename)
        except OSError:
            pass

        (wave, flux) = self._spectrum.getArrays()

        waveunits = self._spectrum.waveunits
        fluxunits = self._spectrum.fluxunits

        # Get rid of zeros at both ends. However, leave one zero at each
        # end, the ETC requires it.....
        nz = flux.nonzero()[0]
        if len(nz) > 1:
            first = nz[0]
            last = nz[-1]
            if first > 0:
                first -= 1
            if last < len(wave)-1:
                last += 1
            wave = wave[first:last+1]
            flux = flux[first:last+1]

        cw = pyfits.Column(name='WAVELENGTH', array=wave, unit=waveunits.name, format='E')
        cf = pyfits.Column(name='FLUX', array=flux, unit=fluxunits.name, format='E')
        
        hdu = pyfits.PrimaryHDU()
        hdulist = pyfits.HDUList([hdu])

        cols = pyfits.ColDefs([cw, cf])
        hdu = pyfits.new_table(cols)
        hdulist.append(hdu)
        hdu.writeto(self._filename)


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
            requestString = self._requestQueue.get()
            tokens = requestString.split('&')
            task = factory(tokens[0], tokens[1:])
            self._resultQueue.put(str(task.run()))


class ServerDispatcher(threading.Thread):
    def run(self):
        global queueManager
        queueManager = QueueManager()

        srv = SocketServer.ThreadingTCPServer(('',8881),RequestHandler)
        print "Creating TCP server: " + str(srv)
        srv.serve_forever()


tasks = {'calcphot':           Calcphot,
         'countrate':          Countrate,
         'SpecSourcerateSpec': SpecSourcerateSpec,
         'thermback':          Thermback}

def factory(task, *args, **kwargs):
    return apply(tasks[task], args, kwargs)


