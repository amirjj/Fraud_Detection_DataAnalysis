# python imports

# flask imports
from flask_wtf import CSRFProtect
from flask_migrate import Migrate as Migrate
from flask_sqlalchemy import SQLAlchemy as SQLAlchemy
from flask_caching import Cache as Cache
from flask_redis import FlaskRedis as FlaskRedis
from flask_login import LoginManager
from flask_mail import Mail
from flask_recaptcha import ReCaptcha
from flask_cors import CORS
from raven.contrib.flask import Sentry

# project imports
from utilities.session import FlaskRedisSession

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
redis = FlaskRedis()
redisSession = FlaskRedisSession(redis)
cache = Cache()
login_manager = LoginManager()
mail = Mail()
recaptcha = ReCaptcha()
cors = CORS()
sentry = Sentry()

