from entities.logbook import Flight
import db


class LogbookRepository:
    def __init__(self):
        self._connection = db.get_db_connection()

    def create(self, flight):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO flights (pilot, departure, arrival, dep_time, arr_time) VALUES (?, ?, ?, ?, ?)",
            (flight.pilot, flight.departure, flight.arrival,
             flight.dep_time, flight.arr_time)
        )
        self._connection.commit()
        return flight

    def clear(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM flights")
        self._connection.commit()

    def find_by_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM flights WHERE pilot = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return [Flight(row["pilot"], row["departure"], row["arrival"], row["dep_time"], row["arr_time"]) for row in rows]
