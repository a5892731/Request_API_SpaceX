'''
file version 1.3

this is a state machine file
'''



from system_v2.user_selection import UserSerialSelection
from system_v2.spacex_data_container import SpacexObjects, ObjectsSort

def booster_status_state(state, vehicles, OBJECT_LIST, OBJECT_CALL_LIST, STATUS_DICT, API_ADDRESS):

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(STATUS_DICT[state], "status", OBJECT_CALL_LIST)
    #  print_objects_by_value_of_key(self, value, key, objects):

    return vehicles

def booster_serial_state(vehicles, OBJECT_LIST, OBJECT_CALL_LIST, API_ADDRESS):
    user = UserSerialSelection(">>> Put vehicle serial number: ")

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(user.return_serial(), "serial", OBJECT_CALL_LIST)

    return vehicles

def capsule_status_state(state, vehicles, OBJECT_LIST , OBJECT_CALL_LIST, STATUS_DICT, API_ADDRESS):
    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(STATUS_DICT[state], "status", OBJECT_CALL_LIST)

    return vehicles

def capsule_serial_state(vehicles, OBJECT_LIST, OBJECT_CALL_LIST, API_ADDRESS):
    user = UserSerialSelection(">>> Put vehicle serial number: ")

    vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, vehicles)
    vehicles = vehicles_objects.objects

    sorted_vehicles = ObjectsSort(vehicles)
    sorted_vehicles.print_objects_by_value_of_key(user.return_serial(), "serial", OBJECT_CALL_LIST)

    return vehicles

def missions_future(OBJECT_LIST, OBJECT_CALL_LIST, API_ADDRESS, objects):
    so = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
    objects = so.objects

    sorted_missions = ObjectsSort(objects)
    sorted_missions.print_objects_by_future_time(OBJECT_CALL_LIST)
    return objects

def missions_previouse(OBJECT_LIST, OBJECT_CALL_LIST, API_ADDRESS, objects):
    so = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
    objects = so.objects

    sorted_missions = ObjectsSort(objects)
    sorted_missions.print_objects_by_previouse_time(OBJECT_CALL_LIST)
    return objects

def missions_by_object_number(OBJECT_LIST, OBJECT_CALL_LIST, API_ADDRESS, objects):
    user = UserSerialSelection(">>> Put object number: ")

    so = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
    objects = so.objects

    sorted_missions = ObjectsSort(objects)
    sorted_missions.print_objects_by_value_of_key(user.return_serial(), "OBJECT NUMBER", OBJECT_CALL_LIST)
    return objects
