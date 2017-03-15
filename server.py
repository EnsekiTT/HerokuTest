import tornado.ioloop
import tornado.web

from tornado.options import define
define("port", default=5000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
