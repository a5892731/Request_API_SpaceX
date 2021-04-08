from system.menu import Menu
from state_machine.states.read_db.read_database import ReadDbBody
import os

class PayloadsBody(ReadDbBody):

    def __init__(self):

        menu_dict = {"1": "All data", "2": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        self.error = ""
        self.table = "payloads"

        if self.choice == "1" and self.error == "":
            menu_dict = {"1": "Sort by table_id", "2": "Sort by mass_kg", "3": "Sort by name"}
            self.connection_to_db()
            self.all_data(menu_dict)
        else:
            pass



if __name__ == "__main__":

    os.chdir("../../..")
    os.chdir("../../..")

    test = PayloadsBody()







    os.chdir("state_machine")
    os.chdir("states")