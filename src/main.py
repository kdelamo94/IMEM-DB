from database import Database
from database import InvalidRollbackError


if __name__ == "__main__":
    db = Database()
    operations = {
        "SET": 0,
        "GET": 1,
        "UNSET": 2,
        "COUNT": 3
    }

    print("Ready for commands:")
    command = input("> ")
    while not command.upper() == "END":


        commandTokens = command.split()
        op = None
        try:
            op = commandTokens[0]
        except IndexError:
            print("Malformed command, no operation specified!")

        if op is not None:
            #Handle SET operation
            if op.upper() == "SET":
                var = None
                value = None
                try:
                    var = commandTokens[1]
                    value = int(commandTokens[2])
                    db.SET(var, value)
                except ValueError:
                    print("Invalid value, please use an integer!")
                except IndexError:
                    print("Malformed command, missing operation parameter!")

            #Handle GET operation
            if op.upper() == "GET":
                try:
                    var = commandTokens[1]
                    value = db.GET(var)
                    if(value):
                        print(value)
                    else:
                        print("NULL")
                except IndexError:
                    print("Malformed Command, missing operation parameter!")

            #Handle UNSET operation
            if op.upper() == "UNSET":
                try:
                    var = commandTokens[1]
                    db.UNSET(var)
                except IndexError:
                    print("Malformed Command, missing operation parameter!")

            #Handle COUNT operation
            if op.upper() == "COUNT":
                value = None
                try:
                    value = int(commandTokens[1])
                    count = db.COUNT(value)
                    print(count)
                except ValueError:
                    print("Invalid value, please use an integer!")
                except IndexError:
                    print("Malformed command, missing operation parameter!")

            #Handle BEGIN operation
            if op.upper() == "BEGIN":
                db.BEGIN()

            #Handle ROLLBACK operation
            if op.upper() == "ROLLBACK":
                try:
                    db.ROLLBACK()
                except InvalidRollbackError as err:
                    print(err.message)

            #Handle COMMIT operation
            if op.upper() == "COMMIT":
                db.COMMIT()

        command = input("> ")
