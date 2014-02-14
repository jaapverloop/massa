# -*- coding: utf-8 -*-

from flask import Flask, g
from .container import build
from .web import bp as web
from .api import bp as api
from .middleware import HTTPMethodOverrideMiddleware


def create_app(config=None):
    app = Flask('massa')
    app.config.from_object(config or 'massa.config.Production')
    app.config.from_envvar('MASSA_CONFIG', silent=True)

    sl = build(app)

    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix='/api')

    @app.before_request
    def globals():
        g.sl = sl

    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
    return app
