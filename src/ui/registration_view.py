from tkinter import ttk, constants, messagebox
from services.logbook_service import UsernameAlreadyInUse, DatabaseNotInitialized
from init_db import initialize_database


class RegistrationView:
    """Class responsible for displaying the user registration view of the app."""

    def __init__(self, root, login_view, logbook_service):
        """Constructor of the class; creates the user registration view.

        Args:
            root: Tkinter root window for displaying.
            param_login: Used for changing to login view.
            logbook_service: Used to call the logbook_service.
        """

        self._root = root
        self._login_view = login_view
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
        """Initializes the user registration view UI elements."""
        self._frame = ttk.Frame(master=self._root)

        self.username_label = ttk.Label(
            master=self._frame, text="Enter username")
        self.username_entry = ttk.Entry(master=self._frame)

        self.password_label = ttk.Label(
            master=self._frame, text="Enter password")
        self.password_entry = ttk.Entry(master=self._frame, show="*")

        self.return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._login_view,
            width=15
        )

        self.register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=self._handle_registration,
            width=15
        )

        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.return_button.grid(row=2, column=0, padx=10, pady=20)
        self.register_button.grid(row=2, column=1, padx=10, pady=20)

    def _handle_registration(self):
        """Method responsible for the registraion of a new user."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) < 5:
            messagebox.showerror("Error", "Username is too short")
            return
        if len(password) < 5:
            messagebox.showerror("Error", "Password is too short")
            return
        if username == password:
            messagebox.showerror("Error", "Username and password are same")
            return

        try:
            self._logbook_service.register_user(username, password)
            messagebox.showinfo("Success", "User created!")
            self._login_view()
        except UsernameAlreadyInUse:
            messagebox.showerror("Error", "Username already exists")
        except DatabaseNotInitialized:
            if messagebox.askyesno("Database Not Initialized", "Do you want to initialize the database?"):
                initialize_database()
            else:
                messagebox.showerror("Error", "Database has not been initialized")
