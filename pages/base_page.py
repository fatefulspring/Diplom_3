from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)


    def scroll_to_element(self, locator):
        self.driver.execute_script(
            'arguments[0].scrollIntoView()', self.get_element(locator)
        )

    def wait_for_element(self, locator):
        Wait(self.driver,5).until(exp_cond.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        self.scroll_to_element(locator)
        self.wait_for_element(locator)
        self.get_element(locator).click()

    def set_element(self, locator, value):
        self.scroll_to_element(locator)
        self.wait_for_element(locator)
        self.get_element(locator).send_keys(*value)

    def switch_to_next_tab(self):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        next_handle = handles[(handles.index(current_handle) + 1) % len(handles)]
        self.driver.switch_to.window(next_handle)

    def drag_and_drop(self, element1, element2):
        element1 = self.driver.find_element(*element1)
        element2 = self.driver.find_element(*element2)
        ActionChains(self.driver).drag_and_drop(element1, element2).perform()

    @property
    def current_url(self):
        return self.driver.current_url