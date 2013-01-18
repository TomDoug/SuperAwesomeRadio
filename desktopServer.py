import socket, sys
from threading import Thread

class server(Thread):
	def run(self):
		self.host = '127.0.0.1'
		self.port = 8888

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print 'socket created'
		
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		s.bind((self.host, self.port))

		print "Socket binded"

		s.listen(5)

		clsock, addr = s.accept()
		string = ""
		self.running = True
		while self.running:
			d = ''
			string = ""
			d = clsock.recv(1024)
			while 1:
			
				string = string + d
				if len(d) < 1000:break
				d = clsock.recv(1024)
				print d
			if string == '':continue
			print string
			if string == 'stop':
				self.running = False
		clsock.close()
		s.close()
t = server()
t.start()
