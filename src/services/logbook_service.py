from entities.user import User
from repositories.user_repository import UserRepository


class LogbookService():
    def __init__(self):
        self._user = None
        self._user_repository = UserRepository()

    def register_user(self, username, password):
        if self._user_repository.find_user(username):
            print("Username already exists")
            return

        user = self._user_repository.create(User(username, password))
        return user
    
    def login(self, username, password):
        login_user = self._user_repository.find_user(username)

        if login_user and login_user.password == password:
            self._user = login_user
            return True
        else:
            print("Invalid username or password")
            return False
