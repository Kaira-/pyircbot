# Copyright (c) Jukka Pietila 2012
# see LICENSE for details

import sys
import socket
import string
import bot

#begin execution
if __name__ == "__main__":
	#check command line arguments
	if len(sys.argv) == 2:
		#conf-file name was given
		f = sys.argv[1]
		mybot = bot.IRCBot(f)
		mybot.processForever()
	else if len(sys.argv) == 1:
		f = "config.conf"
		mybot = bot.IRCBot(f)
		mybot.processForever()
	else:
		sys.exit("Usage: %s <config-file> " % sys.argv[0])
