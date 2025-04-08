from entities.user import User
import db


class UserRepository:
    def __init__(self):
        self._connection = db.get_db_connection()

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * from users where username = ?",
            (username,)
        )
        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None

    def clear(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()