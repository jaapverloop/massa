# -*- coding: utf-8 -*-

from datetime import datetime
from schematics.models import Model
from schematics.types import StringType, DateType, DecimalType, IntType
from schematics.exceptions import ConversionError, ValidationError
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
        Column('reps', Integer(3), nullable=False, default=1),
        Column('note', String(140), nullable=True),
        Column('created_at', DateTime(), nullable=False, default=datetime.utcnow),
    )


def validate(schema, data):
    try:
        schema.import_data(data)
        schema.validate()
    except (ConversionError, ValidationError) as e:
        raise InvalidInputError(details=e.messages)


def is_weight(value):
    if abs(value.as_tuple().exponent) > 1:
        raise ValidationError('More than one decimal exponent not allowed')

    return value


class DomainError(Exception):
    def __init__(self, message=None, details=None):
        if message: self.message = message
        if details: self.details = details


class EntityNotFoundError(DomainError):
    """Raised when an entity does not exist."""
    message = 'Entity does not exist.'


class InvalidInputError(DomainError):
    """Raised when input data is invalid."""
    message = 'Input data is invalid.'


class Db(object):
    def __init__(self, engine):
        self._meta = MetaData(engine)
        define_tables(self._meta)

    def make_tables(self):
        self._meta.create_all()

    def drop_tables(self):
        self._meta.drop_all()

    @property
    def exertion(self):
        return self._meta.tables['exertion']


class InputExertion(Model):
    weight = DecimalType(required=True, validators=[is_weight])
    exercise = StringType(required=True, choices=[
        'SQUAT',
        'BENCHPRESS',
        'DEADLIFT'
        ])
    reps = IntType(min_value=1, max_value=100)
    note = StringType(max_length=140)


class ExertionService(object):
    def __init__(self, table):
        self._table = table

    def get(self, id):
        stmt = self._table.select(self._table.c.id == id)
        row = stmt.execute().fetchone()

        if not row:
            raise EntityNotFoundError()

        return self.make_exposable(row)

    def find_all(self):
        stmt = self._table.select()
        rows = stmt.execute()

        items = []
        for row in rows:
            items.append(self.make_exposable(row))

        return items

    def create(self, **kwargs):
        schema = InputExertion()
        validate(schema, kwargs)

        stmt = self._table.insert()
        result = stmt.execute(**kwargs)
        return result.inserted_primary_key[0]

    def update(self, id, **kwargs):
        entity = self.get(id)

        schema = InputExertion()
        validate(schema, kwargs)

        stmt = self._table.update(self._table.c.id == id)
        stmt.execute(**kwargs)

    def delete(self, id):
        entity = self.get(id)

        stmt = self._table.delete(self._table.c.id == id)
        stmt.execute()

    def make_exposable(self, exertion):
        return {
            'id': exertion.id,
            'weight': exertion.weight,
            'exercise': exertion.exercise,
            'reps': exertion.reps,
            'note': exertion.note,
            'created_at': exertion.created_at.isoformat(),
        }
