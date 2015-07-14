#!/usr/bin/env python


# Open test.feature file

fileToRead = open('testFile.feature')
fileContent = fileToRead.read()
fileToRead.close()
fileToRead = open('testFile.feature','w')
replaceWebsite = fileContent.replace('https://uto.asu.edu/','https://nursingandhealth.asu.edu/')
fileToRead.write(replaceWebsite)
fileToRead.close()