# this is based on Google Cloud, you will need to use Drive API and setup a Key first

# by defaults you won't have any of these files on your PC, let PyCharm install them for you,
# secondary option is to use 'python pip' you can read more about it on the documentation

import gspread # from : https://github.com/burnash/gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds'] # this is where we fetch data from, all data presented here isn't human readable

credentials = ServiceAccountCredentials.from_json_keyfile_name('jasonfile.json',scope) # set the scope and the jason file you generated from google cloud

client = gspread.authorize(credentials) # use the above credentials to authorise a client through gspread

sheet = client.open("TestSheet").sheet1 # get data from the created google sheet

content = sheet.get_all_records() # fetch all the data in the sheet

print(content) # print all the fetched data

# we have not covered update cells part,refer to the git link provided upon import
