# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from knot import Container
from sqlalchemy import create_engine
from .storage import Db
from .exertion.model import ExertionService


def build(app):
    c = Container(app.config)

    @c.factory(cache=True)
    def db(c):
        return Db(create_engine(
            c['SQLALCHEMY_DATABASE_URI'],
            echo=c['SQLALCHEMY_ECHO']
        ))

    @c.factory(cache=True)
    def exertion_service(c):
        return ExertionService(c('db').exertion)

    @c.factory(cache=True)
    def logger(c):
        handler = RotatingFileHandler(
            c('LOGGER_FILENAME', '{}.log'.format(app.name)),
            maxBytes=c('LOGGER_MAX_BYTES', 1024*1024),
            backupCount=c('LOGGER_BACKUP_COUNT', 3)
        )

        handler.setFormatter(logging.Formatter(
            c('LOGGER_FORMAT', "%(asctime)s %(levelname)s: %(message)s")
        ))

        app.logger.setLevel(c('LOGGER_LEVEL', logging.INFO))
        app.logger.addHandler(handler)

        return app.logger

    return c
