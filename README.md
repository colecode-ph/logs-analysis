# Udacity project #3 - Logs Analysis #
This project consists of one Python file, log_report.py, which contains three SQL queries. The queries run against a PostgreSQL database, which was provided for the project. The Python file uses the psycopg2 module to query the database, and display results on the command line in a human readable format. The third query is against a created view. The file was tested in both Python 2 and 3.

## SQL used to create the view used in query #3 ##

`CREATE VIEW error_requests AS
SELECT time::date AS date,
COUNT(*) AS requests,
COUNT(*) FILTER(WHERE status LIKE '4%' OR status LIKE '5%') AS errors
FROM log
GROUP BY time::date;`
