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
		
	def __init__(self, serv, chan, nick):
		self.SERVER = serv		#server goes here
		self.CHANNELS = []		#list of channels goes here
		self.CHANNELS.append(serv)
		self.BOTNICK = nick		#bot's nick goes here
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.readbuf = ""		#buffer for server messages
		self.PORT = 6667
		
	def __init__(self, serv, chan, nick, port):
		self.SERVER = serv		#server goes here
		self.CHANNELS = []		#list of channels goes here
		self.CHANNELS.append(serv)
		self.BOTNICK = nick		#bot's nick goes here
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.readbuf = ""		#buffer for server messages
		self.PORT = port
	
	def _joinchannel(self, chan):
		self.irc.send("JOIN " + chan + "\r\n")
		self.irc.send("PRIVMSG " + chan + " :I LIVE ONCE AGAIN\r\n")	#announce join
	
	def _ping(self, data):
		self.irc.send("PONG " + data.split()[1] + "\r\n")
	
	def _sendmsg(self, msg, chan):
		self.irc.send("PRIVMSG " + chan + " :" + msg + '\r\n')
	
	def processForever(self):
		#this is the important main loop of the bot. PING PONG and so forth
		while 1:
			readbuf = self.irc.recv(1024)
			readbuf = self.readbuf.strip('\r\n')
			prefix, command, args = Parser.parse(readbuf)
			nick = Parser.parsenick(prefix)
			channel = args[0]
			msg = args[1]
			if msg.find(BOTNICK) != -1:
				smsg = nick + ", suck my salty chocolate balls"
				self._sendmsg(smsg, chan)
			if msg.find("PING") != -1:
				self._ping(msg)
				
def ping(data):					#respond to server PINGs
	irc.send("PONG " + data.split()[1] + "\r\n")
	
def sendmsg(chan, msg):		#send message to channel
	irc.send("PRIVMSG " + chan + " :" + msg + "\r\n")

def joinchan(chan):			#join channel
	irc.send("JOIN " + chan + "\r\n")
	irc.send("PRIVMSG " + chan + " :I LIVE ONCE AGAIN\r\n")

class Parser(object):
	@classmethod
	def parsemsg(cls, line):
		"""Breaks a message from IRC server into prefix, command and args
		"""
		prefix = ""
		trailing = []
		if not line:
			raise IRCBadMessage("Empty line.")
		if line[0] == ':':
			prefix, line = line[1:].split(' ', 1)
		if line.find(' :') != -1:
			line, trailing = line.split(' :', 1)
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
		split_list = s.split('!')
		return split_list[0]

class IRCBadMessage(Exception):
	pass
		
		
	
#begin execution

#check command line arguments
#if len(sys.argv) < 2:
