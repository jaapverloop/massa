# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
)


def define_tables(metadata):
    Table('exertion', metadata,
        Column('id', Integer, primary_key=True),
        Column('weight', Numeric(4, 1), nullable=False),
        Column('exercise', String(25), nullable=False),
        Column('sets', Integer(3), nullable=False, default=1),
        Column('reps', Integer(3), nullable=False, default=1),
        Column('note', String(140)),
        Column('created_at', DateTime(), nullable=False, default=datetime.utcnow),
    )


class Db(object):
    def __init__(self, engine):
        self._meta = MetaData(engine)
        define_tables(self._meta)

    @property
    def exertion(self):
        return self._meta.tables['exertion']
