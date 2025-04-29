from entities.flight import Flight
import db


class LogbookRepository:
    """Class responsible for the database operations of the logbook entries."""

    def __init__(self):
        """Constructor of the class."""

        self._connection = db.get_db_connection()

    def create(self, flight):
        """Adds a new logbook entry (flight) to the database.

        Args:
            flight: The flight to be added; a Flight-object.

        Returns:
            Returns the flight added; a Flight-object.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            """INSERT INTO flights (pilot, aircraft_type, aircraft_reg, departure, arrival,
                                    dep_time, arr_time)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (flight.pilot, flight.aircraft_type, flight.aircraft_reg,
             flight.departure, flight.arrival, flight.dep_time, flight.arr_time)
        )
        self._connection.commit()
        return flight

    def clear(self):
        """Deletes all entries from the database."""

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM flights")
        self._connection.commit()

    def find_by_user(self, username):
        """Finds and returns all the logbook entries of the user.

        Args:
            username: The username of the user, whose flights are being searched for.

        Returns:
            Returns a list of Flight-objects added by the user.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM flights WHERE pilot = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return [
            Flight({
                "pilot": row["pilot"],
                "aircraft_type": row["aircraft_type"],
                "aircraft_reg": row["aircraft_reg"],
                "departure": row["departure"],
                "arrival": row["arrival"],
                "dep_time": row["dep_time"],
                "arr_time": row["arr_time"]
            }) for row in rows
        ]
