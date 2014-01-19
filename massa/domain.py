# -*- coding: utf-8 -*-

from schematics.models import Model
from schematics.types import StringType, DateType, DecimalType
from schematics.exceptions import ConversionError, ValidationError
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


def validate(schema, data):
    try:
        schema.import_data(data)
        schema.validate()
    except (ConversionError, ValidationError) as e:
        raise InvalidInputError('Input data invalid', e.messages)


def is_weight(value):
    if abs(value.as_tuple().exponent) > 1:
        raise ValidationError('More than one decimal exponent not allowed')

    return value


class DomainError(Exception):
    def __init__(self, message, details=None):
        self.message = message
        self.details = details


class EntityNotFoundError(DomainError):
    """Raised when an entity does not exist."""


class InvalidInputError(DomainError):
    """Raised when input data is invalid."""


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


class InputMeasurement(Model):
    weight = DecimalType(required=True, validators=[is_weight])
    code = StringType(required=True, choices=[
        'BODYWEIGHT',
        'SQUAT',
        'BENCHPRESS',
        'DEADLIFT'
        ])
    note = StringType(required=False, max_length=140)
    date_measured = DateType(required=True)


class MeasurementService(object):
    def __init__(self, table):
        self._table = table

    def get(self, id):
        stmt = self._table.select(self._table.c.id == id)
        row = stmt.execute().fetchone()

        if not row:
            raise EntityNotFoundError('Measurement does not exist')

        return self.make_exposable(row)

    def find_all(self):
        stmt = self._table.select()
        rows = stmt.execute()

        items = []
        for row in rows:
            items.append(self.make_exposable(row))

        return items

    def create(self, **kwargs):
        schema = InputMeasurement()
        validate(schema, kwargs)

        stmt = self._table.insert()
        result = stmt.execute(**kwargs)
        return result.inserted_primary_key[0]

    def update(self, id, **kwargs):
        entity = self.get(id)

        schema = InputMeasurement()
        validate(schema, kwargs)

        stmt = self._table.update(self._table.c.id == id)
        stmt.execute(**kwargs)

    def delete(self, id):
        entity = self.get(id)

        stmt = self._table.delete(self._table.c.id == id)
        stmt.execute()

    def make_exposable(self, measurement):
        return {
            'id': measurement.id,
            'weight': float(measurement.weight),
            'code': measurement.code,
            'note': measurement.note,
            'date_measured': measurement.date_measured.isoformat(),
        }
