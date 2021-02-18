import json
import requests

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
        self.date_utc = date_utc
        self.cores = cores
        self.id = id

class Lauches:
    def __init__(self):
        self.lauches = []

    def upcoming(self, request_api_address):

        r = requests.get(request_api_address)

        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                None

