# -*- coding: utf-8 -*-

import os
import logging


defaults = {
    'DEBUG': False,
    'TESTING': False,
    'SECRET_KEY': 'ValarMorghulis',
    'SQLALCHEMY_DATABASE_URI': 'sqlite://',
    'SQLALCHEMY_ECHO': False,
    'LOGGER_LEVEL': logging.INFO,
    'LOGGER_FILENAME': 'massa.log',
    'LOGGER_FORMAT': '%(asctime)s %(levelname)s: %(message)s',
    'LOGGER_MAX_BYTES': 1024 * 1024,
    'LOGGER_BACKUP_COUNT': 3,
}


def getenv(key, default):
    value = os.getenv(key, default)

    if isinstance(default, int):
        return int(value)

    if isinstance(default, bool):
        return bool(value)

    return value


class Config(object):
    def __init__(self, settings):
        self.__dict__.update(**settings)


environment = Config({k: getenv(k, v) for k, v in defaults.iteritems()})
