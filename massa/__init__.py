# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.appconfig import AppConfig


def create_app(configfile=None):
    app = Flask('massa')
    AppConfig(app, configfile)

    @app.route('/')
    def index():
        return render_template('index.html')

    from .api import bp
    app.register_blueprint(bp, url_prefix='/api')

    return app
