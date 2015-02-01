import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

from config import basedir

app = Flask(__name__)
app.config.from_object('config')
bc = Bcrypt(app)
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from kaiserapp import views, models
