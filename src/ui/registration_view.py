from tkinter import ttk, constants


class RegistrationView:
    def __init__(self, root, param_login, logbook_service):
        self._root = root
        self._var_login = param_login
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

        self.username_label = ttk.Label(
            master=self._frame, text="Enter username")
        self.username_entry = ttk.Entry(master=self._frame)

        self.password_label = ttk.Label(
            master=self._frame, text="Enter password")
        self.password_entry = ttk.Entry(master=self._frame, show="*")

        self.return_button = ttk.Button(
            master=self._frame, text="Return", command=self._var_login)
        self.register_button = ttk.Button(
            master=self._frame, text="Register", command=self._handle_registration)

        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.return_button.grid(row=2, column=0, padx=5, pady=5)
        self.register_button.grid(row=2, column=1, padx=5, pady=5)

    def _handle_registration(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) < 5:
            print("error: username too short")
            return
        if len(password) < 5:
            print("error: password too short")
            return
        if username == password:
            print("error: username and password are same")
            return

        self._logbook_service.register_user(username, password)
        self._var_login()
