import tornado.ioloop
import tornado.web
from handlers import sectors_handler


def make_app():
    return tornado.web.Application([
        (r"/sectors", sectors_handler.SectorsHandler),
    ])


if __name__ == "__main__":
    port = 8080
    app = tornado.web.Application([
        (r"/sectors", sectors_handler.SectorsHandler)
    ])
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
