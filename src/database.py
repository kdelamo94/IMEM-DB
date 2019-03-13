class Database:
    def __init__(self):
        self.database = {}

    def SET(self, var, value):
        self.database[var] = value

    def UNSET(self, var):
        self.database[var] = None

    def GET(self, var):
        return self.database[var]
