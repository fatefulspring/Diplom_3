import random
import string

import pytest
import requests
from selenium import webdriver

from .constants import USER_REGISTRATION_URL


def generate_registration_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(10)}@{generate_random_string(3)}.{generate_random_string(3)}'
    password = generate_random_string(10)
    name = generate_random_string(10)

    return email, password, name


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()


@pytest.fixture
def user_email_password():
    email, password, name = generate_registration_data()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    requests.post(USER_REGISTRATION_URL, data=payload)
    return email, password
