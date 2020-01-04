# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Maps Setup
#################################################
mapkey = os.environ.get('MAPKEY', '') or "CREATE MAPKEY ENV"

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('us_accidents', '') or "sqlite:///accidentsSQL.sql"


# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)

from .models import accident


# create route that renders index.html template
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
    results = db.session.query(accident.name, accident.lat, accident.lon).all()

    hover_text = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    acc_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
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
