from app import db
import datetime


class Snpp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    destination = db.Column(db.String(15))
    port = db.Column(db.String(15))
    username = db.Column(db.String(15))
    password = db.Column(db.String(15))
    recipientList = db.Column(db.String(15))
    message = db.Column(db.String(15))
    status = db.Column(db.String(15))
    created = db.Column(db.DateTime, index=True, default=datetime.datetime.now())
    updated = db.Column(db.DateTime)

    def __repr__(self):
        return '<SNPP %r' % (self.id)
