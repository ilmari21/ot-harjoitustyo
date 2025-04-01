from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, param_login, param_register):
        self._root = root
        self._var_login = param_login
        self._var_register = param_register
        self._frame = None
        self._initialize()
        self.pack()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.username_label = ttk.Label(master=self._frame, text="Username")
        self.username_entry = ttk.Entry(master=self._frame)
        
        self.password_label = ttk.Label(master=self._frame, text="Password")
        self.password_entry = ttk.Entry(master=self._frame, show="*")

        self.register_button = ttk.Button(master=self._frame, text="New user", command=self._var_register)
        self.login_button = ttk.Button(master=self._frame, text="Login", command=self.login)

        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.register_button.grid(row=2, column=0, padx=5, pady=5)
        self.login_button.grid(row=2, column=1, padx=5, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self._var_login(username, password)