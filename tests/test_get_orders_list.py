import requests
from urls import BASE_URL

class TestGetOrdersList:

    def test_get_orders_list(self):

        response = requests.get(f"{BASE_URL}/api/v1/orders")

        r = response.json()

        assert response.status_code == 200
        assert "orders" in r