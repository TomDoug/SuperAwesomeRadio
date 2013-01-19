from threading import Thread
import socket, time
import pickle, songClass
class MusicPlayer():
	
	songs = []
	artists = []
	def __init__(self):
		host = '127.0.0.1'
		port = 8888
	
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((host,port))
		self.sendMessage("getSongs")
		songString = self.getMessage()
		songList = pickle.loads(songString)
		#sendMessage('stop')
		for i in songList:
			print i.song
	
	def getMessage(self):
		string = ""
		d = self.s.recv(1024)
		while 1:
			string = string + d
			if len(d) < 1000:break
			d = self.s.recv(1024)
			
		return string
	def sendMessage(self, message):
		self.s.send(message)
	def play(self):
		self.sendMessage('0')
	def load(self, song):
		self.sendMessage("loadSong:" + song)
	def stop(self):
		self.sendMessage('1')
	def pause(self):
		self.sendMessage('2')
mp = MusicPlayer()
time.sleep(1)
mp.play()
time.sleep(1)
mp.stop()
time.sleep(1)
mp.pause()
time.sleep(1)
mp.load("dksfjdsakljf")
time.sleep(1)
mp.sendMessage('stop')
mp.s.close()

