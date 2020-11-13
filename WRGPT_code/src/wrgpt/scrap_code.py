# https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://www.wrgpt.org/stats/standings/').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.table

table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)