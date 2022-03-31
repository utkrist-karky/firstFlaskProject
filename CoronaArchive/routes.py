from flask import render_template,url_for,flash,redirect
from numpy import isin
from sqlalchemy import false
from CoronaArchive.forms import *
from CoronaArchive.models import *
from CoronaArchive import app, db, bcrypt
from flask_login import login_user, current_user, logout_user
from datetime import datetime

@app.route('/', methods = ['GET','POST'])
def index(): 
    
    form = Login()
    if current_user.is_authenticated: 
        return redirect(url_for('user_login'))
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            user =  User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_passworAd_hash(user.password,form.password.data):
                login_user(user,remember=false)
                return redirect(url_for('user_login'))
        
        elif Place.query.filter_by(email=form.email.data).first():
            user =  Place.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=false)
                return redirect(url_for('user_login'))
            
                
        elif Agent.query.filter_by(email=form.email.data).first():
            user =  Agent.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=false)
                return redirect(url_for('user_login'))
            
    
        elif Hospital.query.filter_by(email=form.email.data).first():
            user = Hospital.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=false)
                return redirect(url_for('user_login'))
        else: 
            flash(f'Please check the email and the password and try again')
         
        
    return render_template('landing-page.html', form = form)

@app.route('/user-login', methods = ['GET','POST'])
def user_login():
    user_email = current_user.email
    if User.query.filter_by(email=user_email).first():
        if current_user.active_visitation != 0: 
            return render_template('active-visitation.html')
        return render_template('user-home.html')
    elif Place.query.filter_by(email=user_email).first():
        return render_template('place-home.html')
    elif Agent.query.filter_by(email=user_email).first():
        return render_template('agent-home.html')
    elif Hospital.query.filter_by(email=user_email).first():
        form = infectUser()
        if form.validate_on_submit():
            if form.status.data: 
                try: 
                    User.query.get(form.userEmail.data).infected = True
                except:
                    flash(f'that user does not exist')
            else: 
                User.query.get(form.userEmail.data).infected = False
            db.session.commit()
            flash(f'Updated')
            return redirect(url_for('user_login'))
        return render_template('hospital-home.html', form = form)
    else: 
        return render_template('signup-landing.html')

@app.route('/signup_landing')
def signup_landing():
    return render_template('signup-landing.html')

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

@app.route('/scan_qr', methods = ['GET','POST'])
def scan_qr():
    form = ScanQRCodeForm()
    if form.validate_on_submit(): 
        visit = Visitation(entryTime=datetime.now(),userEmail = current_user.email, placeEmail = form.placeEmail.data)
        db.session.add(visit)
        db.session.commit()
        current_user.active_visitation = visit.visitationID
        db.session.commit()
        return redirect(url_for('user_login'))
    return render_template('scan-qr.html', form = form)

@app.route('/end_visit')
def end_visit(): 
    Visitation.query.get(int(current_user.active_visitation)).exitTime = datetime.now()
    current_user.active_visitation = 0
    
    db.session.commit()
    return redirect(url_for('user_login'))

@app.route('/logout')
def logout():
    
    logout_user()
    return redirect(url_for('index'))


@app.route('/place-list')
def place_list():
    return render_template('place_list.html', places = Place.query.all())

@app.route('/dash_board')
def dash_board():
    user_email = current_user.email
    
    if User.query.filter_by(email=user_email).first():
        return render_template('user_dashboard.html', visits = Visitation.query.all())
    elif Place.query.filter_by(email=user_email).first():
        return render_template('place_dashboard.html', visits = Visitation.query.all())
    elif Agent.query.filter_by(email=user_email).first():
        return render_template('Agent_dashboard.html', visits = Visitation.query.all())
    elif Hospital.query.filter_by(email=user_email).first():
        return render_template('hostpital_dashboard.html', visits = Visitation.query.all())
    else: 
        return render_template('signup-landing.html')
 

@app.route('/documentation')
def doc():
    return redirect(url_for('index'))