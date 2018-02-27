"""This module is useful for working with catalog spectra such as
:ref:`pysynphot-appendixa-ck04`, :ref:`pysynphot-appendixa-kurucz1993`, and
:ref:`pysynphot-appendixa-phoenix`.

Spectra are constructed from basis spectra which are indexed for various
combinations of effective temperature (:math:`T_{\\textnormal{eff}}`),
metallicity (``[M/H]``), and log surface gravity (:math:`\\log g`).
The user may specify any combination of :math:`T_{\\textnormal{eff}}`,
``[M/H]``, and :math:`\\log g` so long as each parameter is within the range
for that parameter defined by the catalog.

For example, the :ref:`pysynphot-appendixa-ck04` catalog contains spectra for
effective temperatures between 3500 and 50000 K. In this case, no spectrum can
be constructed for :math:`T_{\\textnormal{eff}}` of 50001 K or 3499 K.
The range of parameters available may vary from catalog to catalog.

More information on catalogs can be found in :ref:`pysynphot-appendixa`.

"""
from __future__ import division

import os
import numpy as N
from astropy.io import fits as pyfits

from . import spectrum
from . import locations

from .Cache import CATALOG_CACHE

import pysynphot.exceptions as exceptions


class Icat(spectrum.TabularSourceSpectrum):
    """This class constructs a model from the grid available in
    :ref:`catalogs <pysynphot-spec-atlas>`.
    Specifically, they are :ref:`pysynphot-appendixa-ck04`,
    :ref:`pysynphot-appendixa-kurucz1993`, and
    :ref:`pysynphot-appendixa-phoenix`.

    Each grid contains a master file named "catalog.fits", as
    defined by ``pysynphot.locations.CAT_TEMPLATE``.
    The basis spectra are located at ``pysynphot.locations.KUR_TEMPLATE``.
    You may inspect the data files in CRDS to see how they
    are formatted.

    Parameters
    ----------
    catdir : {'ck04models', 'k93models', 'phoenix'}
        Name of directory holding the catalogs.

    Teff : float
        Effective temperature of model, in Kelvin.

    metallicity : float
        Metallicity of model.

    log_g : float
        Log surface gravity of model.

    Attributes
    ----------
    name : str
        Short description of the spectrum.

    parameter_names : list of str
        Names for model parameters. This is used for error reporting.

    warnings : dict
        To store warnings.

    isAnalytic : bool
        This is always `False`.

    waveunits, fluxunits : `~pysynphot.units.Units`
        Catalog units for wavelength and flux.

    wave, flux : array_like
        Wavelength set and associated flux in catalog units.

    Raises
    ------
    pysynphot.exceptions.ParameterOutOfBounds
        Given parameter value is out of bounds.

    Examples
    --------
    >>> spec = S.Icat('k93models', 6440, 0, 4.3)

    """
    def __init__(self,catdir,Teff,metallicity,log_g):
        self.isAnalytic=False

        # this is useful for reporting in exceptions which parameter is
        # causing the problems.
        self.parameter_names = ['Teff','metallicity','log G']

        filename = locations.CAT_TEMPLATE.replace('*',catdir)
        self.name="%s(Teff=%g,metallicity=%g,logG=%g)"%(catdir,Teff,metallicity,log_g)

        if filename in CATALOG_CACHE:
            indices = CATALOG_CACHE[filename]
        else:
            table = pyfits.open(filename)

            indexList = table[1].data.field('INDEX')
            filenameList = table[1].data.field('FILENAME')

            table.close()

            indices = self._getArgs(indexList, filenameList)

            CATALOG_CACHE[filename] = indices

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

        for i,index in enumerate(indices):
            list1 = [float(x) for x in index.split(',')]
            list1.append(filenames[i])
            results.append(list1)

        return results

    def _breakList(self, inList, index, parameter):
        par = float(parameter)

        array = [parameters[index] for parameters in inList]
        array = N.array(array, dtype=N.float64)

        upperArray = array[array >= par]
        lowerArray = array[array <= par]

        if upperArray.size == 0:
            maxAllowed = array.max()
            s = "Parameter '%s' exceeds data. Max allowed=%f, entered=%f."
            s = s % (self.parameter_names[index], maxAllowed, parameter)
            raise exceptions.ParameterOutOfBounds(s)

        elif lowerArray.size == 0:
            minAllowed = array.min()
            s = "Parameter '%s' exceeds data. Min allowed=%f, entered=%f."
            s = s % (self.parameter_names[index], minAllowed, parameter)
            raise exceptions.ParameterOutOfBounds(s)

        upper = upperArray.min()
        lower = lowerArray.max()

        upperList = []
        lowerList = []

        for i,parameters in enumerate(inList):
            if array[i] >= par and array[i] <= upper:
                upperList.append(parameters)
            if array[i] >= lower and array[i] <= par:
                lowerList.append(parameters)

        return upperList, lowerList

    def _getSpectrum(self, parlist, basename):
        name = parlist[3]

        filename = name.split('[')[0]
        column = name.split('[')[1][:-1]

        filename = locations.KUR_TEMPLATE.replace('*',
                                                  os.path.join(basename,filename))
        sp = spectrum.TabularSourceSpectrum(filename, fluxname=column)

        totflux = sp.integrate()
        if not N.isfinite(totflux) or totflux <= 0:
            raise exceptions.ParameterOutOfBounds(
                "Parameter '{0}' has no valid data.".format(parlist))

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
