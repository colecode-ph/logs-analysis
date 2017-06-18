import psycopg2

DBNAME = "news"

conn =  psycopg2.connect(database=DBNAME)
cursor = conn.cursor()
sql_query = ("""SELECT articles.title, COUNT(*) AS views
             FROM articles, log
             WHERE log.path LIKE '%' || articles.slug
             GROUP BY articles.title
             ORDER BY views DESC LIMIT 3;""")
cursor.execute(sql_query)
results = cursor.fetchall()
for row in results:
    print (row)