""" This module handles the wavecat.dat table presently used by the
synphot countrate task (and thus the ETC) to select an appropriate wavelength
set for a given obsmode. """

import re
import os


class Wavetable(object):
    """ Class to handle wavecat.dat initialization and access. (This class
    may need a better name; wavetable and waveset are awfully close.)
    Also, put the default waveset into this object with a key of NONE."""
    
    def __init__(self, fname):
        """ Instantiate a Wavetable from a file """
        self.file=fname
        self.lookup={}
        self.setlookup={}
        fs = open(wavecat_file, mode='r')
        lines = fs.readlines()
        fs.close()

        regx = re.compile(r'\S+', re.IGNORECASE)
        for line in lines:
            if not line.startswith("#"):
                try:
                    [obm,coeff] = regx.findall(line)
                    self.lookup[obm] = coeff
                    self.setlookup[frozenset(obm.split(','))] = coeff
                except ValueError:
                    raise ValueError("Error processing line: %s"%line)


    def __getitem__(self, key):
        """Fairly smart lookup: if no exact match, find the most complete
        match.
        """

        ans=None
        try:
            #Try an exact match
            ans = self.lookup[key]
            
        except KeyError:
            #Try input key partially contained in a table key, or
            #vice-versa
            subset=[]
            for k in self.lookup.keys():
                if k in key or key in k:
                    subset.append(k)
            subset.sort()
            try:
                ans=self.lookup[subset[-1]]
            except IndexError:
                ans=None
                
        if ans is None:
            #Try a setwise match.
            #The correct key will be a subset of the input key.
            setkey=set(key.split(','))
            candidates=set()
            for k in self.setlookup:
                if k.issubset(setkey):
                    candidates.add(k)
            if len(candidates) == 1:
                ans = self.setlookup[candidates.pop()]
            elif len(candidates) == 0:
                raise KeyError("%s not found in %s; candidates:%s"%(key,self.file,str(subset)))
            elif len(candidates) > 1:
                raise KeyError("Ambiguous key %s; candidates %s"%(setkey, candidates))
        
        return ans


wavecat_file = "%s/data/wavecat/data/wavecat.dat"%os.path.dirname(__file__)
wavetable=Wavetable(wavecat_file)

##--------------------------------------------------------------
## Original implementation as simple dict
##--------------------------------------------------------------
## wavetable = {}
## wavecat_file = "%s/data/wavecat/data/wavecat.dat"%os.path.dirname(__file__)
## fs = open(wavecat_file, mode='r')
## lines = fs.readlines()
## fs.close()

## regx = re.compile(r'\S+', re.IGNORECASE)
## for line in lines:
##     if not line.startswith("#"):
##         try:
##             [obm,coeff] = regx.findall(line)
##             wavetable[obm] = coeff
##         except ValueError:
##             print "Error processing line: %s"%line
