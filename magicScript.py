#!/usr/bin/env python


# imports 
from xlutils.copy import copy
import xlrd
import yaml
import subprocess
import os
import codecs
from bs4 import BeautifulSoup
import xlwt
import requests


# Get current directory
currentDirectory = os.getcwd()
# Open existing workbook for reading data
workbook = xlrd.open_workbook('convertedSites.xlsx')
# Open a new workbook to write test results
workbookWrite = xlwt.Workbook()
worksheetWrite = workbookWrite.add_sheet('results')
worksheet = workbook.sheet_by_name('Sheet1')
# open config file (To change test website for each iteration)
stream = open(".gemini.yml")
# Load config file into a dictionary
doc = yaml.load(stream)
print "Printing gemini.yml"
print doc
try:
    # Execute shell command to generate baseline tests
    execBaseline = subprocess.Popen("gemini gather sosTest.js",shell=True,stdout=subprocess.PIPE)
    execBaseline.wait()
except:
    print "Unresolved EPIPE Error."

# Create first row of Result Excel Sheet
worksheetWrite.write(0,0,'Website')
worksheetWrite.write(0,1,'Total Tests')
worksheetWrite.write(0,2,'Passed')
worksheetWrite.write(0,3,'Failed')
worksheetWrite.write(0,4,'Skipped')
num_rows = worksheet.nrows - 1
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
    current_cell = -1
    while curr_cell < num_cells:
        # Move to new cell every iteration
        curr_cell += 1
        current_cell += 1
        # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
        cell_type = worksheet.cell_type(curr_row, curr_cell)
        cell_value = worksheet.cell_value(curr_row, curr_cell)
        print "*****"+cell_value
        # Insert website into config file
        doc["rootUrl"]= cell_value
        print "doc"
        print doc
        websiteName = str(cell_value)
        worksheetWrite.write(curr_row+1,current_cell,websiteName)
        splitString = websiteName.split("/")
        fileName = splitString[2]+".html"
        f = open(".gemini.yml", "w+")
        # Insert website into config file
        # with open("\\geminiTestProject\\.gemini.yml","w+") as f:
        yaml.safe_dump(doc,f,default_flow_style=False)
        print "Creating HTML Report"
        execTest = subprocess.Popen("gemini test --reporter html sosTest.js",shell=True,stdout=subprocess.PIPE)
        execTest.wait()
        if not os.path.exists(currentDirectory+"\\"+splitString[2]):
            os.makedirs(currentDirectory+"\\"+splitString[2])
            os.rename(currentDirectory+'\\gemini-report\\index.html',currentDirectory+'\\gemini-report\\'+fileName)
            listOfFiles = os.listdir(currentDirectory+'\\gemini-report')
            # Move files from gemini-report to school directory
            for f in listOfFiles:
                destination = currentDirectory+"\\"+splitString[2]
                fullPath = currentDirectory+'\\gemini-report\\'+f
                command = subprocess.Popen("move" + " " + fullPath + " " + destination, shell=True)
                command.wait()
        # Get Total, Failed, Passed and Skipped tests from HTML Document
        if os.path.exists(currentDirectory+"\\"+splitString[2]):
            currentPath = splitString[2]+"\\"+splitString[2]+".html"
            page = codecs.open(currentDirectory+"\\"+currentPath, 'r')
            document = page.read()
            soup = BeautifulSoup(document)
            for allTests in soup.findAll('dt'):
                allTests = allTests.nextSibling
                print allTests.contents[0].strip()
                current_cell += 1
                worksheetWrite.write(curr_row+1,current_cell,allTests.contents[0].strip())
                # Write test Results to Excel Sheet
                print "Writing to Row:"+str(curr_row)+" Cell: "+str(current_cell)
workbookWrite.save('TestResults.xls')

'''
Format of Result

=============================================================================================================
Website Tested 		|		Total Tests Run		|		Passed		|		Failed		|		Skipped		|
                    |							|					|					|					|
                    |							|					|					|					|
=============================================================================================================
'''