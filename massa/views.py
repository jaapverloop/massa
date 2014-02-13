# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask.views import MethodView


def jsonify_return_value(f):
    def wrapper(*args, **kwargs):
        rv = f(*args, **kwargs)

        msg = [rv, 200, {}]
        if isinstance(rv, tuple):
            for index, value in enumerate(rv):
                msg[index] = value

        body, code, headers = msg

        response = jsonify(body)
        for key, value in headers.iteritems():
            response.headers[key] = value

        return response, code

    return wrapper


def payload():
    return request.get_json() or request.form.to_dict()


def entity_not_found_handler(e):
    return jsonify({'message': e.message}), 404


def invalid_input_handler(e):
    return jsonify({'message': e.message, 'details': e.details}), 400


class JSONEndpoint(MethodView):
    decorators = [jsonify_return_value]
