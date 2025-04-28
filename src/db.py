import sqlite3

con = sqlite3.connect("database.db")


def get_db_connection():
    con.row_factory = sqlite3.Row
    return con


def init_db():
    cursor = get_db_connection()

    cursor.execute(
        """DROP TABLE IF EXISTS users;"""
    )
    cursor.execute(
        """DROP TABLE IF EXISTS flights;"""
    )

    create_tables(cursor, con)

    cursor.close()


def create_tables(cursor, con):
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

    con.commit()


if __name__ == "__main__":
    init_db()
