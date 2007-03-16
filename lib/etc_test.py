
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
import threading
import SocketServer
import spectrum
import locations
import observationmode, observation


def test():
    cl1 = Client ('localhost',\
        'calcphot&spectrum="rn(unit(1,flam),box(5500.0,1),1.0E-18,flam)"&obsmode="acs,hrc,F220W"')
    cl1.start()

    cl2 = Client ('localhost',\
        'countrate&spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"&instrument="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"')
    cl2.start()

    cl3 = Client ('localhost',\
        'thermback&obsmode="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"')
    cl3.start()

    cl4 = Client ('localhost',\
        'SpecSourcerateSpec&spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"&instrument="wfc3,uvis1,g280"&output="C:\TEMP\2007\001\specOB1.fits"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"')
    cl4.start()


class Client(threading.Thread):
    def __init__(self, url, line):
        self._url = url
        self._line = line

        threading.Thread.__init__(self)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self._url,8881))
        print "Client connected to server.  "
        sock.sendall(self._line)
        print "Cleint sent:  ", self._line
        response = sock.recv(8192)
        print "Client received: ", response
        sock.close()

    


