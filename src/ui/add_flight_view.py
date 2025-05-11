from tkinter import ttk, constants, messagebox
from services.logbook_service import NotLoggedIn, DatabaseNotInitialized
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

        self._initialize_entry_fields()

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

    def _initialize_entry_fields(self):
        """Initializes the entry fields."""

        self._aircraft_type_entry = ttk.Entry(master=self._frame)
        self._aircraft_reg_entry = ttk.Entry(master=self._frame)
        self._departure_entry = ttk.Entry(master=self._frame)
        self._arrival_entry = ttk.Entry(master=self._frame)
        self._dep_time_entry = ttk.Entry(master=self._frame)
        self._dep_time_entry.insert(0, "00:00")
        self._arr_time_entry = ttk.Entry(master=self._frame)
        self._arr_time_entry.insert(0, "00:00")

    def _handle_add_flight(self):
        """Method responsible for handling the addition of a new flight."""

        if not self._validate_entries():
            return

        entries = self._get_entries()

        try:
            flight_info = self._logbook_service.create_flight_info(
                self._current_user,
                entries
            )

            self._logbook_service.add_flight(flight_info)
            self._clear_entries()
            messagebox.showinfo("Success", "Flight added!")
            self._logbook_view()
        except NotLoggedIn:
            messagebox.showerror("Error", "No user logged in")
        except DatabaseNotInitialized:
            if messagebox.askyesno("Database Not Initialized", "Do you want to initialize the database?", icon='warning'):
                initialize_database()
            else:
                messagebox.showerror(
                    "Error", "Database has not been initialized")

    def _validate_entries(self):
        """Validates the entries.

        Returns:
            Boolean; True if all the checks are passed, otherwise False.
        """

        entries = self._get_entries()

        validated, error_message = self._logbook_service.validate_flight_data(
            entries)
        if not validated:
            messagebox.showwarning("Invalid input", error_message)
            return False

        return True

    def _get_entries(self):
        """Collects the flight data entries.

        Returns:
            A dictionary containing the flight data entries.
        """

        entries = {
            "aircraft_type": self._aircraft_type_entry.get(),
            "aircraft_reg": self._aircraft_reg_entry.get(),
            "departure": self._departure_entry.get(),
            "arrival": self._arrival_entry.get(),
            "dep_time": self._dep_time_entry.get(),
            "arr_time": self._arr_time_entry.get()
        }

        return entries

    def _clear_entries(self):
        """Clears the entries."""

        self._aircraft_type_entry.delete(0, constants.END)
        self._aircraft_reg_entry.delete(0, constants.END)
        self._departure_entry.delete(0, constants.END)
        self._arrival_entry.delete(0, constants.END)
        self._dep_time_entry.delete(0, constants.END)
        self._dep_time_entry.insert(0, "00:00")
        self._arr_time_entry.delete(0, constants.END)
        self._arr_time_entry.insert(0, "00:00")
