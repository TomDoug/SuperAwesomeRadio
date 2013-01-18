import socket

host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while 1:
	mess = raw_input("Message: ")
	s.send(mess)

	if mess == 'stop':break

s.close()
