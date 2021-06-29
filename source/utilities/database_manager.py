# -*- coding: utf-8 -*-

# flask imports
from flask_script import Manager, prompt_bool

# project imports
from extensions import db

manager = Manager(usage="Perform database operations")


@manager.command
def drop():
    """Drops database tables"""
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


@manager.command
def create():
    """Creates database tables from sqlalchemy models"""
    db.create_all()


@manager.command
def recreate():
    """Recreates database tables (same as issuing 'drop' and then 'create')"""
    drop()
    create()
