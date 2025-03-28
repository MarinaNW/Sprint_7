from api_methods import ApiMethods
from helpers import Helper
from data import Data
import pytest

class TestRegisterCourier:
    def test_register_courier(self):
        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        first_name = Helper.generate_random_string(10)
        response = ApiMethods.register_new_courier(login, password, first_name)
        assert response.reason == 'Created'