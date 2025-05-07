import unittest
from init_services import initialize_services
from services.logbook_service import LogbookService


class TestInitService(unittest.TestCase):
    def test_initialize_services(self):
        test_logbook_service = initialize_services()
        self.assertIsInstance(test_logbook_service, LogbookService)
