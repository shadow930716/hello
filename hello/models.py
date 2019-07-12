from datetime import datetime
from hello import db

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    body=db.Column(db.String(200))
    age=db.Column(db.Integer)
    score=db.Column(db.Integer)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow,index=True)
    