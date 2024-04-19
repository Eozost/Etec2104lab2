import tornado.websocket 
import json


activeClients=[]

class Handler(tornado.websocket.WebSocketHandler):
    async def open(self):
        for c in activeClients:
          await c.write_message(json.dumps({"message": "Someone's here to spin"}))
    
        activeClients.append(self)


    async def on_message(self,msg):
        print("MESSAGE",msg)
        for c in activeClients:
            await c.write_message(msg)

    def on_close(self):
        print("CLOSED")
        for i in range(len(activeClients)):
            if activeClients[i] == self:
                del activeClients[i]
                break

        for c in activeClients:
            c.write_message("Someone stopped spining")


    def check_origin(self,*args):
        print(args)
        return True  #welcome, Friend!
