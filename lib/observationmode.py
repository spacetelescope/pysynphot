## Automatically adapted for numpy.numarray Mar 05, 2007 by 

import string
import glob
import re
import os
import numpy as N
import pyfits

import spectrum
import units
import locations
from locations import irafconvert
import planck
import wavetable

#Flag to control verbosity
DEBUG = False

rootdir = locations.rootdir
datadir = locations.specdir
wavecat = locations.wavecat

# Component tables are defined here.
def _refTable(template):
    names = glob.glob(os.path.join(rootdir,template))
    names.sort()
    try:
        return names[-1]
    except IndexError:
        msg= "No files found for %s."%os.path.join('PYSYN_CDBS',template)
        raise IOError(msg)
    
GRAPHTABLE = _refTable(os.path.join('mtab','*_tmg.fits'))
COMPTABLE  = _refTable(os.path.join('mtab','*_tmc.fits'))
try:
    THERMTABLE = _refTable(os.path.join('mtab','*_tmt.fits'))
except IOError, e:
    THERMTABLE = None
    print "Warning: %s"%str(e)
    print "         No thermal calculations can be performed."
    
CLEAR = 'clear'


class CompTable(object):
    '''CompTable class; opens the specified comptable and populates 1-d
    arrays of component names and file names in the members compnames
    and filenames'''

    def __init__(self, CFile=None):
        '''__init__ instantiates the CompTable object, given the comptable
        file name as an input string.

        Input:   string CFile containing comptable name
        Effect:  populates two data members: compnames and filenames
                 Both are 1-d chararrays'''

        cp = pyfits.open(CFile)

        self.compnames = cp[1].data.field('compname')
        self.filenames = cp[1].data.field('filename')
        compdict = {}
        for i in range(len(self.compnames)):
            compdict[self.compnames[i]] = self.filenames[i]

        cp.close()
        self.name=CFile

class GraphTable(object):
    '''GraphTable class; opens the specified graph table and populates
    1-d arrays of keyword names, innodes, outnodes and component names
    in the members keywords, innodes, outnodes and compnames'''

    def __init__(self, GFile=None):
        ''' __init__ instantiates the GraphTable object, given the graph
        table name as an input string.

        Input:  string GFile containing graph table name
        Effect: populates four data members:
                keywords: CharArray of keyword names
                innodes:  Int32 array of innodes
                outnodes: Int32 array of outnodes
                compnames:CharArray of components names'''

        gp = pyfits.open(GFile)

        self.keywords = gp[1].data.field('keyword')
        self.innodes = gp[1].data.field('innode')
        self.outnodes = gp[1].data.field('outnode')
        self.compnames = gp[1].data.field('compname')
        self.thcompnames = gp[1].data.field('thcompname')

        # keywords must be forced to lower case (STIS keywords are
        # mixed mode %^&^(*^*^%%%@#$!!!)
        for i in range(len(self.keywords)):
            self.keywords[i] = self.keywords[i].lower()


##        for comp in self.compnames:
##            try:
##                if comp.index('nic') == 0:
##                    print comp
##            except:
##                pass

        # prints components associated with a given keyword
