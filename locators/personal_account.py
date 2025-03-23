from selenium.webdriver.common.by import By

INPUT_EMAIL = [By.XPATH,'//label[text() = "Email"]/following-sibling::input']
INPUT_PASSWORD = [By.XPATH,'//label[text() = "Пароль"]/following-sibling::input']
LOGIN_BUTTON = [By.XPATH, "//button[contains(text(), 'Войти')]"]
LOGOUT_BUTTON = [By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']"]
ACCOUNT_BUTTON = [By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href="/account"]']
HISTORY_BUTTON = [By.XPATH,'//a[text() = "История заказов"]']
ORDER_NUMBER = [By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')]//p[contains(@class, 'text_type_digits-default')])[1]"]