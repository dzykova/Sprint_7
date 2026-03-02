import requests
from urls import BASE_URL
import allure

class TestGetOrdersList:

    @allure.title('Проверка API "Получение списка заказов"')
    def test_get_orders_list(self):

        with allure.step('Отправляем запрос на получение списка заказов'):
            response = requests.get(f"{BASE_URL}/api/v1/orders")

        r = response.json()

        assert response.status_code == 200
        assert "orders" in r