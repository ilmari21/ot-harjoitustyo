from entities.user import User
import db


class UserRepository:
    """Class responsible for the database operations of the users."""

    def __init__(self):
        """Constructor of the class."""

        self._connection = db.get_db_connection()

    def create(self, user):
        """Adds a user to the database.

        Args:
            user: The user to be added; a User-object.

        Returns:
            Returns the user added; a User-object.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_user(self, username):
        """Finds and returns the user matching the username.

        Args:
            username: The username of the user, which is being searched for.

        Returns:
            Returns a User-object matching the username.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * from users where username = ?",
            (username,)
        )
        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None

    def clear(self):
        """Deletes all entries from the database."""

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()
