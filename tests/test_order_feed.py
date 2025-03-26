import allure

import constants
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeed
from pages.personal_account_page import PersonalAccount


class TestOrderFeed:
    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_modal_open(self, driver):
        driver.get(constants.BASE_URL)
        page = MainPage(driver)
        page.go_to_order_feed()
        order_feed_page = OrderFeed(driver)
        order_feed_page.click_on_order()
        assert order_feed_page.is_modal_opened()

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_from_history_displayed_order_list(self, driver, user_email_password):
        driver.get(constants.LOGIN_URL)
        page = PersonalAccount(driver)
        page.login(*user_email_password)
        main_page = MainPage(driver)
        main_page.make_order()
        order_number = page.get_first_order()
        assert order_number == main_page.get_first_order_number()

    @allure.title('при создании нового заказа счетчик Выполнено за все время/сегодня увеличивается')
    def test_count_orders(self, driver, user_email_password):
        driver.get(constants.LOGIN_URL)
        page = PersonalAccount(driver)
        page.login(*user_email_password)
        main_page = MainPage(driver)
        before_total_orders, before_today_orders = main_page.get_orders()
        main_page.make_order()
        after_total_orders, after_today_orders = main_page.get_orders()
        assert int(before_total_orders) < int(after_total_orders)
        assert int(before_today_orders) < int(after_today_orders)

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver, user_email_password):
        driver.get(constants.LOGIN_URL)
        page = PersonalAccount(driver)
        page.login(*user_email_password)
        main_page = MainPage(driver)
        main_page.make_order()
        order_number = page.get_first_order()
        assert order_number.replace('#', '') in main_page.get_in_work_order()
