# -*- coding: utf-8 -*-

from . import MassaTestCase, db_context


class ApiTestCase(MassaTestCase):
    @db_context
    def test_get_exertions(self):
        response = self.test_client.get('/api/exertions/')
        self.assert_status_code(response, 200)
        self.assert_is_json(response)
