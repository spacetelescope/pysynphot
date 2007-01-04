import string
import glob
import re
import numarray
import pyfits

import spectrum
import units
import locations
import planck
import wavetable

rootdir = locations.rootdir
userdir = locations.userdir
datadir = locations.specdir
wavecat = locations.wavecat

# Component tables are defined here.
def _refTable(template):
    names = glob.glob(rootdir + template)
    names.sort()
    return names[-1]

GRAPHTABLE = _refTable('mtab/*_tmg.fits')
COMPTABLE  = _refTable('mtab/*_tmc.fits') 
THERMTABLE = _refTable('mtab/*_tmt.fits')
CLEAR = 'clear'

def irafconvert(iraffilename):
    '''Convert the IRAF file name (in directory$file format) to its
    unix equivalent

    Input:    string iraffilename
    Output:   returns string unixfilename
              If '$' not found in the input string, just return
              the input string
              Non-string input raises an AttributeError'''

    ## This dictionary maps IRAF-specific directory names for synphot
    ## directories into their Unix equivalents.

    convertdic = {'crrefer$':rootdir,
                  'crotacomp$':rootdir+'comp/ota/',
                  'cracscomp$':rootdir+'comp/acs/',
                  'crcalobs$':rootdir+'calobs/',
                  'crcalspec$':rootdir+'calspec/',
                  'croldcalspec$':rootdir+'oldcalspec/',
                  'crcomp$':rootdir+'comp/',
                  'crfgs$':rootdir+'fgs/',
                  'crfields$':rootdir+'fields/',
                  'crmodewave$':rootdir+'modewave/',
                  'crcostarcomp$':rootdir+'comp/costar/',
                  'cracscomp$':rootdir+'comp/acs/',
                  'crfoccomp$':rootdir+'comp/foc/',
                  'crfoscomp$':rootdir+'comp/fos/',
                  'crfgscomp$':rootdir+'comp/fgs/',
                  'crhrscomp$':rootdir+'comp/hrs/',
                  'crhspcomp$':rootdir+'comp/hsp/',
                  'crotacomp$':rootdir+'comp/ota/',
                  'crnicmoscomp$':rootdir+'comp/nicmos/',
                  'crnonhstcomp$':rootdir+'comp/nonhst/',
                  'crstiscomp$':rootdir+'comp/stis/',
                  'crstiscomp$':rootdir+'comp/stis/',
                  'crwfc3comp$':rootdir+'comp/wfc3/',
                  'coscomp$':rootdir+'comp/cos/',
                  'crwave$':rootdir+'crwave/',
                  'crwfpccomp$':rootdir+'comp/wfpc/',
                  'crwfpc2comp$':rootdir+'comp/wfpc2/',
                  'crgrid$':rootdir+'grid/',
                  'crgridbz77$':rootdir+'grid/bz77/',
                  'crgridgs$':rootdir+'grid/gunnstryker/',
                  'crgridjac$':rootdir+'grid/jacobi/',
                  'crgridbpgs$':rootdir+'grid/bpgs/',
                  'crgridbk$':rootdir+'grid/bkmodels/',
                  'crgridk93$':rootdir+'grid/k93models/',
                  'crgridagn$':rootdir+'grid/agn/',
                  'crgridgalactic$':rootdir+'grid/galactic/',
                  'crgridkc96$':rootdir+'grid/kc96/',
                  'userFiles$':userdir+'userFiles/',
                  'synphot$': wavecat}

    ## If no $ sign found, just return the filename unchanged
    unixfilename = iraffilename

    dollarpos = iraffilename.find('$')

    if dollarpos != -1:
        irafdir = iraffilename[:dollarpos+1].lstrip()
        unixfilename = iraffilename.replace(irafdir,convertdic[irafdir])

    return unixfilename

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
        for i in range(self.compnames.nelements()):
            compdict[self.compnames[i]] = self.filenames[i]

        cp.close()

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
        nodes = numarray.where(self.innodes == innode)

        ## If there's no entry for the given innode, return -1
        if nodes[0].nelements() == 0:
            return -1

        ## If we don't match anything in the modes list, we find the
        ## outnode corresponding the the string 'default'
        defaultindex = self.keywords[nodes].match('default')[0]

        if defaultindex.nelements() != 0:
            outnode = self.outnodes[nodes[0][defaultindex[0]]]

        ## Now try and match one of the strings in the modes list with
        ## the keywords corresponding to the list of entries with the given
        ## innode
        for mode in modes:
            result = self.keywords[nodes].count(mode)
            if result != 0:
                index = self.keywords[nodes].match(mode)[0]
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
        self.rampFilterWavelength = None

        count = 0
        while outnode != -1:

            previous_outnode = outnode

            nodes = numarray.where(self.innodes == innode)
