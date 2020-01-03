import sys
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy import or_

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
################################################
# Maps Setup
#################################################
mapkey = os.environ.get('MAPKEY', '') or "CREATE MAPKEY ENV"
#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/accidentsSQL.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Catpuss10!@localhost/US_Accidents'
db = SQLAlchemy(app)

######this stuff is to try to get .models to import####
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#######################################################

# from .models import accident

class accident(db.Model):
    __tablename__ = 'us_accidents'
    accid = db.Column('accid', db.Unicode(100))
    severity = db.Column(db.Unicode(100))
    start_time = db.Column(db.Unicode(100))
    end_time = db.Column(db.Unicode(100))
    start_lat = db.Column(db.Unicode(100))
    start_lng = db.Column(db.Unicode(100))
    distance = db.Column(db.Unicode(100))
    description = db.Column(db.Unicode(100))
    number = db.Column(db.Unicode(100))
    street = db.Column(db.Unicode(100))
    city = db.Column(db.Unicode(100))
    county = db.Column(db.Unicode(100))
    state = db.Column(db.Unicode(100))
    zipcode = db.Column(db.Unicode(100))
    weather_timestamp = db.Column(db.Unicode(100))
    temperature = db.Column(db.Unicode(100))
    wind_chill = db.Column(db.Unicode(100))
    humidity = db.Column(db.Unicode(100))
    pressure = db.Column(db.Unicode(100))
    visibility = db.Column(db.Unicode(100))
    wind_direction = db.Column(db.Unicode(100))
    wind_speed = db.Column(db.Unicode(100))
    precipitation = db.Column(db.Unicode(100))
    weather_condition = db.Column(db.Unicode(100))
    astronomical_twilight = db.Column(db.Unicode(100))
    id = db.Column(db.Integer, primary_key=True)

    # def __repr__(self):
    #     return '<accident %r>' % (self.name)

    # def __init__(self, severity, start_time, end_time):
    #     self.severity = severity
    #     self.start_time = start_time
    #     self.end_time = end_time

    def __repr__(self):
        return '<id {}>'.format(self.id)

Base = automap_base()
Base.prepare(db.engine, reflect=True)

@app.route("/")
def home():
    return render_template("index.html")

# create route that renders maps.html template
@app.route("/maps")
def maps():
    return render_template("map.html")

# create route that gives us our map key
@app.route("/mapkey")
def mapkeyroute():
    global mapkey
    config = { "apikey": mapkey }
    return jsonify(config)

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        state = request.form["accState"]

        acc = accident(name=state)
        db.session.add(acc)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

@app.route("/api/accidents")
def accidents():
    results = db.session.query(accident.start_lat, accident.start_lng).all()

    hover_text = [result[0] for result in results]
    start_lat = [result[1] for result in results]
    start_lng = [result[2] for result in results]

    acc_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": start_lat,
        "lon": start_lng,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(acc_data)


if __name__ == "__main__":
    app.run()