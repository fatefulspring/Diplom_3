from selenium.webdriver.common.by import By

SHOW_BUTTON = [By.XPATH,'//div[@class="input__icon input__icon-action"]']
HIDE_BUTTON = [By.XPATH,'//label[text()="Пароль"]/parent::div']
ACTIVE_CLASS = 'input_status_active'

INPUT_EMAIL = [By.XPATH, "//input[@type='text' and contains(@class, 'input__textfield')]"]
RECOVERY_BUTTON = [By.XPATH, "//button[contains(@class, 'button_button_type_primary')]"]
SAVE_BUTTON = [By.XPATH, "//button[contains(text(), 'Сохранить')]"]

LOGIN_TO_ACCOUNT_BUTTON = [By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"]
