# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from knot import Container, service
from sqlalchemy import create_engine
from .storage import Db
from .exertion.model import ExertionService


def build(app):
    c = Container(app.config)

    @service(c)
    def db(c):
        return Db(create_engine(
            c['SQLALCHEMY_DATABASE_URI'],
            echo=c['SQLALCHEMY_ECHO']
        ))

    @service(c)
    def exertion_service(c):
        return ExertionService(c('db').exertion)

    @service(c)
    def logger(c):
        handler = RotatingFileHandler(
            c['LOGGER_FILENAME'],
            maxBytes=c['LOGGER_MAX_BYTES'],
            backupCount=c['LOGGER_BACKUP_COUNT']
        )

        handler.setFormatter(logging.Formatter(c['LOGGER_FORMAT']))
        app.logger.setLevel(c['LOGGER_LEVEL'])
        app.logger.addHandler(handler)

        return app.logger

    return c
