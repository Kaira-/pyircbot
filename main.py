# Copyright (c) Jukka Pietila 2012
# see LICENSE for details

import sys
import socket
import string

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
		print "PONGING with " + (data.split()[1]).srtip(':')
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
					
				prefix, command, args = Parser.parsemsg(readbuf)
				nick = Parser.parsenick(prefix)
				channel = args[0]
				msg = args[1]
				if msg.find(self.BOTNICK) != -1:
					smsg = nick + ", suck my salty chocolate balls"
					self._sendmsg(smsg, channel)
				if msg.find("!quit") != -1:
					self._quit(msg)
					running = 0
			except IRCBadMessage:
				continue
			except:
				continue
				#even if all fails we carry on. Bad design, yay!
			if running == 0:
				break
				
class Parser(object):
	@classmethod
	def parsemsg(cls, line):
		"""Breaks a message from IRC server into prefix, command and args
		"""
		prefix = ""
		trailing = []
		if not line:
			raise IRCBadMessage("Empty line.")
		if line[0] == ":":
			prefix, line = line[1:].split(" ", 1)
		if line.find(" :") != -1:
			line, trailing = line.split(" :", 1)
			args = line.split()
			args.append(trailing)
		else:
			args = line.split()
		command = args.pop(0)
		return prefix, command, args
		
	@classmethod
	def parsenick(cls, s):
		"""Parses the nick from string, if possible
		"""
		split_list = s.split("!")
		return split_list[0]

class IRCBadMessage(Exception):
	pass
		
		
	
#begin execution

#check command line arguments
if len(sys.argv) == 4 or len(sys.argv) == 5:
	#handle params
	server = sys.argv[1]
	channel = sys.argv[2]
	if channel[0] != '#':
		channel = '#' + channel
	nick = sys.argv[3]
	port = 6667
	if len(sys.argv) == 5:
		port = sys.argv[4]
		port = int(port)
	
	print "Server: " + server + " Channel: " + channel + " Nick: " + nick + " Port: " + str(port)
	mybot = IRCBot(server, channel, nick, port)
	mybot.processForever()
else:
	sys.exit("Usage: %s <server> <channel> <nick>  [ <port>] " % sys.argv[0])
