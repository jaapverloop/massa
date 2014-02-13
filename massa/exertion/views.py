# -*- coding: utf-8 -*-

from flask import g, url_for
from ..views import JSONEndpoint, payload


def register(bp):
    bp.add_url_rule(
        '/exertions/',
        view_func=ExertionList.as_view('exertion_list'),
    )

    bp.add_url_rule(
        '/exertions/<id>',
        view_func=ExertionItem.as_view('exertion_item'),
    )


class ExertionList(JSONEndpoint):
    def get(self):
        service = g.sl('exertion_service')
        return {'items': service.find_all()}

    def post(self):
        service = g.sl('exertion_service')
        id = service.create(**payload())
        location = url_for('api.exertion_item', id=id, _external=True)
        return service.get(id), 201, {'Location': location}


class ExertionItem(JSONEndpoint):
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
