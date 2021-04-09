from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
import os

class ReadDbBody(object):

    def __init__(self):

        menu_dict = {"1": "Launches", "2": "Boosters", "3": "Capsules", "4": "Rockets",
                     "5": "Crew", "6": "Payloads", "7": "Ships", "8": "Launchpads",
                     "9": "Landpads", "10": "Main Menu",}


        menu_list = [["Menu list:"]]

        for key in menu_dict:
            menu_list.append([key + ": " + menu_dict[key]])

        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        self.error = ""
        self.table = ""


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

    def send_sql_query(self, query):
        '''
        :param query:
        query = SELECT columns FROM table BY column_name = column_value
        query = SELECT columns FROM table order BY column_name desc
        query = SELECT columns FROM table

        :return: server response
        '''
        response = self.db.execute_read_query(self.db.connection, query, "Read {} table completed".format(self.table))
        Menu([[self.db.status]], " MENU - {} ".format(str(self)))  # drow menu
        if "error" in self.db.status:
            self.error += self.db.status + "\n"
        return response



    def read_sql_response(self, response, table, columns, data_view_limit = 5):
        def print_data_and_wait(menu):
            m = Menu(menu, " MENU - {} ".format(str(self)))  # drow menu
            m.__del__()
            return input("Continue? Y/N: ")

        menu = [[table.capitalize() + " data:"]]
        counter = 0
        if response != None:
            for row in response:
                counter += 1
                for column_number in range(len(row)):

                    if str(row[column_number]) != "[]" and str(row[column_number]) != "None":
                        menu_segment = columns[column_number] + ": " + str(row[column_number])
                        menu.append([menu_segment])
                menu.append(["-" * Menu.menu_width])

                if counter >= data_view_limit:
                    self.choice = print_data_and_wait(menu)
                    if self.choice.upper() == "N":
                        counter = 0
                        break
                    menu = [[table.capitalize() + " data:"]]
                    counter = 0
            if counter > 0:
                self.choice = print_data_and_wait(menu)
        else:
            self.error += "None type object in response\n"





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




    os.chdir("state_machine")
    os.chdir("states")


