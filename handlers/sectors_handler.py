from abc import ABC

import tornado.web
from service import sectors


class SectorsHandler(tornado.web.RequestHandler, ABC):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def get(self):
        s = sectors.Sectors()
        response = s.get_sectors()
        print(response)
        self.write(response)
