from connect_db import get_database_connection


def initialize_database(connection=None):
    connection_closed = False
    if connection is None:
        connection = get_database_connection()
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
            arr_time TEXT,
            elapsed_time INTEGER
        );"""
    )

    connection.commit()


if __name__ == "__main__":
    initialize_database()
