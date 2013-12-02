# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.appconfig import AppConfig


def create_app(configfile=None):
    app = Flask('yoyo')
    AppConfig(app, configfile)

    @app.route('/')
    def index():
        return 'YoYo'

    return app
