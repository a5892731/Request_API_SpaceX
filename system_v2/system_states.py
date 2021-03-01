'''
file version 1.2

this is a state machine file
'''



from system_v2.user_selection import UserSerialSelection
from system_v2.spacex_data_container import SpacexObjects, ObjectsSort
from system_v2.read_data_files import DataImport




def booster_status_state(state, vehicles, OBJECT_LIST, STATUS_DICT, API_ADDRESS):

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(STATUS_DICT[state], "status",
                                                  {"block": "", "reuse_count": "", "serial": "", })

    return vehicles

def booster_serial_state(state, vehicles, OBJECT_LIST, API_ADDRESS):

    user = UserSerialSelection()
    serial = user.return_serial()

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(serial, "serial", OBJECT_LIST)

    return vehicles

def capsule_status_state(state, vehicles, OBJECT_LIST, STATUS_DICT, API_ADDRESS):

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(STATUS_DICT[state], "status",
                                                  {"type": "", "reuse_count": "", "serial": "", })

    return vehicles

def capsule_serial_state(state, vehicles, OBJECT_LIST, API_ADDRESS):
    user = UserSerialSelection()
    serial = user.return_serial()

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(serial, "serial", OBJECT_LIST)

    return vehicles

def missions_future(OBJECT_LIST, OBJECT_CALL_LIST, API_ADDRESS, objects):

    so = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
    objects = so.objects

    sorted_rockets = ObjectsSort(objects)
    sorted_rockets.print_objects_by_future_time(OBJECT_CALL_LIST)
    return objects



def missions_previouse(OBJECT_LIST, OBJECT_CALL_LIST, API_ADDRESS, objects):

    so = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
    objects = so.objects

    sorted_rockets = ObjectsSort(objects)
    sorted_rockets.print_objects_by_previouse_time(OBJECT_CALL_LIST)
    return objects