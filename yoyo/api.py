# -*- coding: utf-8 -*-

from flask import Blueprint
from flask.views import MethodView


class MeasurementList(MethodView):
    def get(self):
        return 'GET: measurement list'

class MeasurementItem(MethodView):
    def get(self, id):
        return 'GET: measurement item with ID %s' % id


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
