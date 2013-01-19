import socket, sys, pickle
from threading import Thread
import os, songClass

class server(Thread):
	def run(self):
		self.running = True
		self.host = ''
		self.port = 8888

		self.songs = []
		for (dirpath, dirname, filenames) in os.walk('C:\\Users\\TomDoug\\Music'): 
		
			for i in filenames:
		
				if i.find('.mp3') != -1:
					path = dirpath + "\\" + i
					#makes a new instance of the song class for each song
					self.songs.append(songClass.song(path))	
		

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print 'socket created'
		
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		self.s.bind((self.host, self.port))

		print "Socket binded"

		self.s.listen(5)

		self.clsock, addr = self.s.accept()
		self.inputLoop()
			
		
	def inputLoop(self):
		while self.running:
			inMess = self.getMessage()
			print inMess
			if inMess == "getSongs":
				self.getSongs()
			if inMess == 'stop':
				self.running = False
				break
			if inMess == '0':
				print "playing"
			if inMess == '1':
				print "Stopping Song"
			if inMess == '2':
				print "pausing"
			if inMess.find("loadSong:") != -1:
				print "loading" + inMess[9:]
		
		self.clsock.close()
		self.s.close()

	def sendMessage(self, message):
		self.clsock.send(message)
	def getSongs(self):
		pick = pickle.dumps(self.songs)
		self.sendMessage(pick)
	def getMessage(self):
		d = ''
		string = ""
				
		string = self.clsock.recv(1024)
		if string == 'stop':
			self.running = False
			print "stopp"
		return string

t = server()
t.start()
