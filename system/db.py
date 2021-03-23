'''
Simple MySQL class file
author: a5892731
'''

import mysql.connector
from mysql.connector import Error

import os
from system.read_data_files import DataImport


class Database:

    version = "1.0"
    version_date = "2021-03-22"
    version_info = ""

    def __init__(self, db_name, host_name, user_name, user_password, tables):
        self.db_name = db_name
        self.host_name = host_name
        self.user_name = user_name
        self.status = ""

        #self.user_password = user_password # password is protected

        #connection = self.create_connection_to_server(user_password)
        #create_database_query = "CREATE DATABASE {}".format(db_name)
        #self.create_database(connection, create_database_query, tables, user_password)


    def create_connection_to_server(self, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=user_password
            )
            self.status = "Connection to MySQL server successful"
        except Error as e:
            self.status = f"The error '{e}' occurred"
        return connection

    def create_database(self, connection, query, tables, user_password):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            self.status = "Database created successfully"

            #self.connection = self.create_connection_to_db(user_password)
            #self.create_tables(tables) # if database just been created then you need to build db tables too

        except Error as e:
            if "1007 (HY000)" in f"{e}":
                self.status = "Database exists"
                self.connection = self.create_connection_to_db(user_password)
            else:
                self.status = f"The error '{e}' occurred"

    def create_tables(self, tables):

        for key in tables:
            self.create_table(key, tables)

    def create_table(self, key, tables):

        def create_columns(key, tables):
            columns = ""
            for column in tables[key]:
                columns += column + ", "
            columns += "PRIMARY KEY ({})".format(tables[key][0].split(" ")[0])
                                                 # "test_table1_id INT AUTO_INCREMENT" and you nead test_table1_id
            return columns

        create_table = """
        CREATE TABLE IF NOT EXISTS {} (
          {}
        ) ENGINE = InnoDB 
        """.format(key, create_columns(key, tables))

        self.execute_query(self.connection, create_table, "DB {} table created successfully".format(key))


    def create_connection_to_db(self, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host= self.host_name,
                user= self.user_name,
                passwd= user_password,
                database= self.db_name
            )
            self.status = "Connection to MySQL DB successful"
        except Error as e:
                self.status = f"The error '{e}' occurred"
        return connection


    def execute_query(self, connection, query, message):

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            self.status = "{}".format(message)
        except Error as e:
            self.status = f"The error '{e}' occurred"

    def execute_sql_val(self, connection, sql, val, message):

        cursor = connection.cursor()
        try:
            cursor.executemany(sql, val)
            connection.commit()
            self.status = "{}".format(message)
        except Error as e:
            self.status = f"The error '{e}' occurred"

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            self.status = f"The error '{e}' occurred"

    def del_db(self, message = "Database deleted"):
        self.execute_query(self.connection, "DROP DATABASE {}".format(self.db_name), message)

    def __del__(self):
        self.status = "Class deleted"



#-----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    ''' 
    WORNING: for tests script from here, you ned to uncomment line 26, 27, 28 and 50, 51 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    
    '''

    os.chdir("..")

    tables2 = DataImport("TABLES.txt", "dict", "db_configuration")

    test = Database("spacex", "127.0.0.1", "root", "", tables2())

    test.del_db()
    print(test.__del__())

    os.chdir("system")

#-----------------------------------------------------------------------------------------------------------------------