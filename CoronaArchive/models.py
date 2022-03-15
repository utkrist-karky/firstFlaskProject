from CoronaArchive import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    if User.query.get(int(user_id)):
        return User.query.get(int(user_id))
    elif Place.query.get(int(user_id)):
        return Place.query.get(int(user_id))
    else:
        return Hospital.query.get(int(user_id))    
    

class User(db.Model,UserMixin):
    userID = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20),unique = True, nullable = False)
    phoneNumber = db.Column(db.String(20),unique = True, nullable = False)
    deviceID = db.Column(db.String(20), unique = True, nullable = True)
    infected = db.Column(db.Boolean,nullable = False, default = False)
    password = db.Column(db.String(60), nullable = False)
    
    def __repr__(self):
        return f"User('{self.name}','{self.infected}')"
    
    def get_id(self):
        return(self.userID)   
    
    
class Place(db.Model,UserMixin):
    placeID = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20),unique = True, nullable = False)
    phoneNumber = db.Column(db.String(20),unique = True, nullable = False)
    QRCode = db.Column(db.String(100), unique = True, nullable = True)
    password = db.Column(db.String(60), nullable = False)
    def __repr__(self):
        return f"Place('{self.name}')"
    
    def get_id(self):
        return(self.placeID) 
    
class Hospital(db.Model,UserMixin):
    hospitalID = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20),unique = True, nullable = False)
    phoneNumber = db.Column(db.String(20),unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    def __repr__(self):
        return f"Hostpital('{self.name}')"
    
    def get_id(self):
        return(self.hospitalID) 