# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from yoyo import create_app


manager = Manager(create_app)
manager.add_option('-c', '--configfile', dest='configfile', required=False)

if __name__ == '__main__':
    manager.run()
