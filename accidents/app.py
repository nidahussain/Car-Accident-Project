import sys
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
import json
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy import or_

################################################
# Maps Setup
#################################################
mapkey = os.environ.get('MAPKEY', '') or "CREATE MAPKEY ENV"
#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///accidentsSQL.sqlite")
engine = create_engine('postgresql://postgres:Catpuss10!@localhost/US_Accidents')
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to table
Accidents = Base.classes.us_accidents
# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Database Setup
#################################################
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/accidentsSQL.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Catpuss10!@localhost/accidents_small'
db = SQLAlchemy(app)

######this stuff is to try to get .models to import####
# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#######################################################
# from .models import accidents

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
    config = { "api_key": mapkey }
    return jsonify(config)

# Query the database and send the jsonified results
# Can we update this to choose a state abbrev. and open a map to that state or list accident data for that state?
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        state = request.form["accState"]
        accidents = accidents(name=state)
        db.session.add(accidents)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

@app.route("/api/accidents")
def getAccidentData():
    results = db.session.query(Accidents.state, Accidents.start_lat, Accidents.start_lng).all()
    state = [result[0] for result in results]
    start_lat = [result[1] for result in results]
    start_lng = [result[2] for result in results]

    # for result in results:
    #     row = list(result)
    #     print(row[0])
    #     print(row[1])
    #     print(row[2])
    #     break

    acc_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": start_lat,
        "lon": start_lng,
        "text": state,
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