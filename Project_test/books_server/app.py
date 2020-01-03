import os
from flask import (Flask,render_template,jsonify,request,redirect)

app = Flask(__name__)
from flask_SQLAlchemy import SQLAlchemy
app.config['SQLAlchemy_DATABASE_URI'] = 'postgresql://postgres:1Menew1!@localhost/Accidents'
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

   