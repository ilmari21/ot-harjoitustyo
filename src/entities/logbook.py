class Flight:
    def __init__(self, pilot, departure, arrival, dep_time=None, arr_time=None):
        self.pilot = pilot
        self.departure = departure
        self.arrival = arrival
        self.dep_time = dep_time
        self.arr_time = arr_time
