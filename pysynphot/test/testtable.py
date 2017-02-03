"""Test table format errors. Usually in real life these occur
in file access, but many of them apply to ArraySpectrum objects
as well & can be tested that way.

"""
import os
import unittest
import numpy as np

from pysynphot import exceptions, spectrum


class WaveProblems(unittest.TestCase):
    def setUp(self):
        self.fx = np.array([10, 20, 20, 30, 50, 100])

    def testpass(self):
        wv = np.array([10, 20, 30, 40, 50, 100])
        sp = spectrum.ArraySourceSpectrum(wv, self.fx)

    def testduprow(self):
        wv = np.array([10, 20, 20, 30, 50, 100])
        try:
            sp = spectrum.ArraySourceSpectrum(wv, self.fx)
        except exceptions.DuplicateWavelength as e:
            self.assertEqual(e.rows, 1)

    def testzero(self):
        wv = np.array([0, 20, 30, 40, 50, 100])
        self.assertRaises(exceptions.ZeroWavelength,
                          spectrum.ArraySourceSpectrum, wv, self.fx)

    def testnosort(self):
        wv = np.array([10, 20, 40, 30, 50, 100])
        self.assertRaises(exceptions.UnsortedWavelength,
                          spectrum.ArraySourceSpectrum, wv, self.fx)


class TestFile(unittest.TestCase):
    def setUp(self):
        # Write an ascii file to test the reading of
        self.wv = np.array([10, 20, 'grackle', 30, 50, 100])
        self.fx = self.wv

        self.fname = os.path.abspath('grackle.dat')
        with open(self.fname, 'w') as out:
            for w, f in zip(self.wv, self.fx):
                out.write("%s  %s\n" % (w, f))

    def tearDown(self):
        try:
            os.unlink(self.fname)
        except Exception as e:
            pass  # ok, not there

    def testbadrow(self):
        try:
            sp = spectrum.FileSourceSpectrum(self.fname)
        except exceptions.BadRow as e:
            self.assertEqual(e.rows, 3)
