import sqlite3


def get_database_connection(db_path='data/database.db'):
    """Creates and returns a SQLite database connection.

    Args:
        db_path: Path to the SQLite database file.

    Returns:
        SQLite connection object.
    """

    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    return con


def get_test_database_connection():
    """Creates an in-memory SQLite database connection for testing.

    Returns:
        SQLite connection object.
    """

    con = sqlite3.connect(':memory:')
    con.row_factory = sqlite3.Row
    return con
