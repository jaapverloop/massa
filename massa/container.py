# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from knot import Container
from sqlalchemy import create_engine
from .domain import Db, MeasurementService


def build(app):
    c = Container(app.config)

    @c.factory(cache=True)
    def db(c):
        return Db(create_engine(
            c['SQLALCHEMY_DATABASE_URI'],
            echo=c['SQLALCHEMY_ECHO']
        ))

    @c.factory(cache=True)
    def measurement_service(c):
        return MeasurementService(c('db').measurement)

    @c.factory(cache=True)
    def logger(c):
        handler = RotatingFileHandler(
            c['LOGGER_FILENAME'],
            maxBytes=c('LOGGER_MAX_BYTES', 1024*1024),
            backupCount=c('LOGGER_BACKUP_COUNT', 3)
        )

        handler.setLevel(c('LOGGER_LEVEL', logging.INFO))
        handler.setFormatter(logging.Formatter(
            c('LOGGER_FORMAT', "%(asctime)s %(levelname)s: %(message)s")
        ))

        app.logger.addHandler(handler)

        return app.logger

    return c
