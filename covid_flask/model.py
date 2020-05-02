from sqlalchemy import func

from .app_setup import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), unique=True, nullable=False)
    cases = db.Column(db.Integer())
    tests = db.Column(db.Integer())
    tested_people = db.Column(db.Integer())
    dead = db.Column(db.Integer())
    icu = db.Column(db.Integer())
    critical = db.Column(db.Integer())
    recovered = db.Column(db.Integer())
    time_updated = db.Column(db.TIMESTAMP(), server_default=func.now(), onupdate=func.current_timestamp())
    time_created = db.Column(db.TIMESTAMP(), server_default=func.now())

    def __repr__(self):
        return '<Data %r>' % self.date


class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    code = db.Column(db.String(), unique=True, nullable=False)



