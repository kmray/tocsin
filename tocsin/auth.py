""" Auth """


class Auth:
    """ Auth class """

    def __init__(self, email: str, password: str) -> None:
        self._email = email
        self._password = password

    @property
    def email(self):
        """E-mail address"""
        return self._email

    @property
    def password(self):
        """Password"""
        return self._password
