#Copyright (c) Jukka Pietilä 2013
#See LICENSE for details

import config
import confwriter
import confreader

class ConfManager(object):
	def __init__(self):
		self._confreader = confreader.ConfReader()
		self._config = self._confreader.readConfig()
		self._confwriter = confwriter.ConfWriter()
		
	def readConfig():
		self._config = self._confreader.readConfig()
		return self._config
		
	def writeConfig():
		self._confwriter.writeConfig(self._config)