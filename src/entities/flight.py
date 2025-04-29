class Flight:
    """Flight class."""

    def __init__(self, flight_info):
        """Constructor of the class; creates a new Flight-object.

        Args:
            flight_info: A dictionary containing the flight information.
        """

        self.pilot = flight_info.get('pilot')
        self.aircraft_type = flight_info.get('aircraft_type')
        self.aircraft_reg = flight_info.get('aircraft_reg')
        self.departure = flight_info.get('departure')
        self.arrival = flight_info.get('arrival')
        self.dep_time = flight_info.get('dep_time')
        self.arr_time = flight_info.get('arr_time')
