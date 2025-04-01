import unittest
from tkinter import Tk
from ui.login_view import LoginView

class TestLoginView(unittest.TestCase):
    def setUp(self):
        self._root = Tk()        
        self._login_tested = False
        self._login_view = LoginView(self._root, self._login_for_testing, self._register_for_testing)

    def _login_for_testing(self, username, password):
        self._login_tested = True
        self._login_username = username
        self._login_password = password

    def _register_for_testing(self):
        pass

    def test_if_login_view_exists(self):
        self.assertNotEqual(self._login_view, None)

    def test_if_login_works(self):
        username = "username"
        password = "password"

        self._login_view.username_entry.insert(0, username)
        self._login_view.password_entry.insert(0, password)
        self._login_view.login()

        self.assertEqual(self._login_username, username)
        self.assertEqual(self._login_password, password)