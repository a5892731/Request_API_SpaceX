from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
import os
from time import sleep

class GetConnectionDataBody(object):

    '''
    function creates connection and build database with tables if needed
    '''

    def __init__(self, api_data = {}):

        self.api_data = api_data
        self.error = ""
        self.connection_to_db()

    def connection_to_db(self):
        Menu([["Connecting ..."]]," MENU - {} ".format(str(self))) # drow menu

        connection_parameters = DataImport("CONNECTION_DATA.txt", "dict", "db_configuration")
        tables = DataImport("TABLES.txt", "dict", "db_configuration")
        # -----------------------------------------------------------------------------------------------------------

        db = Database(connection_parameters()["database"], connection_parameters()["host"],
                        connection_parameters()["user"], "", tables()) # connection_parameters()["password"]
        try:
            connection = db.create_connection_to_server("")  # connection_parameters()["password"]
        except AttributeError:
            pass

        if "error" in db.status:
            self.error += db.status + "\n"
        # -----------------------------------------------------------------------------------------------------------
        else:
            Menu([[db.status]]," MENU - {} ".format(str(self))) # drow menu

            create_database_query = "CREATE DATABASE {}".format(connection_parameters()["database"])
            db.create_database(connection, create_database_query, tables(), "") # connection_parameters()["password"]

            Menu([[db.status]]," MENU - {} ".format(str(self))) # drow menu
            if "error" in db.status:
                self.error += db.status + "\n"
            # -----------------------------------------------------------------------------------------------------------
            if db.status == "Database created successfully":
                db.connection = db.create_connection_to_db("") # connection_parameters()["password"]

                for key in tables(): # if database just been created then you need to build db tables too
                    db.create_table(key, tables())


                    if "error" in db.status:
                        self.error += key + ": " + db.status + "\n\n"
                    Menu([[db.status], [self.error]], " MENU - {} ".format(str(self)))  # drow menu
            # -----------------------------------------------------------------------------------------------------------
            self.db = db
            sleep(1)


    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__


if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")

    test = GetConnectionDataBody()

    os.chdir("state_machine")
    os.chdir("states")