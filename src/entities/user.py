class User:
    """User class."""

    def __init__(self, username, password):
        """Constructor of the class; creates a new User-object.

        Args:
            username: A string depicting the username of the user.
            password: A string depicting the password of the user.
        """

        self.username = username
        self.password = password