##        i = -1
##        for keyword in self.keywords:
##            i = i + 1
##            if keyword == 'acs':
##                print self.compnames[i]

        gp.close()

    def GetNextNode(self, modes, innode):
        '''GetNextNode returns the outnode that matches an element from
        the modes list, starting at the given innode.
        This method isnt actually used, its just a helper method for
        debugging purposes'''
        nodes = N.where(self.innodes == innode)

        ## If there's no entry for the given innode, return -1
        if nodes[0].size == 0:
            return -1

        ## If we don't match anything in the modes list, we find the
        ## outnode corresponding the the string 'default'
        defaultindex = N.where(self.keywords[nodes] == 'default')

        if len(defaultindex[0]) != 0:
            outnode = self.outnodes[nodes[0][defaultindex[0]]]

        ## Now try and match one of the strings in the modes list with
        ## the keywords corresponding to the list of entries with the given
        ## innode
        for mode in modes:
            result = self.keywords[nodes].count(mode)
            if result != 0:
                index = N.where(self.keywords[nodes]==mode)
                outnode = self.outnodes[nodes[0][index[0]]]
                

        ## Return the outnode corresponding either to the matched mode,
        ## or to 'default'
        return outnode

    def GetComponentsFromGT(self, modes, innode):
        '''GetComponentsFromGT returns two lists of component names
        corresponding to those obtained by waling down the graph
        table starting at innode. The first list contains the optical
        components, the second list, the thermal components.'''
        components = []
        thcomponents = []
        outnode = 0
        inmodes=set(modes)
        used_modes=set()
        count = 0
        while outnode >= 0:
            if (DEBUG and (outnode < 0)):
                print "outnode == %d: stop condition"%outnode
       
            previous_outnode = outnode

            nodes = N.where(self.innodes == innode)

            # If there are no entries with this innode, we're done
            if nodes[0].size == 0:
                if DEBUG:
                    print "no such innode %d: stop condition"%innode
                #return (components,thcomponents)
                break

            # Find the entry corresponding to the component named
            # 'default', bacause thats the one we'll use if we don't
            # match anything in the modes list
            defaultindex = N.where(self.keywords[nodes] =='default')

            if 'default' in self.keywords[nodes]:
                dfi=N.where(self.keywords[nodes] == 'default')[0][0]
                outnode = self.outnodes[nodes[0][dfi]]
                component = self.compnames[nodes[0][dfi]]
                thcomponent = self.thcompnames[nodes[0][dfi]]
                used_default=True
            else:
                #There's no default, so fail if you don't match anything
                # in the keyword matching step.
                outnode = -2
                component = thcomponent = None

            # Now try and match something from the modes list
            for mode in modes:

                if mode in self.keywords[nodes]:
                    used_modes.add(mode)
                    index = N.where(self.keywords[nodes]==mode)
                    if len(index[0])>1:
                        raise KeyError('%d matches found for %s'%(len(index[0]),mode))
                    idx=index[0][0]
                    component = self.compnames[nodes[0][idx]]
                    thcomponent = self.thcompnames[nodes[0][idx]]
                    outnode = self.outnodes[nodes[0][idx]]
                    used_default=False

            if DEBUG:
                print "Innode %d  Outnode %d  Compname %s"%(innode, outnode, component)
            components.append(component)
            thcomponents.append(thcomponent)


            innode = outnode

            if outnode == previous_outnode:
                if DEBUG:
                    print "Innode: %d  Outnode:%d  Used default: %s"%(innode, outnode,used_default)
                count += 1
                if count > 3:
                    if DEBUG:
                        print "same outnode %d > 3 times: stop condition"%outnode
                    break

        if (outnode < 0):
            if DEBUG:
                print "outnode == %d: stop condition"%outnode
            raise ValueError("Incomplete obsmode %s"%str(modes))

        
        #Check for unused modes
        if inmodes != used_modes:
            unused=str(inmodes.difference(used_modes))
            raise ValueError("Warning: unused keywords %s"%unused)
        
        return (components,thcomponents)

class BaseObservationMode(object):
    ''' Class that handles the graph table, common to both optical and
    thermal obsmodes.
    '''
    def __init__(self, obsmode, method='HSTGraphTable',graphtable=None):
        #Strip "band()" syntax if present
        tmatch=re.search(r'band\((.*?)\)',obsmode,re.IGNORECASE)
        if tmatch:
            obsmode=tmatch.group(1)
        self._obsmode = obsmode

        if graphtable is None:
            graphtable=GRAPHTABLE

        self.area = units.HSTAREA

        # For sensitivity calculations: 5.03411762e7 is hc in
        # the appropriate units
        self._constant = 5.03411762e7 * self.area
        self.pardict={}

        modes = obsmode.lower().split(',')
        if '#' in obsmode:
            self.modes=[]
            for m in modes:
                if '#' in m:
                    key,val=m.split('#')
                    self.pardict[key]=float(val)
                    self.modes.append("%s#"%key)
                else:
                    self.modes.append(m)
        else:
            self.modes=modes

        gt = GraphTable(graphtable)
        self.gtname=graphtable
        
        self.compnames,self.thcompnames = gt.GetComponentsFromGT(self.modes,1)

        self.components = None #Will be filled by subclasses
        self.pixscale = None

    def __str__(self):
        return self._obsmode


    def __len__(self):
        return len(self.components)

    def _getFileNames(self, comptable, compnames):
        files = []
        for compname in compnames:
            if compname not in [None, '', CLEAR]:
                index = N.where(comptable.compnames == compname)
                try:
                    iraffilename = comptable.filenames[index[0][0]]
                    filename = irafconvert(iraffilename)
                    files.append(filename.lstrip())
                except IndexError:
                    raise IndexError("Can't find %s in comptable %s"%(compname,comptable.name))
            else:
                files.append(CLEAR)

        return files

    def GetFileNames(self):
        return self._throughput_filenames

    def showfiles(self):
        """ Duplicate synphot showfiles behavior"""
        for name in self._throughput_filenames:
            if name != 'clear':
                print name

    def bandWave(self):
        """ Return the binned waveset most appropriate for the obsmode,
        as defined by the wavecat.dat file. """
        
        obm=self._obsmode.lower()

        try:
            coeff = wavetable.wavetable[obm]
        except KeyError,e:
            print "Warning, %s"%str(e)
            return None

        if coeff.startswith('('):
            return self._computeBandwave(coeff)
        else:
            return self._getBandwaveFomFile(coeff)

    def _computeBandwave(self, coeff):
        (a,b,c,nwave) = self._computeQuadraticCoefficients(coeff)

        result = N.zeros(shape=[nwave,], dtype=N.float64)

        for i in range(nwave):
            result[i] = ((a * i) + b) * i + c

        return result

    def _computeQuadraticCoefficients(self, coeff):

        coefficients = (coeff[1:][:-1]).split(',')

        c0 = float(coefficients[0])
        c1 = float(coefficients[1])
        c2 = (c1 - c0) / 1999.0    # arbitraily copied from synphot....
        c3 = c2
        if len(coefficients) > 2:
            c2 = float(coefficients[2])
            c3 = c2
        if len(coefficients) > 3:
            c3 = float(coefficients[3])
            
        nwave = int(2.0 * (c1 - c0) / (c3 + c2)) + 1

        c = c0
        b = c2
        a = (c3 * c3 - c2 * c2) / (4.0 * (c1 - c0))

        return (a,b,c,nwave)

    def _getBandwaveFomFile(self, filename):
        name = irafconvert(filename)

        fs = open(name, mode='r')
        lines = fs.readlines()
        tokens = []
        for line in lines:
            if not line.startswith('#'):
                token = line.split('\n')[0]
                tokens.append(string.atof(token))

        return N.array(tokens)


