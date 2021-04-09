from system.menu import Menu
from state_machine.states.read_db.read_database import ReadDbBody
from system.read_data_files import DataImport

import os
from datetime import date

class LaunchesBody(ReadDbBody):

    def __init__(self):

        self.table = "launches"
        self.error = ""
        self.choice = ""
        self.query = ""
        self.go_back = False

        self.initialization()

    def initialization(self):
        menu_dict = {"1": "All data", "2": "By flight number", "3": "By status", "4": "By Future Flights"}
        secondary_menu_dict = {"5": "By Past Flights", "6": "Go Back", "7": "-", "8": "-"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict],
                     [key + ": " + secondary_menu_dict[key] for key in secondary_menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")

        if self.choice == "1" and self.error == "":
            self.all_data()
        elif self.choice == "2" and self.error == "":
            self.by_flight_number()
        elif self.choice == "3" and self.error == "":
            self.by_status()
        elif self.choice == "4" and self.error == "":
            self.by_time(">")
        elif self.choice == "5" and self.error == "":
            self.by_time("<")
        elif self.choice == "6" and self.error == "":
            self.go_back = True
        else:
            self.go_back = True

    def all_data(self):
        data_view_limit = 5
        menu_dict = {"1": "Sort by id", "2": "Sort by flight_number", "3": "Sort by date_utc", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        try:
            self.choice = menu_dict[self.choice][7:]
        except KeyError:
            pass

        self.connection_to_db()
        column_list = DataImport("ALL_DATA_COLUMN_LIST.txt", "list", "db_configuration/{}".format(self.table))
        os.chdir("..")
        query = DataImport("ALL_DATA_QUERY.txt", "string", "db_configuration/{}".format(self.table))
        os.chdir("..")
        self.query = query().format(self.choice)

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit) # read and print in console


    def by_flight_number(self):
        data_view_limit = 5
        menu_list = [["Enter flight number"]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter flight number: ")

        self.connection_to_db()
        column_list = DataImport("BY_FLIGHT_NUMBER_COLUMN_LIST.txt", "list", "db_configuration/{}".format(self.table))
        os.chdir("..")
        query = DataImport("BY_FLIGHT_NUMBER_QUERY.txt", "string", "db_configuration/{}".format(self.table))
        os.chdir("..")

        self.query = query().format(self.choice)

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit)  # read and print in console



    def by_status(self):
        data_view_limit = 5

        menu_list = [["Enter status"], ["True: success / False: lost"]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter success status: ")

        self.connection_to_db()
        column_list = DataImport("BY_STATUS_COLUMN_LIST.txt", "list", "db_configuration/{}".format(self.table))
        os.chdir("..")
        query = DataImport("BY_STATUS_QUERY.txt", "string", "db_configuration/{}".format(self.table))
        os.chdir("..")

        self.query = query().format(self.choice)

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit) # read and print in console


    def by_time(self, time_condition = ">"): # where > is future and < is past
        data_view_limit = 5
        today = date.today()

        column_list = DataImport("BY_FUTURE_COLUMN_LIST.txt", "list", "db_configuration/{}".format(self.table))
        os.chdir("..")
        query = DataImport("BY_FUTURE_QUERY.txt", "string", "db_configuration/{}".format(self.table))
        os.chdir("..")

        self.connection_to_db()
        self.query = query().format(time_condition, str(today.strftime("%Y-%m-%d")))

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit) # read and print in console





if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


    test = LaunchesBody()





    os.chdir("state_machine")
    os.chdir("states")
    os.chdir("read_db")
    os.chdir("boosters")