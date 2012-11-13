import sys
import socket
import string

#these are only temporarily here until class definition is complete
SERVER = ""
CHANNEL = ""
BOTNICK = ""
readbuf = ""
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
		
	def processForever(self):
		#this is the important main loop of the bot. PING PONG and so forth
		while 1:
			self.readbuf = self.irc.recv(1024)
			self.readbuf = self.readbuf.strip('\r\n')
			

def ping(data):					#respond to server PINGs
	irc.send("PONG " + data.split()[1] + "\r\n")
	
def sendmsg(chan, msg):		#send message to channel
	irc.send("PRIVMSG " + chan + " :" + msg + "\r\n")

def joinchan(chan):			#join channel
	irc.send("JOIN " + chan + "\r\n")
	irc.send("PRIVMSG " + chan + " I LIVE ONCE AGAIN\r\n")

#begin execution

if len(sys.argv) < 2:
	

irc.connect((SERVER, 6667))	#connect to serv using port 6667
irc.send("NICK " + BOTNICK + "\r\n")	#assign nick to the bot
irc.send("USER " + BOTNICK + " " + BOTNICK + " " + BOTNICK + " :This bot is a result of a tutorial covered on http://shellium.org/wiki.\r\n") # user authentication

joinchan(CHANNEL)	#join the channel

while 1:	#looping
	readbuf = irc.recv(2048)	#receive data from server
	readbuf = readbuf.strip('\r\n')	#remove unnecessary linebreaks
	print readbuf					#print from server
	
	if readbuf.find("PING :") != -1:			#if server pings, we pong
		ping(readbuf)