from flask_ldap3_login import LDAP3LoginManager

config = dict()

# Setup LDAP Configuration Variables. Change these to your own settings.
# All configuration directives can be found in the documentation.

# Hostname of your LDAP Server
config['LDAP_HOST'] = ''

# Base DN of your directory
# config['LDAP_BASE_DN'] = 'dc=mydomain,dc=com'
config['LDAP_BASE_DN'] = ''


# The RDN attribute for your user schema on LDAP
config['LDAP_USER_RDN_ATTR'] = 'cn'

# The Attribute you want users to authenticate to LDAP with.
config['LDAP_USER_LOGIN_ATTR'] = 'mail'

# The Username to bind to LDAP with
config['LDAP_BIND_USER_DN'] = None

# The Password to bind to LDAP with
config['LDAP_BIND_USER_PASSWORD'] = None

# Setup a LDAP3 Login Manager.
ldap_manager = LDAP3LoginManager()

# Init the mamager with the config since we aren't using an app
ldap_manager.init_config(config)
