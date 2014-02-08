# -*- coding: utf-8 -*-

import unittest
from massa import create_app


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('massa.config.Testing')
        self.test_client = app.test_client()

    def test_get_exertions(self):
        response = self.test_client.get('/api/exertions/')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.headers['Content-Type'], 'application/json')
        return response


if __name__ == '__main__':
    unittest.main()
