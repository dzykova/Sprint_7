import requests
from data.courier_data import CourierData
from urls import BASE_URL

class TestCreateCourier:

    def test_create_courier_positive(self):

        payload = CourierData.generate_new_courier()

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        r = response.json()

        assert response.status_code == 201
        assert True == r["ok"]

        payload_login = {"login": payload["login"], "password": payload["password"]}
        response_login = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload_login)

        id_courier = []
        r1 = response_login.json()

        if response_login.status_code == 200:
            id_courier.append(r1["id"])

        response_delete = requests.delete(f"{BASE_URL}/api/v1/courier/{id_courier[0]}")

        assert response_delete.status_code == 200

    def test_create_courier_without_login_negative(self):

        payload_registration = {
            "login": "",
            "password": "12345",
            "first_name": "TestCourier"
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload_registration)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" == r["message"]

    def test_create_courier_without_password_negative(self):

        payload_registration = {
            "login": "test12340001",
            "password": "",
            "first_name": "TestCourier"
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload_registration)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" == r["message"]

    def test_create_courier_duplicate_negative(self):

        payload = CourierData.generate_new_courier()

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        r = response.json()

        assert response.status_code == 201
        assert True == r["ok"]

        response_duplicate = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        r1 = response_duplicate.json()

        assert response_duplicate.status_code == 409
        assert "Этот логин уже используется. Попробуйте другой." == r1["message"]

        payload_login = {"login": payload["login"], "password": payload["password"]}
        response_login = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload_login)

        id_courier = []
        r2 = response_login.json()

        if response_login.status_code == 200:
            id_courier.append(r2["id"])

        response_delete = requests.delete(f"{BASE_URL}/api/v1/courier/{id_courier[0]}")

        assert response_delete.status_code == 200

