#!/usr/bin/env python 
import sys
import os
import string
import tux
import time
import signal


def sighandler(sig, frame):
    print "signal handler called"
#    tux.tpdisconnect(handle)
def sigtermhandler(sig, frame):
    print "sigerm handler called"


signal.signal(signal.SIGALRM, sighandler)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
print signal.getsignal(signal.SIGALRM)


data = [ "huhuhuhu", "hallo", "ciao", "END" ]

for num in range(1, 10):
#    tux.tpbegin(300)
    handle = tux.tpconnect("RECV", "out", tux.TPSENDONLY)
#    signal.alarm(10)
    print "handle = %d" % handle
    for item in data:
        print "sending %d, %s ..." % (handle, item)
        evt = tux.tpsend(handle, item, tux.TPRECVONLY)
        evt, ret = tux.tprecv(handle)
        print "tprecv(): evt, ret = %d, %s" % (evt, ret)
        print "sleep ..."
	time.sleep(5)
    if evt == tux.TPEV_SVCSUCC:
#        tux.tpcommit()
        print "transaction commited"
    else:
 #       tux.tpabort()
        print "transaction aborted"

tux.tpterm()
    



# Local Variables: 
# mode:python 
# End: 
