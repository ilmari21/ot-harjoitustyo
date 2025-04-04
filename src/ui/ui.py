from ui.login_view import LoginView
from ui.registration_view import RegistrationView


class UI:
    def __init__(self, root):
        self._root = root
        self._users = {}
        self._current_user = None
        self._current_view = None

    def start(self):
        self._show_login()

    def _show_login(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = LoginView(
            self._root, self._handle_login, self._show_registration)

    def _show_registration(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = RegistrationView(
            self._root, self._handle_registration, self._show_login)

    def _show_main(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None  # WIP

    def _handle_login(self, username, password):
        if username in self._users and self._users[username] == password:
            self._current_user = username
            print("login succesful")
            self._show_main()
        else:
            print("login failed")

    def _handle_registration(self, username, password):
        if username in self._users:
            print("error: username already exists")
            return
        if username == password:
            print("error: username and password are same")
            return
        if len(username) < 5:
            print("error: username too short")
            return
        if len(password) < 5:
            print("error: password too short")

        self._users[username] = password
        print("usernames:")
        for i in self._users:
            print(i)
        self._show_login()
