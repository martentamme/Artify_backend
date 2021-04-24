from abc import ABC

import tornado.web
import sectors


class SectorsHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        s = sectors.Sectors()
        response = s.get_sectors()
        print(response)
        self.write(response)