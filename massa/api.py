# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, g, request, url_for
from flask.views import MethodView
from .domain import EntityNotFoundError


def endpoint(f):
    def wrapper(*args, **kwargs):
        try:
            rv = f(*args, **kwargs)
        except EntityNotFoundError as e:
            rv = {'message': e.msg}, 404

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


class ApiView(MethodView):
    decorators = [endpoint]


class MeasurementList(ApiView):
    def get(self):
        service = g.sl('measurement_service')
        return {'items': service.find_all()}

    def post(self):
        service = g.sl('measurement_service')
        id = service.create(**payload())
        location = url_for('api.measurement_item', id=id, _external=True)
        return service.get(id), 201, {'Location': location}


class MeasurementItem(ApiView):
    def get(self, id):
        service = g.sl('measurement_service')
        return service.get(id)

    def put(self, id):
        service = g.sl('measurement_service')
        service.update(id, **payload())
        return service.get(id), 200

    def delete(self, id):
        service = g.sl('measurement_service')
        service.delete(id)
        return '', 204


bp = Blueprint('api', __name__)

bp.add_url_rule(
    '/measurements/',
    view_func=MeasurementList.as_view('measurement_list'),
    methods=['GET', 'POST']
)

bp.add_url_rule(
    '/measurements/<id>',
    view_func=MeasurementItem.as_view('measurement_item'),
    methods=['GET', 'PUT', 'DELETE']
)
