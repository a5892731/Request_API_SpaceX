from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
from state_machine.states.read_database import ReadDbBody
import os

class LaunchpadsBody(ReadDbBody):

    def __init__(self):

        self.table = "launchpads"
        columns = DataImport("SELECT_{}.txt".format(self.table.upper()), "list", "db_configuration")
        self.connection_to_db()
        self.read_from_table(self.table, columns(), "table_id", "", "ORDER", "DESC")


if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")

    test = LaunchpadsBody()







    os.chdir("state_machine")
    os.chdir("states")