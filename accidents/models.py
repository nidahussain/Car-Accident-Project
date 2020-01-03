from .app import db
# from sqlalchemy import create_engine
# from sqlalchemy import column, Integer, String, Float

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

class accident(db.Model):
    __tablename__ = 'us_accidents'
    accid = db.Column(db.varchar(100))
    severity = db.Column(db.varchar(100))
    start_time = db.Column(db.varchar(100))
    end_time = db.Column(db.varchar(100))
    start_lat = db.Column(db.varchar(100))
    start_lng = db.Column(db.varchar(100))
    distance = db.Column(db.varchar(100))
    description = db.Column(db.varchar(100))
    number = db.Column(db.varchar(100))
    street = db.Column(db.varchar(100))
    city = db.Column(db.varchar(100))
    county = db.Column(db.varchar(100))
    state = db.Column(db.varchar(100))
    zipcode = db.Column(db.varchar(100))
    weather_timestamp = db.Column(db.varchar(100))
    temperature = db.Column(db.varchar(100))
    wind_chill = db.Column(db.varchar(100))
    humidity = db.Column(db.varchar(100))
    pressure = db.Column(db.varchar(100))
    visibility = db.Column(db.varchar(100))
    wind_direction = db.Column(db.varchar(100))
    wind_speed = db.Column(db.varchar(100))
    precipitation = db.Column(db.varchar(100))
    weather_condition = db.Column(db.varchar(100))
    astronomical_twilight = db.Column(db.varchar(100))
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<accident %r>' % (self.name)
