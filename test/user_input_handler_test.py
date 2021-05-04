from tornado.testing import AsyncHTTPTestCase

import handlers.main_handler
from model.user import User


class TestSectorHandler(AsyncHTTPTestCase):
    def get_app(self):
        return handlers.main_handler.make_app()

    def test_get_request(self):
        response = self.fetch("/user_input", method="POST",
                              body='{"name": "test", "sector_id": [5, 12], "agreement": "accepted"}')
        self.assertEqual(200, response.code)
        self.assertEqual(User.user_id, response.body)

    def test_put_request(self):
        user_id = User.select(User.user_id).order_by(User.user_id.desc()).limit(1).get()
        response = self.fetch("/user_input", method="PUT", body='{"user_id": ' + str(
            user_id) + ', "name": "y", "sector_id": [5, 12], "agreement": "accepted"}')
        self.assertEqual(200, response.code)
        self.assertEqual(User.user_id, response.body)
