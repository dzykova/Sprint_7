import requests
import pytest
from data.order_data import OrderData
from urls import BASE_URL

class TestCreateOrder:

    @pytest.mark.parametrize(
        'payload', 
        [
            OrderData.ORDER_DATA_1,
            OrderData.ORDER_DATA_2,
            OrderData.ORDER_DATA_3,
            OrderData.ORDER_DATA_4
        ]
    )
    def test_create_order(self, payload):

        response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)

        r = response.json()

        assert response.status_code == 201
        assert "track" in r