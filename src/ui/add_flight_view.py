from tkinter import ttk, constants, messagebox
import re
from services.logbook_service import NotLoggedIn, DatabaseNotInitialized
from datetime import datetime, timedelta
from init_db import initialize_database


class AddFlightView:
    """Class responsible for displaying the flight adding view of the app."""

    def __init__(self, root, logbook_view, current_user, logbook_service):
        """Constructor of the class; creates the flight adding view.

        Args:
            root: Tkinter root window for displaying.
            logbook_view: Used for changing to logbook view.
            current_user: The current user.
            logbook_service: Used to call the logbook_service.
        """

        self._root = root

        self._logbook_view = logbook_view
        self._current_user = current_user
        self._logbook_service = logbook_service

        self._frame = None

        self._time_pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')

        self._root.minsize(400, 300)

        self._initialize()
        self.pack()

    def pack(self):
        """Displays the view."""
        self._frame.pack(fill=constants.BOTH, expand=True, padx=20, pady=20)

    def destroy(self):
        """Destroys the view."""
        self._frame.destroy()

    def _initialize(self):
        """Initializes the flight adding view UI elements."""
        self._frame = ttk.Frame(master=self._root)

        self._aircraft_type_entry = ttk.Entry(master=self._frame)
        self._aircraft_reg_entry = ttk.Entry(master=self._frame)
        self._departure_entry = ttk.Entry(master=self._frame)
        self._arrival_entry = ttk.Entry(master=self._frame)
        self._dep_time_entry = ttk.Entry(master=self._frame)
        self._dep_time_entry.insert(0, "00:00")
        self._arr_time_entry = ttk.Entry(master=self._frame)
        self._arr_time_entry.insert(0, "00:00")

        labels = [
            ("Aircraft type", self._aircraft_type_entry),
            ("Aircraft registration", self._aircraft_reg_entry),
            ("Departure", self._departure_entry),
            ("Arrival", self._arrival_entry),
            ("Departure time (HH:MM)", self._dep_time_entry),
            ("Arrival time (HH:MM)", self._arr_time_entry)
        ]

        for i, (label_text, entry) in enumerate(labels):
            label = ttk.Label(master=self._frame, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=10)
            entry.grid(row=i, column=1, padx=10, pady=10)

        self.return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._logbook_view,
            width=15
        )

        self.add_flight_button = ttk.Button(
            master=self._frame,
            text="Add flight",
            command=self._handle_add_flight,
            width=15
        )

        self.return_button.grid(row=len(labels), column=0, padx=10, pady=20)
        self.add_flight_button.grid(
            row=len(labels), column=1, padx=10, pady=20)
        self._frame.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def _handle_add_flight(self):
        """Method responsible for the addition of a new flight."""
        aircraft_type = self._aircraft_type_entry.get()
        aircraft_reg = self._aircraft_reg_entry.get()
        departure = self._departure_entry.get()
        arrival = self._arrival_entry.get()
        dep_time = self._dep_time_entry.get()
        arr_time = self._arr_time_entry.get()

        if len(aircraft_type) != 4:
            messagebox.showerror(
                "Error", "Enter aircraft type ICAO designator; it is exactly 4 letters")
            return

        if not aircraft_reg:
            messagebox.showerror(
                "Error", "Enter aircraft registration")
            return

        if len(departure) != 4:
            messagebox.showerror(
                "Error", "Enter departure airport ICAO code; it is exactly 4 letters")
            return
        if len(arrival) != 4:
            messagebox.showerror(
                "Error", "Enter arrival airport ICAO code; it is exactly 4 letters")
            return

        if not dep_time:
            messagebox.showerror(
                "Error", "Enter departure time")
            return
        if not arr_time:
            messagebox.showerror(
                "Error", "Enter arrival time")
            return

        if not self._time_pattern.match(dep_time):
            messagebox.showerror(
                "Error", "Enter departure time in HH:MM format")
            return
        if not self._time_pattern.match(arr_time):
            messagebox.showerror(
                "Error", "Enter arrival time in HH:MM format")
            return

        elapsed_time = self._get_elapsed_time(dep_time, arr_time)

        flight_info = {
            'pilot': self._current_user,
            'aircraft_type': aircraft_type,
            'aircraft_reg': aircraft_reg,
            'departure': departure,
            'arrival': arrival,
            'dep_time': dep_time,
            'arr_time': arr_time,
            'elapsed_time': elapsed_time
        }

        try:
            self._logbook_service.add_flight(flight_info)
            self._aircraft_type_entry.delete(0, constants.END)
            self._aircraft_reg_entry.delete(0, constants.END)
            self._departure_entry.delete(0, constants.END)
            self._arrival_entry.delete(0, constants.END)
            self._dep_time_entry.delete(0, constants.END)
            self._dep_time_entry.insert(0, "00:00")
            self._arr_time_entry.delete(0, constants.END)
            self._arr_time_entry.insert(0, "00:00")
            messagebox.showinfo("Success", "Flight added!")
            self._logbook_view()
        except NotLoggedIn:
            messagebox.showerror("Error", "No user logged in")
        except DatabaseNotInitialized:
            if messagebox.askyesno("Database Not Initialized", "Do you want to initialize the database?"):
                initialize_database()
            else:
                messagebox.showerror(
                    "Error", "Database has not been initialized")

    def _get_elapsed_time(self, dep_time, arr_time):
        dep_time_datetime = datetime.strptime(dep_time, "%H:%M")
        arr_time_datetime = datetime.strptime(arr_time, "%H:%M")
        if arr_time_datetime < dep_time_datetime:
            arr_time_datetime += timedelta(days=1)
        elapsed_time = (arr_time_datetime -
                        dep_time_datetime).total_seconds() / 60
        return elapsed_time
