#copyright (c) Jukka Pietila 2013
#see LICENSE for details

import io
import sys
import string
import config

class ConfReader(object):
	def __init__(self):
		self._CONFNAME = "config.conf"