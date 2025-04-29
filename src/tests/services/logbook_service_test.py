import unittest
import sqlite3
from services.logbook_service import LogbookService
from repositories.user_repository import UserRepository
from repositories.logbook_repository import LogbookRepository
from services.logbook_service import UsernameAlreadyInUse, WrongLoginDetails, NotLoggedIn


def init_test_db(connection):
    cursor = connection.cursor()
    cursor.execute(
        """DROP TABLE IF EXISTS users;"""
    )
    cursor.execute(
        """DROP TABLE IF EXISTS flights;"""
    )
    cursor.execute(
        """CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT
        );"""
    )
    cursor.execute(
        """CREATE TABLE flights (
            pilot TEXT,
            aircraft_type TEXT,
            aircraft_reg TEXT,
            departure TEXT,
            arrival TEXT,
            dep_time TEXT,
            arr_time TEXT
        );"""
    )
    connection.commit()


class TestLogbookService(unittest.TestCase):
    def setUp(self):
        self._connection = sqlite3.connect(':memory:')
        self._connection.row_factory = sqlite3.Row
        init_test_db(self._connection)
        self._user_repository = UserRepository(self._connection)
        self._logbook_repository = LogbookRepository(self._connection)
        self._logbook_service = LogbookService(
            self._user_repository, self._logbook_repository)

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

    def test_add_flight(self):
        test_username = "teuvo"
        test_password = "testi"

        test_flight_info = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30'
        }

        with self.assertRaises(NotLoggedIn):
            self._logbook_service.add_flight(test_flight_info)

        self._logbook_service.register_user(test_username, test_password)
        self._logbook_service.login(test_username, test_password)

        created_flight = self._logbook_service.add_flight(test_flight_info)

        self.assertEqual(test_flight_info.get('pilot'), created_flight.pilot)
        self.assertEqual(test_flight_info.get(
            'aircraft_type'), created_flight.aircraft_type)
        self.assertEqual(test_flight_info.get('aircraft_reg'),
                         created_flight.aircraft_reg)
        self.assertEqual(test_flight_info.get(
            'departure'), created_flight.departure)
        self.assertEqual(test_flight_info.get(
            'arrival'), created_flight.arrival)
        self.assertEqual(test_flight_info.get(
            'dep_time'), created_flight.dep_time)
        self.assertEqual(test_flight_info.get(
            'arr_time'), created_flight.arr_time)

    def test_get_flights_by_user(self):
        test_username = "teuvo"
        test_password = "testi"

        flight_search_empty = self._logbook_service.get_flights_by_user()
        self.assertEqual(len(flight_search_empty), 0)

        self._logbook_service.register_user(test_username, test_password)
        self._logbook_service.login(test_username, test_password)

        test_flight_info = {
            'pilot': test_username,
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30'
        }

        self._logbook_service.add_flight(test_flight_info)

        flight_search = self._logbook_service.get_flights_by_user()

        self.assertEqual(len(flight_search), 1)
        self.assertEqual(flight_search[0].pilot, test_flight_info.get('pilot'))
        self.assertEqual(
            flight_search[0].aircraft_type, test_flight_info.get('aircraft_type'))
        self.assertEqual(
            flight_search[0].aircraft_reg, test_flight_info.get('aircraft_reg'))
        self.assertEqual(flight_search[0].departure,
                         test_flight_info.get('departure'))
        self.assertEqual(flight_search[0].arrival,
                         test_flight_info.get('arrival'))
        self.assertEqual(flight_search[0].dep_time,
                         test_flight_info.get('dep_time'))
        self.assertEqual(flight_search[0].arr_time,
                         test_flight_info.get('arr_time'))
