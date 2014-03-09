# -*- coding: utf-8 -*-

import os


defaults = {
    'DEBUG': False,
    'TESTING': False,
    'SECRET_KEY': '##CHANGEME##',
    'SQLALCHEMY_DATABASE_URI': 'postgresql://massa:secret@localhost/massa',
    'SQLALCHEMY_ECHO': False,
}


class FromEnvConfig(object):
    def __init__(self):
        for key, value in defaults.iteritems():
            setattr(self, key, os.getenv(key, value))
