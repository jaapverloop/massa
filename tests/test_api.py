# -*- coding: utf-8 -*-

from . import MassaTestCase


class ApiTestCase(MassaTestCase):
    def test_get_exertions(self):
        response = self.test_client.get('/api/exertions/')
        self.assert_status_code(response, 200)
        self.assert_is_json(response)
