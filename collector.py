#!/usr/bin/env python
# -*- coding: utf-8 -*-

import googlemaps
from settings import APIKEY
from datetime import datetime

gmaps = googlemaps.Client(key=APIKEY)

origin = "Großbeerenstraße 75, 14482 Potsdam"
destination = "Carmeq GmbH, Carnotstraße 4, 10587 Berlin"
current_time = datetime.now()

direction_results = gmaps.directions(origin=origin,
                 destination=destination,
                 departure_time=current_time,
                 alternatives=False)

travel_duration = direction_results[0]["legs"][0]["duration_in_traffic"]["value"]

print "Departure Time: {}".format(current_time)
print "Origin: {}".format(origin)
print "Destination: {}".format(destination)
print "Travel Duration: {} min {} sec".format(travel_duration / 60, travel_duration % 60)
