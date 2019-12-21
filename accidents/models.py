from .app import db


class Accident(db.Model):
    __tablename__ = 'Accident'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        return '<Accident %r>' % (self.name)
