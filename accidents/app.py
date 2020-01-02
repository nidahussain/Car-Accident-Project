import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
# from models1 import Accident

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models1 import Accident

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getall")
def get_all():
    try:
        accidents=Accident.query.all()
        return jsonify([e.serialize() for e in accidents])
    except Exception as e:
	    return(str(e))