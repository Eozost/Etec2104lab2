import tornado.websocket
import tornado.ioloop
import tornado.web
import json

activeClients = []

class Handler(tornado.websocket.WebSocketHandler):
    async def open(self):
        activeClients.append(self)

    async def on_message(self, msg):
        data = json.loads(msg)
        for c in activeClients:
            await c.write_message(json.dumps(data))

    def on_close(self):
        activeClients.remove(self)

    def check_origin(self, *args):
        return True
def make_app():
    return tornado.web.Application([
        (r"/roulette", Handler),
    ])
if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()