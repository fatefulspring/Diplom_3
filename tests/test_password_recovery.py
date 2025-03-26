import allure

import constants
from pages.main_page import MainPage
from pages.password_recovery_page import RecoveryPage


class TestPasswordRecovery:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_password_recovery(self, driver):
        driver.get(constants.BASE_URL)
        main_page = MainPage(driver)
        main_page.go_to_login_page()
        assert main_page.current_url == constants.LOGIN_URL
        login_page = RecoveryPage(driver)
        login_page.go_to_password_recovery_page()
        assert login_page.current_url == constants.RECOVERY_URL

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email(self, driver):
        driver.get(constants.RECOVERY_URL)
        recovery_page = RecoveryPage(driver)
        recovery_page.password_recovery()
        assert recovery_page.current_url == constants.RESET_URL

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_hide_show_password(self, driver):
        driver.get(constants.RESET_URL)
        recovery_page = RecoveryPage(driver)
        recovery_page.password_recovery()
        recovery_page.reset_password()
        assert recovery_page.password_is_active()
