import unittest
from repositories.logbook_repository import LogbookRepository
from entities.flight import Flight


class TestLogbookRepository(unittest.TestCase):
    def setUp(self):
        self._logbook_repository = LogbookRepository()
        self._logbook_repository.clear()

    def test_flight_creation(self):
        test_flight = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30'
        }

        created_flight = self._logbook_repository.create(test_flight)
        self.assertEqual(test_flight.get('pilot'), created_flight.pilot)
        self.assertEqual(test_flight.get('aircraft_type'), created_flight.aircraft_type)
        self.assertEqual(test_flight.get('aircraft_reg'), created_flight.aircraft_reg)
        self.assertEqual(test_flight.get('departure'), created_flight.departure)
        self.assertEqual(test_flight.get('arrival'), created_flight.arrival)
        self.assertEqual(test_flight.get('dep_time'), created_flight.dep_time)
        self.assertEqual(test_flight.get('arr_time'), created_flight.arr_time)

    def test_find_flights(self):
        test_flight = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30'
        }

        self._logbook_repository.create(test_flight)
        flight_search = self._logbook_repository.find_by_user(
            test_flight.pilot)
        self.assertEqual(len(flight_search), 1)
        self.assertEqual(flight_search[0].pilot, test_flight.get('pilot'))
        self.assertEqual(flight_search[0].aircraft_type, test_flight.get('aircraft_type'))
        self.assertEqual(flight_search[0].aircraft_reg, test_flight.get('aircraft_reg'))
        self.assertEqual(flight_search[0].departure, test_flight.get('departure'))
        self.assertEqual(flight_search[0].arrival, test_flight.get('arrival'))
        self.assertEqual(flight_search[0].dep_time, test_flight.get('dep_time'))
        self.assertEqual(flight_search[0].arr_time, test_flight.get('arr_time'))

    def test_find_flights_when_none_added(self):
        flight_search = self._logbook_repository.find_by_user("teuvo")
        self.assertEqual(len(flight_search), 0)

    def test_clear_repository(self):
        test_flight = {
            'pilot': 'teuvo',
            'aircraft_type': 'C152',
            'aircraft_reg': 'OH-TKT',
            'departure': 'EFHK',
            'arrival': 'EFTP',
            'dep_time': '12:00',
            'arr_time': '13:30'
        }

        self._logbook_repository.create(test_flight)
        self._logbook_repository.clear()
        flight_search = self._logbook_repository.find_by_user(
            test_flight.get('pilot'))
        self.assertEqual(len(flight_search), 0)
