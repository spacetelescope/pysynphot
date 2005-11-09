import spectrum
import math
import numarray

C = 2.99792458e10

def Units(Inunits):

    if Inunits == 'flam': return Flam()
    if Inunits == 'fnu': return Fnu()
    if Inunits == 'photlam' : return Photlam()
    if Inunits == 'jy' : return Jy()
    if Inunits == 'abmag' : return ABMag()
    if Inunits == 'stmag' : return STMag()
    if Inunits == 'angstroms' : return Angstroms()
    if Inunits == 'hz' : return Hz()
    print 'Unknown units: ' + Inunits
    return None

class Flam:

    def __init__(self):

        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'jy':self.ToJy,
                         'abmag':self.ToABMag,
                         'stmag':self.ToSTMag}
    
    def ToFlam(self, InSpectrum):
        '''This is the default, so just return input spectrum.
        Units are erg cm^-2 s^-1 Ang^-1'''
        return InSpectrum

    def ToFnu(self, InSpectrum):
        '''Convert to Fnu.
        Flux units are erg cm^-2 s^-1 Hz^-1
        Wavelength units are Hz'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = (C*1.0e8)/InSpectrum.wavetable[::-1]
        Temp = (InSpectrum.wavetable**2)*InSpectrum.fluxtable/(C*1.0e8)
        OutSpectrum.fluxtable = Temp[::-1]
        OutSpectrum.fluxunits = Units('fnu')
        OutSpectrum.waveunits = Units('hz')
        
        return OutSpectrum

    def ToPhotlam(self, InSpectrum):
        '''Convert to PhotLam.
        Flux units are photons cm^-2 s^-1 Ang^-1
        Wavelength units are unchanged'''

        constant = 5.03411762e7
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = InSpectrum.fluxtable * constant \
                                * InSpectrum.wavetable
        OutSpectrum.fluxunits = Units('photlam')
        OutSpectrum.waveunits = InSpectrum.waveunits
        
        return OutSpectrum

    def ToJy(self, InSpectrum):
        '''Convert to Jy
        Flux units are Jy (10^-23 erg cm^-2 s^-1 Hz^-1
        Wavelength units are unchanged'''

        OutSpectrum = self.Convert(InSpectrum, 'fnu')
        OutSpectrum.fluxtable = OutSpectrum.fluxtable * 1.0e23
        OutSpectrum.fluxunits = Units('jy')
        OutSpectrum.waveunits = InSpectrum.waveunits
        
        return OutSpectrum
    
    def ToABMag(self, InSpectrum):
        '''Convert to ABMag
        Flux units are ABMag
        Wavelength units are unchanged'''
        
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        Temp = (InSpectrum.wavetable**2)*InSpectrum.fluxtable/(C*1.0e8)
        OutSpectrum.fluxtable = -48.6 -2.5*numarray.log10(Temp)
        OutSpectrum.fluxunits = Units('abmag')
        OutSpectrum.waveunits = InSpectrum.waveunits

        return OutSpectrum

    def ToSTMag(self, InSpectrum):
        '''Convert to STMag
        Flux units are STMag
        Wavelength units are unchanged'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = -21.10 - \
                                2.5*numarray.log10(InSpectrum.fluxtable)
        OutSpectrum.fluxunits = Units('stmag')
        OutSpectrum.waveunits = InSpectrum.waveunits
        return OutSpectrum
    
    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum

class Fnu:
        
    def __init__(self):

        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'jy':self.ToJy,
                         'abmag':self.ToABMag,
                         'stmag':self.ToSTMag}
    
    def ToFlam(self, InSpectrum):
        '''Convert to Flam
        Units are erg cm^-2 s^-1 Ang^-1
        Wavelength units are angstroms'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = (C*1.0e8)/InSpectrum.wavetable[::-1]
        Temp = InSpectrum.fluxtable*(InSpectrum.wavetable)**2/(C*1.0e8)
        OutSpectrum.fluxtable = Temp[::-1]
        OutSpectrum.fluxunits = Units('flam')
        OutSpectrum.waveunits = Units('angstroms')
        return OutSpectrum

    def ToFnu(self, InSpectrum):
        '''Convert to Fnu.
        Flux units are erg cm^-2 s^-1 Hz^-1
        Wavelength units are Hz'''

        return InSpectrum

    def ToPhotlam(self, InSpectrum):
        '''Convert to PhotLam.
        Flux units are photons cm^-2 s^-1 Ang^-1
        Wavelength units are unchanged'''

        constant = 5.03411762e7
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = InSpectrum.fluxtable * constant \
                                * InSpectrum.wavetable
        OutSpectrum.fluxunits = Units('photlam')
        OutSpectrum.waveunits = InSpectrum.waveunits
        return OutSpectrum

    def ToJy(self, InSpectrum):
        '''Convert to Jy
        Flux units are Jy (10^-23 erg cm^-2 s^-1 Hz^-1
        Wavelength units are unchanged'''
        
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = InSpectrum.fluxtable * 1.0e23
        OutSpectrum.fluxunits = Units('jy')
        OutSpectrum.waveunits = InSpectrum.waveunits
        return OutSpectrum
    
    def ToABMag(self, InSpectrum):
        '''Convert to ABMag
        Flux units are ABMag
        Wavelength units are unchanged'''
        
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = -48.60 - \
                                2.5*numarray.log10(InSpectrum.fluxtable)
        OutSpectrum.fluxunits = Units('abmag')
        OutSpectrum.waveunits = InSpectrum.waveunits

        return OutSpectrum

    def ToSTMag(self, InSpectrum):
        '''Convert to STMag
        Flux units are STMag
        Wavelength units are angstroms'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.waveunits = InSpectrum.waveunits
        if isinstance(OutSpectrum.waveunits,Angstroms):
            print "It's an Angstroms instance"
        elif isinstance(OutSpectrum.waveunits,Hz):
            print "It's a Hz instance"
        else:
            print "I don't know what the wavelength units are"
        
        return None
    
    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum

class Photlam:

    def __init__(self):


        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'jy':self.ToJy,
                         'abmag':self.ToABMag,
                         'stmag':self.ToSTMag}
    
    def ToFlam(self, InSpectrum):
        '''Convert to Flam
        Units are erg cm^-2 s^-1 Ang^-1'''
        constant = 5.03411762e7
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = InSpectrum.fluxtable / InSpectrum.wavetable \
                                / constant
        OutSpectrum.fluxunits = Units('flam')
        OutSpectrum.waveunits = InSpectrum.waveunits
        return OutSpectrum

    def ToFnu(self, InSpectrum):
        '''Convert to Fnu.
        Flux units are erg cm^-2 s^-1 Hz^-1
        Wavelength units are Hz'''
        constant = 5.03411762e7
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = (C*1.0e8)/InSpectrum.wavetable[::-1]
        Temp = (InSpectrum.wavetable**3)*InSpectrum.fluxtable \
               /(C*1.0e8)/constant
        OutSpectrum.fluxtable = Temp[::-1]
        OutSpectrum.fluxunits = Units('fnu')
        OutSpectrum.waveunits = Units('hz')
        return InSpectrum

    def ToPhotlam(self, InSpectrum):
        '''Convert to PhotLam.
        Flux units are photons cm^-2 s^-1 Ang^-1
        Wavelength units are Angstrom'''
        return InSpectrum

    def ToJy(self, InSpectrum):
        '''Convert to Jy
        Flux units are Jy (10^-23 erg cm^-2 s^-1 Hz^-1
        Wavelength units are Hz'''
        print 'Conversion not implemented yet'
        
        return None
    
    def ToABMag(self, InSpectrum):
        '''Convert to ABMag
        Flux units are ABMag
        Wavelength units are unchanged'''
        
        print 'Conversion not implemented yet'

        return None

    def ToSTMag(self, InSpectrum):
        '''Convert to STMag
        Flux units are STMag
        Wavelength units are Angstrom'''

        print 'Conversion not implemented yet'

        return None
    
    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum

