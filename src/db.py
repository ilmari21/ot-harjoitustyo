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

    create_tables(con)


def create_tables(con):
    cursor = get_db_connection()

    cursor.execute(
        """CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT
        );"""
    )

    con.commit()

if __name__ == "__main__":
    init_db()
