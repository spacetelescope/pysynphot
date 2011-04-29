"""Custom exceptions for pysynphot to raise"""


class PysynphotError(Exception):
    """parent class"""
    pass

class TableFormatError(PysynphotError):
    def __init__(self, msg, rows=None):
        Exception.__init__(self, msg)

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
    pass

class ZeroWavelength(TableFormatError):
    pass


class UnsortedWavelength(TableFormatError):
    pass

class BadRow(TableFormatError):
    pass
