import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="mibv",
        user="mibv")

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('SELECT COUNT(*) FROM nation;')

for count in cur:
	print(count)

conn.commit()

cur.close()
conn.close()
