from faker import Faker
fake = Faker("ru_RU")

class RegistrationModel:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def random_admin(self):
        return {"login": fake.user_name(), "password": fake.password()}