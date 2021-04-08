from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
import os


class SetingsBody(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        self.error = ""
        self.status = ""

        menu_dict = {"1": "delete spacex database", "2": "go back"}
        menu = [key + ": " + menu_dict[key] for key in menu_dict]

        self.choice = self.print_data_and_wait([menu], "Enter menu choice: ")

        if self.choice == "1":
            self.connection_to_db()
            self.delete_db()
        else:
            pass

    def delete_db(self):

        try:
            self.db.del_db()
            self.status = "database <spacex> has been deleted"
        except AttributeError:
            self.status = "database <spacex> does not exist"

        self.choice = self.print_data_and_wait([[self.status]], "Continue? Y/N: ")


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

        self.status = self.db.status

    def print_data_and_wait(self, menu, input_text):
        m = Menu(menu, " MENU - {} ".format(str(self)))  # drow menu
        m.__del__()
        return input(input_text)

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

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

    os.chdir("../..")
    os.chdir("../..")

    SetingsBody()

    os.chdir("state_machine")
    os.chdir("states")