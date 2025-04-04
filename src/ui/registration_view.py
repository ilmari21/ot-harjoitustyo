from tkinter import ttk, constants


class RegistrationView:
    def __init__(self, root, param_register, go_back):
        self._root = root
        self._var_register = param_register
        self._go_back = go_back
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
            master=self._frame, text="Return", command=self._go_back)
        self.register_button = ttk.Button(
            master=self._frame, text="Register", command=self.register)

        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.return_button.grid(row=2, column=0, padx=5, pady=5)
        self.register_button.grid(row=2, column=1, padx=5, pady=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self._var_register(username, password)
