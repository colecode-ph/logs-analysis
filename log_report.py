import psycopg2

DBNAME = "news"
# create the database connection and get the cursor
conn = psycopg2.connect(database=DBNAME)
cursor = conn.cursor()
# query to answer the first question
sql_query = ("""SELECT articles.title, COUNT(*) AS views
             FROM articles, log
             WHERE log.path LIKE '%' || articles.slug
             GROUP BY articles.title
             ORDER BY views DESC LIMIT 3;""")
cursor.execute(sql_query)
results = cursor.fetchall()
# print the question and answer in a human readable format
print ("1. What are the three most popular articles of all time?\n")
for row in results:
    print ('"' + row[0] + '" - ' + str(row[1]) + " views")
print("")

# query to answer the second question
sql_query = ("""SELECT authors.name, COUNT(*) AS views
             FROM authors, log, articles
             WHERE authors.id = articles.author
             AND log.path LIKE '%' || articles.slug
             GROUP BY authors.name
             ORDER BY views DESC;""")
cursor.execute(sql_query)
results = cursor.fetchall()
# print the question and answer in a human readable format
print ("2. What are the three most popular article authors of all time?\n")
for row in results:
    print (row[0] + ' - ' + str(row[1]) + " views")
print("")

# query to answer third question - queries the view error_requests, SEE README.md
sql_query = ("""SELECT to_char(date, 'FMMonth FMDDth, YYYY') AS date,
             round(errors * 100.0 / requests, 1) AS percent
             FROM error_requests
             WHERE (errors * 100.0 / requests) > 1;""")
cursor.execute(sql_query)
results = cursor.fetchall()
# print the question and answer in a human readable format
print ("3. On which days did more than 1% of requests lead to errors?\n")
for row in results:
    print (row[0] + ' - ' + str(row[1]) + "%")
