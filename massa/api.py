# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, g, request, Response, url_for
from flask.views import MethodView


class MeasurementList(MethodView):
    def get(self):
        service = g.sl('measurement_service')
        return jsonify(items=service.find_all())

    def post(self):
        service = g.sl('measurement_service')
        id = service.create(**request.form.to_dict())
        location = url_for('api.measurement_item', id=id)
        response = Response(location, status=201, mimetype='text/plain')
        response.headers['Location'] = location
        return response


class MeasurementItem(MethodView):
    def get(self, id):
        service = g.sl('measurement_service')
        return jsonify(service.find(id))

    def put(self, id):
        service = g.sl('measurement_service')
        service.update(id, **request.form.to_dict())
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
    methods=['GET', 'PUT']
)
