from app import db

class Accident(db.Model):
    __tablename__ = 'us_accidents'
    accid = db.Column(db.Integer, primary_key=True)
    severity = db.Column(db.String())
    start_time = db.Column(db.String())
    end_time = db.Column(db.String())
    start_lat = db.Column(db.String())
    start_lng = db.Column(db.String())
    distance = db.Column(db.String())
    description = db.Column(db.String())
    number = db.Column(db.String())
    street = db.Column(db.String())
    city = db.Column(db.String())
    county = db.Column(db.String())
    state = db.Column(db.String())
    zipcode = db.Column(db.String())
    weather_timestamp = db.Column(db.String())
    temperature = db.Column(db.String())
    wind_chill = db.Column(db.String())
    humidity = db.Column(db.String())
    pressure = db.Column(db.String())
    visibility = db.Column(db.String())
    wind_direction = db.Column(db.String())
    wind_speed = db.Column(db.String())
    precipitation = db.Column(db.String())
    weather_condition = db.Column(db.String())
    astronomical_twilight = db.Column(db.String())
  
    def __init__(self, severity, start_time, end_time):
        self.severity = severity
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'accid': self.accid, 
            'severity': self.severity,
            'start_time': self.start_time,
            'end_time':self.end_time
        }