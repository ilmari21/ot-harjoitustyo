from tkinter import Tk
import sv_ttk
from ui.ui import UI
from init_services import initialize_services


def main():
    window = Tk()
    window.title("Virtual logbook")

    sv_ttk.set_theme("dark")

    logbook_service = initialize_services()

    ui = UI(window, logbook_service)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
