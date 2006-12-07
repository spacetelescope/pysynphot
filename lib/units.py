import math
import string
import numarray
import spectrum   # circular import is required for vegamag transformation 
import locations

C = 2.99792458e18 # speed of light in Angstrom/sec
H = 6.62620E-27   # Planck's constant
HC = H * C
ABZERO = -48.60   # magnitude zero points
STZERO = -21.10

HSTAREA = 45238.93416  # cm^2

# Wavelenghts must be expressed in Angstrom.

def Units(units):
    try:
        return factory(units) 
    except KeyError:
        print 'Unknown units: ' + units
        return None

def _getDeltaWave(wave):
    last = wave.shape[0]-1

    hold1 = numarray.array(shape=wave.shape, type='Float64')
    hold2 = numarray.array(shape=wave.shape, type='Float64')

    hold1[1::] = wave[0:last]
    hold2[0:last] = wave[1::]

    delta = (hold2 - hold1) / 2.0

    delta[0] = wave[1] - wave[0]
    delta[last] = wave[last] - wave[last-1]

    return delta


class _UnitsConverter(object):
    def Convert(self, wave, flux, TargetUnits):
        if self.Dispatch.has_key(TargetUnits):
            result = self.Dispatch[TargetUnits](wave, flux)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return result

class _ToInternalWaveUnitsConverter(_UnitsConverter):
    def __init__(self):
        self.Dispatch = {'angstrom' : self.ToAngstrom}
        self.isFlux = False

class _ToExternalWaveUnitsConverter(_UnitsConverter):
    def __init__(self):
        self.Dispatch = {'angstrom' : self.ToAngstrom,
                         'nm': self.ToNm,
                         'micron': self.ToMicron,
                         'mm': self.ToMm,
                         'cm': self.ToCm,
                         'm': self.ToMeter,
                         'hz': self.ToHz}
        self.isFlux = False

class _ToInternallFluxUnitsConverter(_UnitsConverter):
    def __init__(self):
        self.Dispatch = {'photlam': self.ToPhotlam}
        self.isFlux = True

class _ToExternalFluxUnitsConverter(_UnitsConverter):
    def __init__(self):
        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'photnu': self.ToPhotnu,
                         'jy':self.ToJy,
                         'mjy':self.TomJy,
                         'abmag':self.ToABMag,
                         'stmag':self.ToSTMag,
                         'obmag':self.ToOBMag,
                         'vegamag':self.ToVegaMag,
                         'counts':self.ToCounts}
        self.isFlux = True

class Photlam(_ToExternalFluxUnitsConverter):
    ''' photlam = photons cm^-2 s^-1 Ang^-1)'''
    def __init__(self):
        _ToExternalFluxUnitsConverter.__init__(self)
        self.name = 'photlam'
    
    def ToFlam(self, wave, flux):
        return HC * flux / wave

    def ToFnu(self, wave, flux):
        return H * flux * wave

    def ToPhotlam(self, wave, flux):
        return flux.copy() # No conversion, just copy the array.

    def ToPhotnu(self, wave, flux):
        return flux * wave * wave / C

    def ToJy(self, wave, flux):
        return 1.0e+23 * H * flux * wave
    
    def TomJy(self, wave, flux):
        return 1.0e+26 * H * flux * wave
    
    def ToABMag(self, wave, flux):
        arg = H * flux * wave
        return -1.085736 * numarray.log(arg) + ABZERO
    
    def ToSTMag(self, wave, flux):
        arg = H * C* flux / wave
        return -1.085736 * numarray.log(arg) + STZERO
    
    def ToOBMag(self, wave, flux):
        dw = _getDeltaWave(wave)
        arg = flux * dw * HSTAREA
        return -1.085736 * numarray.log(arg)

    def ToVegaMag(self, wave, flux):
        vegaspec = spectrum.TabularSourceSpectrum(locations.VegaFile)
        resampled = vegaspec.resample(wave)
        normalized = flux / resampled._fluxtable
        return -2.5 * numarray.log10(normalized)

    def ToCounts(self, wave, flux):
        return flux * _getDeltaWave(wave) * HSTAREA

class Flam(_ToInternallFluxUnitsConverter):
    ''' flam = erg cm^-2 s^-1 Ang^-1'''
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'flam'
    
    def ToPhotlam(self, wave, flux):
        return flux * wave / HC

class Photnu(_ToInternallFluxUnitsConverter):
    ''' photnu = photon cm^-2 s^-1 Hz^-1'''
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'photnu'
    
    def ToPhotlam(self, wave, flux):
        return C * flux / (wave * wave)

