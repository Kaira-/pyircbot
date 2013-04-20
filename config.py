#Copyright (c) Jukka Pietila 2013
#see LICENSE for details

class Config(object):
	def __init__(self):
		self.SERVER = ""
		self.BOTNAME = ""
		self.PORT = 6667
		self.CHANNELS = list()
		self.JOINMSG = "I am here."
		self.QUITMSG = "I'm outta here."

	def __init__(self, serv, name, port, channels, joinmsg, quitmsg):
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
		#check channels that all have '#' as first char, and prepend the char to all those channels
		self.CHANNELS = channels.split(",")
		newchans = list()
		for channel in CHANNELS:
			if channel[0] != '#':
				newchans.append('#' + channel)
		self.CHANNELS = list(newchans)
		self.QUITMSG = quitmsg

	def addChannel(self, newchan):
		"""
		Adds a new channel to the list of channels the bot has
		"""
		if newchan[0] != '#':
			chan = '#' + newchan
			self.CHANNELS.append(newchan)
		else:
			self.CHANNELS.append(newchan)
