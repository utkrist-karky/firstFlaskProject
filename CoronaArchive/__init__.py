from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_qrcode import QRcode
app = Flask(__name__)
app.config['SECRET_KEY'] = '1111111111111111'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///corona_archive_db.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
qecode = QRcode(app)
from CoronaArchive import routes