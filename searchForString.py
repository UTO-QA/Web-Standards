#!/usr/bin/env python

import jinja2
import os
from selenium import webdriver
from selenium.webdriver.common import keys, action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Global Variables Declaration
currentDirectory = os.getcwd()
driver = webdriver.Firefox()
correctRedirection = ""
correctLink = ""
navigationBarCheck = ""
globalFooterCheck = ""
# Expected Links for Header
asuLink = "https://www.asu.edu/"
myASULink = "https://my.asu.edu/"
collegesLink = "https://www.asu.edu/colleges/"
mapLink = "https://www.asu.edu/map/"
directoryLink = "https://www.asu.edu/contactasu/"
# Expected Links for global footer
copyrightAndTrademark = "http://www.asu.edu/copyright)"
accessibility = "http://www.asu.edu/accessibility/"
privacy = "http://www.asu.edu/privacy/"
jobsAtASU = "http://www.asu.edu/asujobs/"
emergency = "https://cfo.asu.edu/emergency/"
contactASU = "https://contact.asu.edu/"
driver.get("https://uto.asu.edu")


# Function to fetch website currently being tested
def getWebsiteName():
	fileToRead = file('test.feature')
	for line in fileToRead:
		if "Given I visit" in line:
			websiteString = line.split("\"")
			website = websiteString[1]
			name = website.split("/")
	return name[2]

# Get the failures once test has run
def getFailures():
	parseLines = False
	failures = list()
	outputFile = open("output.txt",'r')
	# Capture all lines between "(::) failed steps (::)"" and "Failed Scenarios"
	for line in outputFile:
		if line.startswith("Failing scenarios:"):
			parseLines = False
		if parseLines:
			if line.strip():
				failures.append(line)
		if line.startswith("(::) failed steps (::)"):
			parseLines = True
	logoResult = checkLogo()
	navigationBarResult = checkNavigationBar()
	footerResult = checkFooter()
	failures.append(logoResult)
	failures.append(navigationBarResult)
	failures.append(footerResult)
	for item in failures:
		if not item.strip():
			failures.remove(item)
		else:
			print item
	return failures

# Get Tests run, skipped and failed
def getTestResults():
	outputFile = open("output.txt",'r')
	for line in outputFile:
		if "steps" in line:
			if not "::" in line:
				testStatus = line[line.find("(")+1:line.find(")")]
	return testStatus

def generateHTML():
	siteName = getWebsiteName()
	failures = getFailures()
	testResults = getTestResults()
	f = open('report.html','w')
	message = """\
	<html>
	<head></head>
	<body>
		<h1>Website Name</h1>
		<p>{siteName}</p>
		<h1>Failures</h1>
		<p>{failures}</p>
		<h1>Test Case Status</h1>
		<p>{testResults}</p>
	</body>
	</html>
	""".format(**locals())
	f.write(message)
	f.close()

def checkLogo():
	# driver.get("https://uto.asu.edu/")
	getLogoId = driver.find_element_by_id('asu_logo')
	# Get location of redirect Link
	targetOnClick = getLogoId.find_element_by_css_selector('a').get_attribute('target')
	# Get redirect link
	pageOnClick = getLogoId.find_element_by_css_selector('a').get_attribute('href')
	print pageOnClick
	print targetOnClick
	# driver.close()
	if str(targetOnClick) == "_top":
		if str(pageOnClick) == "https://www.asu.edu/":
			# Test Case succeded
			correctLink = ""
			return correctLink
	else:
		# Test Case failed
		correctLink = "Clicking on Asu Logo does not give expected Results"
		return correctLink

