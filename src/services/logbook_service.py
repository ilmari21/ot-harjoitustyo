from entities.user import User
from entities.flight import Flight
from repositories.user_repository import UserRepository
from repositories.logbook_repository import LogbookRepository


class WrongLoginDetails(Exception):
    pass

class UsernameAlreadyInUse(Exception):
    pass

class NotLoggedIn(Exception):
    pass


class LogbookService():
    """Class responsible for the main services of the app."""

    def __init__(self):
        """Constructor of the class; creates the logbook service."""

        self._user = None
        self._user_repository = UserRepository()
        self._logbook_repository = LogbookRepository()

    def register_user(self, username, password):
        """Creates a new user, logs in if creation succesful.

        Args:
            username: A string depicting the username of the user.
            password: A string depicting the password of the user.

        Returns:
            Returns created User-object.
        """

        if self._user_repository.find_user(username):
            raise UsernameAlreadyInUse("Username already exists")
        user = self._user_repository.create(User(username, password))
        return user

    def login(self, username, password):
        """Logs in the user.

        Args:
            username: A string depicting the username of the user.
            password: A string depicting the password of the user.

        Returns:
            Returns True if login succesful, otherwise False.
        """

        login_user = self._user_repository.find_user(username)

        if login_user and login_user.password == password:
            self._user = login_user
            return True
        raise WrongLoginDetails("Invalid username or password")

    def add_flight(self, departure, arrival, dep_time=None, arr_time=None):
        """Creates a new logbook entry (flight).

        Args:
            departure: A string depicting the departure airport of the flight.
            arrival: A string depicting the arrival airport of the flight.
            dep_time: A string depicting the departure time of the flight.
            arr_time: A string depicting the arrival time of the flight.

        Returns:
            Returns created Flight-object, if succesful.
        """

        if not self._user:
            raise NotLoggedIn("No user logged in")
        flight = self._logbook_repository.create(
            Flight(self._user.username, departure, arrival, dep_time, arr_time))
        return flight

    def get_flights_by_user(self):
        """Returns all the flights of the user.
        
        Returns:
            Returns a list of Flight-objects added by the user.
        """

        if not self._user:
            return []
        return self._logbook_repository.find_by_user(self._user.username)
