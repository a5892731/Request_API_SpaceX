'''
Read data from file class
author: a5892731
'''
import os


class DataImport:

    version = "1.2"
    version_date = "2021-04-08"
    version_info = ""

    def __init__(self, FILE_NAME, CALL_TYPE, FILE_FOLDER =  "api_configuration"):
        self.list = []
        self.dicionary = {}
        self.string = ""
        self.call_type = CALL_TYPE

        self.open_file(FILE_NAME, FILE_FOLDER)

        if CALL_TYPE == "list":
            self.read_list()
        elif CALL_TYPE == "dict":
            self.read_dict()
        elif CALL_TYPE == "string":
            self.read_string()

    def __call__(self):
        if self.call_type == "list":
            return self.list
        elif self.call_type == "dict":
            return self.dicionary
        elif self.call_type == "string":
            return self.string
        else:
            return None

    def open_file(self, FILE_ADDRESS, FILE_FOLDER):
        os.chdir(FILE_FOLDER)
        self.file = open(FILE_ADDRESS, "r")
        os.chdir("..")

    def read_list(self):
        for line in self.file:
            self.list.append(line.rstrip("\n"))
        self.file.close()

    def read_dict(self):
        for line in self.file:
            line = line.rstrip("\n").split(": ")
            self.dicionary[line[0]] = self.value_data_segregation(line[1])
        self.file.close()

    def read_string(self):
        self.string = self.file.readline()

    def value_data_segregation(self, value):
        if value[0] == "(" and value[-1] == ")":  # if string contains tuple
            output = self.cteate_tuple_from_string(value[1:-2])
        elif value[0] == "[" and value[-1] == "]":  # if string contains list
            output = self.create_list_from_string(value[1:-2])
        else:
            output = value

        return output

    def create_list_from_string(self, string):
        return string.split(", ")

    def cteate_tuple_from_string(self, string):
        return tuple(self.create_list_from_string(string))

    def __del__(self):
        return "data deleted"


if __name__ == "__main__":  # test

    os.chdir("..")

    data = DataImport("BOOSTERS_OBJECT_LIST.txt", "list")
    print(data())

    data2 = DataImport("TABLES.txt", "dict", "db_configuration")
    print(type(data2()["boosters"]))
    print(data2())




    os.chdir("system")