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
        self.crew = []

    def booster_status_state(self, BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, status_value, status):
        self.boosters = self.execute_standard_key_value_state(BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.boosters, status_value, status)

    def booster_serial_state(self, BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, serial_value, serial):
        self.boosters = self.execute_standard_key_value_state(BOOSTERS_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.boosters, serial_value, serial)

    def capsule_status_state(self, CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, CAPSULES_API_ADDRESS, status_value, status):

        self.capsules = self.execute_standard_key_value_state(CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, CAPSULES_API_ADDRESS,
                                                              self.capsules, status_value, status)

    def capsule_serial_state(self, CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, serial_value, serial):
        self.capsules = self.execute_standard_key_value_state(CAPSULES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.capsules, serial_value, serial)

    def lauches_object_number_state(self, LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, object_number_value, object_number,
                                    CREW_LIST, CREW_DATA_TO_DISPLAY, CREW_API_ADDRESS):

        self.lauches = self.execute_double_element_key_value_state(LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                                   self.lauches,
                                                                   CREW_LIST, CREW_DATA_TO_DISPLAY, CREW_API_ADDRESS,
                                                                   self.crew,
                                                                   object_number_value, object_number)

    def lauches_flight_number_state(self, LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, flight_number_value, flight_number,
                                    CREW_LIST, CREW_DATA_TO_DISPLAY, CREW_API_ADDRESS):

        self.lauches = self.execute_double_element_key_value_state(LAUCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                                   self.lauches,
                                                                   CREW_LIST, CREW_DATA_TO_DISPLAY, CREW_API_ADDRESS,
                                                                   self.crew,
                                                                   flight_number_value, flight_number)

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

    def execute_double_element_key_value_state(self, OBJECT_LIST, OBJECT_KEYS_LIST, API_ADDRESS,
                                               objects,
                                               OBJECT2_LIST, OBJECT2_KEYS_LIST, API_ADDRESS2,
                                               objects2,
                                               value, key,
                                               first_object_key = "crew", second_object_key = "id", replace_key = "name"):

        so = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
        objects = so.objects

        if objects2 == []:
            list_bufor = []
            so2 = SpacexObjects(API_ADDRESS2, OBJECT2_LIST, objects2)
            objects2 = so2.objects
            for object in objects:
                if object.OBJECT_DICT[first_object_key] != []:
                    list_of_persons = list(object.OBJECT_DICT[first_object_key])

                    for id in list_of_persons:
                        for person in objects2:
                            if person.OBJECT_DICT[second_object_key] == id:
                                list_bufor.append(person.OBJECT_DICT[replace_key])
                        object.OBJECT_DICT[first_object_key] = list_bufor
                    list_bufor = []

        sorted = ObjectsSort(objects)
        sorted.print_objects_by_value_of_key(value, key, OBJECT_KEYS_LIST)
        return objects

