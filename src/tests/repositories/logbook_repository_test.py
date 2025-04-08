import unittest
from repositories.logbook_repository import LogbookRepository
from entities.logbook import Flight

class TestLogbookRepository(unittest.TestCase):
    def setUp(self):
        self._logbook_repository = LogbookRepository()
        self._logbook_repository.clear()
