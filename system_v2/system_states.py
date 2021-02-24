'''
version 1.2

is a state machine file
'''


from system.vehicles import VehicleSort
from system.user_selection import UserSerialSelection
from system.lauches import LaunchesSort

from system_v2.spacex_data_container import SpacexObjects, ObjectsSort



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


def request_data(data_list, API_ADDRESS, OBJECTS_DICT):
    if data_list == []:
        data_list = SpacexObjects(API_ADDRESS, OBJECTS_DICT).objects
        print(">Data received")
    return data_list

def booster_status_state(state, vehicles, STATUS_DICT):
    boosters = VehicleSort(state, vehicles, STATUS_DICT)
    boosters.print_vehicles_by_status()

def booster_serial_state(state, vehicles, STATUS_DICT):
    user = UserSerialSelection()
    serial = user.return_serial()
    boosters = VehicleSort(state, vehicles, STATUS_DICT)
    boosters.print_vehicle_by_serial(serial)

def capsule_status_state(state, vehicles, STATUS_DICT):
    capsules = VehicleSort(state, vehicles, STATUS_DICT)
    capsules.print_vehicles_by_status()

def capsule_serial_state(state, vehicles, STATUS_DICT):
    user = UserSerialSelection()
    serial = user.return_serial()
    capsule = VehicleSort(state, vehicles, STATUS_DICT)
    capsule.print_vehicle_by_serial(serial)

def missions_future(launches):
    missions = LaunchesSort(launches)
    missions.print_future_launches()

def missions_previouse(launches):
    missions = LaunchesSort(launches)
    missions.print_prefiouse_launches()