# Copyright (c) Jukka Pietila 2012
# see LICENSE for details

import string
import sys
			
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