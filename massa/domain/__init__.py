# -*- coding: utf-8 -*-

from schematics.exceptions import ConversionError, ValidationError


def validate(schema, data):
    try:
        schema.import_data(data)
        schema.validate()
    except (ConversionError, ValidationError) as e:
        raise InvalidInputError(details=e.messages)


def weight_validator(value):
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
