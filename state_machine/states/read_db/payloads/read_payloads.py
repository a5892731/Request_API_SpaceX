from system.read_data_files import DataImport
from state_machine.states.read_db.read_database import ReadDbBody
import os
from system.menu import Menu

class PayloadsBody(ReadDbBody):

    def __init__(self):

        self.table = "payloads"
        self.error = ""
        self.choice = ""
        self.query = ""
        self.go_back = False

        self.initialization()

    def initialization(self):
        menu_dict = {"1": "All data", "2": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")

        if self.choice == "1" and self.error == "":
            self.all_data()
        else:
            self.go_back = True

    def all_data(self):
        data_view_limit = 5
        menu_dict = {"1": "Sort by table_id", "2": "Sort by mass_kg", "3": "Sort by name"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        try:
            self.choice = "payloads." + menu_dict[self.choice][7:]
        except KeyError:
            pass

        self.connection_to_db()
        column_list = DataImport("ALL_DATA_COLUMN_LIST.txt", "list", "db_configuration/{}".format(self.table))
        os.chdir("..")
        query = DataImport("ALL_DATA_QUERY.txt", "string", "db_configuration/{}".format(self.table))
        os.chdir("..")
        self.query = query().format(self.choice)

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit)  # read and print in console


if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


    test = PayloadsBody()




    os.chdir("state_machine")
    os.chdir("states")
    os.chdir("read_db")
    os.chdir("boosters")
