
"""
calcspec
calcabnd
countrate 
bandpass
calcphot   -> pivot or effective wavelength
thermback

"""
import sys, time
import socket
##import threading
import SocketServer
import spectrum
import locations
import observationmode, observation


##class ThreadedServer(threading.Thread):
##    def __init__(self, socket, address):
##        self.socket = socket
##        self.address = address
##
##        threading.Thread.__init__(self)
##
##    def run(self):
##        print "Connected from", self.address
##        try:
##            while True:
##                receivedData = self.socket.recv(8192)
##                if not receivedData:
##                    break
##                print receivedData
##                self.socket.sendall(receivedData)
##            self.socket.close()
##            print "Disconnected from", self.address
##        finally:
##            self.socket.close()
##
##class ServerDispatcher(threading.Thread):
##    def run(self):
##        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##        self.sock.bind(('',8881))
##        self.sock.listen(5)
##        try:
##            while True:
##                srv_socket, address = self.sock.accept()
##                self.srv = ThreadedServer(srv_socket, address)
##                self.srv.start()
##        finally:
##            self.sock.close()
##
##
##def client(url):
##        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##        sock.connect((url,8881))
##        print "Connected to server"
##        for i in range(6):
##            line = "Line " + str(i)
##            sock.sendall(line)
##            print "Sent:", line
##            response = sock.recv(8192)
##            print "Received:", response
##        sock.close()

    


class TestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "Connected from " + str(self.client_address)
        while True:
            receivedData = self.request.recv(8192)
            if not receivedData:
                break
            print receivedData
            self.request.sendall(receivedData)
        self.request.close()
        print "Disconnected from " + str(self.client_address)

srv = SocketServer.ThreadingTCPServer(('',8881),TestHandler)
print srv
srv.serve_forever()


##def calcphot(obsmode):
##    parameters = []
##    parameters.append(obsmode)
##    Calcphot(parameters)
##
##
##class Calcphot(object):
##    def __init__(self, parameters):
##        t1 = time.time()
##        obsmode = observationmode.ObservationMode(parameters[0])
##        sp = spectrum.TabularSourceSpectrum(locations.testdata)
##        obs = observation.Observation(sp, obsmode)
##        efflam = obs.calcphot(func='efflam')
##        t2 = time.time()
##        print efflam
##        print 'elapsed time in python calculator: ', str(t2-t1), 'sec.'


##print sys.argv

##tasks = {'calcphot': Calcphot}
##
##def factory(task, *args, **kwargs):
##    return apply(tasks[task], args, kwargs)
##
##factory(sys.argv[1], sys.argv[2:])



## ['C:/specman/lib/etc.py', 'calcphot', 'acs,hrc,f555w',
## 'em(5000.0,', '10.0,', '1.0E-13,', 'flam)']
