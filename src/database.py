import sqlite3 as sql
from sqlite3 import Error


def sql_connect(basename):
    try:
        con = sql.connect(f'db/{basename}.db')
        return con

    except Error:
        print(Error)


def sql_create(con):
    cursor = con.cursor()

    cursor.execute(
        "CREATE TABLE urls(id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT)")

    con.commit()


def sql_insert(con, urls):
    cursor = con.cursor()

    for url in urls:
        cursor.execute(
            'INSERT INTO urls(url) VALUES(?)', (url,))
        con.commit()


def sql_read(con):
    cursor = con.cursor()
    print(cursor.execute(
        """SELECT * FROM urls"""))


def save_to_data_base(all_urls, basename):
    # DB Operations
    con = sql_connect(basename)
    sql_create(con)
    sql_insert(con, all_urls)