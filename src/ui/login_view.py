from tkinter import ttk, constants, messagebox
from services.logbook_service import WrongLoginDetails, DatabaseNotInitialized
from init_db import initialize_database


class LoginView:
    """Class responsible for displaying the login view of the app."""

    def __init__(self, root, registration_view, logbook_view, logbook_service):
        """Constructor of the class; creates the login view.

        Args:
            root: Tkinter root window for displaying.
            registration_view: Used for changing to user registration view.
            logbook_view: Used for changing to logbook view.
            logbook_service: Used to call the logbook_service.
        """

        self._root = root
        self._registration_view = registration_view
        self._logbook_view = logbook_view
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
        """Initializes the login view UI elements."""

        self._frame = ttk.Frame(master=self._root)

        self._initialize_entry_fields()

        register_button = ttk.Button(
            master=self._frame,
            text="New user",
            command=self._registration_view,
            width=15
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_login,
            width=15
        )

        register_button.grid(row=2, column=0, padx=10, pady=20)
        login_button.grid(row=2, column=1, padx=10, pady=20)

    def _initialize_entry_fields(self):
        """Initializes the entry fields."""

        self._username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        self._password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        self._username_label.grid(row=0, column=0, padx=10, pady=10)
        self._username_entry.grid(row=0, column=1, padx=10, pady=10)
        self._password_label.grid(row=1, column=0, padx=10, pady=10)
        self._password_entry.grid(row=1, column=1, padx=10, pady=10)

    def _handle_login(self):
        """Method responsible for handling the login attempt."""

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            self._logbook_service.login(username, password)
            self._logbook_view()
        except WrongLoginDetails:
            self._password_entry.delete(0, constants.END)
            messagebox.showerror("Error", "Invalid username or password")
        except DatabaseNotInitialized:
            if messagebox.askyesno("Database Not Initialized", "Do you want to initialize the database?", icon='warning'):
                initialize_database()
            else:
                messagebox.showerror(
                    "Error", "Database has not been initialized")
