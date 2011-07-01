from __future__ import division
## Automatically adapted for numpy.numarray Mar 05, 2007 by 
import os
import numpy as N
from numpy import ma as MA
import pyfits

import spectrum
import locations


class Icat(spectrum.TabularSourceSpectrum):
    """spec = Icat(CDBS directory name,Teff,metallicity,logG).
    This class constructs a model from the grid available in catalogs such
    as the Castelli & Kurucz. See the Synphot User's Data Manual, Appendix A,
    for more information
    U{http://www.stsci.edu/hst/HST_overview/documents/synphot/AppA_Catalogs4.html#48115}
    """
    def __init__(self,catdir,Teff,metallicity,log_g):

        self.isAnalytic=False
        
        filename = locations.CAT_TEMPLATE.replace('*',catdir)
        self.name="%s(Teff=%g,z=%g,logG=%g)"%(catdir,Teff,metallicity,log_g)

        table = pyfits.open(filename)

        indexList = table[1].data.field('INDEX')
        filenameList = table[1].data.field('FILENAME')

        indices = self._getArgs(indexList, filenameList)

        list0,list1 = self._breakList(indices, 0, Teff)

        list2,list3 = self._breakList(list0, 1, metallicity)
        list4,list5 = self._breakList(list1, 1, metallicity)

        list6,list7   = self._breakList(list2, 2, log_g)
        list8,list9   = self._breakList(list3, 2, log_g)
        list10,list11 = self._breakList(list4, 2, log_g)
        list12,list13 = self._breakList(list5, 2, log_g)

        sp1 = self._getSpectrum(list6[0],  catdir)
        sp2 = self._getSpectrum(list7[0],  catdir)
        sp3 = self._getSpectrum(list8[0],  catdir)
        sp4 = self._getSpectrum(list9[0],  catdir)
        sp5 = self._getSpectrum(list10[0], catdir)
        sp6 = self._getSpectrum(list11[0], catdir)
        sp7 = self._getSpectrum(list12[0], catdir)
        sp8 = self._getSpectrum(list13[0], catdir)

        spa1 = self._interpolateSpectrum(sp1, sp2, log_g)
        spa2 = self._interpolateSpectrum(sp3, sp4, log_g)
        spa3 = self._interpolateSpectrum(sp5, sp6, log_g)
        spa4 = self._interpolateSpectrum(sp7, sp8, log_g)

        spa5 = self._interpolateSpectrum(spa1, spa2, metallicity)
        spa6 = self._interpolateSpectrum(spa3, spa4, metallicity)

        spa7 = self._interpolateSpectrum(spa5, spa6, Teff)

        sp = spa7[0]

        self._wavetable = sp.GetWaveSet()
        self._fluxtable = sp(self._wavetable)
        self.waveunits = sp.waveunits
        self.fluxunits = sp.fluxunits
        self.warnings = {}
        
    def _getArgs(self, indices, filenames):
        results = []
        i = 0
        for index in indices:
            list1 = map(lambda x: float(x),index.split(','))
            list1.append(filenames[i])
            i = i + 1
            results.append(list1)

        return results

    def _breakList(self, inList, index, parameter):
        par = float(parameter)

        array = N.empty(shape=[len(inList),],dtype=N.float64)
        i = 0
        for parameters in inList:
            array[i] = parameters[index]
            i = i + 1 

        greater = MA.masked_less(array, par)
        less = MA.masked_greater(array, par)

        upper = MA.minimum(greater)
        lower = MA.maximum(less)

        upperArray = MA.masked_inside(array, par, upper)
        lowerArray = MA.masked_inside(array, lower, par)

        upperList = []
        lowerList = []
        i = 0
        for parameters in inList:
            if upperArray.mask[i]:
                upperList.append(parameters)
            if lowerArray.mask[i]:
                lowerList.append(parameters)
            i = i + 1

        return upperList, lowerList

    def _getSpectrum(self, parlist, basename):
        name = parlist[3]

        filename = name.split('[')[0]
        column = name.split('[')[1][:-1]

        filename = locations.KUR_TEMPLATE.replace('*',
                                                  os.path.join(basename,filename))
        sp = spectrum.TabularSourceSpectrum(filename, fluxname=column)

        result = []
        for member in parlist:
            result.append(member)

        result.pop()
        result.append(sp)

        return result

    def _interpolateSpectrum(self, sp1, sp2, par):
        spectrum1 = sp1.pop()
        spectrum2 = sp2.pop()
        par1 = sp1.pop()
        par2 = sp2.pop()
        
        if par1 == par2:
            sp = spectrum1
        else:
            a = (par1 - par) / (par1 - par2)
            b = 1.0 - a

            sp = a * spectrum2 + b * spectrum1

        result = []
        for member in sp1:
            result.append(member)
        result.append(sp)

        return result





