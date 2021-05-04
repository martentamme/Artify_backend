import json

from tornado.testing import AsyncHTTPTestCase

import handlers.main_handler


class TestSectorHandler(AsyncHTTPTestCase):
    def get_app(self):
        return handlers.main_handler.make_app()

    def test_get_request(self):
        response = self.fetch('/sectors')
        json_obj = json.loads(response.body)
        self.assertEqual(200, response.code)
        self.assertEqual(1, json_obj['0']['id'])
        self.assertEqual('Manufacturing', json_obj['0']['name'])
        self.assertEqual(None, json_obj['0']['root_sector_id'])
