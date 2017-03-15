import os

import tornado.web
import tornado.wsgi


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello.")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application([
    ("/", HelloHandler),
], **settings)
