'''
file version 1.0

'''
import os


class DataImport:

    def __init__(self, FILE_ADDRESS, call_type):

        self.list = []
        self.dicionary = {}
        self.call_type = call_type

        self.open_file(FILE_ADDRESS)

        if call_type == "list":
            self.read_list()
        elif call_type == "dict":
            self.read_dict()

    def __call__(self):

        if self.call_type == "list":
            return self.list
        elif self.call_type == "dict":
            return self.dicionary
        else:
            return None

    def open_file(self, FILE_ADDRESS):

        if __name__ == "__main__":  # for running tests from this file
            os.chdir("..")

        os.chdir("data_files")
        self.file = open(FILE_ADDRESS, "r")
        os.chdir("..")
        os.chdir("system_v2")

    def read_list(self):
        for line in self.file:
            self.list.append(line.rstrip("\n"))
        self.file.close()

    def read_dict(self):
        for line in self.file:
            line = line.rstrip("\n").split(": ")
            self.dicionary[line[0]] = line[1]
        self.file.close()


if __name__ == "__main__":  # test

    data = DataImport("BOOSTERS_OBJECT_LIST.txt", "list")
    print(data())

    data2 = DataImport("API_ADDRESS_DICT.txt", "dict")
    print(data2())

