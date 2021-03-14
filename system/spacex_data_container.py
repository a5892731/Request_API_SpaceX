"""
file version 1.6

this is a main data class of this program.
"""


import json
import requests
from datetime import datetime
from terminaltables import SingleTable, DoubleTable


class SpacexObject:

    def __init__(self, OBJECT_DICT, OBJECT_NUMBER):
        self.OBJECT_DICT = OBJECT_DICT
        self.OBJECT_NUMBER = str(OBJECT_NUMBER)
        self.table_width = 69

    def printing_data(self, number, keys):
        data_table_to_print = [[""]]
        data = ""
        for key in keys:
            if self.OBJECT_DICT[key] == []:
                continue
            data += str(key) + ": " + str(self.OBJECT_DICT[key]) + "\n"
        data_table_to_print[0][0] = self.prepare_data_to_print(data).rstrip("\n")
        table = SingleTable(data_table_to_print, title = str(number))
        print(table.table)

    def prepare_data_to_print(self, data):
        num_of_signs = 0
        output = ""
        for sign in data:
            num_of_signs += 1
            output += sign
            if sign == "\n":
                if num_of_signs < self.table_width:
                    output = output.rstrip("\n")
                    output += (self.table_width - num_of_signs) * " " + " \n" # filling the table window
                num_of_signs = 0
            elif num_of_signs >= self.table_width:
                output += "\n"
                num_of_signs = 0

        return output

class SpacexObjects:
    def __init__(self, REQUEST_API_ADDRESS, OBJECT_DICT, objects, object = SpacexObject):
        self.OBJECT_DICT = OBJECT_DICT
        self.objects = objects

        if self.objects == []:
            self.request_data(REQUEST_API_ADDRESS, object)

    def request_data(self, REQUEST_API_ADDRESS, object):
        r = requests.get(REQUEST_API_ADDRESS)
        object = object
        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                self.objects.append(object(self.dict_generator(element, len(self.objects) + 1), len(self.objects) + 1))

    def dict_generator(self, element, object_number):
        dict = {}
        for key in self.OBJECT_DICT:
            if key == "OBJECT NUMBER":
                dict[key] = str(object_number)
            else:
                dict[key] = element[key]
        return dict

class ObjectsSort:
    def __init__(self, objects):
        self.objects = objects

    def sort_objects_by_time(self):
        def item_to_sort(e):
            output = e.OBJECT_DICT["date_utc"][:10].replace("-", "", 2)
            return int(output)
        self.objects.sort(key = item_to_sort)
        return self.objects

    def print_objects_by_value_of_key(self, value, key, objects):
        number_of_elements = 1
        print("Sort by {}: {}".format(key, value))
        for object in self.objects:
            if str(object.OBJECT_DICT[key]) == value:
                object.printing_data(number_of_elements, objects)
                number_of_elements += 1

    def print_objects_by_previouse_time(self, objects):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> previouse launches: ")
        for object in self.objects:
            if int(object.OBJECT_DICT["date_utc"][:10].replace("-", "", 2)) <= \
                    int(str(datetime.utcnow())[:10].replace("-", "", 2)):
                    object.printing_data(number_of_elements, objects)
                    number_of_elements += 1

                    if number_of_elements % 20 == 1:
                        go = input("Continue ? (Y/N): ")
                        if go == "N" or go == "n":
                            break

    def print_objects_by_future_time(self, objects):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> future launches: ")
        for object in self.objects:
            if int(object.OBJECT_DICT["date_utc"][:10].replace("-", "", 2)) >= \
                    int(str(datetime.utcnow())[:10].replace("-", "", 2)):
                    object.printing_data(number_of_elements, objects)
                    number_of_elements += 1

                    if number_of_elements % 20 == 1:
                        go = input("Continue ? (Y/N): ")
                        if go == "N" or go == "n":
                            break






#--------------------------------TESTS-------------------------------------------------------------------------------

if __name__ == "__main__": # test


    BOOSTERS_OBJECT_DICTIONARY = {
                            "block": "", "reuse_count": "", "last_update": "", "launches": "",
                             "serial": "", "id": "", "status": "",
                         }

    CAPSULES_OBJECT_DICTIONARY = {
                            "type": "", "reuse_count": "", "last_update": "", "launches": "",
                             "serial": "", "id": "", "status": "",
                         }

    LAUNCHES_OBJECT_DICTIONARY = {
                            "fairings": "", "links": "", "static_fire_date_utc": "", "rocket": "",
                             "success": "", "details": "", "crew": "", "capsules": "", "payloads": "",
                             "failures": "", "flight_number": "", "name": "", "date_utc": "", "cores": "",
                             "id": "",
                         }
    API_ADDRESS_DICT = {
                        "BOOSTERS": "https://api.spacexdata.com/v4/cores",
                        "CAPSULES": "https://api.spacexdata.com/v4/capsules",
                        "MISSIONS": "https://api.spacexdata.com/v4/launches"
                        }


    objects = []



    so = SpacexObjects(API_ADDRESS_DICT["MISSIONS"], LAUNCHES_OBJECT_DICTIONARY, objects)
    objects = so.objects

    sorted_rockets = ObjectsSort(objects)
    sorted_rockets.print_objects_by_future_time({
                                                     "success": "", "details": "", "crew": "",
                                                     "payloads": "",
                                                     "name": "", "date_utc": "",
                                                 })





'''
    so = SpacexObjects(API_ADDRESS_DICT["BOOSTERS"], BOOSTERS_OBJECT_DICTIONARY, objects)
    objects = so.objects

    sorted_rockets = ObjectsSort(objects)
    sorted_rockets.print_objects_by_value_of_key("active", "status",
                                                 {"block": "", "reuse_count": "", "serial": "", })
'''