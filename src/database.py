from collections import defaultdict

class Database:
    def __init__(self):
        self.database = {}
        self.valueCount = defaultdict(int)


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
