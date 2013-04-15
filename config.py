#Copyright (c) Jukka Pietila 2013
#see LICENSE for details

class Config(object):
	def __init__(self):
		self.SERVER = ""
		self.BOTNAME = ""
		self.PORT = 6667
		self.CHANNELS = []
		
	def __init__(self, serv, name, port, channels):
		self.SERVER = serv
		self.BOTNAME = name
		self.PORT = port
		self.CHANNELS = list(channels)