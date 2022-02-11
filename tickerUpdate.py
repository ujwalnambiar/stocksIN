# This is to load csv into postgreSQL

import psycopg2
import csv
import wget
import os

os.remove(r'C:\Users\UjwalNambiar\Desktop\StocksAI\IN\EQUITY_L.csv')

nseURLLink='https://www1.nseindia.com/content/equities/EQUITY_L.csv'
wget.download(nseURLLink, r'C:\Users\UjwalNambiar\Desktop\StocksAI\IN')

conn = psycopg2.connect("host=localhost dbname=stocksAI user=postgres password=root@123")
cur = conn.cursor()

cur.execute('truncate table stocksin.tickerListNSE')

with open(r'C:\Users\UjwalNambiar\Desktop\StocksAI\IN\EQUITY_L.csv') as f:
    reader = csv.reader(f)
    next(reader) #skip header
    for row in reader:
        cur.execute(
            "insert into stocksin.tickerListNSE values(%s,%s,%s,%s,%s,%s,%s,%s)",row
        )
conn.commit()
conn.close()

