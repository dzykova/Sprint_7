import pytest
import requests
import random
import string
from urls import BASE_URL

@pytest.fixture
def new_courier():
    
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    yield payload

    # teardown
    payload_login = {
        "login": payload["login"],
        "password": payload["password"]
    }

    response_login = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload_login)

    if response_login.status_code == 200:
        courier_id = response_login.json()["id"]
        requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")


@pytest.fixture
def courier():

    def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера
    requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

    yield {
        "login": login,
        "password": password
    }

    # логинимся, чтобы получить id для удаления
    payload_login = {
        "login": login,
        "password": password
    }

    response_login = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload_login)
    courier_id = response_login.json()["id"]

    requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")