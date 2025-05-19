from typing import Optional, List, Tuple


class Users:
    def __init__(self):
        self.users: List[Tuple] = [("admin", "1234gghh")]

    def is_user(self, user):
        for group in self.users:
            if group[0] == user:
                return True
            else:
                continue
        return False

    def valid_user_password(self, user, password):
        for group in self.users:
            if group[0] == user and group[1] == password:
                return True
            else:
                continue
        return False
