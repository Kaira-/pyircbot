# Copyright (c) Jukka Pietila 2012
# see LICENSE for details

import sys
import socket
import string
import bot

#begin execution
if __name__ == "__main__":
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
		mybot = bot.IRCBot(server, channel, nick, port)
		mybot.processForever()
	else:
		sys.exit("Usage: %s <server> <channel> <nick>  [ <port>] " % sys.argv[0])
