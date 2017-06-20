# Udacity project #3 - Logs Analysis #
This project consists of one Python file, log_report.py, which contains three SQL queries. The queries run against a PostgreSQL database, which was provided for the project. The Python file uses the psycopg2 module to query the database, and prints results on the command line in a human readable format. The third query is against a created view. The file was tested in both Python 2 and 3.

## How to run it ##

The log_report.py is run from the command line in an Ubuntu virtual machine running in a Vagrant/Virtualbox environment, however you could run this program in any Linux environment with Python and PostgreSQL install, along with the psycopg2 Python module.
The file is run by typing `python log_report.py` from the command line.

## SQL used to create the view used in query #3 ##

`
CREATE VIEW error_requests AS
SELECT time::date AS date,
COUNT(*) AS requests,
COUNT(*) FILTER(WHERE status LIKE '4%' OR status LIKE '5%') AS errors
FROM log
GROUP BY time::date;`
