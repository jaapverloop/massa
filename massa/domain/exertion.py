# -*- coding: utf-8 -*-

from schematics.models import Model
from schematics.types import StringType, DecimalType, IntType
from . import EntityNotFoundError, validate, weight_validator


class InputExertion(Model):
    weight = DecimalType(
        required=True,
        min_value=1,
        max_value=500,
        validators=[weight_validator])
    exercise = StringType(required=True, choices=[
        'SQUAT',
        'BENCHPRESS',
        'DEADLIFT'
        ])
    sets = IntType(min_value=1, max_value=100)
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
            'sets': exertion.sets,
            'reps': exertion.reps,
            'note': exertion.note,
            'created_at': exertion.created_at.isoformat(),
        }
