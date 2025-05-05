import sqlite3
from connect_db import get_database_connection
from entities.user import User


class DatabaseNotInitialized(Exception):
    pass


class UserRepository:
    """Class responsible for the database operations of the users."""

    def __init__(self, connection=None):
        """Constructor of the class.

        Args:
            connection: The database connection.
        """

        self._connection = connection or get_database_connection()

    def create(self, user):
        """Adds a user to the database.

        Args:
            user: The user to be added; a User-object.

        Returns:
            Returns the user added; a User-object.
        """
        try:
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (user.username, user.password)
            )
            self._connection.commit()
            return user
        except sqlite3.OperationalError:
            raise DatabaseNotInitialized("Database has not been initialized")

    def find_user(self, username):
        """Finds and returns the user matching the username.

        Args:
            username: The username of the user, which is being searched for.

        Returns:
            Returns a User-object matching the username.
        """

        try:
            cursor = self._connection.cursor()
            cursor.execute(
                "SELECT * from users where username = ?",
                (username,)
            )
            row = cursor.fetchone()
            return User(row["username"], row["password"]) if row else None
        except sqlite3.OperationalError:
            raise DatabaseNotInitialized("Database has not been initialized")

    def clear(self):
        """Deletes all entries from the database."""

        try:
            cursor = self._connection.cursor()
            cursor.execute("DELETE FROM users")
            self._connection.commit()
        except sqlite3.OperationalError:
            raise DatabaseNotInitialized("Database has not been initialized")
