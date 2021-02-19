import json
import requests
from datetime import datetime

class LauchesSort:
    def __init__(self,  lauches):
        self.lauches = lauches

    def print_prefiouse_lauches(self):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> previouse lauches: ")
        for lauch in self.lauches:
            if int(lauch.date_utc.replace("-", "", 2)) <= int(str(datetime.utcnow())[:10].replace("-", "", 2)):
                print("\n{}: ".format(number_of_elements))
                lauch.lauch_print_data()
                number_of_elements += 1

    def print_future_lauches(self):
        print("Actual date: " + str(datetime.utcnow())[:10])
        number_of_elements = 1
        print(">>> future lauches: ")
        for lauch in self.lauches:
            if int(lauch.date_utc.replace("-", "", 2)) >= int(str(datetime.utcnow())[:10].replace("-", "", 2)):
                print("\n{}: ".format(number_of_elements))
                lauch.lauch_print_short_data()
                number_of_elements += 1

class Lauch:
    def __init__(self, fairings, links, static_fire_date_utc, rocket, success, details, crew, capsules,
                 payloads, failures, flight_number, name, date_utc, cores, id):
        self.fairings = fairings
        self.links = links
        self.static_fire_date_utc = static_fire_date_utc
        self.rocket = rocket
        self.success = success
        self.details = details
        self.crew = crew
        self.capsules = capsules
        self.payloads = payloads
        self.failures = failures
        self.flight_number = flight_number
        self.name = name
        self.date_utc = date_utc[:10] #up to: YYYY-MM-DD
        self.cores = cores
        self.id = id
    def lauch_print_all_data(self):
        print("rocket: {}".format(self.rocket))
        print("success: {}".format(self.success))
        print("details: {}".format(self.details))
        print("crew: {}".format(self.crew))
        print("capsules: {}".format(self.capsules))
        print("payloads: {}".format(self.payloads))
        print("failures: {}".format(self.failures))
        print("flight_number: {}".format(self.flight_number))
        print("name: {}".format(self.name))
        print("cores: {}".format(self.cores))
        print("date_utc: {}".format(self.date_utc))

    def lauch_print_data(self):
        print("success: {}".format(self.success))
        print("details: {}".format(self.details))
        if len(self.crew) > 0:
            print("crew: {}".format(len(self.crew)))
        if self.failures != []:
            print("failures: {}".format(self.failures))
        print("flight_number: {}".format(self.flight_number))
        print("name: {}".format(self.name))
        print("date_utc: {}".format(self.date_utc))

    def lauch_print_short_data(self):
        if len(self.crew) > 0:
            print("crew: {}".format(len(self.crew)))
        print("flight_number: {}".format(self.flight_number))
        print("name: {}".format(self.name))
        print("date_utc: {}".format(self.date_utc))

class Lauches:
    def __init__(self, request_api_address, lauch = Lauch):
        self.lauches = []
        r = requests.get(request_api_address)
        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                self.lauches.append(lauch(element["fairings"], element["links"], element["static_fire_date_utc"],
                                             element["rocket"], element["success"], element["details"],
                                          element["crew"], element["capsules"], element["payloads"],
                                          element["failures"], element["flight_number"], element["name"],
                                          element["date_utc"], element["cores"], element["id"]))

