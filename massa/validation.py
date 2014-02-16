# -*- coding: utf-8 -*-

from schematics.exceptions import ConversionError, ValidationError
from .errors import InvalidInputError


def validate(schema, data):
    try:
        schema.import_data(data)
        schema.validate()
    except (ConversionError, ValidationError) as e:
        raise InvalidInputError(details=e.messages)


def weight_validator(value):
    if abs(value.as_tuple().exponent) > 1:
        raise ValidationError('Only one decimal point is allowed.')

    return value
