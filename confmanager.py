#Copyright (c) Jukka Pietilä 2013
#See LICENSE for details

import config
import confwriter
import confreader

class ConfManager(object):
	def __init__(self):
		self._conffile = "config.conf"
		self._confreader = confreader.ConfReader()
		self._config = self._confreader.readConfig()
		self._confwriter = confwriter.ConfWriter()

	def __init__self(self, conffile):
		self._conffile = conffile
		self._confreader = confreader.ConfReader(self._conffile)
		self._config = self._confreader.readConfig()
		self._confwriter = confwriter.ConfWriter(self._conffile)

	def readConfig():
		self._config = self._confreader.readConfig()
		return self._config
		
	def writeConfig():
		self._confwriter.writeConfig(self._config)

	def changeConfig(config):
		"""
		saves the changes to config-object and writes the changes to file
		"""
		self._config = config
		self.writeConfig()