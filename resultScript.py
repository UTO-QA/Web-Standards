#!/usr/bin/env python

# Imports
from subprocess import Popen, PIPE, STDOUT
import os

# Execute shell command to generate baseline tests
# Writes result of Test Scenarios into output.txt
execBaseline = Popen("hardy --browser=chrome . > output.txt",shell=True,stdout=PIPE)
for line in execBaseline.stdout:
	print line
output,err = execBaseline.communicate()
retCode = execBaseline.returncode
print str(retCode)

