"""
version 1.1

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
    def __init__(self, request_api_address, OBJECT_DICT, object = SpacexObject):
        self.OBJECT_DICT = OBJECT_DICT
        self.object = object
        self.objects = []
        r = requests.get(request_api_address)
        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                self.objects.append(self.object(self.dict_generator(element)))

    def dict_generator(self, element):
        dict = {}
        for key in self.OBJECT_DICT:
            dict[key] = element[key]
        return dict


class ObjectsSort:
    def __init__(self, objects):
        self.objects = objects

    def print_objects_by_status(self, status, keys):
        number_of_elements = 1
        print("Sort by status: {}".format(status))
        for object in self.objects:
            if object.OBJECT_DICT["status"] == status:
                print("\n{}: ".format(number_of_elements))
                object.printing_data(keys)
                number_of_elements += 1

    def print_objects_by_serial(self, serial, keys):
        object_in_list = False
        for object in self.objects:
            if object.OBJECT_DICT["serial"] == serial:
                object.printing_data(keys)
                object_in_list = True
        if object_in_list == False:
            print(">>> wrong serial number")


    def print_objects_by_previouse_time(self, keys):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> previouse launches: ")
        for object in self.objects:
            if int(object.OBJECT_DICT["date_utc"][:10].replace("-", "", 2)) <= \
                    int(str(datetime.utcnow())[:10].replace("-", "", 2)):

                print("\n{}: ".format(number_of_elements))
                object.printing_data(keys)
                number_of_elements += 1

    def print_objects_by_future_time(self, keys):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> future launches: ")
        for object in self.objects:
            if int(object.OBJECT_DICT["date_utc"][:10].replace("-", "", 2)) >= \
                    int(str(datetime.utcnow())[:10].replace("-", "", 2)):

                print("\n{}: ".format(number_of_elements))
                object.printing_data(keys)
                number_of_elements += 1



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


    objects = SpacexObjects(API_ADDRESS_DICT["MISSIONS"], LAUNCHES_OBJECT_DICTIONARY).objects
    sorted_objests = ObjectsSort(objects)
    sorted_objests.print_objects_by_future_time({
                             "details": "", "crew": "", "capsules": "", "payloads": "",
                             "flight_number": "", "name": "", "date_utc": "",
                         })

    '''
        objects = SpacexObjects(API_ADDRESS_DICT["BOOSTERS"], BOOSTERS_OBJECT_DICTIONARY).objects
        sorted_objests = ObjectsSort(objects)
        sorted_objests.print_objects_by_status("active",{
                                "block": "", "reuse_count": "",
                                 "serial": "",})
    '''