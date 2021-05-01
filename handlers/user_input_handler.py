from abc import ABC
from service import user_input
import tornado.web


class UserInputHandler(tornado.web.RequestHandler, ABC):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

    def options(self):
        pass

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        # user teha
        user_id = user_input.UserData(data['name'], data['agreement'])

        # user/sector teha
        # tagasta user id
        self.write("shit works!")