# ASU Web-Standards

___________________________________

### Requirements
*********
+ npm 
+ Python 2.7.6

### Installation Instructions
***************
+ Install Python 2.7.6

+ Install gemini.js using the following command

	npm install -g gemini
	
+ Install Hardy.IO using the following command

	npm install -g hardy

+ Install PhantomJS 1.9.8 using the following command

	npm install -g phantomjs@1.9.8
	
### How to Run the Script
*************

1. Create an empty folder and install all the libraries as mentioned above from      this folder.
2. Fire up the command prompt and navigate to your project folder. 
3. In another tab of the command prompt type in 
	
	<b>phantomjs --webdriver=4444</b>
	
	This starts the webdriver on port 4444
4. Run the python script using the following command: 
	
	<b>python magicScript.py</b>

5. Allow the script to finish running. Your project folder will now have folders for all the websites that have been tested with the html reports for each of the websites inside the corresponding folder.
6.  Close the window running webdriver. 
7.  From the project folder in the command prompt type in the following commands:
	
	<b>hardy selenium start</b>
	
	<b>python searchForString.py</b>
8. Allow the script to run. Once the script has run the website folders will have an HTML report with the errors found in the layout of the headers and footers. 
9. Close the command prompt running selenium. 

### Further Reading Up
**********************
For detailed instructions on running the tools refer the following links:

* Gemini.js

	([https://github.com/gemini-testing/gemini](https://github.com/gemini-testing/gemini))

* Hardy.IO

	([http://hardy.io/](http://hardy.io/))
	
* Python

	([https://www.python.org/doc/](https://www.python.org/doc/))

