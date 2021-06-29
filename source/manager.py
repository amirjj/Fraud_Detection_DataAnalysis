#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;


# flask imports
from flask_script import Manager as Manager
from flask_migrate import MigrateCommand as MigrateCommand

# project imports
from application import create_app
from config import DevelopmentConfig
from utilities.database_manager import manager as database_manager

app = create_app(DevelopmentConfig)
manager = Manager(app)

manager.add_command("database", database_manager)
manager.add_command("migration", MigrateCommand)

@manager.command
def run():
    """
    Run server on port 5000 and domain name 4konj.local
    """
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)


@manager.command
def routes():
    """
    Get all application http routes
    """
    import urllib

    output = [urllib.unquote("\033[1m{:50s} {:20s} {}\033[0;0m".format('Endpoint', 'Methods', 'Rule'))]
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    manager.run()
