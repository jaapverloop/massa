# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, g
from flask.views import MethodView


class MeasurementList(MethodView):
    def get(self):
        service = g.sl('measurement_service')
        return jsonify(items=service.find_all())


class MeasurementItem(MethodView):
    def get(self, id):
        service = g.sl('measurement_service')
        return jsonify(service.find(id))


bp = Blueprint('api', __name__)

bp.add_url_rule(
    '/measurements/',
    view_func=MeasurementList.as_view('measurement_list'),
    methods=['GET']
)

bp.add_url_rule(
    '/measurements/<id>',
    view_func=MeasurementItem.as_view('measurement_item'),
    methods=['GET']
)
