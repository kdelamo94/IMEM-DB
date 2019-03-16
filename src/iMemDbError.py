class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidRollbackError(Error):

    def __init__(self, message):
        self.message = message

class InvalidCommitError(Error):

    def __init__(self, message):
        self.message = message
