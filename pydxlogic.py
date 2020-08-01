from pydatabasex import DatabaseX


class Logic:
    def __init__(self):
        self.__databaseXObj = self.__createDatabaseX()

    def get_databaseXObj(self):
        return self.__databaseXObj

    def __createDatabaseX(self):
        database = DatabaseX()
        return database
