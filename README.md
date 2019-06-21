# web-scrap-view-counts
Web scrap dynamic websites using Selenium by CSS_SELECTOR in python.

## Overview
The original purpose of this script was to web scrape multiple dynamic websites (that use JAVA behind the scenes) and search for the "View Count:" element by CSS_SELECTOR. After retrieving the view count element, the python script would parse out the unnecessary information and make a list of numbers that were contained within the web element and then output them inside an excel file with other ancillary data.
Although the usage was intended for primarily what was stated above, it would be very simple to modify the CSS_SELECTOR line to match a user's needs.

## Requirements
* Python 3.4+
* Works on Linux, Windows, and Mac OSX.

#### Packages Needed
- os (default)
- time (default)
- pandas (http://pandas.pydata.org/)
- numpy (https://pypi.org/project/numpy/)
- requests (https://pypi.org/project/requests/)
- bs4 (https://pypi.org/project/beautifulsoup4/)
- selenium (https://pypi.org/project/selenium/)

#### Drivers 
From the selenium homepage:

*Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the script can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.*

*Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.*

*Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.*

Broswer | Driver Link
------------ | -------------
Chrome | https://sites.google.com/a/chromium.org/chromedriver/downloads
Firefox | https://github.com/mozilla/geckodriver/releases
Edge: | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Safari | https://webkit.org/blog/6900/webdriver-support-in-safari-10/

## Documentation
This script currently operates off of a table (excel, csv, etc.) to retrieve the list of URLs the user would like to pass into selenium and find the 'View Count:' number. 

EXCEL CURRENT SETUP

Story_Map | Creator(s) | Views | Total Views | Last_Count | Story_URL
------------ | -------------|-------------|-------------|-------------|-------------|
Text Field | Text Field | Integer Field | Integer Field | Date Time | URL

Once the user's table has been established in the variable 'df', the user will then need to identify which columns/fields are needed in lines 84-93. 

CURRENT VARAIBLE VALUES IN SCRIPT

Columns | Field Name in Table
------------ | -------------
col1 | 'Story_Map'
col2 | 'Views'
col3 | 'Total_Views'
col4 | 'Last_Count'
col5 | 'Story_URL'

## Running The Script
Current setup is in python 3.

Update lines:
Lines 69-72: Browser and webdriver paths will need to be changed based on user 'file paths'.

Lines 76-82: .xlsx input file path will need to be changed based on user 'file paths'.

Lines 84-93: The columns/fields are user defined based upon the input table.

Lines 135-142: .xlsx output file path will need to be changed based on user 'file paths'.
run script

## Release Notes
Version: v1 06/21/2019

## Usage

## Author Notes
