from tkinter import ttk, constants
import re


class LogbookView:
    """Class responsible for displaying the main view of the app."""

    def __init__(self, root, login_view, add_flight_view, current_user, logbook_service):
        """Constructor of the class; creates the main view.

        Args:
            root: Tkinter root window for displaying.
            param_login: Used for changing to login view.
            current_user: The current user.
            logbook_service: Used to call the logbook_service.
        """

        self._root = root

        self._login_view = login_view
        self._add_flight_view = add_flight_view
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
        """Initializes the logbook view UI elements."""
        self._frame = ttk.Frame(master=self._root)
        self._added_flight_list_frame = ttk.Frame(self._frame)

        self.logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._login_view,
            width=15
        )

        self.show_add_flight_button = ttk.Button(
            master=self._frame, text="Add flight", command=self._add_flight_view, width=15)

        self.logout_button.grid(row=0, column=0, padx=10, pady=20)
        self.show_add_flight_button.grid(row=0, column=1, padx=10, pady=20)
        self._frame.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10)
        self._added_flight_list_frame.grid(
            row=1, column=0, columnspan=2, pady=5)
        self._update_added_flights_list()

    def _update_added_flights_list(self):
        """Updates the list of added flights."""
        for widget in self._added_flight_list_frame.winfo_children():
            widget.destroy()

        self.flights_tree = ttk.Treeview(self._added_flight_list_frame, columns=(
            "Aircraft Type", "Registration", "Departure", "Arrival", "Duration", "Elapsed time"), show='headings')
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
            self.flights_tree.insert("", "end", values=(flight.aircraft_type, flight.aircraft_reg,
                                     flight.departure, flight.arrival, flight_duration, formatted_elapsed_time))

        formatted_total_time = f"{int(total_time // 60):02}:{int(total_time % 60):02}"

        ttk.Label(
            master=self._frame,
            text=f"Total flights: {len(flights)}    Total flight time: {formatted_total_time}",
            font=("Segoe UI", 10)
        ).grid(row=len(flights) + 1, column=0, columnspan=2, padx=10, pady=2)
