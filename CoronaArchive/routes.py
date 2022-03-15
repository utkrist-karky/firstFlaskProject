from flask import render_template,url_for,flash,redirect
from sqlalchemy import false
from CoronaArchive.forms import *
from CoronaArchive.models import *
from CoronaArchive import app, db, bcrypt
from flask_login import login_user

@app.route('/', methods = ['GET','POST'])
def index(): 
    form = Login()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            user =  User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=false)
                return redirect(url_for('user_login'))
            elif form.email.data == 'admin' and form.password.data == 'password':
                return redirect(url_for('get_admin'))
            else: 
                flash("Oh snap")
        elif Place.query.filter_by(email=form.email.data).first():
            user =  Place.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=false)
                return redirect(url_for('user_login'))
            elif form.email.data == 'admin' and form.password.data == 'password':
                return redirect(url_for('get_admin'))
            else: 
                flash("Oh snap")
    
        else:
            user = Hospital.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=false)
                return redirect(url_for('user_login'))
            elif form.email.data == 'admin' and form.password.data == 'password':
                return redirect(url_for('get_admin'))
            else: 
                flash("Oh snap") 
        
    return render_template('landing-page.html', form = form)

@app.route('/user-login')
def user_login():
    return render_template('user-home.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email = form.email.data, phoneNumber = form.phone_number.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'User Account created, You can now login')
        return redirect(url_for('index'))
    
    return render_template('registration.html', form = form)

@app.route('/signup-places', methods = ['GET','POST'])
def signup_places():
    form = PlaceRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Place(name=form.name.data, email = form.email.data, phoneNumber = form.phone_number.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Place Account created, You can now login')
        return redirect(url_for('index'))
    
    return render_template('registration.html', form = form)

@app.route('/signup-hospital', methods = ['GET','POST'])
def signup_hospital():
    form = HospitalRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Hospital(name=form.name.data, email = form.email.data, phoneNumber = form.phone_number.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Hospital Account created, You can now login')
        return redirect(url_for('index'))
        
    return render_template('registration.html', form = form)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/create-account')
def create():
    return render_template('user-home.html')

@app.route('/create-account-places')
def create_places():
    return render_template('place-home.html')

@app.route('/create-account-hospital')
def create_hospital():
    return render_template('hospital-home.html')

@app.route('/admin-access')
def get_admin():
    return render_template('agent-home.html')