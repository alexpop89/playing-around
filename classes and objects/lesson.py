class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __get_full_name(self):
        return self.first_name + ' ' + self.last_name

    full_name = property(
        fget=__get_full_name,
        doc="Users full name"
    )


class UserWhoCanLogin(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email)
        self.password = password

    def login(self):
        print('Logging in')