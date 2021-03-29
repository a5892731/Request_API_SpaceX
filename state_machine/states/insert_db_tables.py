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

        for key in api_data:

            row_count = 0
            for object in api_data[key]:

                if (row_count) < (len(api_data[key]) - self.db_sizes[key]):
                    # row in db
                    continue

                row_count += 1
                # --------------------------------------------------------------------------------------------------
                columns = ""
                columns_values_count = ""  # in (%s, %s) = 2
                row_values = ()
                table_values = []

                for column in object.OBJECT_DICT:
                    if column == "id":
                        columns += key.lower() + "_id" + ", "
                    else:
                        columns += column + ", "

                    columns_values_count += "%s, "

                    if object.OBJECT_DICT[column] != None:
                        row_values = row_values + (str(object.OBJECT_DICT[column]),)
                    else:
                        row_values = row_values + ("None",)

                self.insert_to_table(key.lower(), columns.rstrip(", "), columns_values_count.rstrip(", "),
                                     [row_values])

                table_values.append(row_values)

                if "error" in self.db.status:
                    self.error += self.db.status + " in " + key + "\n\n"

            #self.insert_to_table(key.lower(), columns.rstrip(", "), columns_values_count.rstrip(", "), [table_values])

            Menu([[("Insert table: {}\nProgress: {}%\n\n{}".format(key, (progress / len(api_data) * 100), self.error))]],
                " MENU - {} ".format(str(self)))  # drow menu
            progress += 1

    def insert_to_table(self, table_name, colun_names, row_count, values, message="IT IS WORKING !"):

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