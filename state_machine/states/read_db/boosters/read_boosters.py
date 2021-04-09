from system.menu import Menu
from state_machine.states.read_db.read_database import ReadDbBody
from system.read_data_files import DataImport

import os

class BoostersBody(ReadDbBody):

    def __init__(self):

        self.table = "boosters"
        self.error = ""
        self.choice = ""
        self.query = ""
        self.go_back = False

        self.initialization()

    def initialization(self):
        menu_dict = {"1": "All data", "2": "By serial", "3": "By status", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")

        if self.choice == "1" and self.error == "":
            self.all_data()
        elif self.choice == "2" and self.error == "":
            self.by_serial()
        elif self.choice == "3" and self.error == "":
            self.by_status()
        elif self.go_back == "4" and self.error == "":
            self.by_status()
        else:
            pass

    def all_data(self):
        data_view_limit = 5
        menu_dict = {"1": "Sort by table_id", "2": "Sort by reuse_count", "3": "Sort by serial", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        try:
            self.choice = menu_dict[self.choice][7:]
        except KeyError:
            pass

        self.connection_to_db()
        column_list = DataImport("ALL_DATA_COLUMN_LIST.txt", "list", "db_configuration/boosters")
        os.chdir("..")
        query = DataImport("ALL_DATA_QUERY.txt", "string", "db_configuration/boosters")
        os.chdir("..")
        self.query = query().format(self.choice)

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit) # read and print in console

    def by_serial(self):
        data_view_limit = 5
        menu_list = [["Enter booster serial number"]]

        column_list = DataImport("BY_SERIAL_COLUMN_LIST.txt", "list", "db_configuration/boosters")
        os.chdir("..")
        query = DataImport("BY_SERIAL_QUERY.txt", "string", "db_configuration/boosters")
        os.chdir("..")
        column_list2 = DataImport("BY_SERIAL_COLUMN_LIST_2.txt", "list", "db_configuration/boosters")
        os.chdir("..")
        query2 = DataImport("BY_SERIAL_QUERY_2.txt", "string", "db_configuration/boosters")
        os.chdir("..")
        rows = column_list()

        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter serial: ")

        self.connection_to_db()

        self.query = query().format(self.choice)
        response = self.send_sql_query(self.query)  # ask for booster data

        self.query = query2().format(self.choice)
        response2 = self.send_sql_query(self.query)  # ask for relation data from another table

        for object in response2:        # create response list for printing
            for element in object:
                response[0] += element,
        duplicats = len(response2)

        for number in range(int(duplicats)):
            for object in column_list2():
                rows.append(str(number + 1) + ") " + object )   # create row titles list for response

        self.read_sql_response(response, self.table, rows, data_view_limit) # read and print in console

    def by_status(self):
        data_view_limit = 5
        menu_dict = {"1": "active", "2": "inactive", "3": "lost", "4": "expended"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]

        self.connection_to_db()
        column_list = DataImport("ALL_DATA_COLUMN_LIST.txt", "list", "db_configuration/boosters")
        os.chdir("..")
        query = DataImport("ALL_DATA_QUERY.txt", "string", "db_configuration/boosters")
        os.chdir("..")

        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter serial: ")
        self.query = query().format(self.choice)

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit) # read and print in console

    def go_back(self):
        self.go_back = True










if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


    test = BoostersBody()





    os.chdir("state_machine")
    os.chdir("states")
    os.chdir("read_db")
    os.chdir("boosters")