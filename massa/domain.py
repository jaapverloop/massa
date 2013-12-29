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

    def find(self, id):
        stmt = self._table.select(self._table.c.id == id)
        row = stmt.execute().fetchone()
        return self.make_exposable(row)

    def find_all(self):
        stmt = self._table.select()
        rows = stmt.execute()

        items = []
        for row in rows:
            items.append(self.make_exposable(row))

        return items

    def create(self, **kwargs):
        stmt = self._table.insert()
        result = stmt.execute(**kwargs)
        return result.inserted_primary_key[0]

    def update(self, id, **kwargs):
        stmt = self._table.update(self._table.c.id == id)
        stmt.execute(**kwargs)

    def delete(self, id):
        stmt = self._table.delete(self._table.c.id == id)
        stmt.execute()

    def make_exposable(self, measurement):
        return {
            'id': measurement.id,
            'weight': float(measurement.weight),
            'code': measurement.code,
        }
