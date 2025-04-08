import unittest
from repositories.user_repository import UserRepository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self._user_repository = UserRepository()
        self._user_repository.clear()

    def test_user_registration(self):
        test_user = User("teuvo", "testi")
        self._user_repository.create(test_user)
        user_find = self._user_repository.find_user(test_user.username)
        self.assertEqual(test_user.username, user_find.username)
