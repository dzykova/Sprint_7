import requests
from data.courier_data import CourierData
from urls import BASE_URL
import allure

class TestCreateCourier:

    @allure.title('Проверка API "Создание курьера" - позитивный кейс')
    def test_create_courier_positive(self, new_courier):

        with allure.step('Отправляем запрос на создание курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier", data=new_courier)

        r = response.json()

        assert response.status_code == 201
        assert True == r["ok"]
    
    @allure.title('Проверка API "Создание курьера" без логина в реквесте - негативный кейс')
    def test_create_courier_without_login_negative(self):

        with allure.step('Отправляем запрос на создание курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier", data=CourierData.COURIER_DATA_1)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" == r["message"]

    @allure.title('Проверка API "Создание курьера" без пароля в реквесте - негативный кейс')
    def test_create_courier_without_password_negative(self):

        with allure.step('Отправляем запрос на создание курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier", data=CourierData.COURIER_DATA_2)

        r = response.json()

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" == r["message"]

    @allure.title('Проверка API "Создание курьера" с дублирующимися данными - негативный кейс')
    def test_create_courier_duplicate_negative(self, new_courier):

        with allure.step('Отправляем запрос на создание курьера'):
            response = requests.post(f"{BASE_URL}/api/v1/courier", data=new_courier)
        

        with allure.step('Повторно отправляем запрос на создание курьера с такими же данными как в предыдущем шаге'):
            if response.status_code == 201:
                response_duplicate = requests.post(f"{BASE_URL}/api/v1/courier", data=new_courier)

        r = response_duplicate.json()

        assert response_duplicate.status_code == 409
        assert "Этот логин уже используется. Попробуйте другой." == r["message"]

