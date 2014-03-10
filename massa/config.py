# -*- coding: utf-8 -*-

import os


allowed_settings = [
    'DEBUG',
    'TESTING',
    'SECRET_KEY',
    'SQLALCHEMY_DATABASE_URI',
    'SQLALCHEMY_ECHO',
    'LOGGER_LEVEL',
    'LOGGER_FORMAT',
    'LOGGER_FILENAME',
    'LOGGER_MAX_BYTES',
    'LOGGER_BACKUP_COUNT',
]


class FromEnvConfig(object):
    def __init__(self):
        for key in allowed_settings:
            value = os.getenv(key)
            if value is not None:
                setattr(self, key, value)
