import time
import math
import threading
import SocketServer
import numarray

import spectrum
import locations
import observationmode
import observation
import spparser as P


class Calcphot(object):
    def __init__(self, parameters):
        for parameter in parameters:
             name,value = parameter.split('=')
             if name == 'spectrum':
                 self._spectrum = value.strip('"')
             elif name == 'obsmode':
                 self._obsmode = value.strip('"')

    def run(self):
        t1 = time.time()
        om = observationmode.ObservationMode(self._obsmode)
        sp = P.interpret(P.parse(P.scan(self._spectrum)))
        ob = observation.Observation(sp, om)
        efflam = ob.calcphot(func='efflam')
        t2 = time.time()
        print "efflam =", str(efflam)
        print 'elapsed time in calcphot: ', str(t2-t1), 'sec.'
        return efflam


class RequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        print "Connected from " + str(self.client_address)
        while True:
            receivedData = self.request.recv(8192)
            if not receivedData:
                break
            print receivedData

            self._processRequest(receivedData)

        self.request.close()
        print "Disconnected from " + str(self.client_address)

    def _processRequest(self, requestString):
        tokens = requestString.split('&')
        task = factory(tokens[0], tokens[1:])
        self.request.sendall(str(task.run()))


class ServerDispatcher(threading.Thread):
    def run(self):
        srv = SocketServer.ThreadingTCPServer(('',8881),RequestHandler)
        print "Creating TCP server: " + str(srv)
        srv.serve_forever()


tasks = {'calcphot': Calcphot}

def factory(task, *args, **kwargs):
    return apply(tasks[task], args, kwargs)


def startServer():
    dispatcher = ServerDispatcher()
    dispatcher.start()







