from tkinter import ttk, constants


class MainView:
    def __init__(self, root, param_login, current_user, logbook_service):
        self._root = root
        self._var_login = param_login
        self._current_user = current_user
        self._logbook_service = logbook_service
        self._frame = None
        self._initialize()
        self.pack()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.departure_label = ttk.Label(
            master=self._frame, text="Enter departure")
        self.departure_entry = ttk.Entry(master=self._frame)

        self.arrival_label = ttk.Label(
            master=self._frame, text="Enter arrival")
        self.arrival_entry = ttk.Entry(master=self._frame)

        self.return_button = ttk.Button(
            master=self._frame, text="Logout", command=self._var_login)
        self.register_button = ttk.Button(
            master=self._frame, text="Add", command=self._handle_add_flight)

        self.departure_label.grid(row=0, column=0, padx=5, pady=5)
        self.departure_entry.grid(row=0, column=1, padx=5, pady=5)
        self.arrival_label.grid(row=1, column=0, padx=5, pady=5)
        self.arrival_entry.grid(row=1, column=1, padx=5, pady=5)
        self.return_button.grid(row=2, column=0, padx=5, pady=5)
        self.register_button.grid(row=2, column=1, padx=5, pady=5)

    def _handle_add_flight(self):
        departure = self.departure_entry.get()
        arrival = self.arrival_entry.get()

        if len(departure) != 4:
            print("error: ICAO code is exactly 4 letters")
            return
        if len(arrival) != 4:
            print("error: ICAO code is exactly 4 letters")
            return

        self._logbook_service.add_flight(departure, arrival)
        self.departure_entry.delete(0, constants.END)
        self.arrival_entry.delete(0, constants.END)
        print("Flight added!")
