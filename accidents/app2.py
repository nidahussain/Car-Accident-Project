import os
import sqlite3
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy
from flask import json
from flask import url_for
import psycopg2

# start here
from configparser import ConfigParser

# ###try this###
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# db = SQLAlchemy(app)
# from .models import Accident
# ###end try this###
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
engine = create_engine("sqlite:///accidentsSQL.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Accident = Base.classes.accidentsSQL
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///data/accidentsSQL.sqlite"
db = SQLAlchemy(app)
from .models import accident
Base = automap_base()
Base.prepare(db.engine, reflect=True)

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
######## FLASK END

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

# end here

conn = psycopg2.connect("dbname=US_Accidents user=postgres password=Catpuss10!")

def get_accidents():
    """ query data from the accidents table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM us_accidents ORDER BY start_time")
        print("The number of accidents: ", cur.rowcount)
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_accidents()