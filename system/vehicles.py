import json
import requests

class VehicleSort:
    def __init__(self, state, vehicles, STATUS_DICT):
        self.vehicles = vehicles
        self.state = state
        self.STATUS_DICT = STATUS_DICT
    def print_vehicles_by_status(self):
        number_of_elements = 1
        print("Sort by status: {}".format(self.STATUS_DICT[self.state]))
        for vehicle in self.vehicles:
            if vehicle.status == self.STATUS_DICT[self.state]:
                print("\n{}: ".format(number_of_elements))
                vehicle.printing_data()
                number_of_elements += 1
    def print_vehicle_by_serial(self, serial):
        vehicle_in_list = False
        for vehicle in self.vehicles:
            if vehicle.serial == serial:
                vehicle.printing_all_data()
                vehicle_in_list = True
        if vehicle_in_list == False:
            print(">>> wrong vehicle serial number")

class Vehicle:
    def __init__(self, type,  reuse_count, last_update, launches, serial, id, status):
        self.type = type
        self.reuse_count = reuse_count
        self.last_update = last_update
        self.launches = launches
        self.serial = serial
        self.id = id
        self.status = status

    def printing_all_data(self):
        print("type: {}".format(self.type))
        print("reuse_count: {}".format(self.reuse_count))
        print("last_update: {}".format(self.last_update))
        print("launches: {}".format(self.launches))
        print("serial: {}".format(self.serial))
        print("id: {}".format(self.id))
        print("status: {}".format(self.status))

    def printing_data(self):
        print("serial: {}".format(self.serial))
        print("reuse_count: {}".format(self.reuse_count))


class Vehicles:
    def __init__(self, request_api_adress, vehicle = Vehicle):
        self.vehicles = []
        r = requests.get(request_api_adress)
        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                try:
                    self.vehicles.append(vehicle(element["block"], element["reuse_count"], element["last_update"],
                                         element["launches"], element["serial"],
                                         element["id"], element["status"]))
                except KeyError:
                    self.vehicles.append(vehicle(element["type"], element["reuse_count"], element["last_update"],
                                         element["launches"], element["serial"],
                                         element["id"], element["status"]))