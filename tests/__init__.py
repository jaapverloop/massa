# -*- coding: utf-8 -*-

import unittest
from massa import create_app


class MassaTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app('massa.config.Testing')
        self.test_client = app.test_client()

    def assert_status_code(self, response, expected):
        return self.assertEquals(expected, response.status_code)

    def assert_content_type(self, response, expected):
        return self.assertEquals(expected, response.headers['Content-Type'])

    def assert_is_json(self, response):
        return self.assert_content_type(response, 'application/json')
