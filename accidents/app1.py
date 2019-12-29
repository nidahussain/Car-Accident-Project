import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///accidentsSQL.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Accident = Base.classes.accidentsSQL

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/accidents<br/>"
        f"/api/v1.0/states"
    )

@app.route("/api/v1.0/accidents")
def IDs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all accident IDs"""
    # Query all accidents
    results = session.query(Accident.id).all()

    session.close()

    # Convert list of tuples into normal list
    all_IDs = list(np.ravel(results))

    return jsonify(all_IDs)


@app.route("/api/v1.0/accidents")
def accidents():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Return a list of accident data including the year (start_time has the year but need to parse), 
    # Start_lat, Start_lng and Weather_Condition of each accident"""
    # Query all passengers
    results = session.query(accidents.ID, accidents.Start_Time, accidents.Start_Lat, accidents.Start_Lng, accidents.Weather_Condition).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_accidents
    all_accidents = []
    for ID, Start_Time, Start_Lat, Start_Lng, Weather_Condition in results:
        accident_dict = {}
        accident_dict["id"] = ID
        accident_dict["start_time"] = Start_Time
        accident_dict["start_lat"] = Start_Lat
        accident_dict["start_lng"] = Start_Lng
        accident_dict["weather_condition"] = Weather_Condition
        all_accidents.append(accident_dict)

    return jsonify(all_accidents)


if __name__ == '__main__':
    app.run(debug=True)
