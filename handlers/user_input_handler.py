from abc import ABC
from service import user_service, user_and_sector_service
import tornado.web


class UserInputHandler(tornado.web.RequestHandler, ABC):
    def set_default_headers(self):
        # for CORS policy
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, PUT, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

    def options(self):
        pass

    def post(self):
        # post data
        data = tornado.escape.json_decode(self.request.body)
        # create UserService() and add user to DB
        user_data = user_service.UserService(data['name'], data['agreement'])
        user_id = user_data.addUserToDB()
        # create UserAndSectorService() and add it to DB
        user_and_sector_data = user_and_sector_service.UserAndSectorService(user_id, data['sector_id'])
        user_and_sector_data.addUserAndSectorToDB()
        # return the user id provided by the database in response
        self.write({"user_id": user_id})

    def put(self):
        # put data
        data = tornado.escape.json_decode(self.request.body)
        # create UserAndSectorService() and update DB with new data
        user_and_sector_data = user_and_sector_service.UserAndSectorService(data['user_id'], data['sector_id'])
        user_and_sector_data.updateSectorChoices()
