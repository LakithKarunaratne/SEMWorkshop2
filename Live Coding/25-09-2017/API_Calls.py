# this is on Google API

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('jasonfile.json',scope)

client = gspread.authorize(credentials)

sheet = client.open("TestSheet").sheet1

content = sheet.get_all_records()
print(content)