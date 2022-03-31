from CoronaArchive import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    if User.query.get((user_id)):
        return User.query.get((user_id))
    elif Place.query.get((user_id)):
        return Place.query.get((user_id))
    elif Agent.query.get((user_id)):
        return Agent.query.get((user_id))
    else:
        return Hospital.query.get((user_id))    
    

class User(db.Model,UserMixin):

    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20),unique = True, nullable = False, primary_key = True)
    phoneNumber = db.Column(db.String(20),unique = True, nullable = False)
    deviceID = db.Column(db.String(20), unique = True, nullable = True)
    infected = db.Column(db.Boolean,nullable = False, default = False)
    active_visitation = db.Column(db.Integer, default = 0)
    password = db.Column(db.String(60), nullable = False)
    visitations = db.relationship('Visitation', backref='user', lazy=True)
    
    def __repr__(self):
        return f"User('{self.name}','{self.infected}')"
    
    def get_id(self):
        return(self.email)   
    
    
class Place(db.Model,UserMixin):

    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20),unique = True, nullable = False, primary_key = True)
    phoneNumber = db.Column(db.String(20),unique = True, nullable = False)
    QRCode = db.Column(db.String(100), unique = True, nullable = True)
    password = db.Column(db.String(60), nullable = False)
    visitations = db.relationship('Visitation',backref='place',lazy=True)
    def __repr__(self):
        return f"Place('{self.name}')"
    
    def get_id(self):
        return(self.email) 
    
class Hospital(db.Model,UserMixin):
    
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20),unique = True, nullable = False,primary_key = True)
    phoneNumber = db.Column(db.String(20),unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    def __repr__(self):
        return f"Hostpital('{self.name}')"
    
    def get_id(self):
        return(self.email) 


class Visitation(db.Model,UserMixin):
    visitationID = db.Column(db.Integer,primary_key = True)
    entryTime = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    exitTime = db.Column(db.DateTime,nullable = True, default = datetime.utcnow)
    userEmail = db.Column(db.String, db.ForeignKey('user.email'), nullable = False)
    placeEmail = db.Column(db.String, db.ForeignKey('place.email'), nullable = False)
    
    
class Agent(db.Model,UserMixin):

    email = db.Column(db.String(20),unique = True, nullable = False,primary_key = True)
    password = db.Column(db.String(60), nullable = False)
    def get_id(self):
        return(self.email)
    

