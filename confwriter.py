import io
import config
import sys
import os

class ConfWriter(object):
	def __init__(self):
		self._CONFNAME = "config.conf"

	def __init__(self, confname):
		self._CONFNAME = confname

	def writeConfig(self, conf):
		"""
		Writes the contents of the Config-object into config-file,
		overwriting old values.
		@conf - The Config-object that is taken as param and extracted
		"""
		if type(conf) is not config.Config:
			raise Exception("Given parameter was not Config!")

		name = conf.BOTNAME
		server = conf.SERVER
		port = conf.PORT
		channels = list(conf.CHANNELS)
		joinmsg = conf.JOINMSG

		try:
			with open(self._CONFNAME, "w") as f:
				f.write("NAME=" + str(name) + "\r\n")
				f.write("SERVER=" + str(server) + "\r\n")
				f.write("CHANNELS=" + ",".join(channels) + "\r\n")
				f.write("PORT=" + port + "\r\n")
				f.write("JOINMSG=" + joinmsg + "\r\n")
		except IOError as e:
			print "I/O Error ({0}): {1}".format(e.errno, e.strerror)