##            print
##            print "innode: ", innode, " nodes: ", nodes

            # If there are no entries with this innode, we're done
            if nodes[0].nelements() == 0:
                return (components,thcomponents)

            # Find the entry corresponding to the component named
            # 'default', bacause thats the one we'll use if we don't
            # match anything in the modes list
            defaultindex = self.keywords[nodes].match('default')[0]
##            print "default index is: ", defaultindex

            if defaultindex.nelements() != 0:
                outnode = self.outnodes[nodes[0][defaultindex[0]]]
                component = self.compnames[nodes[0][defaultindex[0]]]
##                print "component: ", component, " outnode: ", outnode
                thcomponent = self.thcompnames[nodes[0][defaultindex[0]]]

            # Now try and match something from the modes list
            for mode in modes:
##                print "mode: ", mode

                # handle #-separated ramp filter spec.
                modeFields = mode.lower().split('#')
                if len(modeFields) > 1:
                    mode = modeFields[0] + '#'
                    self.rampFilterWavelength = float(modeFields[1])

                result = self.keywords[nodes].count(mode)

                if result != 0:
                    index = self.keywords[nodes].match(mode)[0]
                    component = self.compnames[nodes[0][index[0]]]
                    thcomponent = self.thcompnames[nodes[0][index[0]]]
                    outnode = self.outnodes[nodes[0][index[0]]]
##                    print "from modes list:  index: ", index, "  component: ", component, " outnode: ", outnode
                    
            components.append(component)
            thcomponents.append(thcomponent)

            innode = outnode
 
            if outnode == previous_outnode:
                count += 1
                if count > 3:
                    break

        return (components,thcomponents)


class BaseObservationMode(object):
    ''' Class that handles the graph table, common to both optical and
    thermal obsmodes.
    '''
    def __init__(self, obsmode, method='HSTGraphTable',graphtable=None):

        self._obsmode = obsmode

        self.area = units.HSTAREA

        # For sensitivity calculations: 5.03411762e7 is hc in
        # the appropriate units
        self._constant = 5.03411762e7 * self.area

        modes = obsmode.lower().split(',')

        gt = GraphTable(GRAPHTABLE)

        self.compnames,self.thcompnames = gt.GetComponentsFromGT(modes,1)
        self._rampFilterWavelength = gt.rampFilterWavelength

        self.pixscale = None

    def _getFileNames(self, comptable, compnames):
        files = []
        for compname in compnames:
            if compname != None and compname != '' and compname != CLEAR:
                index = numarray.where(comptable.compnames == compname)
                try:
                    iraffilename = comptable.filenames[index[0][0]]
                    filename = irafconvert(iraffilename)
                    files.append(filename.lstrip())
                except IndexError:
                    files.append(CLEAR)
            else:
                files.append(CLEAR)

        return files

    def GetFileNames(self):
        return self._throughput_filenames

    def bandWave(self):

        # ETC-generated obsmodes for STIS must be massaged
        # before looking up in the wavetable. Ugly code below
        # begs for refactoring....

        obmlist = self._obsmode.lower().split(',')
        if ('ccd','fuvmama','nuvmama').__contains__(obmlist[1]):
            obmlist = [obmlist[0]] + obmlist[2:]

        if obmlist[0] == 'stis':            
            for element in obmlist[1:]:
                if element.startswith('s'):
                    obmlist.remove(element)

        obm = ""
        for element in obmlist:
            obm = obm + ',' + element
        obm = obm[1:]
        try:
            coeff = wavetable.wavetable[obm]
            if coeff.startswith('('):
                return self._computeBandwave(coeff)
            else:
                return self._getBandwaveFomFile(coeff)
        except KeyError:
            if obm.startswith('stis'):
                obm = ""
                for element in obmlist[:-1]:
                    obm = obm + ',' + element
                obm = obm[1:]

                try:
                    coeff = wavetable.wavetable[obm]

                    if coeff.startswith('('):
                        return self._computeBandwave(coeff)
                    else:
                        return self._getBandwaveFomFile(coeff)
                except KeyError:
                    return None
            else:
                return None

    def _computeBandwave(self, coeff):
        (a,b,c,nwave) = self._computeQuadraticCoefficients(coeff)

        result = numarray.zeros(shape=[nwave,], type='Float64')

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

        return numarray.array(tokens)


