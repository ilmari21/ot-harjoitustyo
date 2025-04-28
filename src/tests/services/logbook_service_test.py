import unittest
from services.logbook_service import LogbookService
from repositories.user_repository import UserRepository
from repositories.logbook_repository import LogbookRepository
from services.logbook_service import UsernameAlreadyInUse, WrongLoginDetails


class TestLogbookService(unittest.TestCase):
    def setUp(self):
        self._logbook_service = LogbookService()
        self._user_repository = UserRepository()
        self._logbook_repository = LogbookRepository()
        self._logbook_service._user_repository = self._user_repository
        self._logbook_service._logbook_repository = self._logbook_repository
        self._user_repository.clear()
        self._logbook_repository.clear()

    def test_user_registration(self):
        test_username = "teuvo"
        test_password = "testi"

        created_user = self._logbook_service.register_user(
            test_username, test_password)

        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.username, test_username)
        self.assertEqual(created_user.password, test_password)

        user_search = self._user_repository.find_user(test_username)
        self.assertIsNotNone(user_search)
        self.assertEqual(user_search.username, test_username)
        self.assertEqual(user_search.password, test_password)

    def test_user_registration_username_already_exists(self):
        test_username = "teuvo"
        test_password = "testi"

        self._logbook_service.register_user(test_username, test_password)

        with self.assertRaises(UsernameAlreadyInUse):
            self._logbook_service.register_user(test_username, "teppo")

        user_search = self._user_repository.find_user(test_username)
        self.assertIsNotNone(user_search)
        self.assertEqual(user_search.password, test_password)

    def test_user_login(self):
        test_username = "teuvo"
        test_password = "testi"

        self._logbook_service.register_user(test_username, test_password)

        test_login = self._logbook_service.login(test_username, test_password)

        self.assertTrue(test_login)
        self.assertIsNotNone(self._logbook_service._user)
        self.assertEqual(self._logbook_service._user.username, test_username)

    def test_user_login_wrong_password(self):
        test_username = "teuvo"
        test_password = "testi"

        self._logbook_service.register_user(test_username, test_password)

        with self.assertRaises(WrongLoginDetails):
            self._logbook_service.login(test_username, "teppo")

        self.assertIsNone(self._logbook_service._user)
