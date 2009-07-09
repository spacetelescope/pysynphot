from __future__ import division
"""This module contains the machinery necessary to run a server. At
present it is an ETC-specific server, but the ETC functionality is
encapsulated in a single method of the QueuManager.

The server will connect to the port specified in the environment
variable PYSYN_PORT. If this variable is not set, it will use
the default_port specified below.

Use the startServer() function to start the server. This is done
automatically if __name__ == '__main__'."""

import os
import time
import traceback
import threading, Queue
import SocketServer

debug = 1
default_port = 8881

#Enforce defined PYSYN_CDBS, without which we are useless
if 'PYSYN_CDBS' not in os.environ:
    raise OSError('PYSYN_CDBS is not defined.')

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
                self._resultQueue.put( self.factory(tokens[0], tokens[1:]) )
            except Exception, e:
                self._resultQueue.put("Pysynphot ERROR: %s"%str(e))
                traceback.print_exc()

    def factory(self, taskname, *args, **kwargs):
        """This method encapsulates the ETC dependency.
        Eventually, pysynphot servers that support more than just the
        ETC functionality might be desired, and we could probably
        refactor and make specialized subclasses."""
        import etc
        return str(apply(etc.tasks[taskname], args, kwargs))
##         import etc
##         return str(apply(etc.tasks[taskname],args,kwargs).run())
    
class ServerDispatcher(threading.Thread):
    def run(self):
        global queueManager
        queueManager = QueueManager()
        port=int(os.environ.get('PYSYN_PORT',default_port))
        SocketServer.ThreadingTCPServer.allow_reuse_address = True
        srv = SocketServer.ThreadingTCPServer(('',port),RequestHandler)
        print "Creating TCP server: %s on port %d"%(str(srv),port)
        srv.serve_forever()


def startServer():
    dispatcher = ServerDispatcher()
    dispatcher.start()


if __name__ == '__main__':
    startServer()


            
