#Code:
# Run this in the terminal or auto install on Pycharm
# Pip install gspread oauth2client

import gspread

from oauth2client.service_account import ServiceAccountCredentials

# define the scope of operations
scope = ['https://spreadsheets.google.com/feeds']

# set the credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('Name of Key.json',scope)

# setup the client
client = gspread.authorize(credentials)

# open the Google Sheet
sheet = client.open('TestSheet').sheet1

# get contents
content = sheet.get_all_records()

# print all recieved contents
print(content)

#commands

