#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(128), unique=True)
    address = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '{}: {}'.format(self.alias, self.address)


class Journey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    travel_duration = db.Column(db.Integer, nullable=False)

    origin = relationship("Location", foreign_keys=[origin_id])
    destination = relationship("Location", foreign_keys=[destination_id])


    def __repr__(self):
        format_string = 'origin: {} destination: {} departure time: {} travel time: {} min {} sec'
        travel_duration_min = self.travel_duration / 60
        travel_duration_sec = self.travel_duration % 60
        return format_string.format(self.origin.alias, self.destination.alias,
                                    self.departure_time, travel_duration_min, travel_duration_sec)

    @hybrid_property
    def departure_hour(self):
        return self.departure_time.hour

    @departure_hour.expression
    def departure_hour(cls):
        return db.func.extract('hour', cls.departure_time).cast(db.Integer)

    @staticmethod
    def _extract_quarter_hour(minute):
        return minute / 15

    @hybrid_property
    def departure_quarter(self):
        return self._extract_quarter_hour(self.departure_time.minute)

    @departure_quarter.expression
    def departure_quarter(cls):
        minute = db.func.extract('minute', cls.departure_time).cast(db.Integer)
        return cls._extract_quarter_hour(minute)

    @staticmethod
    def averages(destination_alias):
        destination_id = Location.query.filter_by(alias=destination_alias).first().id

        calculated_averages = db.session \
            .query(func.avg(Journey.travel_duration) / 60) \
            .filter(Journey.destination_id == destination_id) \
            .group_by(Journey.departure_hour, Journey.departure_quarter) \
            .order_by(Journey.departure_hour, Journey.departure_quarter) \
            .all()
        return calculated_averages
