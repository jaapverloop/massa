# -*- coding: utf-8 -*-

from flask import current_app, g
from flask.ext.script import Manager, Server, prompt_bool
from massa import create_app


manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)

manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = 5000,
))


@manager.command
def db_create_tables():
  """Create all the db tables."""
  current_app.preprocess_request()
  db = g.sl('db')
  db.create_tables()


@manager.command
def db_drop_tables():
  """Drop all the db tables."""
  if prompt_bool('Are you sure you want to drop all the db tables?'):
    current_app.preprocess_request()
    db = g.sl('db')
    db.drop_tables()


@manager.command
def db_reset_tables():
  """Drop and (re)create all the db tables."""
  if prompt_bool('Are you sure you want to reset all the db tables?'):
    current_app.preprocess_request()
    db = g.sl('db')
    db.drop_tables()
    db.create_tables()


if __name__ == '__main__':
    manager.run()
