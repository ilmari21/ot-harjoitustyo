import unittest
import sqlite3
import db


class TestDatabaseOperations(unittest.TestCase):
    def test_get_db_connection(self):
        test_connection = db.get_db_connection(':memory:')
        self.assertIsNotNone(test_connection)
        self.assertIsInstance(test_connection, sqlite3.Connection)

    def test_init_db(self):
        test_connection = db.get_db_connection(':memory:')
        db.init_db(test_connection)
        cursor = test_connection.cursor()

        try:
            cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY);")
            table_created = True
        except:
            table_created = False
        cursor.close()
        test_connection.close()

        self.assertTrue(table_created)
