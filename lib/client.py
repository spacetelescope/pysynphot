from __future__ import division
"""Defines a Client class that can be used to communicate with the
Server class defined in server.py.

The client will connect to the port specified in the environment
variable PYSYN_PORT. If this variable is not set, it will use
the default_port imported from server.py.

"""

import socket
import threading
import SocketServer
import os

from server import default_port

class Client(threading.Thread):
    def __init__(self, url, line):
        self._url = url
        self._line = line
        self._port = int(os.environ.get('PYSYN_PORT',default_port))
        print "Client will use url, port (%s,%s)"%(self._url,self._port)
        threading.Thread.__init__(self)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self._url,self._port))
        hr= "\n==============================================\n"
        print hr,"Client connected to server.  "
        sock.sendall(self._line)
        print "Client sent:  ", self._line
        self._response = sock.recv(8192)
        print "%s Client sent: %s \n Client received: %s"%(hr,self._line,
                                                           self._response)
        sock.close()



