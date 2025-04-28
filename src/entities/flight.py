class Flight:
    """Flight class."""

    def __init__(self, pilot, aircraft_type, aircraft_reg, departure, arrival, dep_time=None, arr_time=None):
        """Constructor of the class; creates a new Flight-object.

        Args:
            pilot: A string depicting the username of the pilot.
            aircraft_type: A string depicting the aircraft type.
            aircraft_reg: A string depicting the aircraft registration.
            departure: A string depicting the departure airport of the flight.
            arrival: A string depicting the arrival airport of the flight.
            dep_time: A string depicting the departure time of the flight.
            arr_time: A string depicting the arrival time of the flight.
        """

        self.pilot = pilot
        self.aircraft_type = aircraft_type
        self.aircraft_reg = aircraft_reg
        self.departure = departure
        self.arrival = arrival
        self.dep_time = dep_time
        self.arr_time = arr_time
