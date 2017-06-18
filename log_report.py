import psycopg2

DBNAME = "news"

conn =  psycopg2.connect(database=DBNAME)
cursor = conn.cursor()
cursor.execute("SELECT title FROM articles;")
results = cursor.fetchall()
print (results)