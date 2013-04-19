#copyright (c) Jukka Pietila 2013
#see LICENSE for details

import io
import sys
import string
import config

class ConfReader(object):
	def __init__(self):
		self._CONFNAME = "config.conf"

	def __init__(self, confname):
		self._CONFNAME = confname
	
	def readConfig(self):
		name = self._findValue("NAME")
		server = self._findValue("SERVER")
		channels = self._findValue("CHANNELS")
		port = self._findValue("PORT")
		joinmsg = self._findValue("JOINMSG")
		config = config.Config(server, name, port, channels, joinmsg)

	def _findValue(self, value):
		"""
		Attempts to find the seeked value from self._CONFNAME.
		If the value can not be found, it returns None, otherwise
		it returns a string representation of the value
		"""
		try:
			with open(self._CONFNAME) as f:
				for line in f.readlines():
					#strip trailing and leading whitespaces
					str = line.lstrip()
					#check if the first non-whitespace character in line is comment-character '#'
					if str[0] == '#':
						continue
					if str.startswith(value):
						val = str.split("=")[1]
						return val
			return None
		except IOError as e:
			print "I/O Error ({0}): {1}".format(e.errno, e.strerror)
			return None