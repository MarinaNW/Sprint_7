import random
import string
from faker import Faker


class Helper:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_phone_number():
        fake = Faker('ru_RU')
        phone_number = '+7 ' + f'{fake.msisdn()[0:3]} {fake.msisdn()[3:6]} {fake.msisdn()[6:8]} {fake.msisdn()[8:10]}'
        return phone_number