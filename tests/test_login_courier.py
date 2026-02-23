import requests
from data.courier_data import CourierData
from urls import BASE_URL

class TestLoginCourier:

    def test_login_courier_positive(self):

        login_pass = CourierData.register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        r = response.json()

        assert response.status_code == 200
        assert "id" in r

        id_courier = []
        id_courier.append(r["id"])

        response_delete = requests.delete(f"{BASE_URL}/api/v1/courier/{id_courier[0]}")

        assert response_delete.status_code == 200

    def test_login_courier_without_login_negative(self):

        payload = {
            "login": "",
            "password": "12345"
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для входа" == r["message"]

    def test_login_courier_without_password_negative(self):

        payload = {
            "login": "test123",
            "password": ""
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для входа" == r["message"]

    def test_login_courier_with_unexisted_data_negative(self):

        payload = {
            "login": "test123",
            "password": "07"
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        r = response.json()

        assert response.status_code == 404
        assert "Учетная запись не найдена" == r["message"]