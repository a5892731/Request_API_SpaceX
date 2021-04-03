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

        if self.choice == "1" and self.error == "":
            menu_dict = {"1": "Sort by id", "2": "Sort by flight_number", "3": "Sort by date_utc", "4": "Go Back"}
            self.connection_to_db()
            self.all_data(menu_dict)
        if self.choice == "2" and self.error == "":
            self.connection_to_db()
            menu_list = [["Enter flight number"]]
            Menu(menu_list, " MENU - {} ".format(str(self)))
            self.choice = input(">>> Enter flight number: ")
            self.by_column_value("flight_number", self.choice)
        if self.choice == "3" and self.error == "":
            self.connection_to_db()
            menu_list = [["Enter status"], ["True: success / False: lost"]]
            Menu(menu_list, " MENU - {} ".format(str(self)))
            self.choice = input(">>> Enter success status: ")
            self.by_column_value("success", self.choice)
        else:
            Menu([[".."]], " MENU - {} ".format(str(self)))



if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")

    test = LaunchesBody()
    #test.on_user_choice()






    os.chdir("state_machine")
    os.chdir("states")