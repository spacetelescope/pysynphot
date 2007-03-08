## Automatically adapted for numpy.numarray Mar 05, 2007 by 

import numpy as N
from numpy import ma as MA
import pyfits

import spectrum
import locations


class Icat(spectrum.TabularSourceSpectrum):

    def __init__(self,args):

        filename = locations.CAT_TEMPLATE.replace('*',args[0])

        table = pyfits.open(filename)

        indexList = table[1].data.field('INDEX')
        filenameList = table[1].data.field('FILENAME')

        indices = self._getArgs(indexList, filenameList)

        list0,list1 = self._breakList(indices, 0, args[1])

        list2,list3 = self._breakList(list0, 1, args[2])
        list4,list5 = self._breakList(list1, 1, args[2])

        list6,list7   = self._breakList(list2, 2, args[3])
        list8,list9   = self._breakList(list3, 2, args[3])
        list10,list11 = self._breakList(list4, 2, args[3])
        list12,list13 = self._breakList(list5, 2, args[3])

        sp1 = self._getSpectrum(list6[0],  args[0])
        sp2 = self._getSpectrum(list7[0],  args[0])
        sp3 = self._getSpectrum(list8[0],  args[0])
        sp4 = self._getSpectrum(list9[0],  args[0])
        sp5 = self._getSpectrum(list10[0], args[0])
        sp6 = self._getSpectrum(list11[0], args[0])
        sp7 = self._getSpectrum(list12[0], args[0])
        sp8 = self._getSpectrum(list13[0], args[0])

        spa1 = self._interpolateSpectrum(sp1, sp2, args[3])
        spa2 = self._interpolateSpectrum(sp3, sp4, args[3])
        spa3 = self._interpolateSpectrum(sp5, sp6, args[3])
        spa4 = self._interpolateSpectrum(sp7, sp8, args[3])

        spa5 = self._interpolateSpectrum(spa1, spa2, args[2])
        spa6 = self._interpolateSpectrum(spa3, spa4, args[2])

        spa7 = self._interpolateSpectrum(spa5, spa6, args[1])

        sp = spa7[0]

        self._wavetable = sp.GetWaveSet()
        self._fluxtable = sp(self._wavetable)
        self.waveunits = sp.waveunits
        self.fluxunits = sp.fluxunits

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

        array = N.empty(shape=[len(inList),],dtype=N.float32)
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

        filename = locations.KUR_TEMPLATE.replace('*',basename + '/' + filename)

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





