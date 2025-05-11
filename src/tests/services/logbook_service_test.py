import unittest
from init_db import initialize_database
from connect_db import get_test_database_connection
from services.logbook_service import LogbookService
from repositories.logbook_repository import LogbookRepository
from repositories.user_repository import UserRepository
from services.logbook_service import UsernameAlreadyInUse, WrongLoginDetails, NotLoggedIn, DatabaseNotInitialized
from entities.user import User


class TestLogbookService(unittest.TestCase):
    def setUp(self):
        self._connection = get_test_database_connection()
        initialize_database(self._connection)
        self._logbook_repository = LogbookRepository(self._connection)
        self._user_repository = UserRepository(self._connection)
        self._logbook_service = LogbookService(
            self._logbook_repository, self._user_repository)

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

    def test_user_logout(self):
        test_username = "teuvo"
        test_password = "testi"

        self._logbook_service.register_user(test_username, test_password)

        self._logbook_service.login(test_username, test_password)

        self._logbook_service.logout()
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
            'arr_time': '13:30',
            'elapsed_time': 90
        }

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
        self.assertEqual(test_flight_info.get(
            'elapsed_time'), created_flight.elapsed_time)

    def test_add_flight_not_logged_in(self):
        test_flight_info = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30',
            'elapsed_time': 90
        }

        with self.assertRaises(NotLoggedIn):
            self._logbook_service.add_flight(test_flight_info)

    def test_get_flights_by_user(self):
        test_username = "teuvo"
        test_password = "testi"

        flight_search_empty = self._logbook_service.get_flights_by_user()
        self.assertEqual(len(flight_search_empty), 0)

        self._logbook_service.register_user(test_username, test_password)
        self._logbook_service.login(test_username, test_password)

        test_flight_info = {
            'pilot': test_username,
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30',
            'elapsed_time': 90
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
        self.assertEqual(flight_search[0].elapsed_time,
                         test_flight_info.get('elapsed_time'))

    def test_user_login_database_not_initialized(self):
        test_username = "teuvo"
        test_password = "testi"

        test_connection = get_test_database_connection()

        test_logbook_repository = LogbookRepository(test_connection)
        test_user_repository = UserRepository(test_connection)
        test_logbook_service = LogbookService(
            test_logbook_repository, test_user_repository)

        with self.assertRaises(DatabaseNotInitialized):
            test_logbook_service.login(test_username, test_password)

    def test_user_registration_database_not_initialized(self):
        test_username = "teuvo"
        test_password = "testi"

        test_connection = get_test_database_connection()

        test_logbook_repository = LogbookRepository(test_connection)
        test_user_repository = UserRepository(test_connection)
        test_logbook_service = LogbookService(
            test_logbook_repository, test_user_repository)

        with self.assertRaises(DatabaseNotInitialized):
            test_logbook_service.register_user(test_username, test_password)

    def test_add_flight_database_not_initialized(self):
        test_flight_info = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30',
            'elapsed_time': 90
        }

        test_connection = get_test_database_connection()

        test_logbook_repository = LogbookRepository(test_connection)
        test_user_repository = UserRepository(test_connection)
        test_logbook_service = LogbookService(
            test_logbook_repository, test_user_repository)

        test_logbook_service._user = User("teuvo", "testi")

        with self.assertRaises(DatabaseNotInitialized):
            test_logbook_service.add_flight(test_flight_info)

    def test_get_flights_by_user_database_not_initialized(self):
        test_connection = get_test_database_connection()

        test_logbook_repository = LogbookRepository(test_connection)
        test_user_repository = UserRepository(test_connection)
        test_logbook_service = LogbookService(
            test_logbook_repository, test_user_repository)

        test_logbook_service._user = User("teuvo", "testi")

        with self.assertRaises(DatabaseNotInitialized):
            test_logbook_service.get_flights_by_user()

    def test_calculate_elapsed_time(self):
        test_elapsed_time = self._logbook_service._calculate_elapsed_time(
            "12:00", "13:30")

        self.assertEqual(test_elapsed_time, 90)

    def test_calculate_elapsed_time_overnight(self):
        test_elapsed_time = self._logbook_service._calculate_elapsed_time(
            "23:00", "01:00")

        self.assertEqual(test_elapsed_time, 120)

    def test_validate_flight_data_valid(self):
        test_entries = {
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '14:00'
        }

        validated, error_message = self._logbook_service.validate_flight_data(
            test_entries)
        self.assertTrue(validated)
        self.assertEqual(error_message, "")

    def test_validate_flight_data_invalid_aircraft_type(self):
        test_entries = {
            'aircraft_type': 'Cessna',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '14:00'
        }

        validated, error_message = self._logbook_service.validate_flight_data(
            test_entries)
        self.assertFalse(validated)
        self.assertEqual(
            error_message, "Enter aircraft type ICAO designator; it is exactly 4 letters")

    def test_validate_flight_data_invalid_aircraft_registration(self):
        test_entries = {
            'aircraft_type': 'C152',
            'aircraft_reg': '',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '14:00'
        }

        validated, error_message = self._logbook_service.validate_flight_data(
            test_entries)
        self.assertFalse(validated)
        self.assertEqual(error_message, "Enter aircraft registration")

    def test_validate_flight_data_invalid_departure(self):
        test_entries = {
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'HEL',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '14:00'
        }

        validated, error_message = self._logbook_service.validate_flight_data(
            test_entries)
        self.assertFalse(validated)
        self.assertEqual(
            error_message, "Enter departure airport ICAO code; it is exactly 4 letters")

    def test_validate_flight_data_invalid_arrival(self):
        test_entries = {
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'Tampere',
            'dep_time': '12:00',
            'arr_time': '14:00'
        }

        validated, error_message = self._logbook_service.validate_flight_data(
            test_entries)
        self.assertFalse(validated)
        self.assertEqual(
            error_message, "Enter arrival airport ICAO code; it is exactly 4 letters")

    def test_validate_flight_data_invalid_departure_time(self):
        test_entries = {
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:60',
            'arr_time': '14:00'
        }

        validated, error_message = self._logbook_service.validate_flight_data(
            test_entries)
        self.assertFalse(validated)
        self.assertEqual(error_message, "Enter departure time in HH:MM format")

    def test_validate_flight_data_invalid_arrival_time(self):
        test_entries = {
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '24:00'
        }

        validated, error_message = self._logbook_service.validate_flight_data(
            test_entries)
        self.assertFalse(validated)
        self.assertEqual(error_message, "Enter arrival time in HH:MM format")

    def test_create_flight_info(self):
        test_entries = {
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '14:00'
        }

        test_pilot = "teuvo"
        test_flight_info = self._logbook_service.create_flight_info(
            test_pilot, test_entries)

        self.assertEqual(test_flight_info['pilot'], test_pilot)
        self.assertEqual(
            test_flight_info['aircraft_type'], test_entries['aircraft_type'])
        self.assertEqual(
            test_flight_info['aircraft_reg'], test_entries['aircraft_reg'])
        self.assertEqual(
            test_flight_info['departure'], test_entries['departure'])
        self.assertEqual(test_flight_info['arrival'], test_entries['arrival'])
        self.assertEqual(
            test_flight_info['dep_time'], test_entries['dep_time'])
        self.assertEqual(
            test_flight_info['arr_time'], test_entries['arr_time'])
        self.assertEqual(test_flight_info['elapsed_time'], 120)

    def test_validate_credentials(self):
        test_username = "teuvo"
        test_password = "testi"

        validated, error_message = self._logbook_service.validate_credentials(
            test_username, test_password)
        self.assertTrue(validated)
        self.assertEqual(error_message, "")

    def test_validate_credentials_username_too_short(self):
        test_username = "tepi"
        test_password = "testi"

        validated, error_message = self._logbook_service.validate_credentials(
            test_username, test_password)
        self.assertFalse(validated)
        self.assertEqual(error_message, "Username is too short")

    def test_validate_credentials_password_too_short(self):
        test_username = "teuvo"
        test_password = "tepi"

        validated, error_message = self._logbook_service.validate_credentials(
            test_username, test_password)
        self.assertFalse(validated)
        self.assertEqual(error_message, "Password is too short")

    def test_validate_credentials_same_username_password(self):
        test_username = "teuvo"
        test_password = "teuvo"

        validated, error_message = self._logbook_service.validate_credentials(
            test_username, test_password)
        self.assertFalse(validated)
        self.assertEqual(error_message, "Username and password are same")

    def test_format_elapsed_time(self):
        test_formatted_time = self._logbook_service.format_elapsed_time(0)
        self.assertEqual(test_formatted_time, "00:00")

        test_formatted_time = self._logbook_service.format_elapsed_time(30)
        self.assertEqual(test_formatted_time, "00:30")

        test_formatted_time = self._logbook_service.format_elapsed_time(60)
        self.assertEqual(test_formatted_time, "01:00")

    def test_get_statistics(self):
        test_username = "teuvo"
        test_password = "testi"
        self._logbook_service.register_user(test_username, test_password)
        self._logbook_service.login(test_username, test_password)

        test_flights = [
            {
                'pilot': test_username,
                'aircraft_type': 'C152',
                'aircraft_reg': 'OH-ABC',
                'departure': 'EFHK',
                'arrival': 'EFTU',
                'dep_time': '12:00',
                'arr_time': '13:30',
                'elapsed_time': 90
            },
            {
                'pilot': test_username,
                'aircraft_type': 'C172',
                'aircraft_reg': 'OH-XYZ',
                'departure': 'EFTU',
                'arrival': 'EFHK',
                'dep_time': '14:00',
                'arr_time': '15:00',
                'elapsed_time': 60
            }
        ]

        for flight in test_flights:
            self._logbook_service.add_flight(flight)

        stats = self._logbook_service.get_statistics()

        self.assertEqual(stats['total_flights'], 2)
        self.assertEqual(stats['formatted_total_time'], "02:30")
