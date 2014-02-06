# -*- coding: utf-8 -*-

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
