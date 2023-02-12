from flask import Flask
from flask_simpleldap import LDAP

from flask_login import current_user, login_user, logout_user, login_required
from flask import flash, url_for, g


app = Flask(__name__)

ldap = LDAP(app)

@app.route('/ldap')
@ldap.login_required
def ldap_protected():
    return 'Success!'

@app.before_request
def before_request():
    g.user = current_user
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
