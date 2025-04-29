import unittest
import sqlite3
import db


class TestDatabaseOperations(unittest.TestCase):
    def test_get_db_connection(self):
        test_connection = db.get_db_connection()
        self.assertIsNotNone(test_connection)
        self.assertIsInstance(test_connection, sqlite3.Connection)
