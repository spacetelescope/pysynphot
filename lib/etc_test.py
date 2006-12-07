
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
            'Sourcerate&countrate.cenwave="INDEF"&refdata.area=45238.93416&countrate.verbose=yes&countrate.detector=" "&refdata.mode="a"&refdata.grtbl="mtab$*_tmg.fits"&countrate.form="counts"&countrate.exptime=1.0&countrate.spec_elem=" "&countrate.instrument="acs,hrc,F220W"&countrate.magform=vegamag&countrate.mode="a"&countrate.wavecat="synphot$data/wavecat.dat"&countrate.spectrum="((earthshine.fits*0.5)%2brn(spec(Zodi.fits),band(V),22.7,vegamag)%2b(el1215a.fits*0.5)%2b(el1302a.fits*0.5)%2b(el1356a.fits*0.5)%2b(el2471a.fits*0.5))"&countrate.magnitude=" "&countrate.reddening=0.0&countrate.aperture=" "&countrate.refwave=INDEF&countrate.flux_tot=0.0&refdata.cmptbl="mtab$*_tmc.fits"&countrate.flux_ref=INDEF&countrate.refdata=""&countrate.redlaw=gal1')
    cl2.start()
    cl3 = Client ('localhost',\
            'Sourcerate&countrate.cenwave="INDEF"&refdata.area=45238.93416&countrate.verbose=yes&countrate.detector=" "&refdata.mode="a"&refdata.grtbl="mtab$*_tmg.fits"&countrate.form="counts"&countrate.exptime=1.0&countrate.spec_elem=" "&countrate.instrument="acs,hrc,F220W"&countrate.magform=vegamag&countrate.mode="a"&countrate.wavecat="synphot$data/wavecat.dat"&countrate.spectrum="rn(unit(1,flam),box(5500.0,1),1.0E-18,flam)"&countrate.magnitude=" "&countrate.reddening=0.0&countrate.aperture=" "&countrate.refwave=INDEF&countrate.flux_tot=0.0&refdata.cmptbl="mtab$*_tmc.fits"&countrate.flux_ref=INDEF&countrate.refdata=""&countrate.redlaw=gal1')
    cl3.start()

##    cl1 = Client ('localhost', 'request 1')
##    cl1.start()
##    cl2 = Client ('localhost', 'request 2')
##    cl2.start()
##    cl3 = Client ('localhost', 'request 3')
##    cl3.start()



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

    


