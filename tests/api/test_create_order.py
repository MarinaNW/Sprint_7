from api_methods import ApiMethods
from helpers import Helper
from data import Data
import pytest
import allure

@allure.title("Тесты на создание заказа")
class TestCreateOrder:

    @allure.title("Тесты на указание цвета самоката при создании заказа")
    @pytest.mark.parametrize(
        "firstName, lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color",
        [(Helper.generate_random_string(5),
         Helper.generate_random_string(5),
         Data.address,
         Data.metroStation,
         Helper.generate_phone_number(),
         Data.rentTime,
         Data.deliveryDate,
         Data.comment,
         Data.colors[0]),
         (Helper.generate_random_string(5),
          Helper.generate_random_string(5),
          Data.address,
          Data.metroStation,
          Helper.generate_phone_number(),
          Data.rentTime,
          Data.deliveryDate,
          Data.comment,
          Data.colors[1]),
         (Helper.generate_random_string(5),
          Helper.generate_random_string(5),
          Data.address,
          Data.metroStation,
          Helper.generate_phone_number(),
          Data.rentTime,
          Data.deliveryDate,
          Data.comment,
          Data.colors[2]),
         (Helper.generate_random_string(5),
          Helper.generate_random_string(5),
          Data.address,
          Data.metroStation,
          Helper.generate_phone_number(),
          Data.rentTime,
          Data.deliveryDate,
          Data.comment,
          Data.colors[3])
        ]
    )
    def test_field_color(self,firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        response = ApiMethods.create_order(firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color)
        assert response.status_code == 201

    @allure.title("Тест на наличие в теле ответа track")
    def test_track_in_request_response(self):
        response = ApiMethods.create_order(Helper.generate_random_string(5), Helper.generate_random_string(5), Data.address,
                                       Data.metroStation, Helper.generate_phone_number(), Data.rentTime,
                                       Data.deliveryDate, Data.comment, Data.color)
        assert "track" in response.json()

