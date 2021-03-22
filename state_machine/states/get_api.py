from system.menu import Menu
from system.read_data_files import DataImport
from system.spacex_data_container import SpacexObjects
import requests

class GetDataFromApiBody(object):

    def __init__(self):
        self.api_data = {}
        self.request_status = 0
        self.error = ""
        self.get_configuration()


    def get_configuration(self):

        api_adreses = DataImport("API_ADDRESS_DICT.txt", "dict", "data_files")
        objects_list = DataImport("OBJECT_LIST.txt", "list", "data_files")
        data = {}

        progress = 1
        for key in objects_list():
            Menu([["loading API data: {} %".format(int(progress / len(objects_list()) * 100))]], " MENU - {} ".format(str(self)))
            # -------------------------------------------------------------------------------------------
            r = requests.get(api_adreses()[key])
            self.request_status = r.status_code
            if self.request_status == 200:
                object_list = DataImport((key + "_OBJECT_LIST.txt"), "list", "data_files")
                so = SpacexObjects(api_adreses()[key], object_list(), [])
                objects = so.objects
                #-------------------------------------------------------------------------------------------
                data[key] = objects
                progress += 1

            else:
                api_statuses = DataImport("API_STATUSES.txt", "dict", "data_files")
                self.error = str(self.request_status) + ": " + api_statuses()[str(self.request_status)]
                break

        self.api_data = data

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

