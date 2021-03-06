from system.menu import Menu

class InsertDbTablesBody(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self, api_data, DB, db_sizes):
        self.api_data = api_data
        self.db = DB
        self.db_sizes = db_sizes
        self.error = ""
        progress = 0
        columns = ""
        row_allocation = ""
        previous_key = ""

        for key in api_data:
            table_values = []
            row_count = 0

            Menu([[("Inserting table: {}".format(key))],
                  [("Progress: {}%".format(int(progress / len(api_data) * 100)))],
                  [("{}".format((self.db.status + ": " + previous_key)))]], " MENU - {} ".format(str(self)))  # drow menu
            previous_key = key

            for object in api_data[key]:

                if (row_count) < (len(api_data[key]) - (len(api_data[key]) - self.db_sizes[key])):
                    row_count += 1
                    continue

                row_count += 1
                # --------------------------------------------------------------------------------------------------
                columns = ""
                row_allocation = ""  # in (%s, %s) = 2
                row_values = ()


                for column in object.OBJECT_DICT:
                    columns += column + ", "

                    row_allocation += "%s, "

                    if object.OBJECT_DICT[column] != None:
                        row_values = row_values + (str(object.OBJECT_DICT[column]),)
                    else:
                        row_values = row_values + ("None",)

                table_values.append(row_values)


                if "error" in self.db.status:
                    self.error += key.capitalize() + " table: " + self.db.status +"\n\n"

            self.insert_to_table(key.lower(), columns.rstrip(", "), row_allocation.rstrip(", "), table_values)
            progress += 1

        Menu([[("Progress: {}%".format(int(progress / len(api_data) * 100)))],
              [("{}".format((self.db.status + ": " + key)))]], " MENU - {} ".format(str(self)))  # drow menu

    def insert_to_table(self, table_name, colun_names, row_count, values, message="Data inserted to table"):

        sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, colun_names, row_count)
        val = values  # val must be a list  > val = [(..., ...., ....)]
        self.db.execute_sql_val(self.db.connection, sql, val, message)

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__