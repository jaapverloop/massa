# -*- coding: utf-8 -*-

import unittest
from flask import g
from massa import create_app


def create_testable_app():
    return create_app('massa.config.Testing')


def create_db_tables(app):
    with app.test_request_context():
        app.preprocess_request()
        db = g.sl('db')
        db.create_tables()


def drop_db_tables(app):
    with app.test_request_context():
        app.preprocess_request()
        db = g.sl('db')
        db.drop_tables()


def db_context(f):
    def wrapper(test_case):
        app = test_case.app
        create_db_tables(app)
        f(test_case)
        drop_db_tables(app)

    return wrapper


class MassaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_testable_app()
        self.test_client = self.app.test_client()

    def assert_status_code(self, response, expected):
        return self.assertEquals(expected, response.status_code)

    def assert_content_type(self, response, expected):
        return self.assertEquals(expected, response.headers['Content-Type'])

    def assert_is_json(self, response):
        return self.assert_content_type(response, 'application/json')
