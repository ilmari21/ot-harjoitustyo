from ui.login_view import LoginView
from ui.registration_view import RegistrationView
from ui.main_view import MainView
from services.logbook_service import LogbookService


class UI:
    def __init__(self, root):
        self._root = root
        self._current_user = None
        self._current_view = None
        self._logbook_service = LogbookService()

    def start(self):
        self._show_login()

    def _show_login(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = LoginView(
            self._root, self._show_registration, self._show_main, self._logbook_service)

    def _show_registration(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = RegistrationView(
            self._root, self._show_login, self._logbook_service)

    def _show_main(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_user = self._logbook_service._user.username
        self._current_view = MainView(
            self._root, self._show_login, self._current_user, self._logbook_service)
