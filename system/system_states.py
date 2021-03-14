'''
file version 2.3

this is a state machine file
'''


from system.spacex_data_container import SpacexObjects, ObjectsSort

class SystemStates:

    def __init__(self):

        self.boosters = []
        self.capsules = []
        self.launches = []
        self.crew = []
    # ------------------------------------------------------------------------------------------------------------------
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

    def launches_object_number_state(self, LAUNCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                     object_number_value, object_number):

        self.launches = self.execute_standard_key_value_state(LAUNCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                              self.launches,
                                                              object_number_value, object_number)

    def launches_flight_number_state(self, LAUNCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                    flight_number_value, flight_number):

        self.launches = self.execute_standard_key_value_state(LAUNCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS,
                                                             self.launches,
                                                             flight_number_value, flight_number)
    # ------------------------------------------------------------------------------------------------------------------
    def launches_previouse(self, LAUNCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "previosue", key = "time"):
        so = SpacexObjects(API_ADDRESS, LAUNCHES_LIST, self.launches)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        sorted_missions.print_objects_by_previouse_time(ITEMS_TO_DISPLAY_LIST)
        self.launches = objects

    def launches_future(self, LAUNCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "future", key = "time"):
        so = SpacexObjects(API_ADDRESS, LAUNCHES_LIST, self.launches)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        sorted_missions.print_objects_by_future_time(ITEMS_TO_DISPLAY_LIST)
        self.launches = objects
    # ------------------------------------------------------------------------------------------------------------------
    def launches_sort_by_time(self, LAUNCHES_LIST, ITEMS_TO_DISPLAY_LIST, API_ADDRESS, value = "UP", key = "time"):
        so = SpacexObjects(API_ADDRESS, LAUNCHES_LIST, self.launches)
        objects = so.objects
        sorted_missions = ObjectsSort(objects)
        self.launches = sorted_missions.sort_objects_by_time()
        print(">>> data sorted by {}!".format(key))
    # ------------------------------------------------------------------------------------------------------------------
    def get_crew_data_state(self, LAUNCHES_LIST, API_ADDRESS,
                            CREW_LIST, CREW_API_ADDRESS,
                            first_object_key = "crew", second_object_key = "id", replace_key = "name"):

        self.launches = self.replace_id_whith_elements_in_object_list_standard_state(LAUNCHES_LIST, API_ADDRESS, self.launches,
                                                                                    CREW_LIST, CREW_API_ADDRESS, self.crew,
                                                                                    first_object_key,
                                                                                    second_object_key,
                                                                                    replace_key)
    def get_launches_data_for_capsules_state(self, CAPSULES_LIST, CAPSULES_API_ADDRESS,
                                             LAUNCHES_LIST, LAUNCHES_API_ADDRESS,
                                             first_object_key = "launches", second_object_key = "id", replace_key = "flight_number"):

        self.capsules = self.replace_id_whith_elements_in_object_list_standard_state(CAPSULES_LIST, CAPSULES_API_ADDRESS, self.capsules,
                                                                                    LAUNCHES_LIST, LAUNCHES_API_ADDRESS, self.launches,
                                                                                    first_object_key,
                                                                                    second_object_key,
                                                                                    replace_key)
    def get_launches_data_for_boosters_state(self, BOOSTERS_LIST, BOOSTERS_API_ADDRESS,
                                             LAUNCHES_LIST, LAUNCHES_API_ADDRESS,
                                             first_object_key = "launches", second_object_key = "id", replace_key = "flight_number"):

        self.boosters = self.replace_id_whith_elements_in_object_list_standard_state(BOOSTERS_LIST, BOOSTERS_API_ADDRESS, self.boosters,
                                                                                     LAUNCHES_LIST, LAUNCHES_API_ADDRESS, self.launches,
                                                                                     first_object_key,
                                                                                     second_object_key,
                                                                                     replace_key)
    # ------------------------------------------------------------------------------------------------------------------
    def execute_standard_key_value_state(self, OBJECT_LIST, OBJECT_KEYS_LIST, API_ADDRESS, objects, value = "", key = ""):
        vehicles_objects = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
        objects = vehicles_objects.objects
        sorted_vehicles = ObjectsSort(objects)
        sorted_vehicles.print_objects_by_value_of_key(value, key, OBJECT_KEYS_LIST)
        return objects

    def replace_id_whith_elements_in_object_list_standard_state(self, OBJECT_LIST, API_ADDRESS, objects,
                                                                OBJECT2_LIST, API_ADDRESS2, objects2,
                                                                first_object_key, second_object_key, replace_key):
        so = SpacexObjects(API_ADDRESS, OBJECT_LIST, objects)
        objects = so.objects
        so2 = SpacexObjects(API_ADDRESS2, OBJECT2_LIST, objects2)
        objects2 = so2.objects

        list_bufor = []
        for object in objects:
            if object.OBJECT_DICT[first_object_key] != []:
                list_of_persons = list(object.OBJECT_DICT[first_object_key])
                for id in list_of_persons:
                    for person in objects2:
                        if person.OBJECT_DICT[second_object_key] == id or person.OBJECT_DICT[replace_key] == id:
                            list_bufor.append(person.OBJECT_DICT[replace_key])
                    object.OBJECT_DICT[first_object_key] = list_bufor
                list_bufor = []
        print(">>> {} {} replaced by {} in object list.".format(first_object_key, second_object_key, replace_key))
        return objects