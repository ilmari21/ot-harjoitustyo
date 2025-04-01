import unittest
from tkinter import Tk
from ui.login_view import LoginView

class TestLoginView(unittest.TestCase):
    def setUp(self):
        self._root = Tk()
        self._login_view = LoginView(self._root, self._login_for_testing, self._register_for_testing)

    def _login_for_testing(self, username, password):
        pass

    def _register_for_testing(self):
        pass

    def test_if_login_view_exists(self):
        self.assertNotEqual(self._login_view, None)