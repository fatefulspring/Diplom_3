from locators import recovery as recovery_locator

from .base_page import BasePage


class RecoveryPage(BasePage):
    def password_recovery(self):
        self.set_element(recovery_locator.INPUT_EMAIL, 'eamail@gmail.com')
        self.click_on_element(recovery_locator.RECOVERY_BUTTON)
        self.wait_for_element(recovery_locator.SAVE_BUTTON)

    def reset_password(self):
        self.click_on_element(recovery_locator.SHOW_BUTTON)
        self.driver.find_element(*recovery_locator.HIDE_BUTTON)

    def password_is_active(self):
        return recovery_locator.ACTIVE_CLASS in self.get_element(recovery_locator.HIDE_BUTTON).get_attribute('class')

    def go_to_password_recovery_page(self):
        self.click_on_element(recovery_locator.LOGIN_TO_ACCOUNT_BUTTON)
