'''
version 1.2

this is a state machine file
'''



from system_v2.user_selection import UserSerialSelection
from system_v2.spacex_data_container import SpacexObjects, ObjectsSort




def booster_status_state(state, vehicles, OBJECT_DICT, STATUS_DICT, API_ADDRESS):

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_DICT, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(STATUS_DICT[state], "status",
                                                  {"block": "", "reuse_count": "", "serial": "", })

    return vehicles

def booster_serial_state(state, vehicles, STATUS_DICT, API_ADDRESS):

    user = UserSerialSelection()
    serial = user.return_serial()

    vehicles_objects = SpacexObjects(API_ADDRESS, STATUS_DICT, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(serial, "serial", STATUS_DICT)

    return vehicles

def capsule_status_state(state, vehicles,OBJECT_DICT, STATUS_DICT, API_ADDRESS):

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_DICT, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(STATUS_DICT[state], "status",
                                                  {"type": "", "reuse_count": "", "serial": "", })

    return vehicles

def capsule_serial_state(state, vehicles, STATUS_DICT, API_ADDRESS):
    user = UserSerialSelection()
    serial = user.return_serial()

    vehicles_objects = SpacexObjects(API_ADDRESS, STATUS_DICT, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(serial, "serial", STATUS_DICT)

    return vehicles

def missions_future(OBJECT_DICT, API_ADDRESS, objects):

    so = SpacexObjects(API_ADDRESS, OBJECT_DICT, objects)
    objects = so.objects

    sorted_rockets = ObjectsSort(objects)
    sorted_rockets.print_objects_by_future_time({
                                                     "details": "", "crew": "",
                                                     "payloads": "",
                                                     "name": "", "date_utc": "",
                                                 })
    return objects



def missions_previouse(OBJECT_DICT, API_ADDRESS, objects):

    so = SpacexObjects(API_ADDRESS, OBJECT_DICT, objects)
    objects = so.objects

    sorted_rockets = ObjectsSort(objects)
    sorted_rockets.print_objects_by_previouse_time({
                                                "success": "",
                                                "name": "", "date_utc": "",
                                                 })
    return objects