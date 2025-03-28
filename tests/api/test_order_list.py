from api_methods import ApiMethods
import allure

@allure.title("Тест на возврат списка заказов в тело ответа")
def test_get_order_list():
    response = ApiMethods.get_order_list()
    assert "orders" in response.json() and len(response.json()['orders']) > 0
