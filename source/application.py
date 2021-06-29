# python imports
import os
import logging
from logging.handlers import RotatingFileHandler



from flask_sqlalchemy import SQLAlchemy as SQLAlchemy
from flask_login import LoginManager


# flask imports
from flask import Flask, request, render_template, redirect, url_for

from config import DefaultConfig
from config import DevelopmentConfig
from config import TestingConfig


app = Flask(__name__)
login_manager = LoginManager()

def configure_app(app, configuration):
    app.config.from_object(DefaultConfig)
#     app.config.from_object(TestingConfig)

    if configuration is not None:
        app.config.from_object(configuration)

    app.config.from_pyfile('environ.py', silent=True)


def configure_blueprints(app):
    for blueprint in app.config['BLUEPRINTS']:
        bp = __import__('blueprints.%s' % blueprint, fromlist=[blueprint])

        for route in bp.__all__:
            app.register_blueprint(getattr(bp, route))


def configure_extensions(app):
    import extensions as ex
    from extensions import migrate, db

    for extension in app.config['EXTENSIONS']:
        try:
            getattr(ex, extension).init_app(app)
        except (AttributeError, TypeError):
            pass
    migrate.init_app(app, db, directory='migrations/', compare_type=True)


def configure_request_handlers(app):
    @app.after_request
    def add_header(response):
        response.cache_control.private = True
        response.cache_control.public = False
        return response


def configure_directories(app):
    for key, value in app.config.items():
        if key.endswith('DIR'):
            if not os.path.exists(value):
                os.makedirs(value, mode=0775)
                app.logger.info("{} created at {}".format(key, value))


def configure_loggers(app):
    from utilities.log import report_logger

    file_handler = RotatingFileHandler(app.config['LOG_LOCATION'], maxBytes=1000000, backupCount=10)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    file_handler.setLevel(logging.INFO)
    report_logger.setLevel(logging.INFO)
    report_logger.addHandler(file_handler)


def configure_sentry(app):
    from extensions import sentry

    if 'SENTRY_DSN' in app.config:
        sentry.init_app(app, dsn=app.config['SENTRY_DSN'])



def lmcreate(app):
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # app.config['WTF_CSRF_SECRET_KEY'] = 'random key for form'
    # app.config['LDAP_PROVIDER_URL'] = 'ldap://ldap.testathon.net:389/'
    # app.config['LDAP_PROTOCOL_VERSION'] = 3
    # app.config['LDAP_BASE_DN'] = 'OU=Users,OU=MTN Irancell Accounts,DC=mtnirancell,DC=ir'
    # app.config['LDAP_USERNAME'] = 'CN=amir.jams,OU=Users,OU=MTN Irancell Accounts,DC=mtnirancell,DC=ir'

    db = SQLAlchemy(app)

    app.secret_key = 'some_random_key'


    login_manager.init_app(app)
    # login_manager.login_view = 'base.web.login'
    login_manager.login_view = 'base.web.login'

    # db.create_all()



def create_app(configuration):
    configure_app(app, configuration)
    configure_directories(app)
    configure_extensions(app)
    configure_blueprints(app)
    lmcreate(app)
    configure_request_handlers(app)
    configure_loggers(app)
    configure_sentry(app)

    return app

# def get_app():
#     app = Flask(__name__)
#     return app