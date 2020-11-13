import os
from _datetime import datetime
import pandas as pd
import csv

dfs = pd.read_html('http://www.wrgpt.org/stats/standings/', header=0)
cwd = os.getcwd()
cwdParent = os.path.abspath('..')
cwdGParent = os.path.abspath('../..')

dateTimeObj = datetime.now()
stamp = str(dateTimeObj.year) + '/' + str(dateTimeObj.month) + '/' + str(dateTimeObj.day)

filename = os.path.join(cwdGParent, 'bankrollsRawData.csv')
results = open(filename, 'a', newline='')
results.write("-------\n")
results.write(stamp)
results.write("\n")
writer = csv.writer(results)
for df in dfs:
    print(df.head())
    bankroll_list = df["Bankroll"].tolist()
    print(bankroll_list)
    writer.writerow(bankroll_list)

results.close()
