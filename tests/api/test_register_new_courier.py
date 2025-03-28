import allure
from api_methods import ApiMethods
from helpers import Helper
from data import Data
import pytest

@allure.title("Тесты на создании курьера")
class TestRegisterCourier:

    @allure.title("Тест на успешное создание курьера")
    def test_register_courier(self):
        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        first_name = Helper.generate_random_string(10)
        response = ApiMethods.register_new_courier(login, password, first_name)
        assert response.reason == 'Created'

    @allure.title("Тесты на невозможность создать 2х одинаковых")
    def test_register_two_identical_couriers_false(self):
        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        first_name = Helper.generate_random_string(10)
        response_one = ApiMethods.register_new_courier(login, password, first_name)
        assert response_one.reason == 'Created'
        response_two = ApiMethods.register_new_courier(login, password, first_name)
        assert response_two.reason == 'Conflict'

    @allure.title("Тест на обязательность заполнения всех обязательных полей")
    def test_presence_of_required_fields_for_registration_courier(self):
        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        first_name = Helper.generate_random_string(10)
        response = ApiMethods.register_new_courier_and_return_login_password(login, password, first_name)
        assert len(response)==3

    @allure.title("Тест на возвращение правильного кода ответа")
    def test_status_code(self):
        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        first_name = Helper.generate_random_string(10)
        response = ApiMethods.register_new_courier(login, password, first_name)
        assert response.status_code == 201

    @allure.title("Тест на возвращение корректного тела при успешном запросе")
    def test_answer_true(self):
        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        first_name = Helper.generate_random_string(10)
        response = ApiMethods.register_new_courier(login, password, first_name)
        assert response.json()['ok'] == True

    @allure.title("Тест на возврат ошибки при отсутствии обязательного поля")
    @pytest.mark.parametrize(
        "login, password,first_name",
        [
            ("Helper.generate_random_string(10)", "", "Helper.generate_random_string(10)"),
            ("", "Helper.generate_random_string(10)", "Helper.generate_random_string(10)"),
        ]
    )
    def test_successful_registration_with_required_fields(self,login, password,first_name):
        response = ApiMethods.register_new_courier(login, password, first_name)
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title("Тест на возврат ошибки при создание пользователя с логином, который уже есть")
    def test_register_two_identical_logins_false(self):
        login = Helper.generate_random_string(10)
        response_one = ApiMethods.register_new_courier(login, Data.password, Data.first_name)
        assert response_one.reason == 'Created'
        response_two = ApiMethods.register_new_courier(login, Data.password_another, Data.first_name_another)
        assert response_two.json()['message'] == "Этот логин уже используется. Попробуйте другой."


        