class Jy:
        
    def __init__(self):

        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'jy':self.ToJy,
                         'abmag':self.ToABMag,
                         'stmag':self.ToSTMag}
    
    def ToFlam(self, InSpectrum):
        '''Convert to Flam
        Units are erg cm^-2 s^-1 Ang^-1'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = (C*1.0e8)/InSpectrum.wavetable[::-1]
        Temp = InSpectrum.fluxtable*(InSpectrum.wavetable)**2/(C*1.0e8)
        OutSpectrum.fluxtable = Temp[::-1]
        OutSpectrum.fluxunits = Units('flam')
        OutSpectrum.waveunits = Units('angstroms')
        return OutSpectrum

    def ToFnu(self, InSpectrum):
        '''Convert to Fnu.
        Flux units are erg cm^-2 s^-1 Hz^-1
        Wavelength units are Hz'''
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = InSpectrum.fluxtable * 1.0e-23
        
        return OutSpectrum

    def ToPhotlam(self, InSpectrum):
        '''Convert to PhotLam.
        Flux units are photons cm^-2 s^-1 Ang^-1
        Wavelength units are Angstrom'''

        constant = 5.03411762e7
        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = InSpectrum.fluxtable * constant \
                                * InSpectrum.wavetable
        OutSpectrum.fluxunits = Units('photlam')
        return OutSpectrum

    def ToJy(self, InSpectrum):
        '''Convert to Jy
        Flux units are Jy'''

        return InSpectrum

    def ToABMag(self, InSpectrum):
        '''Convert to ABMag
        Flux units are ABMag
        Wavelength units are unchanged'''
        
        print 'Conversion not implemented yet'

        return None

    def ToSTMag(self, InSpectrum):
        '''Convert to STMag
        Flux units are STMag
        Wavelength units are Angstrom'''

        print 'Conversion not implemented yet'

        return None
    
    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum

class ABMag:
        
    def __init__(self):

        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'jy':self.ToJy,
                         'abmag':self.ToABMag,
                         'stmag':self.ToSTMag}
    
    def ToFlam(self, InSpectrum):
        '''Convert to Flam
        Units are erg cm^-2 s^-1 Ang^-1'''

        return None

    def ToFnu(self, InSpectrum):
        '''Convert to Fnu.
        Flux units are erg cm^-2 s^-1 Hz^-1
        Wavelength units are Hz'''
        return None

    def ToPhotlam(self, InSpectrum):
        '''Convert to PhotLam.
        Flux units are photons cm^-2 s^-1 Ang^-1
        Wavelength units are Angstrom'''

        return None

    def ToJy(self, InSpectrum):
        '''Convert to Jy
        Flux units are Jy'''

        return None

    def ToABMag(self, InSpectrum):
        '''Convert to ABMag
        Flux units are ABMag
        Wavelength units are unchanged'''
        
        return InSpectrum

        return None

    def ToSTMag(self, InSpectrum):
        '''Convert to STMag
        Flux units are STMag
        Wavelength units are Angstrom'''

        print 'Conversion not implemented yet'

        return None
    
    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum
    
class STMag:
        
    def __init__(self):

        self.Dispatch = {'flam': self.ToFlam,
                         'fnu': self.ToFnu,
                         'photlam': self.ToPhotlam,
                         'jy':self.ToJy,
                         'abmag':self.ToABMag,
                         'stmag':self.ToSTMag}
    
    def ToFlam(self, InSpectrum):
        '''Convert to Flam
        Units are erg cm^-2 s^-1 Ang^-1'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = InSpectrum.wavetable
        OutSpectrum.fluxtable = 10.0**(-0.4*(InSpectrum.fluxtable + 21.10))
        OutSpectrum.fluxunits = Units('flam')
        OutSpectrum.waveunits = InSpectrum.waveunits
        
        return OutSpectrum

    def ToFnu(self, InSpectrum):
        '''Convert to Fnu.
        Flux units are erg cm^-2 s^-1 Hz^-1
        Wavelength units are Hz'''
        return None

    def ToPhotlam(self, InSpectrum):
        '''Convert to PhotLam.
        Flux units are photons cm^-2 s^-1 Ang^-1
        Wavelength units are Angstrom'''

        return None

    def ToJy(self, InSpectrum):
        '''Convert to Jy
        Flux units are Jy'''

        return None

    def ToABMag(self, InSpectrum):
        '''Convert to ABMag
        Flux units are ABMag
        Wavelength units are unchanged'''
        
        print 'Conversion not implemented yet'

        return None

    def ToSTMag(self, InSpectrum):
        '''Convert to STMag
        Flux units are STMag
        Wavelength units are Angstrom'''

        return InSpectrum
    
    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum

