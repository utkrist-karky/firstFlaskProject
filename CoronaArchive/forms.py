
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError 
from CoronaArchive.models import *
class UserRegistrationForm(FlaskForm):
    name = StringField('Full Name',validators=[DataRequired(), Length(min = 2, max =20)])
    address = StringField('Adress',validators=[DataRequired()])
    phone_number = StringField('Phone Number',validators = [DataRequired(),Length(min = 8, max = 12)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
    SubmitField = SubmitField('Sign up')
    
    def validate_email(self,email):
        if User.query.filter_by(email=email.data).first() or Place.query.filter_by(email=email.data).first() or Hospital.query.filter_by(email=email.data).first():
            raise ValidationError('Email Adress already taken')
        
    def validate_phone_number(self,phone_number):
        if User.query.filter_by(phoneNumber=phone_number.data).first() or Place.query.filter_by(phoneNumber=phone_number.data).first() or Hospital.query.filter_by(phoneNumber=phone_number.data).first():
            raise ValidationError('Phone number already taken')
    
class PlaceRegistrationForm(FlaskForm):
    name = StringField('Place Name',validators=[DataRequired(), Length(min = 2, max =20)])
    address = StringField('Adress',validators=[DataRequired()])
    phone_number = StringField('Phone Number',validators = [DataRequired(),Length(min = 8, max = 12)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
    SubmitField = SubmitField('Sign up')
    
    def validate_email(self,email):
        if User.query.filter_by(email=email.data).first() or Place.query.filter_by(email=email.data).first() or Hospital.query.filter_by(email=email.data).first():
            raise ValidationError('Email Adress already taken')
        
    def validate_phone_number(self,phone_number):
        if User.query.filter_by(phoneNumber=phone_number.data).first() or Place.query.filter_by(phoneNumber=phone_number.data).first() or Hospital.query.filter_by(phoneNumber=phone_number.data).first():
            raise ValidationError('Phone number already taken')
    
class HospitalRegistrationForm(FlaskForm):
    name = StringField('Hospital Name',validators=[DataRequired(), Length(min = 2, max =20)])
    address = StringField('Adress',validators=[DataRequired()])
    phone_number = StringField('Phone Number',validators = [DataRequired(),Length(min = 8, max = 12)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
    SubmitField = SubmitField('Sign up')
    
    def validate_email(self,email):
        if User.query.filter_by(email=email.data).first() or Place.query.filter_by(email=email.data).first() or Hospital.query.filter_by(email=email.data).first():
            raise ValidationError('Email Adress already taken')
        
    def validate_phone_number(self,phone_number):
        if User.query.filter_by(phoneNumber=phone_number.data).first() or Place.query.filter_by(phoneNumber=phone_number.data).first() or Hospital.query.filter_by(phoneNumber=phone_number.data).first():
            raise ValidationError('Phone number already taken')

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    SubmitField = SubmitField('Login')