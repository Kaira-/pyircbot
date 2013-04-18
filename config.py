#Copyright (c) Jukka Pietila 2013
#see LICENSE for details

class Config(object):
	def __init__(self):
		self.SERVER = ""
		self.BOTNAME = ""
		self.PORT = 6667
		self.CHANNELS = []
		self.JOINMSG = "I am here."
	def __init__(self, serv, name, port, channels, joinmsg):
		"""
		Constructs a new Config-object with given parameters.
		@serv - Servername to connect to
		@name - The bot's name
		@port - Port to utilize during establishing connection
		@channels - A string representation of channels where the bot
		will join, separated by ','
		@joinmsg - A message to be sent when the bot joins the channel
		"""
		self.SERVER = serv
		self.BOTNAME = name
		self.PORT = port
		self.JOINMSG = joinmsg
		self.CHANNELS = channels.split(",")
