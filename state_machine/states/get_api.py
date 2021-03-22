from system.menu import Menu
from system.read_data_files import DataImport
from system.spacex_data_container import SpacexObjects
import requests
import time

class GetDataFromApiBody(object):

    def __init__(self):
        self.api_data = {}
        self.request_status = 0
        self.get_configuration()


    def get_configuration(self):

        api_adreses = DataImport("API_ADDRESS_DICT.txt", "dict", "data_files")
        api_statuses = DataImport("API_STATUSES.txt", "dict", "data_files")

        objects_list = DataImport("OBJECT_LIST.txt", "list", "data_files")
        data = {}

        progress = 1
        for key in objects_list():

            r = requests.get(api_adreses()[key])
            self.request_status = r
            if r != 200:

                object_list = DataImport((key + "_OBJECT_LIST.txt"), "list", "data_files")
                so = SpacexObjects(api_adreses()[key], object_list(), [])
                objects = so.objects

                #-------------------------------------------------------------------------------------------
                menu_list = [["loading API data: {} %".format(int(progress / len(objects_list()) * 100))]]
                self.print_menu(menu_list)
                progress += 1
                data[key] = objects
            else:
                menu_list = [["{}: {}".format(key, api_statuses()[r])]]
                time.sleep(5)
                self.print_menu(menu_list)

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

    def print_menu(self, menu_list):
        menu = Menu(menu_list)
        menu.drow_menu(" MENU - " + str(self) + " ")
        menu.clear_screen()