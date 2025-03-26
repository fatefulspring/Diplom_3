
from locators import personal_account as personal_account_locator

from .base_page import BasePage


class PersonalAccount(BasePage):
    def login(self, email, password):
        self.set_element(personal_account_locator.INPUT_EMAIL, email)
        self.set_element(personal_account_locator.INPUT_PASSWORD, password)
        self.click_on_element(personal_account_locator.LOGIN_BUTTON)

    def logout(self):
        self.click_on_element(personal_account_locator.LOGOUT_BUTTON)
        self.wait_for_element(personal_account_locator.INPUT_EMAIL)

    def go_to_account(self):
        self.click_on_element(personal_account_locator.ACCOUNT_BUTTON)

    def get_first_order(self):
        self.click_on_element(personal_account_locator.ACCOUNT_BUTTON)
        self.click_on_element(personal_account_locator.HISTORY_BUTTON)
        return self.get_element(personal_account_locator.ORDER_NUMBER).text
