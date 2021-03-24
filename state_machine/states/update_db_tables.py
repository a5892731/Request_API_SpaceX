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

        for key in api_data:
            row_count = 0
            for object in api_data[key]:
                row_count += 1
                columns = ""
                columns_values_count = ""  # in (%s, %s) = 2
                columns_values = ""
                for column in object.OBJECT_DICT:
                    columns += column + ", "
                    columns_values_count += "%s, "
                    if object.OBJECT_DICT[column] != None:
                        columns_values += str(object.OBJECT_DICT[column]) + ", "
                    else:
                        columns_values += "None" + ", "





                #sql = "INSERT INTO {} ({}) VALUES ({})".format(key.lower(), columns, columns_values_count)
                #val = [(tuple(columns_values))]



                #sql = "INSERT INTO {} (date, coustomer_id, order_name, order_value, status) VALUES (%s, %s, %s, %s, %s)".format("orders")
                #val = [('SELECT DATE(NOW())', user_id, order_name, order_value, status,)]
                #self.db.execute_sql_val(self.db.connection, sql, val, "DZIALA")



                query = "INSERT INTO {} ({}) VALUES ({})".format(key.lower(), columns.lower(), columns_values)
                self.db.execute_query(self.db.connection, query, "DZIALA")

                print(self.db.status)
                # from here





                if row_count >= (len(api_data[key]) - self.db_sizes[key]):
                    break




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
    pass
