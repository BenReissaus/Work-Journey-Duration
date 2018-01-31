from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from models import Journey, Location
from sqlalchemy import func

app = Flask(__name__)

@app.route('/work-journey-time')
def work_journey_time():
    return render_template('work_journey_time.jinja2')


@app.route('/calculate-averages')
def calculate_averages():

    destination = request.args.get("destination", default="home")
    if destination != "home" and destination != "work":
        destination = "home"

    return jsonify(Journey.averages(destination))
