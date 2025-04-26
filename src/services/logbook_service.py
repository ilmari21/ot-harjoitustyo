from tkinter import messagebox
from entities.user import User
from entities.flight import Flight
from repositories.user_repository import UserRepository
from repositories.logbook_repository import LogbookRepository


class LogbookService():
    def __init__(self):
        self._user = None
        self._user_repository = UserRepository()
        self._logbook_repository = LogbookRepository()

    def register_user(self, username, password):
        if self._user_repository.find_user(username):
            messagebox.showinfo("Error", "Username already exists")
            return None
        user = self._user_repository.create(User(username, password))
        return user

    def login(self, username, password):
        login_user = self._user_repository.find_user(username)

        if login_user and login_user.password == password:
            self._user = login_user
            return True
        messagebox.showinfo("Error", "Invalid username or password")
        return False

    def add_flight(self, departure, arrival, dep_time=None, arr_time=None):
        if not self._user:
            messagebox.showinfo("Error", "No user logged in")
            return None
        flight = self._logbook_repository.create(
            Flight(self._user.username, departure, arrival, dep_time, arr_time))
        return flight

    def get_flights_by_user(self):
        if not self._user:
            return []
        return self._logbook_repository.find_by_user(self._user.username)
