from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
import os

class ReadDbBody(object):

    def __init__(self):
        self.error = ""
        self.connection_to_db()
        self.choice = ""

        if self.error == "":
            self.read_boosters()

    def connection_to_db(self):
        Menu([["Connecting ..."]], " MENU - {} ".format(str(self)))  # drow menu

        connection_parameters = DataImport("CONNECTION_DATA.txt", "dict", "db_configuration")
        tables = DataImport("TABLES.txt", "dict", "db_configuration")
        # ----------------------------------------------------------------------------CONNECTION---------------------

        self.db = Database(connection_parameters()["database"], connection_parameters()["host"],
                            connection_parameters()["user"], "", tables())  # connection_parameters()["password"]
        try:
            self.db.connection = self.db.create_connection_to_db("")  # connection_parameters()["password"]
        except AttributeError:
            self.error = "Error: cant find database"

        if "error" in self.db.status:
            self.error += self.db.status + "\n"
        # -----------------------------------------------------------------------------------------------------------



    def read_boosters(self, table = "boosters"):

        select = ""

        objects = DataImport("SELECT_{}.txt".format(table.upper()), "list", "db_configuration")
        for object in objects():
            select += object + ", "
        select = select.rstrip(", ")

        query = "SELECT {} FROM {} ORDER BY id DESC".format(select, table)
        response = self.db.execute_read_query(self.db.connection, query, "Read {} table completed".format(table))
        Menu([[self.db.status]], " MENU - {} ".format(str(self)))  # drow menu

        menu = [[table.capitalize() + " data:"]]
        counter = 0
        for row in response:
            counter += 1
            for column_number in range(len(row)):
                menu_segment = objects()[column_number] + ": " + str(row[column_number])
                menu.append([menu_segment])
            menu.append(["-" * Menu.menu_width])


            if counter >= 5:
                m = Menu(menu, " MENU - {} ".format(str(self)))  # drow menu
                m.__del__()
                self.choice = input("Continue? Y/N: ")
                if self.choice.upper() == "N":
                    break
                menu = [[table.capitalize() + " data:"]]
                counter = 0



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

    test = ReadDbBody()

    os.chdir("state_machine")
    os.chdir("states")