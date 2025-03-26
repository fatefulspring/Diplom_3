import allure

from constants import BASE_URL, FEED_URL, LOGIN_URL
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccount


class TestMainFunc:
    @allure.title('переход по клику на «Конструктор»')
    def test_go_to_construct(self, driver):
        driver.get(LOGIN_URL)
        page = MainPage(driver)
        page.go_to_constructor()
        assert page.current_url == BASE_URL

    @allure.title('переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self, driver):
        driver.get(LOGIN_URL)
        page = MainPage(driver)
        page.go_to_order_feed()
        assert page.current_url == FEED_URL

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        driver.get(BASE_URL)
        page = MainPage(driver)
        page.click_on_ingredient()
        assert page.is_ingredient_details_modal_opened()

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_click_ingredient_and_close_window(self, driver):
        driver.get(BASE_URL)
        page = MainPage(driver)
        page.click_on_ingredient()
        page.close_ingredient_detail_modal()
        assert not page.is_ingredient_details_modal_opened()

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_count(self, driver):
        driver.get(BASE_URL)
        page = MainPage(driver)
        page.move_ingredient_to_basket()
        assert page.get_ingredient_counter() == '2'


    @allure.title('залогиненный пользователь может оформить заказ')
    def test_create_order_with_login_user(self, driver, user_email_password):
        driver.get(LOGIN_URL)
        account_page = PersonalAccount(driver)
        account_page.login(*user_email_password)
        page = MainPage(driver)
        assert page.make_order()