class Fnu(_ToInternallFluxUnitsConverter):
    ''' fnu = erg cm^-2 s^-1 Hz^-1'''
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'fnu'
    
    def ToPhotlam(self, wave, flux):
        return flux /wave / H

class Jy(_ToInternallFluxUnitsConverter):
    ''' jy = 10^-23 erg cm^-2 s^-1 Hz^-1'''
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'jy'

    def ToPhotlam(self, wave, flux):
        return flux / wave * (1.0e-23 / H)

class mJy(_ToInternallFluxUnitsConverter):
    ''' mjy = 10^-26 erg cm^-2 s^-1 Hz^-1'''
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'mjy'

    def ToPhotlam(self, wave, flux):
        return flux / wave * (1.0e-26 / H)

class ABMag(_ToInternallFluxUnitsConverter):
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'abmag'
    
    def ToPhotlam(self, wave, flux):
        return 1.0 / (H * wave) * 10.0**(-0.4 * (flux - ABZERO))

class STMag(_ToInternallFluxUnitsConverter):
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'stmag'
    
    def ToPhotlam(self, wave, flux):
        return wave / H / C * 10.0**(-0.4 * (flux - STZERO))

class OBMag(_ToInternallFluxUnitsConverter):
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'obmag'
    
    def ToPhotlam(self, wave, flux):
        dw = _getDeltaWave(wave)
        return 10.0**(-0.4 * flux) / (dw * HSTAREA)

class VegaMag(_ToInternallFluxUnitsConverter):
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'vegamag'
    
    def ToPhotlam(self, wave, flux):
        vegaspec = spectrum.TabularSourceSpectrum(locations.VegaFile)
        resampled = vegaspec.resample(wave)
        return resampled.fluxtable * 10.0**(-0.4 * flux)

class Counts(_ToInternallFluxUnitsConverter):
    def __init__(self):
        _ToInternallFluxUnitsConverter.__init__(self)
        self.name = 'counts'
    
    def ToPhotlam(self, wave, flux):
        return flux / (_getDeltaWave(wave) * HSTAREA)

class Angstrom(_ToExternalWaveUnitsConverter):
    def __init__(self):
        _ToExternalWaveUnitsConverter.__init__(self)
        self.name = 'angstrom'

    def ToAngstrom(self, wave, dummy):
        return wave
    
    def ToNm(self, wave, dummy):
        return wave / 10.0
    
    def ToMicron(self, wave, dummy):
        return wave * 1.0e-4
    
    def ToMm(self, wave, dummy):
        return wave * 1.0e-7
    
    def ToCm(self, wave, dummy):
        return wave * 1.0e-8
    
    def ToMeter(self, wave, dummy):
        return wave * 1.0e-10
    
    def ToHz(self, wave, dummy):
        return C / wave

class Hz(_ToInternalWaveUnitsConverter):
    def __init__(self):
        _ToInternalWaveUnitsConverter.__init__(self)
        self.name = 'hz'
    
    def ToAngstrom(self, wave, dummy):
        return C / wave

class _MetricWavelength(_ToInternalWaveUnitsConverter):
    def ToAngstrom(self, wave, dummy):
        return wave * self.factor

class Nm(_MetricWavelength):
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'nm'
        self.factor = 10.0
    
class Micron(_MetricWavelength):
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'micron'
        self.factor = 1.0e4

class Mm(_MetricWavelength):
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'mm'
        self.factor = 1.0e7

class Cm(_MetricWavelength):
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'cm'
        self.factor = 1.0e8

class Meter(_MetricWavelength):
    def __init__(self):
        _MetricWavelength.__init__(self)
        self.name = 'm'
        self.factor = 1.0e10


################   Factory for Units subclasses.   #####################

unitsClasses = {'flam'      : Flam,
                'fnu'       : Fnu,
                'photlam'   : Photlam,
                'photnu'    : Photnu,
                'jy'        : Jy,
                'mjy'       : mJy,
                'abmag'     : ABMag,
                'stmag'     : STMag,
                'obmag'     : OBMag,
                'vegamag'   : VegaMag,
                'counts'    : Counts,
                'angstrom'  : Angstrom,
                'angstroms' : Angstrom,
                'nm'        : Nm,
                'micron'    : Micron,
                'um'        : Micron,
                'mm'        : Mm,
                'cm'        : Cm,
                'm'         : Meter,
                'meter'     : Meter,
                'hz'        : Hz}

def factory(unit, *args, **kwargs):
    return apply(unitsClasses[string.lower(unit)], args, kwargs)

