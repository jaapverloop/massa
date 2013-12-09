# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from massa import create_app


manager = Manager(create_app)
manager.add_option('-c', '--configfile', dest='configfile', required=False)

manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = 8080,
))

if __name__ == '__main__':
    manager.run()
