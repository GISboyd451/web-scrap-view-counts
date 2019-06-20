# Name: web_scrap_view_counts.py
# Author: GISBoyd451 (Contractor)
# Python version: 3.7
# Date: 06/20/2019
# Updates: v1
# Description:  Original design for this script was to pass in an excel sheet with other ancillary information including a column
#               containing the URLs of all the websites we would like to web scrape the View Count <element> from.
#               The script will then cycle through each row in the .xlsx file and retrieve and connect to the URL provided.
#               The connection will be established through the selenium (interfaced with a browser) and simulate the copying 
#               and pasting of the CSS_SELECTOR (View Count <element>) the user has provided. 
#               This script serves as a template for future web scraping needs for the client and can be modified to grab a 
#               single website element or multiple items depending on the project needs.
# ---------------------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------------------

# Example dynamic website with (View Count <element>)
# https://blm-egis.maps.arcgis.com/home/item.html?id=c1c223baba454f19b782cb09899c2445
# <span class="inline-block margin-right-1 margin-left-0">View Count: 545</span>  (View Count <element>)

# Example Excel file headers that the 'vanilla' script grabs. 
############################################################################
# | Story_Map | Creator(s) | Views | Total_Views | Last_Count | Story_URL |#
# |           |            |       |             |            |           |#
# |  !Text!   |   !Text!   | !num! |    !num!    | !Date!Time!|   !URL!   |#
# ##########################################################################

'''
Use the client's excel sheet and get the view counts from all the story maps and 
put them into a table. The table will then get uploaded to their googledrive later. 
'''

# Preliminary test to see if we can access webpages without higher permissions. We want to see the status code as 200.
'''import requests
from bs4 import BeautifulSoup
result = requests.get("https://blm-egis.maps.arcgis.com/home/item.html?id=c1c223baba454f19b782cb09899c2445")
print(result.status_code) # Status Code was 200 = accessible
#print(result.headers)
src = result.content
soup = BeautifulSoup(src, features="html.parser")'''

# Firefox webdriver installation: geckodriver.exe
# https://github.com/mozilla/geckodriver/releases
#
# Chrome webdriver installation: chromedriver.exe 
# http://chromedriver.chromium.org/downloads   **Note: You will need to download the driver that supports your version of Chrome. (Mine is currently: Chrome version 72 32-bit)

# Before running code, you will need a webdriver for selenium (see above). I have tested the code on two environments currently: Firefox & Chrome.
# At a later date, internet explorer can be tested as well (if needed).
# The internet browsers, such as Chrome and Firefox will need to be installed to your system path (Admin installed). PATH, e. g., place it in /usr/bin or /usr/local/bin 
# Otherwise selenium will be unable to find the browser app.

# Packages
import os
import time
import datetime
import pandas as pd
import numpy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Sample path for Firefox driver syntax
#browser = webdriver.Firefox(executable_path='T:\\ProjectsNational\\NationalDataQuality\\Sprint\\####_scripts\\calculate_views\\geckodriver')

# Disable Extensions in order to bypass admin error
capabilities = { 'chromeOptions':  { 'useAutomationExtension': False}}
# Sample path for Chrome driver syntax w/ options
browser = webdriver.Chrome(executable_path='T:\\ProjectsNational\\NationalDataQuality\\Sprint\\Alec_scripts\\calculate_views\\chromedriver',desired_capabilities = capabilities)
#print(type(browser))

# Point to directory with excel (change wd)
try:
    os.chdir("T:/ProjectsNational/NationalDataQuality/Sprint/Alec_scripts/calculate_views") #This will have to be changed if excel sheet is moved or path is different for user
    print("Directory Changed")
except:
    print("Directory not changed")
# Bring in excel file with URLs
df = pd.read_excel(r'story_map_view_counts.xlsx') # Excel file

##############################
##############################
# Columns/fields user defined:
col1 = 'Last_Count'
col2 = 'Views'
col3 = 'Total_Views'
col4 = 'Story_URL'
col5 = 'Story_Map'
##############################
##############################

# Set Last_Count column as system date and time
t = datetime.datetime.now()
df[col1] = t

# Erase old Views and Total_Views data Columns. Set to zero
df[col2] = 0
df[col3] = 0

# This loop works but we need to have a delay system in order to not overload websites.
# Temporary list
tmp = []
for index, row in df.iterrows():
    browser.get(row[col4],)
    timeout = 60
    try:
        d = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.inline-block:nth-child(3)")))
        print(d)
        print(d.text)
        tmp.append(d.text)
        time.sleep(2) # add two second delay to prevent spamming websites
    except:
        print("Not able to retrieve view count on"+row[col5])
        time.sleep(10)
print("Completed Web Searching")
browser.quit()

# Convert items in list (tmp) to correct integer format
tmp = [s.strip('View Count:') for s in tmp] #Gets rid of 'View Count:' 
tmp = [s.replace(',', '') for s in tmp] #Gets rid of commas in certain numbers
tmp = list(map(int, tmp)) #Gets integers

tmp = pd.DataFrame(tmp)
tmp.index = df.index
df[col2] = tmp

# Get total
Total = df[col2].sum()
df[col3] = Total

#Write information to excel:
out_path = 'T:\\ProjectsNational\\NationalDataQuality\\Sprint\\Alec_scripts\\calculate_views\\story_map_view_counts.xlsx' #Output path should be the same everytime because we are updating table
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index = False)
try:
    writer.save()
    print('story_map_view_counts table has been saved.')
except:
    print('File failed to save.')
#########################################################
#########################################################