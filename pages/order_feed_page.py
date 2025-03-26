from locators import order_feed as order_feed_locator

from .base_page import BasePage


class OrderFeed(BasePage):
    def click_on_order(self):
        self.click_on_element(order_feed_locator.ORDER_BUTTON)

    def is_modal_opened(self):
        return self.get_element(order_feed_locator.ORDER_MODAL) is not None
