import tornado.ioloop
import tornado.web
import tornado.websocket
from servo_controller import ServoController

cl = []
sc = ServoController()


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        if self not in cl:
            cl.append(self)

    def on_message(self, message):
        if message not in ['power_on', 'power_off']:
            return

        if message == 'power_on':
            self.__power_on()

        if message == 'power_off':
            self.__power_off()

        for client in cl:
            client.write_message(message)

    def on_close(self):
        if self in cl:
            cl.remove(self)

    def __power_on(self):
        sc.move(45)

    def __power_off(self):
        sc.move(-45)

application = tornado.web.Application([
    (r"/light", WebSocketHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()
