from flask import Flask, g, request, session, redirect, url_for
from flask_simpleldap import LDAP

app = Flask(__name__)
app.secret_key = 'dev key'
app.debug = True

# app.config['LDAP_HOST'] = '10.132.57.208'
# app.config['LDAP_BASE_DN'] = 'OU=Business Risk Management,OU=Tehran,OU=Staff,OU=Users,OU=MTN Irancell Accounts,DC=mtnirancell,DC=ir'
# app.config['LDAP_USERNAME'] = 'CN=Amir Jamshidi Jam - 02704,OU=Business Risk Management,OU=Tehran,OU=Staff,OU=Users,OU=MTN Irancell Accounts,DC=mtnirancell,DC=ir'

ldap = LDAP(app)

@app.route('/')
@ldap.basic_auth_required
def index():
    return 'Welcome, {0}!'.format(g.ldap_username)

@app.route('/lo')
def lo():
    g.ldap_username = None
    return "done"
if __name__ == '__main__':
    app.run(host='0.0.0.0')