import allure
import requests
from curl import CURL

class ApiMethods:
    @staticmethod
    def register_new_courier(login, password, first_name):
        return requests.post(CURL.register_courier, json={"login": login,"password": password,"firstName": first_name})

    @staticmethod
    def register_new_courier_and_return_login_password(login, password, first_name):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(CURL.register_courier, json={"login": login,"password": password,"firstName": first_name})

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
             login_pass.append(login)
             login_pass.append(password)
             login_pass.append(first_name)

        # возвращаем список
        return login_pass

    @staticmethod
    def login_of_courier(login, password):
        return requests.post(CURL.login_courier,json={"login": login, "password": password})

    @staticmethod
    def login_courier_and_return_login_password(login, password):
        login_pass = []
        response = requests.post(CURL.login_courier, json={"login": login,"password": password})

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 200:
             login_pass.append(login)
             login_pass.append(password)
        # возвращаем список
        return login_pass

    @staticmethod
    def create_order(firstName, lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color):
        payload = {
    "firstName": firstName,
    "lastName": lastName,
    "address": address,
    "metroStation": metroStation,
    "phone": phone,
    "rentTime": rentTime,
    "deliveryDate": deliveryDate,
    "comment": comment,
    "color": [
        color
    ]
}
        return requests.post(CURL.create_order, json=payload)

    @staticmethod
    def get_order_list():
        return requests.get(CURL.create_order)