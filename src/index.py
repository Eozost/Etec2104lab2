import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("<a href='/static/roulette.html'>Visit the casino</a>")