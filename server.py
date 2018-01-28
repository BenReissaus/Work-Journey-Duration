from flask import Flask
from flask import render_template
from flask import jsonify
from models import QueryResult
app = Flask(__name__)

@app.route('/work-journey-time')
def work_journey_time():
    return render_template('work_journey_time.jinja2')


@app.route('/calculate-averages')
def calculate_averages(destination="home"):

    if destination != "home" and destination != "work":
        destination = "home"

    return jsonify(QueryResult.averages(destination))
