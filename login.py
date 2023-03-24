from user import *

class Login:
    def __init__(self, username, password):
        self._username = username
        self._password = password
    def login(self):
        print(self._username)
        print(self._password)
        user = User()
        boo = user.check_valid(self._username, self._password)
        return boo