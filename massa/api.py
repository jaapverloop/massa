# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, g, request, url_for
from flask.views import MethodView
from .errors import EntityNotFoundError, InvalidInputError


def endpoint(f):
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


class ApiView(MethodView):
    decorators = [endpoint]


class ExertionList(ApiView):
    def get(self):
        service = g.sl('exertion_service')
        return {'items': service.find_all()}

    def post(self):
        service = g.sl('exertion_service')
        id = service.create(**payload())
        location = url_for('api.exertion_item', id=id, _external=True)
        return service.get(id), 201, {'Location': location}


class ExertionItem(ApiView):
    def get(self, id):
        service = g.sl('exertion_service')
        return service.get(id)

    def put(self, id):
        service = g.sl('exertion_service')
        service.update(id, **payload())
        return service.get(id), 200

    def delete(self, id):
        service = g.sl('exertion_service')
        service.delete(id)
        return '', 204


bp = Blueprint('api', __name__)
bp.app_errorhandler(EntityNotFoundError)(entity_not_found_handler)
bp.app_errorhandler(InvalidInputError)(invalid_input_handler)

bp.add_url_rule(
    '/exertions/',
    view_func=ExertionList.as_view('exertion_list'),
)

bp.add_url_rule(
    '/exertions/<id>',
    view_func=ExertionItem.as_view('exertion_item'),
)
