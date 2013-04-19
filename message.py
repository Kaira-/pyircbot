#Copyright (c) Jukka Pietila 2013
#See LICENSE for details

class Message(object):
	"""
	Message defines a representation of message that can be sent to or
	received from an IRC server. The main components of a message are
	its "author" (aka who sent it), target, type and body.
	"""