class ObservationMode(BaseObservationMode):

    def __init__(self, obsmode, method='HSTGraphTable',graphtable=None,
                 comptable=None):

        if graphtable is None:
            graphtable=GRAPHTABLE
        if comptable is None:
            comptable=COMPTABLE

        BaseObservationMode.__init__(self, obsmode, method, graphtable)

        ct = CompTable(comptable)
        self.ctname = comptable
        
        self._throughput_filenames = self._getFileNames(ct, self.compnames)

        self.components = self._getOpticalComponents(self._throughput_filenames)

    def _getOpticalComponents(self, throughput_filenames):
        components = []
        for throughput_name in throughput_filenames:
            if throughput_name.endswith('#]'):
                barename,parkey=throughput_name.split('[')
                parkey=parkey[:-2]
            else:
                parkey=None
            component = _Component(throughput_name,
                                   interpval=self.pardict.get(parkey))

            if not component.isEmpty():
                components.append(component)

        return components

    def Sensitivity(self):
        '''Calculate the sensitivity by combining the throughput curves
        with hc/lambda to convert erg/cm^2/sec/Angstrom to counts/sec.
        Multiplying this by the flux in erg/cm^2/sec/Angstrom will give
        counts/sec/Angstrom'''
        sensitivity = spectrum.TabularSpectralElement()

        product = self._multiplyThroughputs()

        sensitivity.wavetable = product.GetWaveSet()
        sensitivity.throughputtable = product(sensitivity.wavetable) * \
                                      sensitivity.wavetable * self._constant

        return sensitivity

    def Throughput(self):
        '''Throughput returns the TabularSpectralElement obtained by
        multiplying the SpectralElement components together.  Unitless'''
        try:
            throughput = spectrum.TabularSpectralElement()

            product = self._multiplyThroughputs(0)

            throughput.wavetable = product.GetWaveSet()
            throughput.throughputtable = product(throughput.wavetable)
            throughput.name='*'.join([str(x) for x in self.components])

##            throughput = throughput.resample(spectrum.default_waveset)

            return throughput

        except IndexError:   # graph table is broken.
            return None


    def _multiplyThroughputs(self, index):
        product = self.components[index].throughput
        if len(self.components) > index:
            for component in self.components[index+1:]:
                if component.throughput != None:
                    product = product * component.throughput
        return product

        
    def ThermalSpectrum(self):
        try:
            # delegate to subclass.
            thom = _ThermalObservationMode(self._obsmode)
            self.pixscale = thom.pixscale
            return thom._getSpectrum()
        except IndexError:   # graph table is broken.
            raise IndexError("Cannot calculate thermal spectrum; graphtable may be broken")


