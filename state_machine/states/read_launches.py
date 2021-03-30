from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
from state_machine.states.read_database import ReadDbBody
import os

class LaunchesBody(ReadDbBody):

    def __init__(self):

        menu_dict = {"1": "All data", "2": "By flight number", "3": "By status", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        self.error = ""
        self.table = "launches"

        if self.choice == 1 and self.error == "":
            self.connection_to_db()
            self.all_data()
        if self.choice == 2 and self.error == "":
            self.connection_to_db()
            menu_list = [["Enter flight number"]]
            Menu(menu_list, " MENU - {} ".format(str(self)))
            self.choice = input(">>> Enter flight number: ")
            self.by_column_value(self, "flight_number", self.choice)
        if self.choice == 3 and self.error == "":
            self.connection_to_db()
            menu_list = [["Enter status"],["True", "False"]]
            Menu(menu_list, " MENU - {} ".format(str(self)))
            self.choice = input(">>> Enter success status: ")
            self.by_column_value(self, "success", self.choice)
        else:
            pass


    def all_data(self):
        menu_dict = {"1": "Sort by id", "2": "Sort by flight_number", "3": "Sort by date_utc", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        order_type = "DESC"


        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")

        try:
            if "Sort" in menu_dict[self.choice]:
                order_by = menu_dict[self.choice][8:]
                columns = DataImport("SELECT_{}.txt".format(self.table.upper()), "list", "db_configuration")
                self.read_from_table(self.table, columns(), order_by, "", "ORDER", order_type)
        except KeyError:
            pass

    def by_column_value(self, column = "serial", value = "B1051"):
        '''
        :param column: sugestions: serial, flight_number, status, id
        :param value: 
        :return:  print tables in console
        '''
        columns = DataImport("SELECT_{}.txt".format(self.table.upper()), "list", "db_configuration")
        self.read_from_table(self.table, columns(), column, value)



if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")

    test = LaunchesBody()
    test.on_user_choice()






    os.chdir("state_machine")
    os.chdir("states")