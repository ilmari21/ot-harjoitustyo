from tkinter import Tk
from ui.ui import UI
from init_services import initialize_services


def main():
    window = Tk()
    window.title("Virtual logbook")

    logbook_service = initialize_services()

    ui = UI(window, logbook_service)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
