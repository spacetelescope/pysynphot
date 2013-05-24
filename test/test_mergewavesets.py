import testutil

import pysynphot as S


# The function S.spectrum.MergeWaveSets is designed so that merged wave sets
# have no two adjacent values which differ by less than S.spectrum.MERGETHRESH.
# This tests that.
class TestMergeWaveSets(testutil.FPTestCase):
    def test_merge_wave_sets(self):
        bb = S.BlackBody(20000)
        ext = S.Extinction(0.04, 'gal1')

        new_wave = S.spectrum.MergeWaveSets(bb.wave, ext.wave)

        delta = new_wave[1:] - new_wave[:-1]

        self.assertTrue((delta > S.spectrum.MERGETHRESH).all(),
                        msg='Deltas should be < %g, min delta = %f' %
                            (S.spectrum.MERGETHRESH, delta.min()))
