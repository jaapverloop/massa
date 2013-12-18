# -*- coding: utf-8 -*-

from knot import Container
from sqlalchemy import create_engine
from .domain import Db, MeasurementService


def build(config):
    c = Container(config)

    @c.factory(cache=True)
    def db(c):
        return Db(create_engine(
            c['SQLALCHEMY_DATABASE_URI'],
            echo=c['SQLALCHEMY_ECHO']
        ))

    @c.factory(cache=True)
    def measurement_service(c):
        return MeasurementService(c('db').measurement)

    return c
