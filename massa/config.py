# -*- coding: utf-8 -*-

class Production(object):
    DEBUG = False
    SECRET_KEY = '##CHANGEME##'
    SQLALCHEMY_DATABASE_URI = 'postgresql://massa:secret@localhost/massa'
    SQLALCHEMY_ECHO = False


class Development(Production):
    DEBUG = True
