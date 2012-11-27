# Copyright (c) Jukka Pietila 2012
# see LICENSE for details

import sys
import string
import socket
import msgparser

class IRCBot(object):
	def __init__(self):
		self.SERVER = ""
		self.CHANNELS = []
		self.BOTNICK = "SomeBot"
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.PORT = 6667
		
	def __init__(self, serv, chan, nick, port):
		self.SERVER = serv		#server goes here
		self.CHANNELS = []		#list of channels goes here
		self.CHANNELS.append(chan)
		self.BOTNICK = nick		#bot's nick goes here
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.readbuf = ""		#buffer for server messages
		self.PORT = port
		self._connect()
		
	def _connect(self):
		self.irc.connect((self.SERVER, self.PORT))
		self.irc.send("NICK " + self.BOTNICK + "\r\n")
		self.irc.send("USER " + self.BOTNICK + " " + self.BOTNICK + " " + self.BOTNICK + " :This bot is herpaderp.\r\n")
		self._joinchannel(self.CHANNELS[0])
	
	def _joinchannel(self, chan):
		self.irc.send("JOIN " + chan + "\r\n")
		self._sendmsg("EVEN IN DEATH I STILL SURF", chan)	#announce join
	
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
			self.irc.send("QUIT :Quitting... \r\n")
		
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
	