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
    version_date = "2021-03-15"
    version_info = ""

    def __init__(self, db_name, host_name, user_name, user_password, tables):
        self.db_name = db_name
        self.host_name = host_name
        self.user_name = user_name
        #self.user_password = user_password # password is protected

        connection = self.create_connection_to_server(user_password)
        create_database_query = "CREATE DATABASE {}".format(db_name)
        self.create_database(connection, create_database_query, tables, user_password)


    def create_connection_to_server(self, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=user_password
            )
            print(">>> Connection to MySQL server successful")
        except Error as e:
            print(f">>> The error '{e}' occurred")
        return connection

    def create_database(self, connection, query, tables, user_password):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print(">>> Database created successfully")
            self.connection = self.create_connection_to_db(user_password)
            self.create_tables(tables) # if database just been created then you need to build db tables too

        except Error as e:
            if "1007 (HY000)" in f"{e}":
                print(">>> Database exists")
                self.connection = self.create_connection_to_db(user_password)
            else:
                print(f">>> The error '{e}' occurred")

    def create_tables(self, tables):

        def create_columns(key, tables):
            columns = ""
            for column in tables[key]:
                columns += column + ", "
            columns += "PRIMARY KEY ({})".format(tables[key][0].split(" ")[0])
                                                 # "test_table1_id INT AUTO_INCREMENT" and you nead test_table1_id
            return columns

        for key in tables:
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
            print(">>> Connection to MySQL DB successful")
        except Error as e:
                print(f">>> The error '{e}' occurred")
        return connection


    def execute_query(self, connection, query, message):

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print(">>> {}".format(message))
        except Error as e:
            print(f">>> The error '{e}' occurred")

    def execute_sql_val(self, connection, sql, val, message):

        cursor = connection.cursor()
        try:
            cursor.executemany(sql, val)
            connection.commit()
            print(">>> {}".format(message))
        except Error as e:
            print(f">>> The error '{e}' occurred")

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f">>> The error '{e}' occurred")

    def del_db(self, message = "Database deleted"):
        self.execute_query(self.connection, "DROP DATABASE {}".format(self.db_name), message)

    def __del__(self):
        return ">>> Class deleted"




#-----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

# create database test:

    '''    tables = {"test_table1": ("test_table1_id INT AUTO_INCREMENT", "column1 CHAR(20)", "column2 CHAR(20)", "column3 CHAR(20)"),
              "test_table2": ("test_table2_id INT AUTO_INCREMENT", "column1 CHAR(20)", "column2 CHAR(20)", "column3 CHAR(20)")}

    test = Database("spacex", "127.0.0.1", "root", "", tables)
    print(test.__del__())'''


#-----------------------------------------------------------------------------------------------------------------------
    os.chdir("..")

    tables2 = DataImport("TABLES.txt", "dict", "db_configuration")

    test = Database("spacex", "127.0.0.1", "root", "", tables2())

    test.del_db()
    print(test.__del__())

    os.chdir("system")

#-----------------------------------------------------------------------------------------------------------------------