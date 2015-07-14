#!/usr/bin/env python

# Imports
from xlutils.copy import copy
import re
import xlrd
from subprocess import Popen, PIPE, STDOUT
import os
import xlwt
# from searchForString import getWebsiteName, getFailures, getTestResults, generateHTML, checkNavigationBar, checkFooter, renderToTemplate

# Global Variables Declaration
currentDirectory = os.getcwd()
# driver = webdriver.Firefox()
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
copyrightAndTrademark = "http://www.asu.edu/copyright/"
accessibility = "http://www.asu.edu/accessibility/"
privacy = "http://www.asu.edu/privacy/"
jobsAtASU = "http://www.asu.edu/asujobs/"
emergency = "https://cfo.asu.edu/emergency/"
contactASU = "https://contact.asu.edu/"
newWebsite = ""
website = ""



# Get current directory
currentDirectory = os.getcwd()
# Open existing workbook for reading data
workbook = xlrd.open_workbook('***Enter path to excel sheet here***')
# Open Sheet1 from workbook
worksheet = workbook.sheet_by_name('Sheet1')
# Get number of rows in the Excel sheet
num_rows = worksheet.nrows - 1
# Get number of columns in the Excel Sheets
num_cells = worksheet.ncols - 1
print "Number of cells: "+str(num_cells)
curr_row = -1
# Iterate over all websites in input file
while curr_row < num_rows:
	# Move to next row
	curr_row += 1
	row = worksheet.row(curr_row)
	print 'Row:', curr_row
	curr_cell = -1
	while curr_cell < num_cells:
		# Move to new cell every iteration
		curr_cell += 1
		# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
		cell_type = worksheet.cell_type(curr_row, curr_cell)
		cell_value = worksheet.cell_value(curr_row, curr_cell)
		print "currently testing*****"+cell_value+"*****"
		fileToRead = open('test.feature','r')
		fileContent = fileToRead.read()
		with open('test.feature','r') as f:
			for line in f:
				if "As a user" in line:
					print line
					website = re.search("(?P<url>https?://[^\s]+)", line).group("url") or re.search("(?P<url>www[^\s]+)", line)
					print str(website)
					fileToRead.close()
					break
		fileToChange = open('test.feature','w')
		replaceWebsite = fileContent.replace(str(website),str(cell_value))
		fileToChange.write(replaceWebsite)
		fileToChange.close()
		# Execute shell command to generate baseline tests
		# Writes result of Test Scenarios into output.txt
		execBaseline = Popen("hardy --browser=chrome . > output.txt",shell=True,stdout=PIPE)
		execBaseline.wait()
		generateHTMLReport = Popen("python searchForString.py")
		generateHTMLReport.wait()


