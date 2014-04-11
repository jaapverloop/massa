# -*- coding: utf-8 -*-

import logging
from getenv import env


DEBUG = env('DEBUG', False)
TESTING = env('TESTING', False)
SECRET_KEY = env('SECRET_KEY', 'ValarMorghulis')
SQLALCHEMY_DATABASE_URI = env('SQLALCHEMY_DATABASE_URI', 'sqlite://')
SQLALCHEMY_ECHO = env('SQLALCHEMY_ECHO', False)
LOGGER_LEVEL = env('LOGGER_LEVEL', logging.INFO)
LOGGER_FILENAME = env('LOGGER_FILENAME', 'massa.log')
LOGGER_FORMAT = env('LOGGER_FORMAT', '%(asctime)s %(levelname)s: %(message)s')
LOGGER_MAX_BYTES = env('LOGGER_MAX_BYTES', 1024 * 1024)
LOGGER_BACKUP_COUNT = env('LOGGER_BACKUP_COUNT', 3)
