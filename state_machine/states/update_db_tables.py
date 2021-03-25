from system.menu import Menu

class UpdateDbTablesBody(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self, api_data, DB, db_sizes):
        self.api_data = api_data
        self.db = DB
        self.db_sizes = db_sizes
        self.error = ""

        for key in api_data:
            row_count = 0
            for object in api_data[key]:
                row_count += 1
                columns = ""
                columns_values_count = ""  # in (%s, %s) = 2
                columns_values = ()
                val = []

                for column in object.OBJECT_DICT:
                    if column == "id":
                        columns += key.lower() + "_id" + ", "
                    else:
                        columns += column + ", "
                    columns_values_count += "%s, "
                    if object.OBJECT_DICT[column] != None:
                        columns_values = columns_values + (str(object.OBJECT_DICT[column]),)
                    else:
                        columns_values = columns_values + ("None",)


                sql = "INSERT INTO {} ({}) VALUES ({})".format(key.lower(), columns.rstrip(", "), columns_values_count.rstrip(", "))
                #val.append(columns_values)
                val = [columns_values]
                self.db.execute_sql_val(self.db.connection, sql, val, "IT IS WORKING !")

                if "error" in self.db.status:
                    self.error += self.db.status + " in " + key + "\n\n"
                    Menu([[(self.db.status + " in >>> " + key)]], " MENU - {} ".format(str(self)))  # drow menu

                if (row_count - 1) >= (len(api_data[key]) - self.db_sizes[key]):
                    print("break")
                    break



            Menu([[("Insert table: {}".format(key))]], " MENU - {} ".format(str(self)))  # drow menu


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


if __name__ == "__main__":


    print(type([]))
