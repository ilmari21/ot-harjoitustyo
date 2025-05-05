import sqlite3


def get_database_connection(db_path='data/database.db'):
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    return con


def get_test_database_connection():
    con = sqlite3.connect(':memory:')
    con.row_factory = sqlite3.Row
    return con
