# -*- coding: utf-8 -*-

from flask import Flask, render_template, g
from flask.ext.appconfig import AppConfig
from .container import build
from .web import bp as web
from .api import bp as api


def create_app(configfile=None):
    app = Flask('massa')
    AppConfig(app, configfile)

    sl = build(app.config)

    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix='/api')

    @app.before_request
    def globals():
        g.sl = sl

    return app
