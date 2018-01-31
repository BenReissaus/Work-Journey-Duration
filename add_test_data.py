#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *
import datetime

home = Location.query.filter_by(alias="home").first()
work = Location.query.filter_by(alias="work").first()
datetime_start = datetime.datetime.strptime('28.01.2018 19:56', '%d.%m.%Y %H:%M')

for i in range(6):
    departure_time = datetime_start + datetime.timedelta(minutes=i*7)
    qr = Journey(origin=home, destination=work, departure_time=departure_time,
                 departure_hour=departure_time.hour,
                 departure_quarter=departure_time.minute / 15,
                 travel_duration=i * 4)
    db.session.add(qr)

db.session.commit()
