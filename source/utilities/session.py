import pickle
from datetime import timedelta
from uuid import uuid4
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin


class RedisSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, id=None, new=False):
        def on_update(self):
            self.modified = True

        CallbackDict.__init__(self, initial, on_update)
        self.id = id
        self.new = new
        self.modified = False


class RedisSessionInterface(SessionInterface):
    serializer = pickle
    session_class = RedisSession

    def __init__(self, redis, prefix='psession:'):
        self.redis = redis
        self.prefix = prefix

    @staticmethod
    def generate_id():
        return str(uuid4())

    @staticmethod
    def get_redis_expiration_time(app, session):
        if session.permanent:
            return app.permanent_session_lifetime
        return timedelta(days=1)

    def open_session(self, app, request):
        id = request.cookies.get(app.session_cookie_name)
        if not id:
            id = self.generate_id()
            return self.session_class(id=id, new=True)
        val = self.redis.get(self.prefix + id)
        if val is not None:
            data = self.serializer.loads(val)
            return self.session_class(data, id=id)
        return self.session_class(id=id, new=True)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            self.redis.delete(self.prefix + session.id)
            if session.modified:
                response.delete_cookie(app.session_cookie_name,
                                       domain=domain)
            return
        redis_exp = self.get_redis_expiration_time(app, session)
        cookie_exp = self.get_expiration_time(app, session)
        val = self.serializer.dumps(dict(session))
        self.redis.setex(self.prefix + session.id, int(redis_exp.total_seconds()), val)
        response.set_cookie(app.session_cookie_name, session.id,
                            expires=cookie_exp, httponly=True,
                            domain=domain)


class FlaskRedisSession(object):
    def __init__(self, redis, app=None):
        self.redis = redis
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.session_interface = RedisSessionInterface(self.redis)
