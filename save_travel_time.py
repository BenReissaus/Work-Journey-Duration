#!/usr/bin/env python
# -*- coding: utf-8 -*-

import googlemaps
import sys
from settings import APIKEY
from models import *
import datetime

gmaps = googlemaps.Client(key=APIKEY)


work = Location.query.filter_by(alias="work").first()
home = Location.query.filter_by(alias="home").first()

current_time = datetime.datetime.now()


def save_go_home_time():
    save_travel_time(origin=work, destination=home, departure_time=current_time)


def save_go_to_work_time():
    save_travel_time(origin=home, destination=work, departure_time=current_time)


def save_travel_time(origin, destination, departure_time):
    direction_results = gmaps.directions(origin=origin.address,
                                         destination=destination.address,
                                         departure_time=departure_time,
                                         mode='driving',
                                         traffic_model='best_guess',
                                         alternatives=False)

    travel_duration = get_travel_duration(direction_results)

    qr = Journey(origin=origin, destination=destination,
                 departure_time=current_time, travel_duration=travel_duration)

    db.session.add(qr)
    db.session.commit()


def get_travel_duration(google_query_result):
    return google_query_result[0]["legs"][0]["duration_in_traffic"]["value"]


if __name__ == "__main__":
    error_message = "Usage: python save_travel_time.py [work | home]"
    if len(sys.argv) != 2:
        print error_message
        sys.exit(1)

    direction = sys.argv[1]

    if direction == "home":
        save_go_home_time()
    elif direction == "work":
        save_go_to_work_time()
    else:
        print error_message
        sys.exit(1)
