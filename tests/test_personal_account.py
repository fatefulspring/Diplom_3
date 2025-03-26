import allure

from constants import LOGIN_URL, ORDER_HISTORY_URL
from pages.personal_account_page import PersonalAccount


class TestPersonalAccount:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        driver.get(LOGIN_URL)
        page = PersonalAccount(driver)
        assert page.current_url == LOGIN_URL

    @allure.title('переход в раздел «История заказов»')
    def test_personal_account_order_history(self, driver, user_email_password):
        driver.get(LOGIN_URL)
        page = PersonalAccount(driver)
        page.login(*user_email_password)
        driver.get(ORDER_HISTORY_URL)
        assert page.current_url == ORDER_HISTORY_URL

    @allure.title('выход из аккаунта')
    def test_personal_account_logout(self, driver, user_email_password):
        driver.get(LOGIN_URL)
        page = PersonalAccount(driver)
        page.login(*user_email_password)
        page.go_to_account()
        page.logout()
        assert page.current_url == LOGIN_URL