from system.read_data_files import DataImport
from state_machine.states.read_db.read_database import ReadDbBody
import os

class RocketsBody(ReadDbBody):

    def __init__(self):

        self.table = "rockets"
        columns = DataImport("SELECT_{}.txt".format(self.table.upper()), "list", "db_configuration")
        self.connection_to_db()
        self.read_from_table(self.table, columns(), "table_id", "", "ORDER", "ASC")


if __name__ == "__main__":

    os.chdir("../../..")
    os.chdir("../../..")

    test = RocketsBody()







    os.chdir("state_machine")
    os.chdir("states")