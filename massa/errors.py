# -*- coding: utf-8 -*-

from flask import jsonify


def register_error_handlers(app):
    app.register_error_handler(EntityNotFoundError, entity_not_found_handler)
    app.register_error_handler(InvalidInputError, invalid_input_handler)


def entity_not_found_handler(e):
    return jsonify(e.as_dict()), 404


def invalid_input_handler(e):
    return jsonify(e.as_dict()), 400


class DomainError(Exception):
    def __init__(self, message=None, details=None):
        if message: self.message = message
        if details: self.details = details

    def as_dict(self):
        data = {}
        if self.message: data['message'] = self.message
        if self.details: data['details'] = self.details
        return data


class EntityNotFoundError(DomainError):
    """Raised when an entity does not exist."""
    message = 'Entity does not exist.'


class InvalidInputError(DomainError):
    """Raised when input data is invalid."""
    message = 'Input data is invalid.'
