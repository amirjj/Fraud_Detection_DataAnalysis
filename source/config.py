import os
from datetime import timedelta

SESSION_MANAGER_CONFIG = {}

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    DEPLOYMENT = False

    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    BLUEPRINTS = ('base',)
    EXTENSIONS = ('db', 'csrf', 'redis', 'redisSession', 'cache', 'login_manager', 'mail', 'recaptcha',  'cors')

    LDAP_PROVIDER_URL = ''
    
    LDAP_HOST = ''
    LDAP_LOGIN_VIEW = 'base.web.login'

    LDAP_BASE_DN = 'OU=Users,OU=MTN Irancell Accounts,DC=mtnirancell,DC=ir'
    LDAP_USERNAME = ''


    SECRET_KEY = 'Development'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Server Info
    SERVER_URL = os.environ.get('SERVER_URL')

    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = "RECAPTCHA_SITE_KEY"
    RECAPTCHA_SECRET_KEY = "RECAPTCHA_SECRET_KEY"
    RECAPTCHA_THEME = "light"
    RECAPTCHA_TYPE = "image"
    RECAPTCHA_SIZE = "normal"
    RECAPTCHA_RTABINDEX = 10

    REDIS_HOST = '127.0.0.1'
    
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = None

    REDIS_URL = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)

    SESSION_TYPE = 'redis'

    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SESSION_REFRESH_EACH_REQUEST = False
    SESSION_COOKIE_SECURE = True

    NOTIFICATION_REDIS_DB = 2

    UAT_SERVERS = ["teauc-test1"]
    PRODUCTION_SERVERS = ["teauc-pt1", "teauc-pt2", "teauc-pt3", "teauc-pt4", "teauc-pt5", "teauc-pt6", "teauc-pt7"]

    UPLOAD_DIR = os.path.join(basedir, 'upload')
    CORPORATE_UPLOAD_DIR = os.path.join(UPLOAD_DIR, 'corporate')

    CACHE_NO_NULL_WARNING = True

    TEMPLATES_AUTO_RELOAD = True

    LOG_ADMINS = []
    LOG_LOCATION = os.path.join(basedir, 'app.log')


class DeploymentConfig(DefaultConfig):
    DEVELOPMENT = False
    DEBUG = False
    ENVIRONMENT = 'PRODUCTION'

    APP_IP = ''
    APP_PORT = '8000'
    APP_URL = APP_IP  # + ':' + APP_PORT

    SESSION_MANAGER_CONFIG = {
        'login_url': APP_URL + '/user/login',
        'logout_url': APP_URL + '/user/logout'
    }

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    APP_IP = 'http://10.233.50.80'
    APP_PORT = '8000'
    APP_URL = APP_IP + ':' + APP_PORT


    SESSION_MANAGER_CONFIG = {
        'login_url': APP_URL + '/login',
        'logout_url': APP_URL + '/logout'
    }

    # SESSION_MANAGER_CONFIG = {
    #     'login_url': APP_URL + '/user/login',
    #     'logout_url': APP_URL + '/user/logout'
    # }


class PreProductionConfig(DefaultConfig):
    DEBUG = True
    ENVIRONMENT = 'PREPRODUCTION'

    APP_IP = ''
    APP_PORT = '18000'
    APP_URL = APP_IP + ':' + APP_PORT

    SESSION_MANAGER_CONFIG = {
        'login_url': APP_URL + '/user/login',
        'logout_url': APP_URL + '/user/logout'
    }


class TestingConfig(DefaultConfig):
    TESTING = True
