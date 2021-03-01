'''
file version 2.1

this is a state machine file
'''


from system_v2.spacex_data_container import SpacexObjects, ObjectsSort

class SystemStates:

    def __init__(self):

        self.boosters = []
        self.capsules = []
        self.lauches = []

    def booster_status_state(self, BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, status_value, status):
        self.boosters = self.execute_standard_key_value_state(BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.boosters, status_value, status)

    def booster_serial_state(self, BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, serial_value, serial):
        self.boosters = self.execute_standard_key_value_state(BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.boosters, serial_value, serial)

    def capsule_status_state(self, CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, status_value, status):
        self.capsules = self.execute_standard_key_value_state(CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.capsules, status_value, status)

    def capsule_serial_state(self, CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, serial_value, serial):
        self.capsules = self.execute_standard_key_value_state(CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.capsules, serial_value, serial)

    def lauches_object_number_state(self, LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, object_number_value, object_number):
        self.lauches = self.execute_standard_key_value_state(LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.lauches, object_number_value, object_number)

    def lauches_flight_number_state(self, LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, flight_number_value, flight_number):
        self.lauches = self.execute_standard_key_value_state(LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.lauches, flight_number_value, flight_number)
    def lauches_previouse(self, LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "previosue", key = "time"):
        so = SpacexObjects(API_ADDRESS, LAUCHES_LIST, self.lauches)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        sorted_missions.print_objects_by_previouse_time(ITEMS_TO_DISPLAY_LIST)
        self.lauches = objects

    def lauches_future(self, LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "future", key = "time"):
        so = SpacexObjects(API_ADDRESS, LAUCHES_LIST, self.lauches)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        sorted_missions.print_objects_by_future_time(ITEMS_TO_DISPLAY_LIST)
        self.lauches = objects

    def lauches_sort_by_time(self, LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "future", key = "time"):
        so = SpacexObjects(API_ADDRESS, LAUCHES_LIST, self.lauches)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        self.lauches = sorted_missions.sort_objects_by_time()

    def execute_standard_key_value_state(self, OBJECT_LIST, OBJECT_KEYS_LIST, API_ADDRESS, objects, value = "", key = ""):
        vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
        objects = vehicles_objects.objects
        sorted_vehicles = ObjectsSort(objects)
        sorted_vehicles.print_objects_by_value_of_key(value, key, OBJECT_KEYS_LIST)
        return objects

