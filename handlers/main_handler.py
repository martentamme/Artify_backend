import tornado.ioloop
import tornado.web
from handlers import sectors_handler, user_input_handler


def make_app():
    return tornado.web.Application([
        (r"/sectors", sectors_handler.SectorsHandler),
        (r"/user_input", user_input_handler.UserInputHandler)
    ])


if __name__ == "__main__":
    port = 8080
    app = make_app()
    app.listen(port)
    print("port " + str(port) + " is listening!")
    tornado.ioloop.IOLoop.current().start()
