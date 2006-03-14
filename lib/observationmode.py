import pyfits
import numarray
import spectrum
import units
import locations

rootdir = locations.rootdir

GRAPHTABLE = rootdir + 'mtab/p1s1748gm_tmg.fits'
COMPTABLE  = rootdir + 'mtab/p1s1748hm_tmc.fits'


def irafconvert(iraffilename):
    '''Convert the IRAF file name (in directory$file format) to its
    unix equivalent

    Input:    string iraffilename
    Output:   returns string unixfilename
              If '$' not found in the input string, just return
              the input string
              Non-string input raises an AttributeError'''

    ## This dictionary maps IRAF-specific directory names for synphot
    ## directories into their unix equivalents

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
                  'crgridkc96$':rootdir+'grid/kc96/'}

    ## If no $ sign found, just return the filename unchanged
    unixfilename = iraffilename

    dollarpos = iraffilename.find('$')

    if dollarpos != -1:
        irafdir = iraffilename[:dollarpos+1]
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

    def GetComponents(self, modes, innode):
        '''GetComponents returns a list of component names corresponding
        to those obtained by waling down the graph table starting at
        innode'''
        components = []
        outnode = 0

        while outnode != -1:

            nodes = numarray.where(self.innodes == innode)

            ## If there are no entries with this innode, we're done
            if nodes[0].nelements() == 0:
                return components

            ## Find the entry corresponding to the component named
            ## 'default', bacause thats the one we'll use if we don't
            ## match anything in the modes list
            defaultindex = self.keywords[nodes].match('default')[0]

            if defaultindex.nelements() != 0:
                outnode = self.outnodes[nodes[0][defaultindex[0]]]
                component = self.compnames[nodes[0][defaultindex[0]]]

            ## Now try and match something from the modes list
            for mode in modes:
                result = self.keywords[nodes].count(mode)
                if result != 0:
                    index = self.keywords[nodes].match(mode)[0]
                    component = self.compnames[nodes[0][index[0]]]
                    outnode = self.outnodes[nodes[0][index[0]]]

            ## We only include components that aren't named 'clear'
            if component != 'clear':
                components.append(component)
            innode = outnode

        return components

class ObservationMode(object):
    '''The ObservationMode class handles converting the given obsmode
    into a list of component file names'''

    def __init__(self, obsmode, method='HSTGraphTable',graphtable=None):
        '''__init__ populates the files data member given the obsmode'''

        self.area = units.HSTAREA

        # For sensitivity calculations: 5.03411762e7 is hc in
        # the appropriate units
        self._constant = 5.03411762e7 * self.area

        # Convert the comma-delimited obsmode string into a list of
        # lowercase strings
        modes = obsmode.lower().split(',')

        # For the moment the graph table and component table names are hardcoded
        gt = GraphTable(GRAPHTABLE)
        components = gt.GetComponents(modes,1)
        ct = CompTable(COMPTABLE)

        # Turn the list of components found by traversing the graph
        # table into a list of filenames by reading the component table
        self.files = []

        for component in components:
            index = numarray.where(ct.compnames == component)
            iraffilename = ct.filenames[index[0][0]]

            ## Convert iraf file name in the component table into a
            ## Unix file name
            filename = irafconvert(iraffilename)
            self.files.append(filename)

    def GetFiles(self):
        '''Helper function to provide an interface to the list of files'''
        return self.files

    def GetComponents(self):
        '''Return a list of s obtained from the
        list of component file names'''
        Components = []

        for file in self.files:
            Components.append(spectrum.TabularSpectralElement(file))

        return Components

    def Sensitivity(self):
        '''Calculate the sensitivity by combining the throughput curves
        with hc/lambda to convert erg/cm^2/sec/Angstrom to counts/sec.
        Multiplying this by the flux in erg/cm^2/sec/Angstrom will give
        counts/sec/Angstrom'''
        sensitivity = spectrum.TabularSpectralElement()

        product = self._multiplyComponents()

        sensitivity.wavetable = product.GetWaveSet()
        sensitivity.throughputtable = product(sensitivity.wavetable) * \
        sensitivity.wavetable * self._constant

        return sensitivity

    def Throughput(self):
        '''Throughput returns the TabularSpectralElement obtained by
        multiplying the SpectralElement components together.  Unitless'''
        throughput = spectrum.TabularSpectralElement()

        product = self._multiplyComponents()

        throughput.wavetable = product.GetWaveSet()
        throughput.throughputtable = product(throughput.wavetable)

        return throughput

    def _multiplyComponents(self):
        components = self.GetComponents()
        product = components[0]
        for component in components[1:]:
            product = product * component
        return product







