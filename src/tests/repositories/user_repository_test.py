import unittest
import db
from repositories.user_repository import UserRepository
from entities.user import User
from services.logbook_service import UsernameAlreadyInUse


def init_test_db(connection):
    cursor = connection.cursor()
    cursor.execute(
        """DROP TABLE IF EXISTS users;"""
    )
    cursor.execute(
        """DROP TABLE IF EXISTS flights;"""
    )
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


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self._connection = db.get_db_test_connection()
        init_test_db(self._connection)
        self._user_repository = UserRepository(self._connection)

    def test_user_registration(self):
        test_user = User("teuvo", "testi")
        create_user = self._user_repository.create(test_user)
        self.assertEqual(test_user.username, create_user.username)
        self.assertEqual(test_user.password, create_user.password)

    # def test_user_registration_username_in_use(self):
    #     test_user = User("teuvo", "testi")
    #     self._user_repository.create(test_user)
    #     with self.assertRaises(UsernameAlreadyInUse):
    #         self._user_repository.create(test_user)

    def test_find_user(self):
        test_user = User("teuvo", "testi")
        self._user_repository.create(test_user)
        user_search = self._user_repository.find_user("teuvo")
        self.assertEqual(test_user.username, user_search.username)
        self.assertEqual(test_user.password, user_search.password)

    def test_find_not_existing_user(self):
        user_search = self._user_repository.find_user("kalevi")
        self.assertIsNone(user_search)

    def test_clear_repository(self):
        test_user = User("teuvo", "testi")
        self._user_repository.create(test_user)
        self._user_repository.clear()
        self.assertIsNone(self._user_repository.find_user("teuvo"))
