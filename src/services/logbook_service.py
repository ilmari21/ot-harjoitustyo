from sqlite3 import OperationalError
import re
from datetime import datetime, timedelta
from entities.user import User
from entities.flight import Flight


class WrongLoginDetails(Exception):
    pass


class UsernameAlreadyInUse(Exception):
    pass


class NotLoggedIn(Exception):
    pass


class DatabaseNotInitialized(Exception):
    pass


class LogbookService():
    """Class responsible for the main services of the app."""

    def __init__(self, logbook_repository, user_repository):
        """Constructor of the class; creates the logbook service.

        Args:
            user_repository: The user repository.
            logbook_repository: The logbook repository.
        """

        self._logbook_repository = logbook_repository
        self._user_repository = user_repository
        self._user = None

        self._time_pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')

    def register_user(self, username, password):
        """Creates a new user.

        Args:
            username: A string depicting the username of the user.
            password: A string depicting the password of the user.

        Returns:
            Created User-object, if succesful.
        """

        try:
            if self._user_repository.find_user(username):
                raise UsernameAlreadyInUse("Username already exists")
            user = self._user_repository.create(User(username, password))
            return user
        except OperationalError as error:
            raise DatabaseNotInitialized(
                "Database has not been initialized") from error

    def login(self, username, password):
        """Logs in the user.

        Args:
            username: A string depicting the username of the user.
            password: A string depicting the password of the user.

        Returns:
            Boolean; True if login succesful, otherwise False.
        """

        try:
            login_user = self._user_repository.find_user(username)
            if login_user and login_user.password == password:
                self._user = login_user
                return True
            raise WrongLoginDetails("Invalid username or password")
        except OperationalError as error:
            raise DatabaseNotInitialized(
                "Database has not been initialized") from error

    def logout(self):
        """Logs out the user."""

        self._user = None

    def add_flight(self, flight_info):
        """Creates a new logbook entry (flight).

        Args:
            flight_info: A dictionary containing the flight information.

        Returns:
            Created Flight-object, if succesful.
        """

        try:
            if not self._user:
                raise NotLoggedIn("No user logged in")
            flight = self._logbook_repository.create(
                Flight(flight_info))
            return flight
        except OperationalError as error:
            raise DatabaseNotInitialized(
                "Database has not been initialized") from error

    def get_flights_by_user(self):
        """Returns all the flights of the user.

        Returns:
            A list of Flight-objects added by the user.
        """

        try:
            if not self._user:
                return []
            return self._logbook_repository.find_by_user(self._user.username)
        except OperationalError as error:
            raise DatabaseNotInitialized(
                "Database has not been initialized") from error

    def _calculate_elapsed_time(self, dep_time, arr_time):
        """Calculates the elapsed time between departure and arrival.

        Args:
            dep_time: A string depicting the departure time.
            arr_time: A string depicting the arrival time.

        Returns:
           Elapsed time integer in minutes.
        """

        dep_time_datetime = datetime.strptime(dep_time, "%H:%M")
        arr_time_datetime = datetime.strptime(arr_time, "%H:%M")
        if arr_time_datetime < dep_time_datetime:
            arr_time_datetime += timedelta(days=1)
        return (arr_time_datetime - dep_time_datetime).total_seconds() / 60

    def validate_flight_data(self, entries):
        """Validates flight data according to business rules.

        Args:
            entries: A dictionary containing the flight data.

        Returns:
            A tuple consisting of boolean and the possible error message.
        """

        if len(entries.get('aircraft_type', '')) != 4:
            return False, "Enter aircraft type ICAO designator; it is exactly 4 letters"

        if not entries.get('aircraft_reg', ''):
            return False, "Enter aircraft registration"

        if len(entries.get('departure', '')) != 4:
            return False, "Enter departure airport ICAO code; it is exactly 4 letters"

        if len(entries.get('arrival', '')) != 4:
            return False, "Enter arrival airport ICAO code; it is exactly 4 letters"

        if not self._time_pattern.match(entries.get('dep_time', '')):
            return False, "Enter departure time in HH:MM format"

        if not self._time_pattern.match(entries.get('arr_time', '')):
            return False, "Enter arrival time in HH:MM format"

        return True, ""

    def create_flight_info(self, pilot, entries):
        """Creates a flight info dictionary with all necessary data.

        Args:
            pilot: The pilot's username
            entries: Dictionary containing flight data entries.

        Returns:
            A dictionary containing all flight information, including pilot and elapsed time.
        """

        elapsed_time = self._calculate_elapsed_time(
            entries.get('dep_time', ''),
            entries.get('arr_time', '')
        )

        return {
            'pilot': pilot,
            'aircraft_type': entries.get('aircraft_type', ''),
            'aircraft_reg': entries.get('aircraft_reg', ''),
            'departure': entries.get('departure', ''),
            'arrival': entries.get('arrival', ''),
            'dep_time': entries.get('dep_time', ''),
            'arr_time': entries.get('arr_time', ''),
            'elapsed_time': elapsed_time
        }

    def validate_credentials(self, username, password):
        """Validates the user credentials.

        Args:
            username: A string depicting the username of the user.
            password: A string depicting the password of the user.

        Returns:
            A tuple consisting of boolean and the possible error message.
        """

        if len(username) < 5:
            return False, "Username is too short"

        if len(password) < 5:
            return False, "Password is too short"

        if username == password:
            return False, "Username and password are same"

        return True, ""

    def format_elapsed_time(self, minutes):
        """Formats elapsed time in minutes to HH:MM format.

        Args:
            minutes: elapsed time in minutes.

        Returns:
            Elapsed time string in HH:MM format.
        """

        return f"{int(minutes // 60):02}:{int(minutes % 60):02}"

    def get_statistics(self):
        """Get flight statistics for the current user.

        Returns:
            A dictionary containing total flights and formatted total time.
        """

        flights = self.get_flights_by_user()
        total_time = sum(flight.elapsed_time for flight in flights)

        return {
            'total_flights': len(flights),
            'formatted_total_time': self.format_elapsed_time(total_time)
        }
