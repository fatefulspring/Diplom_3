from time import sleep

from selenium.common.exceptions import NoSuchElementException

from locators import main as main_locator

from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        self.click_on_element(main_locator.LOGIN_TO_ACCOUNT_BUTTON)

    def go_to_constructor(self):
        self.click_on_element(main_locator.CONSTRUCTOR_BUTTON)

    def go_to_order_feed(self):
        self.click_on_element(main_locator.ORDER_FEED_BUTTON)

    def click_on_ingredient(self):
        self.click_on_element(main_locator.FIRST_INGREDIENT_BUTTON)

    def is_ingredient_details_modal_opened(self):
        try:
            return self.driver.find_element(*main_locator.IS_INGREDIENT_MODAL_OPENED)
        except NoSuchElementException:
            return False

    def close_ingredient_detail_modal(self):
        self.click_on_element(main_locator.CLOSE_INGREDIENT_DETAILS_MODAL_BUTTON)

    def move_ingredient_to_basket(self):
        self.get_element(main_locator.FIRST_INGREDIENT_BUTTON)
        self.drag_and_drop(main_locator.FIRST_INGREDIENT_BUTTON, main_locator.BURGER_CONSTRUCTOR_BASKET)

    def get_ingredient_counter(self):
        return self.get_element(main_locator.INGREDIENT_COUNTER).text

    def make_order(self):
        self.go_to_constructor()
        self.move_ingredient_to_basket()
        self.click_on_element(main_locator.MAKE_ORDER_BUTTON)
        sleep(2)
        order_number = self.driver.find_element(*main_locator.ORDER_NUMBER)
        self.click_on_element(main_locator.CLOSE_ORDER_BUTTON)
        return order_number

    def is_order_modal_opened(self):
        return self.driver.find_element(*main_locator.ORDER_NUMBER)

    def get_first_order_number(self):
        self.go_to_order_feed()
        return self.get_element(main_locator.FIRST_ORDER_NUMBER).text

    def get_orders(self):
        self.go_to_order_feed()
        return self.get_element(main_locator.TOTAL_ORDERS).text, self.get_element(main_locator.TODAY_ORDERS).text

    def get_in_work_order(self):
        self.go_to_order_feed()
        return [self.get_element(main_locator.IN_WORK_ORDER).text, self.get_element(main_locator.READY_ORDER).text]