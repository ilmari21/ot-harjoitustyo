import unittest
from repositories.user_repository import UserRepository
from entities.user import User

def setUp(self):
    self._user_repository = UserRepository()

def test_user_registration(self):
    test_user = User("teuvo", "testi")
    self._user_repository.add_user(test_user)
    user_find = self._user_repository.find_user(test_user.username)
    self.assertEqual(test_user, user_find)