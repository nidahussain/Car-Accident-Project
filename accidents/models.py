from .app import db


class Accident(db.Model):
    __tablename__ = 'Accidents'

    ID = db.Column(db.varchar, primary_key=True)
    Start_Time = db.Column(db.varchar)
    Start_Lat = db.Column(db.varchar)
    Start_Lon = db.Column(db.varchar)
    Weather_Condition = db.Column(db.varchar)

    def __repr__(self):
        return '<Accident %r>' % (self.name)
