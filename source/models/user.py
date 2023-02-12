# python imports
import datetime
import jdatetime
import ldap
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired
from application import app
from flask import jsonify

# project imports
from extensions import db

# from application import create_app
# from config import DefaultConfig
# TODO remove redundant jsonified property

# app = create_app(DefaultConfig)

def get_ldap_connection():
    print app.config['LDAP_PROVIDER_URL']


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username

    @staticmethod
    def try_login(username, password):
        print username
        print password

        conn = get_ldap_connection()

        print conn

        conn.simple_bind_s(
            '' % username,
            password
        )

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class LoginForm(Form):
    username = TextField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
