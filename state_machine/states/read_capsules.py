from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
from state_machine.states.read_database import ReadDbBody
import os

class CapsulesBody(ReadDbBody):

    def __init__(self):

        menu_dict = {"1": "All data", "2": "By serial", "3": "By status", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        self.error = ""
        self.table = "capsules"


        if self.choice == "1" and self.error == "":
            menu_dict = {"1": "Sort by table_id", "2": "Sort by reuse_count", "3": "Sort by serial", "4": "Go Back"}
            self.connection_to_db()
            self.all_data(menu_dict)
        if self.choice == "2" and self.error == "":
            self.connection_to_db()
            menu_list = [["Enter capsule serial number"]]
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





if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")

    test = CapsulesBody()







    os.chdir("state_machine")
    os.chdir("states")