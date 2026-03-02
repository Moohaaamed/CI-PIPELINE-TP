"""Simple in-memory user manager used by tests."""


class UserManager:
    """Manage users in memory keyed by unique username."""

    def __init__(self):
        self._users = {}

    def add_user(self, username, user_data):
        if username in self._users:
            raise ValueError("User already exists")
        self._users[username] = user_data

    def get_user(self, username):
        return self._users.get(username)

    def remove_user(self, username):
        if username not in self._users:
            raise KeyError("User not found")
        return self._users.pop(username)

    def list_users(self):
        return dict(self._users)
