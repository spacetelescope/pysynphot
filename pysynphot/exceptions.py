"""Custom exceptions for ``pysynphot`` to raise."""

# TODO: error message about BaseException
class PysynphotError(Exception):
    """Parent class for ``pysynphot`` exceptions.

    Parameters
    ----------
    msg : str
        Error message.

    """
    def __init__(self,msg):
        Exception.__init__(self,msg)


# Exceptions to do with table access.

class TableFormatError(PysynphotError):
    """Exception to do with table access.

    Parameters
    ----------
    msg : str
        Error message.

    rows : list
        Rows with wrong values.

    """
    def __init__(self, msg, rows=None):
        PysynphotError.__init__(self, msg)

        # Save rows with wrong values as an attribute so calling code
        # can access it directly
        self.rows = rows

        # Also make this info go into the visibly displayed message in
        # Python 2.7 (self.args) and Python 2.5/6 (self.message)
        args = list(self.args)
        args.append("Invalid entries at or about row: "+str(rows))

        self.args = tuple(args)
        self.message = self.args


class DuplicateWavelength(TableFormatError):
    """Exception for duplicate wavelength values in table."""
    pass


class ZeroWavelength(TableFormatError):
    """Exception for wavelength values containing zero."""
    pass


class UnsortedWavelength(TableFormatError):
    """Exception for wavelength values not in ascending or descending order."""
    pass


class BadRow(TableFormatError):
    """Exception for invalid row in table."""
    pass


# Exceptions to do with overlap checking

class OverlapError(PysynphotError):
    """Exception to do with overlap checking."""
    pass


class PartialOverlap(OverlapError):
    """Exception for partial overlap between two spectra."""
    pass


class DisjointError(OverlapError):
    """Exception for no overlap between two spectra."""
    pass


# Exceptions to do with graph table traversal

class GraphtabError(PysynphotError):
    """Exception to do with graph table traversal."""
    pass


class UnusedKeyword(GraphtabError):
    """Exception for unused keyword in graph table lookup."""
    pass


class IncompleteObsmode(GraphtabError):
    """Exception for incomplete observation mode in graph table lookup."""
    pass


class AmbiguousObsmode(GraphtabError):
    """Exception for ambiguous observation mode in graph table lookup."""
    pass


# Exceptions for undefined optional values

class UndefinedBinset(PysynphotError):
    """Exception for undefined ``binset`` in bandpass or observation."""
    pass


# Exceptions for interpolation/extrapolation

class ExtrapolationNotAllowed(PysynphotError):
    """Exception for invalid extrapolation."""
    pass


# Exceptions for catalog problems

class ParameterOutOfBounds(PysynphotError):
    """Exception for invalid parameter value in a catalog."""
    pass


# if two sources in Composite* spectrum shouldn't go together

class IncompatibleSources(PysynphotError):
    """Exception for operation on two incompatible spectra types."""
    pass
