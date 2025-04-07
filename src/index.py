from tkinter import Tk
from ui.ui import UI
from db import init_db


def main():
    window = Tk()
    window.title("Virtual logbook")

    ui = UI(window)
    ui.start()

    # init_db()

    window.mainloop()


if __name__ == "__main__":
    main()
