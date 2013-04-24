# Copyright (c) Jukka Pietila 2012
# see LICENSE for details

import sys
import string
import socket
import msgparser
import confmanager

class IRCBot(object):
	def __init__(self):
		self._CONFFILE = "config.conf"
		self._CONFMAN = confmanager.ConfManager(self._CONFFILE)
		self._config = self._CONFMAN.readConfig()
		self.SERVER = self._config.SERVER
		self.CHANNELS = self._config.CHANNELS
		self.BOTNICK = self._config.BOTNAME
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.PORT = self._config.PORT
		self.JOINMSG = self._config.JOINMSG

	def __init__(self, conffile):
		self._CONFFILE = conffile
		self._CONFMAN = confmanager.ConfManager(self._CONFFILE)
		self._config = self._CONFMAN.readConfig()
		self.SERVER = self._config.SERVER
		self.CHANNELS = self._config.CHANNELS
		self.BOTNICK = self._config.BOTNAME
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.PORT = self._config.PORT
		self.JOINMSG = self._config.JOINMSG
		self.QUITMSG = self._config.QUITMSG
		
	def _connect(self):
		self.irc.connect((self.SERVER, self.PORT))
		self.irc.send("NICK " + self.BOTNICK + "\r\n")
		self.irc.send("USER " + self.BOTNICK + " " + self.BOTNICK + " " + self.BOTNICK + " :This bot is herpaderp.\r\n")
		self._joinchannel(self.CHANNELS[0])
	
	def _joinchannel(self, chan):
		self.irc.send("JOIN " + chan + "\r\n")
		self._sendmsg(self.JOINMSG, chan)	#announce join
	
	def _ping(self, data):
		self.irc.send("PONG " + (data.split()[1]).strip(':') + "\r\n")
	
	def _quit(self, msg):
		msg_split = msg.split()[1:]
		qmsg = ""
		for w in msg_split:
			qmsg = qmsg + w + " "
		if qmsg != "":
			self.irc.send("QUIT :" + qmsg + "\r\n")
		else:
			self.irc.send("QUIT :" + self.QUITMSG + "... \r\n")
		
	def _sendmsg(self, msg, chan):
		self.irc.send("PRIVMSG " + chan + " :" + msg + "\r\n")
	
	def processForever(self):
		#this is the important main loop of the bot. PING PONG and so forth
		running = 1
		readbuf = []
		while 1:
			readbuf = self.irc.recv(2048)
			readbuf = readbuf.strip('\r\n')
			readbuf = readbuf.strip('\n\r')
			print readbuf
			if readbuf == "":
				continue
			try:
				#first, answer to PINGs
				if readbuf.find("PING") != -1 and readbuf.find("PRIVMSG") == -1:
					self._ping(readbuf)
					
				prefix, command, args = msgparser.Parser.parsemsg(readbuf)
				parser.nick = msgparser.Parser.parsenick(prefix)
				channel = args[0]
				msg = args[1]
				if msg.find(self.BOTNICK) != -1:
					smsg = nick + ", suck my salty chocolate balls"
					self._sendmsg(smsg, channel)
				if msg.find("!quit") != -1:
					self._quit(msg)
					running = 0
			except msgparser.IRCBadMessage:
				continue
			except:
				continue
				#even if all fails we carry on. Bad design, yay!
			if running == 0:
				break
	