#! /usr/bin/env python
import sys
import string
import os
import re

getenv=os.environ.get

for line in sys.stdin.readlines():
    line = re.sub('%%APPDIR%%', getenv('APPDIR', ''), line)
    line = re.sub('%%TUXDIR%%', getenv('TUXDIR', ''), line)
    line = re.sub('%%TUXCONFIG%%', getenv('TUXCONFIG', ''), line)
    line = re.sub('%%QMCONFIG%%', getenv('QMCONFIG', ''), line)
    line = re.sub('%%UNAME%%', os.uname()[1], line)
    line = re.sub('%%PWD%%', os.getcwd(), line)
    print string.rstrip(line)

