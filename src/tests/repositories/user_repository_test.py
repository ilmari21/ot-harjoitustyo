import unittest
from init_db import initialize_database
from connect_db import get_test_database_connection
from repositories.user_repository import UserRepository, DatabaseNotInitialized
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self._connection = get_test_database_connection()
        initialize_database(self._connection)
        self._user_repository = UserRepository(self._connection)

    def test_user_registration(self):
        test_user = User("teuvo", "testi")
        create_user = self._user_repository.create(test_user)
        self.assertEqual(test_user.username, create_user.username)
        self.assertEqual(test_user.password, create_user.password)

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

    def test_user_registration_database_not_initialized(self):
        test_repository = UserRepository(get_test_database_connection())

        with self.assertRaises(DatabaseNotInitialized):
            test_repository.create(User("teuvo", "testi"))

    def test_find_user_database_not_initialized(self):
        test_repository = UserRepository(get_test_database_connection())

        with self.assertRaises(DatabaseNotInitialized):
            test_repository.find_user("teuvo")

    def test_clear_database_not_initialized(self):
        test_repository = UserRepository(get_test_database_connection())

        with self.assertRaises(DatabaseNotInitialized):
            test_repository.clear()
