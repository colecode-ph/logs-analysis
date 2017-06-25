# Udacity project #3 - Logs Analysis #
This project consists of a Python file, log_report.py, which queries a PostgreSQL database, and prints results via the command line. An output.txt file is also included to show the output of the executed Python file.

The Python file uses the imported psycopg2 module to interact with the database. The file was tested in both Python 2 and 3, on an Ubuntu 16.04 virtual machine, running in a Vagrant/Virtualbox environment.

## PostgreSQL database structure ##
The database contains three tables: articles, authors, and log. The log table contains the contents of a web server request log. The PostgreSQL database was generated with a provided script, which is not included in the repository, however the \d readout of the tables, along with the output.txt file should provide a good idea of the database content:

    Table "public.articles"
     Column |           Type           |                       Modifiers
    --------+--------------------------+-------------------------------------------------------
     author | integer                  | not null
     title  | text                     | not null
     slug   | text                     | not null
     lead   | text                     |
     body   | text                     |
     time   | timestamp with time zone | default now()
     id     | integer                  | not null default nextval('articles_id_seq'::regclass)
    Indexes:
        "articles_pkey" PRIMARY KEY, btree (id)
        "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
    Foreign-key constraints:
        "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


    Table "public.authors"
     Column |  Type   |                      Modifiers
    --------+---------+------------------------------------------------------
     name   | text    | not null
     bio    | text    |
     id     | integer | not null default nextval('authors_id_seq'::regclass)
    Indexes:
        "authors_pkey" PRIMARY KEY, btree (id)
    Referenced by:
        TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


    Table "public.log"
     Column |           Type           |                    Modifiers
    --------+--------------------------+--------------------------------------------------
     path   | text                     |
     ip     | inet                     |
     method | text                     |
     status | text                     |
     time   | timestamp with time zone | default now()
     id     | integer                  | not null default nextval('log_id_seq'::regclass)
    Indexes:
        "log_pkey" PRIMARY KEY, btree (id)


## How to run it ##

The file is an executable so it can be is by typing `log_report.py` from the command line.

## SQL used to create the view used in query #3 ##

The third query in log_report.py is against a view which was created with the following:

    `
    CREATE VIEW error_requests AS
    SELECT time::date AS date,
    COUNT(*) AS requests,
    COUNT(*) FILTER(WHERE status LIKE '4%' OR status LIKE '5%') AS errors
    FROM log
    GROUP BY time::date;`
