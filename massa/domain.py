# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    Date,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
)


def define_tables(metadata):
    Table('measurement', metadata,
        Column('id', Integer, primary_key=True),
        Column('weight', Numeric(4, 1), nullable=False),
        Column('code', String(25), nullable=False),
        Column('note', String(140), nullable=True),
        Column('date_measured', Date(), nullable=False),
    )


class Db(object):
    def __init__(self, engine):
        self._meta = MetaData(engine)
        define_tables(self._meta)

    def make_tables(self):
        self._meta.create_all()

    def drop_tables(self):
        self._meta.drop_all()

    @property
    def measurement(self):
        return self._meta.tables['measurement']


class MeasurementService(object):
    def __init__(self, table):
        self._table = table

    def create(self, **kwargs):
        i = self._table.insert()
        i.execute(**kwargs)
