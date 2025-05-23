from ui.login_view import LoginView
from ui.registration_view import RegistrationView
from ui.logbook_view import LogbookView
from ui.add_flight_view import AddFlightView


class UI:
    """Class for the user interface of the app."""

    def __init__(self, root, logbook_service):
        """Constructor of the class; creates the UI class."""

        self._root = root
        self._current_user = None
        self._current_view = None
        self._logbook_service = logbook_service

    def start(self):
        """Method for starting the UI."""
        self._show_login()

    def _show_login(self):
        """Method for displaying the login view of the app."""
        if self._current_view:
            self._current_view.destroy()
        self._current_view = LoginView(
            self._root, self._show_registration, self._show_logbook, self._logbook_service)

    def _show_registration(self):
        """Method for displaying the user registration view of the app."""
        if self._current_view:
            self._current_view.destroy()
        self._current_view = RegistrationView(
            self._root, self._show_login, self._logbook_service)

    def _show_logbook(self):
        """Method for displaying the logbook view of the app."""
        if self._current_view:
            self._current_view.destroy()
        self._current_user = self._logbook_service._user.username
        self._current_view = LogbookView(
            self._root, self._show_login, self._show_add_flight, self._current_user, self._logbook_service)

    def _show_add_flight(self):
        """Method for displaying the add flight view of the app."""
        if self._current_view:
            self._current_view.destroy()
        self._current_user = self._logbook_service._user.username
        self._current_view = AddFlightView(
            self._root, self._show_logbook, self._current_user, self._logbook_service)
