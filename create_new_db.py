from CoronaArchive import db, bcrypt
from CoronaArchive.models import Agent, User, Place, Hospital

db.create_all()
agent = Agent(email = 'admin', password = bcrypt.generate_password_hash('password').decode('utf-8'))
db.session.add(agent)
db.session.commit()
user= User(name='Monica Geller', email = 'm.geller@gmail.com', phoneNumber = '12345678', password= bcrypt.generate_password_hash('password').decode('utf-8'))
db.session.add(user)
db.session.commit()
place = Place(name='Pizza Protein', email = 'p.protein@gmail.com', phoneNumber = '76458975', password= bcrypt.generate_password_hash('password').decode('utf-8'))
db.session.add(place)
db.session.commit()
hospital = Hospital(name='Hospital1', email = 'hospital1@gmail.com', phoneNumber = '5522641404', password= bcrypt.generate_password_hash('password').decode('utf-8'))
db.session.add(hospital)
db.session.commit()
db.session.commit()
user= User(name='Ross Geller', email = 'r.geller@gmail.com', phoneNumber = '364870552', password= bcrypt.generate_password_hash('password').decode('utf-8'))
db.session.add(user)
db.session.commit()
place = Place(name='Pizza Protein', email = 'pp', phoneNumber = '76458975', password= bcrypt.generate_password_hash('password').decode('utf-8'))
db.session.add(place)
db.session.commit()
hospital = Hospital(name='New Hospital', email = 'hosp', phoneNumber = '5522641404', password= bcrypt.generate_password_hash('password').decode('utf-8'))
db.session.add(hospital)
db.session.commit()