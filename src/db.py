import sqlite3


def get_db_connection(db_path='database.db'):
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    return con


def get_db_test_connection():
    con = sqlite3.connect(':memory:')
    con.row_factory = sqlite3.Row
    return con


def init_db(connection=None):
    connection_closed = False
    if connection is None:
        connection = get_db_connection()
        connection_closed = True

    cursor = connection.cursor()

    cursor.execute(
        """DROP TABLE IF EXISTS users;"""
    )
    cursor.execute(
        """DROP TABLE IF EXISTS flights;"""
    )

    create_tables(cursor, connection)

    cursor.close()

    if connection_closed:
        connection.close()


def create_tables(cursor, connection):
    cursor.execute(
        """CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT
        );"""
    )

    cursor.execute(
        """CREATE TABLE flights (
            pilot TEXT,
            aircraft_type TEXT,
            aircraft_reg TEXT,
            departure TEXT,
            arrival TEXT,
            dep_time TEXT,
            arr_time TEXT
        );"""
    )

    connection.commit()


if __name__ == "__main__":
    init_db()
