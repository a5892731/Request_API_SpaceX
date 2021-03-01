'''
file version 2.0

this is a state machine file
'''


from system_v2.spacex_data_container import SpacexObjects, ObjectsSort

class SystemStates:

    def __init__(self):

        self.boosters = []
        self.capsules = []
        self.missions = []

    def booster_status_state(self, BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, status_value, status):
        self.boosters = self.execute_standard_key_value_state(BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.boosters, status_value, status)

    def booster_serial_state(self, BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, serial_value, serial):
        self.boosters = self.execute_standard_key_value_state(BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.boosters,
                                                    serial_value, serial)

    def capsule_status_state(self, CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, status_value, status):
        self.capsules = self.execute_standard_key_value_state(CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.capsules, status_value, status)

    def capsule_serial_state(self, CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, serial_value, serial):
        self.capsules = self.execute_standard_key_value_state(CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.capsules, serial_value, serial)

    def missions_object_number_state(self, MISSIONS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, object_number_value, object_number):
        self.capsules = self.execute_standard_key_value_state(MISSIONS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.missions, object_number_value, object_number)

    def missions_previouse(self, MISSIONS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "previosue", key = "time"):
        so = SpacexObjects(API_ADDRESS, MISSIONS_LIST, self.missions)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        sorted_missions.print_objects_by_previouse_time(ITEMS_TO_DISPLAY_LIST)
        self.missions = objects

    def missions_future(self, MISSIONS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "future", key = "time"):
        so = SpacexObjects(API_ADDRESS, MISSIONS_LIST, self.missions)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        sorted_missions.print_objects_by_future_time(ITEMS_TO_DISPLAY_LIST)
        self.missions = objects

    def execute_standard_key_value_state(self, OBJECT_LIST, OBJECT_KEYS_LIST, API_ADDRESS, objects, value = "", key = ""):
        vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
        objects = vehicles_objects.objects
        sorted_vehicles = ObjectsSort(objects)
        sorted_vehicles.print_objects_by_value_of_key(value, key, OBJECT_KEYS_LIST)
        return objects

