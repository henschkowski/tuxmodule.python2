#!/usr/bin/env python 

import sys
import tux

if len(sys.argv) < 2:
    print "Usage: %s <string> [<string>]*" % (sys.argv[0])
    sys.exit(1)

for index in range(1, len(sys.argv)):
    print tux.tpcall("TOUPPER", sys.argv[index])

sys.exit(0)

# Local Variables: 
# mode:python 
# End: 