class _ThermalObservationMode(BaseObservationMode):

    def __init__(self, obsmode, method='HSTGraphTable',graphtable=None,
                 comptable=None, thermtable=None):

        if graphtable is None:
            graphtable = GRAPHTABLE
        if comptable is None:
            comptable = COMPTABLE
        if thermtable is None:
            thermtable = THERMTABLE
                        
            

        BaseObservationMode.__init__(self, obsmode, method, graphtable)

        ct = CompTable(comptable)
        self.ctname=comptable
        
        throughput_filenames = self._getFileNames(ct, self.compnames)

        thct = CompTable(thermtable)
        self.thname = thermtable
        
        thermal_filenames = self._getFileNames(thct, self.thcompnames)

        self.components = self._getThermalComponents(throughput_filenames, \
                                                     thermal_filenames)

        self.pixscale = self._getPixelScale()

    def _getPixelScale(self):
        obsmode = self._obsmode.split(',')
        obsmode = str(obsmode[0]) + ',' + str(obsmode[1])

        fname=os.path.join(locations.specdir,'detectors.dat')
        fs = open(fname,mode='r')
        lines = fs.readlines()
        fs.close()
        
        regx = re.compile(r'\S+', re.IGNORECASE)
        for line in lines:
            try:
                tokens = regx.findall(line)
                if tokens[0] == obsmode:
                    break
            except Exception, e:
                raise ValueError("Error processing %s: %s"%(fname,str(e)))

        return float(tokens[1])

    def _getThermalComponents(self, throughput_filenames, thermal_filenames):
        components = []
        for i in range(len(throughput_filenames)):
            throughput_name = throughput_filenames[i]
            thermal_name = thermal_filenames[i]

            component = _ThermalComponent(throughput_name, thermal_name, \
                                          self._rampFilterWavelength)
            if not component.isEmpty():
                components.append(component)

        return components

    def _multiplyThroughputs(self):
        ''' Overrides base class in order to deal with opaque components.
        '''
        index = 0
        for component in self.components:
            if component.throughput != None:
                break
            index += 1

        return BaseObservationMode._multiplyThroughputs(self, index)

    def _getSpectrum(self):
        sp = spectrum.TabularSourceSpectrum()
        sp._wavetable = self._getWavesetIntersection()
        sp._fluxtable = N.zeros(shape=sp._wavetable.shape,dtype=N.float64)

        sp.waveunits = units.Units('angstrom')
        sp.fluxunits = units.Units('photlam')

        minw = sp._wavetable[0]
        maxw = sp._wavetable[-1]

        for component in self.components:
            # transmissive section
            if component.throughput != None:
                sp = sp * component.throughput

                sp = spectrum.trimSpectrum(sp, minw, maxw)

            # thermal section
            if component.emissivity != None:
                bb = self._bb(sp.GetWaveSet(), component.emissivity.temperature)
 
                sp_comp = component.emissivity.beamFillFactor * bb * \
                          component.emissivity

                sp = sp + sp_comp

                sp = spectrum.trimSpectrum(sp, minw, maxw)

        return sp

    def _getWavesetIntersection(self):
        minw = spectrum.default_waveset[0]
        maxw = spectrum.default_waveset[-1]

        for component in self.components[1:]:
            if component.emissivity != None:
                wave = component.emissivity.GetWaveSet()

                minw = max(minw, wave[0])
                maxw = min(maxw, wave[-1])

        result = self._mergeEmissivityWavesets()

        result = N.compress(result > minw, result)
        result = N.compress(result < maxw, result)

        # intersection with vega spectrum (why???)
        vegasp = spectrum.TabularSourceSpectrum(locations.VegaFile)
        vegaws = vegasp.GetWaveSet()
        result = N.compress(result > vegaws[0], result)
        result = N.compress(result < vegaws[-1], result)

        return result

    def _mergeEmissivityWavesets(self):
        index = 1
        for component in self.components:
            emissivity = component.emissivity
            if emissivity == None:
                index = index + 1
            else:
                result = emissivity.GetWaveSet()
                break;

        for component in self.components[index:]:
            if component.emissivity != None:
                result = spectrum.MergeWaveSets(result, \
                         component.emissivity.GetWaveSet())
        return result

    def _bb(self, wave, temperature):
        sp = spectrum.TabularSourceSpectrum()
        sp._wavetable = wave
        sp._fluxtable = planck.bb_photlam_arcsec(wave, temperature)
        return sp


class _Component(object):
    def __init__(self, throughput_name, interpval):
        self.throughput_name = throughput_name

        self._empty = True

        self.throughput = self._buildThroughput(throughput_name, interpval)

    def __str__(self):
        return str(self.throughput)
    
    def _buildThroughput(self, name, interpval):
        if name != CLEAR:
            if interpval is None:
                self._empty = False
                return spectrum.TabularSpectralElement(name)
            else:
                self._empty = False
                return spectrum.InterpolatedSpectralElement(name, interpval)
        else:
            return None

    def isEmpty(self):
        return self._empty


class _ThermalComponent(_Component):

    def __init__(self, throughput_name, thermal_name, rampFilterWavelength):
        self.throughput_name = throughput_name
        self.thermal_name = thermal_name

        self._empty = True

        self.throughput = self._buildThroughput(throughput_name, rampFilterWavelength)

        if thermal_name != CLEAR:
            self._empty = False
            self.emissivity = spectrum.ThermalSpectralElement(thermal_name)
        else:
            self.emissivity = None











