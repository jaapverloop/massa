# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, g, request, url_for
from flask.views import MethodView
from .domain import EntityNotFoundError


def return_or_catch(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except EntityNotFoundError as e:
            return jsonify(status_code=404, message=e.msg), 404

    return wrapper


class MeasurementList(MethodView):
    def get(self):
        service = g.sl('measurement_service')
        return jsonify(items=service.find_all())

    def post(self):
        service = g.sl('measurement_service')
        id = service.create(**request.form.to_dict())
        location = url_for('api.measurement_item', id=id, _external=True)
        response = jsonify(status_code=201, location=location)
        response.headers['Location'] = location
        return response, 201


class MeasurementItem(MethodView):
    @return_or_catch
    def get(self, id):
        service = g.sl('measurement_service')
        return jsonify(service.find(id))

    @return_or_catch
    def put(self, id):
        service = g.sl('measurement_service')
        service.update(id, **request.form.to_dict())
        return jsonify(status_code=204), 204

    @return_or_catch
    def delete(self, id):
        service = g.sl('measurement_service')
        service.delete(id)
        return jsonify(status_code=204), 204


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
