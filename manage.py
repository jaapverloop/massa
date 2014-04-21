#!/usr/bin/env python
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


if __name__ == '__main__':
    manager.run()
