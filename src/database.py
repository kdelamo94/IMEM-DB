from collections import defaultdict

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidRollbackError(Error):
    def __init__(self, message):
        self.message = message

class InvalidCommitError(Error):
    def __init__(self, message):
        self.message = message

class Database:
    def __init__(self):

        #Stores a map of variable names and data values
        self.database = {}
        self.tempDatabase = {}

        #Stores a map of data values and the number of times those values occur
        self.valueCount = defaultdict(int)
        self.tempValueCount = defaultdict(int)

        #Stores a stack containing states of the database
        self.transactionStack = []

    #Method to set values in the database
    def SET(self, var, value):
        if var in self.database:
            self.valueCount[self.database[var]] -= 1
        self.database[var] = value
        self.valueCount[value] += 1

    def UNSET(self, var):
        if var in self.database:
            self.valueCount[self.database[var]] -= 1
            self.database[var] = None

    def GET(self, var):
        if var not in self.database:
            return None
        return self.database[var]

    def COUNT(self, value):
        return self.valueCount[value]

    def BEGIN(self):
        self.transactionStack.append(
            [
                self.database.copy(),
                self.valueCount.copy()
            ]
        )

    def ROLLBACK(self):
        if self.transactionStack:
            self.database, self.transactionStack = self.transactionStack.pop()
        else:
            raise InvalidRollbackError("INVALID ROLLBACK")

    def COMMIT(self):
        if not self.transactionStack:
            raise InvalidCommitError("NOTHING TO COMMIT")
        while not self.transactionStack:
            self.transactionStack.pop()
