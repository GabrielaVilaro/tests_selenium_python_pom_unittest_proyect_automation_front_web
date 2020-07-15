import random
import string


class FunctionsUtils:

    def __init__(self):
        self.prefix = 'test123+'
        self.domain = 'gmail.com'

    # función que genera un email random
    def generate_email(self):
        random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                              for _ in range(10))
        return self.prefix + random_part + '@' + self.domain

    def generate_number_phone(self):
        random_number = ''.join(random.choice(string.digits)
                              for _ in range(10))
        return random_number

