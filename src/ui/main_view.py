from tkinter import ttk, constants
from services.logbook_service import LogbookService


class MainView:
    def __init__(self, root, param_login):
        self._root = root
        self._var_login = param_login
        self._logbook_service = LogbookService()
        self._frame = None
        self._initialize()
        self.pack()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.username_label = ttk.Label(master=self._frame, text="WIP")

        self.username_label.grid(row=0, column=0, padx=5, pady=5)
