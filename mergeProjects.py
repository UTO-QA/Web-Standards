#!/usr/bin/env python

import subprocess
from time import sleep

runSelenium = subprocess.Popen("hardy selenium start")
sleep(5)
runHardy = subprocess.Popen("python resultScript.py")
runHardy.wait()
stopSelenium = subprocess.Popen("hardy selenium stop")
sleep(5)
startWebdriver = subprocess.Popen("phantomjs --webdriver=4444")
sleep(5)
runGemini = subprocess.Popen("python magicScript.py")