# check all the links of the navigation bar
def checkNavigationBar():
	# driver.get("https://uto.asu.edu/")
	getNavigationBar = driver.find_element_by_id('asu_universal_nav')
	navBarElements = getNavigationBar.find_elements_by_css_selector('a')
	# Global ASU Link
	asuHome = navBarElements[0].get_attribute('href')
	# MyASU Link
	myASU = navBarElements[1].get_attribute('href')
	# Colleges and Schools Link
	collegesAndSchools = navBarElements[2].get_attribute('href')
	# Maps and Locations link
	mapCSS = driver.find_element_by_css_selector('#asu_universal_nav > ul > li:nth-child(4) > a')
	mapAndLocations = mapCSS.get_attribute('href')
	# Directory Link
	directoryCSS = driver.find_element_by_css_selector('#asu_universal_nav > ul > li:nth-child(5) > a')
	directory = directoryCSS.get_attribute('href')
	if asuHome == asuLink and myASU == myASULink and collegesAndSchools == collegesLink and mapAndLocations == mapLink and directory == directoryLink:
		navigationBarCheck = ""
		return navigationBarCheck
	else:
		navigationBarCheck =  "Navigation Bar Links Incorrect"
		return navigationBarCheck
	# driver.close()

# check all links of asu global footer
def checkFooter():
	# driver.get("https://uto.asu.edu/")
	getNavigationBar = driver.find_element_by_id('asu_footer')
	footerElements = getNavigationBar.find_elements_by_css_selector('a')
	# Copyrights&Trademark Link
	copyrightFooter = footerElements[0].get_attribute('href')
	# Accessibility Link
	acessibilityFooter = footerElements[1].get_attribute('href')
	# Privacy Link
	privacyFooter = footerElements[2].get_attribute('href')
	# JobsAtASU link
	jobsFooter = footerElements[3].get_attribute('href')
	# Emergency Link
	emergencyFooter = footerElements[4].get_attribute('href')
	# Contact Link
	contactFooter = footerElements[5].get_attribute('href')
	print copyrightFooter
	print acessibilityFooter
	print privacyFooter
	print jobsFooter
	print emergencyFooter
	print contactFooter
	if copyrightFooter == copyright and acessibilityFooter == accessibility and privacyFooter == privacy and jobsFooter == jobsAtASU and emergencyFooter == emergency and contactFooter == contactASU :
		globalFooterCheck = ""
		return globalFooterCheck
	else:
		globalFooterCheck =  "Global Footer Links are incorrect"
		return globalFooterCheck
	# driver.close()



# Check Dynamic Serach Results Layout
'''def checkSearchReults():
	driver.get("https://uto.asu.edu")
	action = action_chains.ActionChains(driver)
	# open up the developer console, mine on MAC, yours may be diff key combo
	action.send_keys(keys.Keys.CONTROL+keys.Keys.SHIFT+'k')
	action.perform()
	time.sleep(3)
	# this below ENTER is to rid of the above "i"
	action.send_keys(keys.Keys.ENTER)
	# inject the JavaScript...
	action.send_keys("document.querySelectorAll('input.asu_search_button').click()"+keys.Keys.ENTER)
	action.perform()
	time.sleep(30)
	driver.close()'''

def renderToTemplate():
	templateLoader = jinja2.FileSystemLoader(os.getcwd())

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
	templateEnv = jinja2.Environment( loader=templateLoader )

# This constant string specifies the template file we will use.

# Read the template file using the environment object.
# This also constructs our Template object.
	template = templateEnv.get_template('report.html')

# Specify any input variables to the template as a dictionary.
# templateVars = { "title" : "Test Example",
#                 "description" : "A simple inquiry of function." }

# Finally, process the template to produce our final text.
	outputText = template.render(websiteName = getWebsiteName() , testStatus = getTestResults(), failures = getFailures())
	print outputText
	siteName = getWebsiteName()
	fileName = siteName+".html"
	with open(fileName,"wb") as f:
		f.write(outputText)
		f.close()

def main():
	renderToTemplate()
	# result = checkLogo()
	# print result
	# checkNavigationBar()
	result = checkFooter()
	print result
	driver.close()



main()
