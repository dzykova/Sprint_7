import requests
from data.courier_data import CourierData
from urls import BASE_URL
import allure

class TestLoginCourier:

    @allure.title('Проверка API "Логин курьера" - позитивный кейс')
    def test_login_courier_positive(self, courier):


        with allure.step('Отправляем запрос на логин курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=courier)

        r = response.json()

        assert response.status_code == 200
        assert "id" in r

    @allure.title('Проверка API "Логин курьера" без логина в реквесте - негативный кейс')
    def test_login_courier_without_login_negative(self):

        with allure.step('Отправляем запрос на логин курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=CourierData.COURIER_DATA_3)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для входа" == r["message"]

    @allure.title('Проверка API "Логин курьера" без пароля в реквесте - негативный кейс')
    def test_login_courier_without_password_negative(self):

        with allure.step('Отправляем запрос на логин курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=CourierData.COURIER_DATA_4)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для входа" == r["message"]

    @allure.title('Проверка API "Логин курьера" с несуществующими данными - негативный кейс')
    def test_login_courier_with_unexisted_data_negative(self):

        with allure.step('Отправляем запрос на логин курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=CourierData.COURIER_DATA_5)

        r = response.json()

        assert response.status_code == 404
        assert "Учетная запись не найдена" == r["message"]