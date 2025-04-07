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
