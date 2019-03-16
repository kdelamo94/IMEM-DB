from collections import defaultdict
from iMemDbError import InvalidRollbackError
from iMemDbError import InvalidCommitError

class Database:

    """
    Initializes the db, value-freq dictionary, and the transaction
    stack
    """
    def __init__(self):

        #Stores a map of variable names and data values
        self.database = {}

        #Stores a map of data values and the number of times those values occur
        self.valueCount = defaultdict(int)

        #Stores a stack containing states of the database
        self.transactionStack = []

    """
    Method to set values in the database, also maintains a value freq
    table to reflect this change
    """
    def SET(self, var, value):
        #Check if var is in the database
        if var in self.database:
            #var is in the db decrement freq of its value
            self.valueCount[self.database[var]] -= 1

        #set var to new val, increment that vals freq
        self.database[var] = value
        self.valueCount[value] += 1

    """
    Method to set value in db back to null. Also update value-freqeuency
    table to reflect this change.
    """
    def UNSET(self, var):
        #Check if var exists in db
        if var in self.database:
            #Set it to None if so, decrement freq of its value
            self.valueCount[self.database[var]] -= 1
            self.database[var] = None

    """
    Returns the value of variable found in database. Returns None if
    not found.
    """
    def GET(self, var):
        #Check if var is not in database
        if var not in self.database:
            return None
        return self.database[var]

    """
    Return number of times a value appears in db in O(1) or constant time
    """
    def COUNT(self, value):
        #return value count, defaults to 0
        return self.valueCount[value]

    """
    Pushes a copy of the database state onto the transaction stack
    so that it may be rolled back to when commanded.
    """
    def BEGIN(self):
        #append a copy of database to the transaction stack
        self.transactionStack.append(
            [
                self.database.copy(),
                self.valueCount.copy()
            ]
        )

    """
    Pops the most recently saved state of the transaction stack and
    sets the database equal to it.
    Raises:
    InvalidRollbackError - stack is empty when called.
    """
    def ROLLBACK(self):

        if self.transactionStack:
            #transaction stack is not empty
            self.database, self.valueCount = self.transactionStack.pop()
        else:
            #transaction stack is empty
            raise InvalidRollbackError("INVALID ROLLBACK")

    """
    Simply pops all saved states of the database off of the stack
    Raises:
    InvalidCommitError - stack is empty when called.
    """
    def COMMIT(self):

        if not self.transactionStack:
            #transaction stack is empty
            raise InvalidCommitError("NOTHING TO COMMIT")

        while not self.transactionStack:
            self.transactionStack.pop()
