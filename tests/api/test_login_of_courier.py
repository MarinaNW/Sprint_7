import allure
from api_methods import ApiMethods
from helpers import Helper
from data import Data
import pytest

@allure.title("Тесты логина курьера")
class TestLoginCourier:
    @allure.title("Тест на возможность авторизоваться")
    def test_log_courier_true(self):
        response = ApiMethods.login_of_courier(Data.login, Data.password)
        assert response.status_code == 200

    @allure.title("Тест на необходимость указывать все обязательные поля для авторизации")
    def test_presence_of_required_fields_for_registration_courier(self):
        response = ApiMethods.login_courier_and_return_login_password(Data.login, Data.password)
        assert len(response)==2

    @allure.title("Тест на возврат ошибки при указании некорректного логина или пароля")
    @pytest.mark.parametrize(
        "login, password",
        [
            ("Data.login", "Data.password_another"),
            ("Data.login_another", "Data.password"),
        ]
    )
    def test_incorrect_login_or_password(self, login, password):
        response = ApiMethods.login_of_courier(login, password)
        assert response.status_code == 404


    @allure.title("Тест на возврат ошибки при отсутствии обязательного поля")
    @pytest.mark.parametrize(
        "login, password",
        [
            ("Data.login", ""),
            ("", "Data.password"),
        ]
    )
    def test_mandatory_fields_login_and_password(self, login, password):
        response = ApiMethods.login_of_courier(login, password)
        assert response.status_code == 400

    @allure.title("Тест на авторизацию под несуществующим пользователем")
    def test_login_non_existent_user(self):
        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        response = ApiMethods.login_of_courier(login, password)
        assert response.status_code == 404

    @allure.title("Тест на возврат id при успешном запросе")
    def test_login_and_return_id(self):
        response = ApiMethods.login_of_courier(Data.login, Data.password)
        assert response.json()['id'] == Data.id

