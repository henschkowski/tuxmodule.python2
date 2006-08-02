#!/home/hensch/bin/python 
import sys
import os
import string
import tux
import time

import reloader
import pyserver

class server:
	def subscTOUPPER(self, arg):
		ret = string.upper(arg)
		tux.tpnotify(self.cltid, ret)
		return tux.TPSUCCESS

	def TOUPPERFAIL(self, arg):
		ret = string.upper(arg)
		return tux.TPFAIL

	def COUNTER(self, arg):
		self.counter += 1
		return `self.counter`

	def RESETCOUNTER(self, arg):
		self.counter = 0
		return tux.TPSUCCESS

	def TOUPPER(self, arg):     # get string and return string
		print self.name
		try:
			print self.cd
		except:
			print "No Conversation "
		print self.flags
		print self.appkey
		print self.cltid

		tux.userlog("client-ID = %s" % (self.cltid))
		
		print "converting %s" % arg
		return string.upper(arg)

	def UNSOLmethod_for_call_from_service_UNSOL(self, arg):     # get string and return string

		print "UNSOL: %s" % self.cltid
                tux.tpnotify(self.cltid, "1") 
		time.sleep(1)
	        tux.tpnotify(self.cltid, "2") 
		tux.tpnotify(self.cltid, "3") 

		tux.tpbroadcast("simple", None, None, "4") 
		
		return string.upper(arg)

	def TUPPER(self, arg):
		print "call TUPPER"
		tux.tpforward("TOUPPER", arg)

	def service123456789abcdefghijklm(self, arg):   # change FML argument buffer and return it
		print "call service_1"
		print arg.keys()
		arg['TA_OPERATION'][0] = "OK"
		arg['TA_OPERATION'].append("NOK")
		print arg
		return arg

	def ping(self, arg):
		return arg

	def service_3(self, arg):   # get whatever and return new FML buffer (elements are lists)
		print "call service_3"

		return { 'VORNAME': ['Ralf', 'Andreas'], 'NACHNAME': ['Henschkowski'] }

	def service_4(self, arg):
		print "call service_4"  # return new FML buffer (elements can be strings -> occurence 0)

		return { 'VORNAME': 'Ralf_Andreas', 'NACHNAME': ['Henschkowski'] }

	def service_5(self, arg):   # return Tux. returncode		print "call service_5"
		tux.tpunadvertise("service_4")
		return tux.TPSUCCESS

	def __init__(self):         # called whenever class is loaded/instantiated
		self.RESETCOUNTER(0)

	def init(self, arguments):  # called on server boot
		tux.tpopen()
		tux.tpadvertise("ping")
		tux.tpadvertise("TOUPPER")
		tux.tpadvertise("TOUPPERFAIL")
		tux.tpadvertise("COUNTER")
		tux.tpadvertise("RESETCOUNTER")
		tux.tpadvertise("service_3")
		tux.tpadvertise("UNSOL", "UNSOLmethod_for_call_from_service_UNSOL")
		tux.tpadvertise("subscTOUPPER")

		tux.tpsubscribe("TOUPPER_EVT", "", { 'flags': tux.TPEVSERVICE, 'name1': "subscTOUPPER" } )

if __name__ == '__main__': 

	myserver = pyserver.server()   # initial server class instance
	rel = reloader.reloader(pyserver, myserver) # dynamic reloader
	tux.mainloop(sys.argv, myserver, rel.reloader_func)

# Local Variables: 
# mode:python 
# End: 

