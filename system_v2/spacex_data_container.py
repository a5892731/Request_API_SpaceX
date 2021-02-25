"""
version 1.2

this is a main data class of this program.
"""


import json
import requests
from datetime import datetime


class SpacexObject:

    def __init__(self, OBJECT_DICT):
        self.OBJECT_DICT = OBJECT_DICT

    def printing_data(self, keys):
        for key in keys:
            print("{}: {}".format(key, self.OBJECT_DICT[key]))

class SpacexObjects:
    def __init__(self, REQUEST_API_ADDRESS, OBJECT_DICT, objects, object = SpacexObject):
        self.OBJECT_DICT = OBJECT_DICT
        self.objects = objects

        if self.objects == []:
            self.request_data(REQUEST_API_ADDRESS, object)

    def request_data(self, REQUEST_API_ADDRESS, object):
        r = requests.get(REQUEST_API_ADDRESS)
        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                self.objects.append(object(self.dict_generator(element)))

    def dict_generator(self, element):
        dict = {}
        for key in self.OBJECT_DICT:
            dict[key] = element[key]
        return dict

class ObjectsSort:
    def __init__(self, objects):
        self.objects = objects

    def print_objects_by_value_of_key(self, value, key, objects):
        number_of_elements = 1
        print("Sort by {}: {}".format(key, value))
        for object in self.objects:
            if object.OBJECT_DICT[key] == value:
                print("\n{}: ".format(number_of_elements))
                object.printing_data(objects)
                number_of_elements += 1

    def print_objects_by_previouse_time(self, objects):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> previouse launches: ")
        for object in self.objects:
            if int(object.OBJECT_DICT["date_utc"][:10].replace("-", "", 2)) <= \
                    int(str(datetime.utcnow())[:10].replace("-", "", 2)):

                print("\n{}: ".format(number_of_elements))
                object.printing_data(objects)
                number_of_elements += 1

    def print_objects_by_future_time(self, objects):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> future launches: ")
        for object in self.objects:
            if int(object.OBJECT_DICT["date_utc"][:10].replace("-", "", 2)) >= \
                    int(str(datetime.utcnow())[:10].replace("-", "", 2)):

                print("\n{}: ".format(number_of_elements))
                object.printing_data(objects)
                number_of_elements += 1


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