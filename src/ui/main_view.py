from tkinter import ttk, constants, messagebox
import re
from services.logbook_service import NotLoggedIn
from datetime import datetime, timedelta


class MainView:
    """Class responsible for displaying the main view of the app."""

    def __init__(self, root, param_login, current_user, logbook_service):
        """Constructor of the class; creates the main view.

        Args:
            root: Tkinter root window for displaying.
            param_login: Used for changing to login view.
            current_user: The current user.
            logbook_service: Used to call the logbook_service.
        """

        self._root = root

        self._var_login = param_login
        self._current_user = current_user
        self._logbook_service = logbook_service

        self._frame = None
        self._show_flights_frame = None
        self._add_flight_frame = None

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
        """Initializes the main view UI elements."""
        self._frame = ttk.Frame(master=self._root)
        self._show_flights_frame = ttk.Frame(master=self._frame)
        self._add_flight_frame = ttk.Frame(master=self._frame)

        self._show_main_view()

    def _show_main_view(self):
        """Displays the logbook view where the added flights are listed."""
        if self._add_flight_frame:
            self._add_flight_frame.grid_remove()

        self.logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._var_login,
            width=15
        )

        self.show_add_flight_button = ttk.Button(
            master=self._frame, text="Add flight", command=self._show_add_flight, width=15)

        self.logout_button.grid(row=0, column=0, padx=10, pady=20)
        self.show_add_flight_button.grid(row=0, column=1, padx=10, pady=20)
        self._show_flights_frame.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10)
        self._update_added_flights_list()

    def _show_add_flight(self):
        """Displays the flight adding view where the a new flight can be added."""
        self._show_flights_frame.grid_remove()

        self.logout_button.grid_remove()
        self.show_add_flight_button.grid_remove()

        self.aircraft_type_label = ttk.Label(
            master=self._add_flight_frame, text="Aircraft type")
        self.aircraft_type_entry = ttk.Entry(master=self._add_flight_frame)

        self.aircraft_reg_label = ttk.Label(
            master=self._add_flight_frame, text="Aircraft registration")
        self.aircraft_reg_entry = ttk.Entry(master=self._add_flight_frame)

        self.departure_label = ttk.Label(
            master=self._add_flight_frame, text="Departure")
        self.departure_entry = ttk.Entry(master=self._add_flight_frame)

        self.arrival_label = ttk.Label(
            master=self._add_flight_frame, text="Arrival")
        self.arrival_entry = ttk.Entry(master=self._add_flight_frame)

        self.dep_time_label = ttk.Label(
            master=self._add_flight_frame, text="Departure time (HH:MM)")
        self.dep_time_entry = ttk.Entry(master=self._add_flight_frame)
        self.dep_time_entry.insert(0, "00:00")

        self.arr_time_label = ttk.Label(
            master=self._add_flight_frame, text="Arrival time (HH:MM)")
        self.arr_time_entry = ttk.Entry(master=self._add_flight_frame)
        self.arr_time_entry.insert(0, "00:00")

        self.return_button = ttk.Button(
            master=self._add_flight_frame,
            text="Return",
            command=self._show_main_view,
            width=15
        )

        self.add_flight_button = ttk.Button(
            master=self._add_flight_frame,
            text="Add flight",
            command=self._handle_add_flight,
            width=15
        )

        self.aircraft_type_label.grid(row=0, column=0, padx=10, pady=10)
        self.aircraft_type_entry.grid(row=0, column=1, padx=10, pady=10)
        self.aircraft_reg_label.grid(row=1, column=0, padx=10, pady=10)
        self.aircraft_reg_entry.grid(row=1, column=1, padx=10, pady=10)
        self.departure_label.grid(row=2, column=0, padx=10, pady=10)
        self.departure_entry.grid(row=2, column=1, padx=10, pady=10)
        self.arrival_label.grid(row=3, column=0, padx=10, pady=10)
        self.arrival_entry.grid(row=3, column=1, padx=10, pady=10)
        self.dep_time_label.grid(row=4, column=0, padx=10, pady=10)
        self.dep_time_entry.grid(row=4, column=1, padx=10, pady=10)
        self.arr_time_label.grid(row=5, column=0, padx=10, pady=10)
        self.arr_time_entry.grid(row=5, column=1, padx=10, pady=10)
        self.return_button.grid(row=6, column=0, padx=10, pady=20)
        self.add_flight_button.grid(row=6, column=1, padx=10, pady=20)
        self._add_flight_frame.grid(
            row=7, column=0, columnspan=2, padx=10, pady=10)
        self._update_added_flights_list()

    def _update_added_flights_list(self):
        """Updates the list of added flights."""
        for widget in self._show_flights_frame.winfo_children():
            widget.destroy()

        self.flights_tree = ttk.Treeview(self._show_flights_frame, columns=("Aircraft Type", "Registration", "Departure", "Arrival", "Duration", "Elapsed time"), show='headings')
        self.flights_tree.heading("Aircraft Type", text="Aircraft Type")
        self.flights_tree.heading("Registration", text="Registration")
        self.flights_tree.heading("Departure", text="Departure")
        self.flights_tree.heading("Arrival", text="Arrival")
        self.flights_tree.heading("Duration", text="Duration")
        self.flights_tree.heading("Elapsed time", text="Elapsed time")

        self.flights_tree.column("Aircraft Type", width=100, anchor='center')
        self.flights_tree.column("Registration", width=100, anchor='center')
        self.flights_tree.column("Departure", width=100, anchor='center')
        self.flights_tree.column("Arrival", width=100, anchor='center')
        self.flights_tree.column("Duration", width=100, anchor='center')
        self.flights_tree.column("Elapsed time", width=100, anchor='center')

        self.flights_tree.grid(row=0, column=0, columnspan=2, pady=5)

        total_time = 0

        flights = self._logbook_service.get_flights_by_user()
        for flight in flights:
            flight_duration = f"{flight.dep_time} - {flight.arr_time}" if flight.dep_time and flight.arr_time else "N/A"
            total_time += flight.elapsed_time
            formatted_elapsed_time = f"{int(flight.elapsed_time // 60):02}:{int(flight.elapsed_time % 60):02}"
            self.flights_tree.insert("", "end", values=(flight.aircraft_type, flight.aircraft_reg, flight.departure, flight.arrival, flight_duration, formatted_elapsed_time))

        formatted_total_time = f"{int(total_time // 60):02}:{int(total_time % 60):02}"

        ttk.Label(
            master=self._show_flights_frame,
            text=f"Total flights: {len(flights)}    Total flight time: {formatted_total_time}",
            font=("Segoe UI", 10)
        ).grid(row=len(flights) + 1, column=0, columnspan=2, padx=10, pady=2)

        # ttk.Label(
        #     master=self._show_flights_frame,
        #     text=f"Total flight time: {formatted_total_time}",
        #     font=("Segoe UI", 10)
        # ).grid(row=len(flights) + 2, column=0, columnspan=2, padx=10, pady=2)

    def _handle_add_flight(self):
        """Method responsible for the addition of a new flight."""
        aircraft_type = self.aircraft_type_entry.get()
        aircraft_reg = self.aircraft_reg_entry.get()
        departure = self.departure_entry.get()
        arrival = self.arrival_entry.get()
        dep_time = self.dep_time_entry.get()
        arr_time = self.arr_time_entry.get()

        if len(aircraft_type) != 4:
            messagebox.showinfo(
                "Error", "Enter aircraft type ICAO designator; it is exactly 4 letters")
            return

        if not aircraft_reg:
            messagebox.showinfo(
                "Error", "Enter aircraft registration")
            return

        if len(departure) != 4:
            messagebox.showinfo(
                "Error", "Enter departure airport ICAO code; it is exactly 4 letters")
            return
        if len(arrival) != 4:
            messagebox.showinfo(
                "Error", "Enter arrival airport ICAO code; it is exactly 4 letters")
            return

        if not dep_time:
            messagebox.showinfo(
                "Error", "Enter departure time")
            return
        if not arr_time:
            messagebox.showinfo(
                "Error", "Enter arrival time")
            return

        if not self._time_pattern.match(dep_time):
            messagebox.showinfo(
                "Error", "Enter departure time in HH:MM format")
            return
        if not self._time_pattern.match(arr_time):
            messagebox.showinfo(
                "Error", "Enter arrival time in HH:MM format")
            return
        
        dep_time_datetime = datetime.strptime(dep_time, "%H:%M")
        arr_time_datetime = datetime.strptime(arr_time, "%H:%M")
        if arr_time_datetime < dep_time_datetime:
            arr_time_datetime += timedelta(days=1)
        elapsed_time = (arr_time_datetime - dep_time_datetime).total_seconds() / 60

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
            self.aircraft_type_entry.delete(0, constants.END)
            self.aircraft_reg_entry.delete(0, constants.END)
            self.departure_entry.delete(0, constants.END)
            self.arrival_entry.delete(0, constants.END)
            self.dep_time_entry.delete(0, constants.END)
            self.dep_time_entry.insert(0, "00:00")
            self.arr_time_entry.delete(0, constants.END)
            self.arr_time_entry.insert(0, "00:00")
            messagebox.showinfo("Success", "Flight added!")
            self._show_main_view()
        except NotLoggedIn:
            messagebox.showinfo("Error", "No user logged in")