class ObservationMode(BaseObservationMode):

    def __init__(self, obsmode, method='HSTGraphTable',graphtable=None):

        BaseObservationMode.__init__(self, obsmode, method, graphtable)

        ct = CompTable(COMPTABLE)
        self._throughput_filenames = self._getFileNames(ct, self.compnames)

        self.components = self._getOpticalComponents(self._throughput_filenames)

    def _getOpticalComponents(self, throughput_filenames):
        components = []
        for throughput_name in throughput_filenames:
            component = _Component(throughput_name, self._rampFilterWavelength)

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
            return None


class _ThermalObservationMode(BaseObservationMode):

    def __init__(self, obsmode, method='HSTGraphTable',graphtable=None):

        BaseObservationMode.__init__(self, obsmode, method, graphtable)

        ct = CompTable(COMPTABLE)
        throughput_filenames = self._getFileNames(ct, self.compnames)

        thct = CompTable(THERMTABLE)
        thermal_filenames = self._getFileNames(thct, self.thcompnames)

        self.components = self._getThermalComponents(throughput_filenames, \
                                                     thermal_filenames)

        self.pixscale = self._getPixelScale()

    def _getPixelScale(self):
        obsmode = self._obsmode.split(',')
        obsmode = str(obsmode[0]) + ',' + str(obsmode[1])

        fs = open(locations.specdir + 'detectors.dat',mode='r')
        lines = fs.readlines()

        regx = re.compile(r'\S+', re.IGNORECASE)
        for line in lines:
            try:
                tokens = regx.findall(line)
                if tokens[0] == obsmode:
                    break
            except:
                pass

        fs.close()

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
        sp._fluxtable = numarray.zeros(shape=sp._wavetable.shape,type='Float32')

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

        result = numarray.compress(result > minw, result)
        result = numarray.compress(result < maxw, result)

        # intersection with vega spectrum (why???)
        vegasp = spectrum.TabularSourceSpectrum(locations.VegaFile)
        vegaws = vegasp.GetWaveSet()
        result = numarray.compress(result > vegaws[0], result)
        result = numarray.compress(result < vegaws[-1], result)

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

    def __init__(self, throughput_name, rampFilterWavelength):
        self.throughput_name = throughput_name

        self._empty = True

        self.throughput = self._buildThroughput(throughput_name, rampFilterWavelength)

    def _buildThroughput(self, name, rampFilterWavelength):
        if name != CLEAR:
            if len(name.split('[')) == 1:
                self._empty = False
                return spectrum.TabularSpectralElement(name)
            else:
                self._empty = False
                return spectrum.InterpolatedSpectralElement(name, rampFilterWavelength)
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