class Angstroms:

    def __init__(self):

        self.Dispatch = {'angstroms' : self.ToAngstroms,
                         'hz': self.ToHz}

    def ToAngstroms(self, InSpectrum):
        '''Return original spectrum object'''

        return InSpectrum
    
    def ToHz(self, InSpectrum):
        '''Convert wavetable to Hz
        Units are Hz'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = (C*1.0e8)/InSpectrum.wavetable[::-1]
        OutSpectrum.waveunits = Units('hz')
        OutSpectrum.fluxtable = InSpectrum.fluxtable[::-1]
        OutSpectrum.fluxunits = InSpectrum.fluxunits
        
        return OutSpectrum

    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum

class Hz:

    def __init__(self):

        self.Dispatch = {'angstroms': self.ToAngstroms,
                         'hz' : self.ToHz}
    
    def ToAngstroms(self, InSpectrum):
        '''Convert wavetable to Angstroms
        Units are Angstroms'''

        OutSpectrum = spectrum.TabularSourceSpectrum()
        OutSpectrum.wavetable = (C*1.0e8)/InSpectrum.wavetable[::-1]
        OutSpectrum.waveunits = Units('angstroms')
        OutSpectrum.fluxtable = InSpectrum.fluxtable[::-1]
        OutSpectrum.fluxunits = InSpectrum.fluxunits
        
        return OutSpectrum

    def ToHz(self, InSpectrum):
        '''Return original spectrum object'''

        return InSpectrum

    def Convert(self, InSpectrum, TargetUnits):

        if self.Dispatch.has_key(TargetUnits):
            OutSpectrum = self.Dispatch[TargetUnits](InSpectrum)
        else:
            print 'Units ' + TargetUnits + ' not recognized'
            raise KeyError
        return OutSpectrum
