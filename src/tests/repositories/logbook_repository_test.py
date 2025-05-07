import unittest
from init_db import initialize_database
from connect_db import get_test_database_connection
from repositories.logbook_repository import LogbookRepository
from entities.flight import Flight


class TestLogbookRepository(unittest.TestCase):
    def setUp(self):
        self._connection = get_test_database_connection()
        initialize_database(self._connection)
        self._logbook_repository = LogbookRepository(self._connection)

    def test_flight_creation(self):
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

        test_flight = Flight(test_flight_info)
        created_flight = self._logbook_repository.create(test_flight)
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

    def test_find_flights(self):
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

        test_flight = Flight(test_flight_info)
        self._logbook_repository.create(test_flight)
        flight_search = self._logbook_repository.find_by_user(
            test_flight_info['pilot'])
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

    def test_multiple_flights_creation(self):
        test_flight1_info = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30',
            'elapsed_time': 90
        }
        test_flight2_info = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFTP',
            'arrival': 'EFTU',
            'dep_time': '14:00',
            'arr_time': '15:30',
            'elapsed_time': 90
        }
        test_flight3_info = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFTP',
            'arrival': 'EFHK',
            'dep_time': '16:00',
            'arr_time': '17:30',
            'elapsed_time': 90
        }

        test_flight1 = Flight(test_flight1_info)
        test_flight2 = Flight(test_flight2_info)
        test_flight3 = Flight(test_flight3_info)
        self._logbook_repository.create(test_flight1)
        self._logbook_repository.create(test_flight2)
        self._logbook_repository.create(test_flight3)
        flight_search = self._logbook_repository.find_by_user('teuvo')
        self.assertEqual(len(flight_search), 3)

    def test_find_flights_when_none_added(self):
        flight_search = self._logbook_repository.find_by_user("teuvo")
        self.assertEqual(len(flight_search), 0)

    def test_clear_repository(self):
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

        test_flight = Flight(test_flight_info)
        self._logbook_repository.create(test_flight)
        self._logbook_repository.clear()
        flight_search = self._logbook_repository.find_by_user(
            test_flight_info['pilot'])
        self.assertEqual(len(flight_search), 0)

    def test_find_flights_invalid_username(self):
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

        test_flight = Flight(test_flight_info)
        self._logbook_repository.create(test_flight)
        flight_search = self._logbook_repository.find_by_user('kalevi')
        self.assertEqual(len(flight_search), 0)
