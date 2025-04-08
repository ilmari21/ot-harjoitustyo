from entities.logbook import Flight
import db


class LogbookRepository:
    def __init__(self):
        self._connection = db.get_db_connection()

    def create(self, flight):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO flights (pilot, departure, arrival) VALUES (?, ?, ?)",
            (flight.pilot, flight.departure, flight.arrival)
        )
        self._connection.commit()
        return flight

    def clear(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM flights")
        self._connection.commit()
