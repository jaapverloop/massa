# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server, prompt_bool
from massa import create_app
from massa.domain import make_tables, drop_tables


manager = Manager(create_app)
manager.add_option('-c', '--configfile', dest='configfile', required=False)

manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = 8080,
))

@manager.command
def dbmake():
  """Make all the db tables."""
  make_tables()

@manager.command
def dbdrop():
  """Drop all the db tables."""
  if prompt_bool('Are you sure you want to drop all the db tables?'):
    drop_tables()

if __name__ == '__main__':
    manager.run()
