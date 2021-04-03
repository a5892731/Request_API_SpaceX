from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
from state_machine.states.read_database import ReadDbBody
import os

class BoostersBody(ReadDbBody):

    def __init__(self):

        menu_dict = {"1": "All data", "2": "By serial", "3": "By status", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        self.error = ""
        self.table = "boosters"

        if self.choice == "1" and self.error == "":
            self.connection_to_db()
            self.all_data()
        if self.choice == "2" and self.error == "":
            self.connection_to_db()
            menu_list = [["Enter booster serial number"]]
            Menu(menu_list, " MENU - {} ".format(str(self)))
            self.choice = input(">>> Enter serial: ")
            self.by_column_value("serial", self.choice)
        if self.choice == "3" and self.error == "":
            self.connection_to_db()
            menu_dict = {"1": "active", "2": "inactive", "3": "lost", "4": "expended"}
            sub_menu_list = [key + ": " + menu_dict[key] for key in menu_dict]
            menu_list = [sub_menu_list]
            Menu(menu_list, " MENU - {} ".format(str(self)))
            self.choice = input(">>> Enter status: ")
            try:
                self.by_column_value("status", menu_dict[self.choice])
            except KeyError:
                pass
        else:
            pass


    def all_data(self):
        menu_dict = {"1": "Sort by id", "2": "Sort by reuse_count", "3": "Sort by serial", "4": "Go Back"}
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

    test = BoostersBody()







    os.chdir("state_machine")
    os.chdir("states")