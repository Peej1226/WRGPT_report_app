# https://www.codementor.io/@dankhan/web-scrapping-using-python-and-beautifulsoup-o3hxadit4

import os
from _datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv

# TODO lots of stuff
cwd = os.getcwd()
cwdParent = os.path.abspath('..')
cwdGParent = os.path.abspath('../..')
# print(cwd)
# print(cwdParent)
# print(cwdGParent)

# https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/
dateTimeObj = datetime.now()
stamp = str(dateTimeObj.year) + '/' + str(dateTimeObj.month) + '/' + str(dateTimeObj.day)

filename = os.path.join(cwdGParent, 'standingsRawData.csv')
results = open(filename, 'a', newline='')
results.write("-------\n")
results.write(stamp)
results.write("\n")
playerStandings = {'HM' : 0,
                   'Big Tone': 0,
                   'Tyler': 0,
                   'Peej1226':0}
page = requests.get('http://www.wrgpt.org/stats/standings/')
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.table
table_rows = table.find_all('tr')

writer = csv.writer(results)
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    if len(row) > 0 and row[1] in playerStandings:
        writer.writerow(row)
        # results.write("\n")

results.close()
