# -*- coding: utf-8 -*-

import logging


class Production(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '##CHANGEME##'
    SQLALCHEMY_DATABASE_URI = 'postgresql://massa:secret@localhost/massa'
    SQLALCHEMY_ECHO = False
    LOGGER_FILENAME = 'massa.log'


class Development(Production):
    DEBUG = True
    LOGGER_LEVEL = logging.DEBUG
