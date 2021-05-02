from abc import ABC

import tornado.web
from service import sector_service


class SectorsHandler(tornado.web.RequestHandler, ABC):

    def set_default_headers(self):
        # for CORS policy
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def get(self):
        s = sector_service.SectorService()
        response = s.get_sectors()
        self.write(response)
