import allure

from pages.personal_account_page import PersonalAccount

from .constants import LOGIN_URL, ORDER_HISTORY_URL
from .helpers import register_user


class TestPersonalAccount:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        driver.get(LOGIN_URL)
        assert driver.current_url == LOGIN_URL

    @allure.title('переход в раздел «История заказов»')
    def test_personal_account_order_history(self, driver):
        driver.get(LOGIN_URL)
        email, password = register_user()
        page = PersonalAccount(driver)
        page.login(email, password)
        driver.get(ORDER_HISTORY_URL)
        assert driver.current_url == ORDER_HISTORY_URL

    @allure.title('выход из аккаунта')
    def test_personal_account_logout(self, driver):
        driver.get(LOGIN_URL)
        email, password = register_user()
        page = PersonalAccount(driver)
        page.login(email, password)
        page.go_to_account()
        page.logout()
        assert driver.current_url == LOGIN_URL