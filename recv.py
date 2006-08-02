#!/home/hensch/bin/python 
import sys
import os
import string
import tux


class server:
	def RECV(self, arg):
		print "connect to RECV ..."
		try:
			handle = self.cd
			print "   cd = %i"  % self.cd
                except:
			print "no cd given"

		try:
			print "   arg = %s" % arg
		except:
			print "no arg given"


		try:
			print "   name = %s" % self.name
		except:
			print "no name given"


		try:
			while 1:
				evt, rec = tux.tprecv(handle)
				print evt, rec
				if rec == "END":
					tux.userlog("server returning TPSUCCESS")
					return tux.TPSUCCESS
				else:
					ret = "len = %d" % len(rec)
#					tux.userlog("call TOUPPER ...")
#					tux.tpcall("TOUPPER", "")		
					tux.userlog("sending %s ..." % (ret))
					ret = tux.tpsend(handle, ret, tux.TPRECVONLY)
		except RuntimeError, e:
			exception = "got exception: %s" % e
			tux.userlog(exception)
			return tux.TPFAIL
	
		except:
			tux.userlog( "got exception")
			return tux.TPFAIL
	
	def init(self, arguments):

		tux.tpopen()
		tux.tpadvertise("RECV");
		
	def cleanup(self):
		tux.userlog("cleanup in recv_py called!")


srv = server()

def exithandler():
	print "huuhhu"
sys.exitfunc = exithandler

if __name__ == '__main__': 
	tux.mainloop(sys.argv, srv, None)

# Local Variables: 
# mode:python 
# End: 
