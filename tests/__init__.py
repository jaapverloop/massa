# -*- coding: utf-8 -*-

import unittest
from flask import g
from massa import create_app


def create_testable_app():
    return create_app('massa.config.Testing')


class MassaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_testable_app()
        self.test_client = self.app.test_client()

        with self.app.test_request_context():
            self.app.preprocess_request()
            db = g.sl('db')
            db.create_tables()

    def tearDown(self):
        with self.app.test_request_context():
            self.app.preprocess_request()
            db = g.sl('db')
            db.drop_tables()

    def assert_status_code(self, response, expected):
        return self.assertEquals(expected, response.status_code)

    def assert_content_type(self, response, expected):
        return self.assertEquals(expected, response.headers['Content-Type'])

    def assert_is_json(self, response):
        return self.assert_content_type(response, 'application/json')
