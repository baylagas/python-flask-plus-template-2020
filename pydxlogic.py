from pydatabasex import DatabaseX


class Logic:
    def __init__(self):
        self.__databaseXObj = self.createDatabaseX()

    def get_databaseXObj(self):
        return self.__databaseXObj

    def createDatabaseX(self):
        database = DatabaseX()
        return database
